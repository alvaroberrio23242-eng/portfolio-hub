import os
from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
if not app.secret_key:
    raise RuntimeError("SECRET_KEY environment variable is required")

ADMIN_USER = os.environ.get("ADMIN_USER")
ADMIN_PASS = os.environ.get("ADMIN_PASS")
if not ADMIN_USER or not ADMIN_PASS:
    raise RuntimeError("ADMIN_USER and ADMIN_PASS environment variables are required")

from cafe_app import cafe_bp
app.register_blueprint(cafe_bp, url_prefix="/cafe")


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("authenticated"):
        return redirect(url_for("family"))

    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == ADMIN_USER and password == ADMIN_PASS:
            session["authenticated"] = True
            return redirect(url_for("family"))
        error = "Credenciales inválidas."

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("authenticated", None)
    return redirect(url_for("index"))


@app.route("/familia")
def family():
    if not session.get("authenticated"):
        return redirect(url_for("login"))
    return render_template("family.html")


if __name__ == "__main__":
    app.run(debug=False, port=5000)
