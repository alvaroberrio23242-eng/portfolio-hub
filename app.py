import hmac
import os
import secrets

from dotenv import load_dotenv

load_dotenv()

from flask import Flask, redirect, render_template, request, session, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.security import check_password_hash

import content
import render

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")
if not app.secret_key:
    raise RuntimeError("SECRET_KEY environment variable is required")
if len(app.secret_key) < 32:
    raise RuntimeError(
        "SECRET_KEY must be at least 32 characters; generate one with "
        'python -c "import secrets; print(secrets.token_hex(32))"'
    )

ADMIN_USER = os.environ.get("ADMIN_USER")
ADMIN_PASS_HASH = os.environ.get("ADMIN_PASS_HASH")
if not ADMIN_USER or not ADMIN_PASS_HASH:
    raise RuntimeError("ADMIN_USER and ADMIN_PASS_HASH environment variables are required")

PORTFOLIO = content.load()
SITE_ORIGIN = PORTFOLIO["site"]["origin"].rstrip("/")

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    # Render sirve HTTPS; se puede desactivar con SESSION_COOKIE_SECURE=0 para
    # pruebas locales sobre http://.
    SESSION_COOKIE_SECURE=os.environ.get("SESSION_COOKIE_SECURE", "1") == "1",
    MAX_CONTENT_LENGTH=64 * 1024,
)

limiter = Limiter(key_func=get_remote_address, app=app, storage_uri="memory://")

CSP = "; ".join(
    (
        "default-src 'self'",
        "base-uri 'self'",
        "object-src 'none'",
        "frame-ancestors 'none'",
        "form-action 'self'",
        "img-src 'self' data:",
        "media-src 'self'",
        # El hub usa <style> inline, atributos style= y <script> inline.
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
        "font-src 'self' https://fonts.gstatic.com",
        "script-src 'self' 'unsafe-inline'",
        "connect-src 'self'",
        "upgrade-insecure-requests",
    )
)


@app.after_request
def set_security_headers(response):
    response.headers.setdefault("Content-Security-Policy", CSP)
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "DENY")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Permissions-Policy", "geolocation=(), microphone=(), camera=()")
    response.headers.setdefault("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
    return response


def csrf_token():
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_urlsafe(32)
    return session["csrf_token"]


def csrf_valid(token):
    expected = session.get("csrf_token")
    if not expected or not token:
        return False
    return hmac.compare_digest(expected, token)


@app.context_processor
def inject_context():
    return {
        "site": PORTFOLIO["site"],
        "nav": PORTFOLIO["nav"],
        "hero": PORTFOLIO["hero"],
        "evidence": PORTFOLIO["evidence"],
        "case_studies": PORTFOLIO["case_studies"],
        "capabilities": PORTFOLIO["capabilities"],
        "projects": PORTFOLIO["projects"],
        "about": PORTFOLIO["about"],
        "contact": PORTFOLIO["contact"],
        "footer": PORTFOLIO["footer"],
        "site_origin": SITE_ORIGIN,
        "csrf_token": csrf_token,
    }


render.configure_flask(app, PORTFOLIO)

from cafe_app import cafe_bp

app.register_blueprint(cafe_bp, url_prefix="/cafe")


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
@limiter.limit("5 per minute", methods=["POST"])
def login():
    if session.get("authenticated"):
        return redirect(url_for("family"))

    error = None
    if request.method == "POST":
        if not csrf_valid(request.form.get("csrf_token", "")):
            return render_template("login.html", error="Sesión inválida. Recarga la página."), 400
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        user_ok = hmac.compare_digest(
            username.encode("utf-8"), (ADMIN_USER or "").encode("utf-8")
        )
        pass_ok = check_password_hash(ADMIN_PASS_HASH, password)
        if user_ok and pass_ok:
            session.clear()
            session["authenticated"] = True
            return redirect(url_for("family"))
        error = "Credenciales inválidas."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/familia")
def family():
    if not session.get("authenticated"):
        return redirect(url_for("login"))
    return render_template("family.html")


@app.errorhandler(404)
def not_found(_error):
    return render_template(
        "404.html",
        status_code=404,
        heading="Esta página no existe",
        message="El enlace puede estar desactualizado. Vuelve al portafolio para ver el trabajo disponible.",
    ), 404


@app.errorhandler(429)
def rate_limited(_error):
    return render_template("429.html"), 429


if __name__ == "__main__":
    app.run(debug=False, port=5000)
