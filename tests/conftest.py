"""Fixtures y helpers compartidos por la suite de Portfolio Hub.

Este modulo es la unica pieza que/setup de pruebas. Expone dos APIs que
consumen los tests:

- La de ``test_content``/``test_sync``/``test_render``/``test_seo``/
  ``test_links`` (fixtures ``portfolio``, ``surfaces``, ``static_html`` y
  helpers ``iter_links``, ``iter_media``, ``static_path``).
- La de ``test_auth``/``test_routes``/``test_security`` (constantes
  ``TEST_USER``/``TEST_PASSWORD``/``WRONG_*``, helpers ``login`` y
  ``do_login``, y el objeto ``flask_app``).
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from werkzeug.security import generate_password_hash

# Credenciales de las pruebas. El hash se genera aqui, nunca se hardcodea.
TEST_USER = "test-user"
TEST_PASSWORD = "test-password-0000"
WRONG_USER = "usuario-inexistente"
WRONG_PASSWORD = "password-inexistente-0000"

# Alias que consume test_auth.py.
ADMIN_USER = TEST_USER
TEST_ADMIN_USER = TEST_USER
TEST_ADMIN_PASS = TEST_PASSWORD

os.environ.setdefault("SECRET_KEY", "test-secret-key-" + "0" * 48)
os.environ.setdefault("ADMIN_USER", TEST_USER)
os.environ.setdefault("SESSION_COOKIE_SECURE", "0")
os.environ.setdefault("ADMIN_PASS_HASH", generate_password_hash(TEST_PASSWORD))

import pytest

import app as hub_app
import content
import render
import scripts.build_static as build_static
from cafe_app import PRODUCTS

flask_app = hub_app.app

# La raiz del repositorio. test_urls la usa para leer index.html y las
# plantillas por ruta relativa; con BASE_DIR la suite no depende de cwd.
RAIZ = BASE_DIR


def _csrf_from(client):
    body = client.get("/login").get_data(as_text=True)
    match = re.search(r'name="csrf_token" value="([^"]+)"', body)
    assert match, "el formulario de login no expone un token CSRF"
    return match.group(1)


def login(client, username=TEST_USER, password=TEST_PASSWORD, token=None):
    """POST real contra /login con un token CSRF válido (o forzado)."""
    return client.post(
        "/login",
        data={
            "username": username,
            "password": password,
            "csrf_token": token or _csrf_from(client),
        },
    )


def do_login(client, username, password):
    """POST a /login con credenciales explicitas, sin depender de defaults."""
    return client.post(
        "/login",
        data={
            "username": username,
            "password": password,
            "csrf_token": _csrf_from(client),
        },
    )


@pytest.fixture(scope="session")
def portfolio():
    return content.load()


@pytest.fixture(scope="session")
def raiz():
    """Raiz del repositorio, independiente del directorio de trabajo."""
    return RAIZ


@pytest.fixture(scope="session")
def productos():
    """Catalogo de /cafe tal y como lo declara cafe_app.PRODUCTS."""
    return PRODUCTS


@pytest.fixture
def app():
    return hub_app.app


@pytest.fixture
def _fresh_client():
    """Cliente sin sesion. Cada uno es un contexto independiente."""
    hub_app.app.config.update(TESTING=True)
    hub_app.limiter.reset()
    return hub_app.app.test_client()


@pytest.fixture
def client(_fresh_client):
    """Cliente nuevo por test: la sesion y el limiter no se filtran.

    No se usa `with _fresh_client`: un test puede pedir `client` y `logged_in`
    a la vez, y Werkzeug 3 rechaza anidar dos contextos de cliente
    ("Cannot nest client invocations"). La cookie de sesion la mantiene el
    jar del propio cliente, que no necesita el bloque `with`.
    """
    yield _fresh_client
    hub_app.limiter.reset()


@pytest.fixture
def csrf(client):
    """Token CSRF leido del formulario real, no de la sesion interna."""
    return _csrf_from(client)


@pytest.fixture
def logged_in(_fresh_client):
    """Sesion iniciada via el formulario, en un cliente DISTINTO a `client`.

    Construye su propio cliente en lugar de reutilizar `_fresh_client`: pytest
    cachea las fixtures de funcion dentro de un mismo test, asi que compartirla
    haria que `client` y `logged_in` fueran el mismo objeto y la prueba cruzada
    "autenticar uno no desbloquea al otro" no comprobaria nada.
    """
    hub_app.app.config.update(TESTING=True)
    hub_app.limiter.reset()
    test_client = hub_app.app.test_client()
    response = login(test_client)
    assert response.status_code == 302, "no se pudo iniciar sesion en el fixture"
    yield test_client
    hub_app.limiter.reset()


@pytest.fixture
def logged_in_client(_fresh_client):
    """Alias de ``logged_in`` para los tests que usan ese nombre."""
    hub_app.app.config.update(TESTING=True)
    hub_app.limiter.reset()
    test_client = hub_app.app.test_client()
    response = login(test_client)
    assert response.status_code == 302, "no se pudo iniciar sesion en el fixture"
    yield test_client
    hub_app.limiter.reset()


@pytest.fixture(scope="session")
def static_html():
    return build_static.render_html()


@pytest.fixture
def web_html(client):
    return client.get("/").get_data(as_text=True)


@pytest.fixture
def surfaces(portfolio, static_html, web_html):
    """Las dos superficies renderizadas, para comparar paridad."""
    return {"static": static_html, "web": web_html}


def iter_links(data):
    """Recorre todos los enlaces declarados en la fuente de verdad."""
    for action in data["hero"]["actions"]:
        yield "hero.actions", action
    for item in data["evidence"]:
        yield "evidence", {"href": item["url"], "available": item["available"], "note": item["note"]}
    for case in data["case_studies"]["items"]:
        for link in case["links"]:
            yield f"case_studies.{case['name']}", link
    for project in data["projects"]["items"]:
        for link in project["links"]:
            yield f"projects.{project['name']}", link


def iter_media(data):
    """Recorre todos los medios declarados en la fuente de verdad."""
    media = data["hero"]["media"]
    yield "hero", media["src"]
    if media.get("poster"):
        yield "hero", media["poster"]
    yield "about", data["about"]["avatar"]
    yield "hero", data["hero"]["avatar"]
    for item in data["evidence"]:
        yield f"evidence.{item['name']}", item["media"]["src"]
        if item["media"].get("poster"):
            yield f"evidence.{item['name']}", item["media"]["poster"]
    for case in data["case_studies"]["items"]:
        yield f"case_studies.{case['name']}", case["media"]["src"]
        if case["media"].get("poster"):
            yield f"case_studies.{case['name']}", case["media"]["poster"]


def static_path(relative):
    """Ruta absoluta de un asset relativo a `static/`."""
    return BASE_DIR / "static" / relative


def iter_html_hrefs(html):
    """Extrae los href de un documento ya renderizado."""
    for match in re.finditer(r'href="([^"]+)"', html):
        yield match.group(1)


def iter_html_srcs(html):
    """Extrae los src de un documento ya renderizado."""
    for match in re.finditer(r'\ssrc="([^"]+)"', html):
        yield match.group(1)


__all__ = [
    "BASE_DIR",
    "RAIZ",
    "PRODUCTS",
    "ADMIN_USER",
    "TEST_USER",
    "TEST_PASSWORD",
    "TEST_ADMIN_USER",
    "TEST_ADMIN_PASS",
    "WRONG_USER",
    "WRONG_PASSWORD",
    "content",
    "hub_app",
    "flask_app",
    "render",
    "build_static",
    "login",
    "do_login",
    "iter_links",
    "iter_media",
    "static_path",
    "iter_html_hrefs",
    "iter_html_srcs",
]
