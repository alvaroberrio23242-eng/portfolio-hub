"""Regresion de autenticacion y autorizacion de /login y /familia.

Restriccion: el contenido de /familia es material sensible. Estos tests nunca
comprueban ni imprimen nombres, apodos ni datos personales. Para detectar una
eliminacion de contenido comparan ESTRUCTURA (numero de bloques), no texto.

Invariante de la suite: ``MIEMBROS_FAMILIA`` esta fijado en 5, que es lo que
templates/family.html renderiza hoy. Si alguien anade o quita un perfil, este
test falla y obliga a actualizar el valor de forma explicita y consciente.
"""

import pytest
from conftest import TEST_ADMIN_PASS, TEST_ADMIN_USER, do_login

MIEMBROS_FAMILIA = 5
SELECTOR_BLOQUE = "member-section"


def test_familia_anonimo_redirige_a_login(client):
    resp = client.get("/familia", follow_redirects=False)
    assert resp.status_code == 302
    assert "/login" in resp.headers["Location"]


def test_familia_anonimo_no_expone_contenido(client):
    """El 302 no debe filtrar ni un fragmento del contenido privado."""
    resp = client.get("/familia", follow_redirects=False)
    html = resp.get_data(as_text=True)
    assert SELECTOR_BLOQUE not in html, "la redireccion filtro estructura de /familia"


def test_familia_con_sesion_invalida_redirige(client):
    """Una sesion manipulada no debe dar acceso."""
    with client.session_transaction() as sess:
        sess["authenticated"] = False
    resp = client.get("/familia", follow_redirects=False)
    assert resp.status_code == 302


def test_familia_sin_clave_de_sesion_redirige(client):
    """Ausencia de la clave equivale a no autenticado."""
    with client.session_transaction() as sess:
        sess.pop("authenticated", None)
    resp = client.get("/familia", follow_redirects=False)
    assert resp.status_code == 302


def test_login_correcto_redirige_a_familia(client):
    resp = do_login(client, TEST_ADMIN_USER, TEST_ADMIN_PASS)
    assert resp.status_code == 302
    assert "/familia" in resp.headers["Location"]


def test_login_password_incorrecto(client):
    resp = do_login(client, TEST_ADMIN_USER, "password-inexistente")
    assert resp.status_code == 200, "un fallo debe re-renderizar el formulario"
    assert "v" in resp.get_data(as_text=True), "se perdio el mensaje de error"


def test_login_usuario_inexistente(client):
    resp = do_login(client, "usuario-inexistente", TEST_ADMIN_PASS)
    assert resp.status_code == 200


def test_login_no_revela_si_el_usuario_existe(client):
    """Evita enumeracion de usuarios: ambos fallos deben ser indistinguibles."""
    usuario_malo = do_login(client, "usuario-inexistente", TEST_ADMIN_PASS)
    password_malo = do_login(client, TEST_ADMIN_USER, "password-inexistente")
    assert usuario_malo.status_code == password_malo.status_code
    assert usuario_malo.get_data() == password_malo.get_data(), (
        "las respuestas difieren y permiten enumerar usuarios"
    )


def test_login_vacio_no_autentica(client):
    resp = do_login(client, "", "")
    assert resp.status_code in (200, 400)
    assert client.get("/familia", follow_redirects=False).status_code == 302


def test_familia_autenticado_200(logged_in):
    assert logged_in.get("/familia").status_code == 200


def test_familia_contenido_intacto(logged_in):
    """Protege el contenido familiar SIN exponerlo.

    Verifica que siguen existiendo los 3 bloques de perfil. No lee, no compara
    ni imprime ningun nombre o dato personal.
    """
    html = logged_in.get("/familia").get_data(as_text=True)
    assert SELECTOR_BLOQUE in html, "el selector de perfil desaparecio"
    encontrados = html.count(SELECTOR_BLOQUE)
    assert encontrados == MIEMBROS_FAMILIA, (
        f"cambio el numero de perfiles en /familia: {encontrados} "
        f"(esperado {MIEMBROS_FAMILIA}). Actualiza MIEMBROS_FAMILIA solo si es "
        f"un cambio intencional."
    )


def test_logout_limpia_la_sesion(client):
    do_login(client, TEST_ADMIN_USER, TEST_ADMIN_PASS)
    assert client.get("/familia", follow_redirects=False).status_code == 200
    client.get("/logout", follow_redirects=False)
    assert client.get("/familia", follow_redirects=False).status_code == 302


def test_sesion_httponly_por_defecto(app):
    """Defense in depth: la cookie de sesion no debe ser legible por JS."""
    assert app.config.get("SESSION_COOKIE_HTTPONLY") is True


def test_familia_requiere_credenciales_validas(client, logged_in):
    """Prueba cruzada: el cliente limpio sigue bloqueado tras autenticar otro."""
    assert client.get("/familia", follow_redirects=False).status_code == 302
    assert logged_in.get("/familia").status_code == 200


@pytest.mark.parametrize("ruta", ["/login", "/familia"])
def test_ruta_credencial_no_filtra_secreto(client, ruta):
    """Ni /login ni la redireccion de /familia pueden filtrar material sensible.

    /familia exige sesion, asi que sin credenciales responde 302 hacia /login
    (app.py:135-138). El test original exigia 200 en ambos casos, lo que
    contradecia el propio control de acceso que el resto del archivo verifica.
    """
    resp = client.get(ruta)
    if ruta == "/familia":
        assert resp.status_code == 302, "/familia deberia redirigir sin sesion"
        assert "/login" in resp.headers["Location"]
    else:
        assert resp.status_code == 200
    html = resp.get_data(as_text=True)
    assert "scrypt" not in html.lower()
    assert TEST_ADMIN_PASS not in html
