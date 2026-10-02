"""Ambas superficies deben renderizar el mismo contenido con URLs correctas."""

import re

import pytest

import content
import render
from conftest import TEST_PASSWORD


WEB_ROUTES = ["/", "/login", "/cafe/", "/cafe/productos"]
PRIVATE_ROUTES = ["/familia"]


@pytest.mark.parametrize("path", WEB_ROUTES)
def test_public_routes_render(client, path):
    response = client.get(path)
    assert response.status_code == 200, f"{path} -> {response.status_code}"


@pytest.mark.parametrize("path", PRIVATE_ROUTES)
def test_private_routes_redirect_to_login(client, path):
    response = client.get(path)
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_unknown_route_renders_404_page(client):
    response = client.get("/no-existe-esta-ruta")
    assert response.status_code == 404
    body = response.data.decode("utf-8")
    assert "no existe" in body
    assert "Volver al portafolio" in body


def test_both_surfaces_render_every_project(surfaces, portfolio):
    for name, html in surfaces.items():
        for project in portfolio["projects"]["items"]:
            assert project["name"] in html, f"{name} no menciona {project['name']}"


def test_both_surfaces_render_every_case_study(surfaces, portfolio):
    for name, html in surfaces.items():
        for case in portfolio["case_studies"]["items"]:
            assert case["name"] in html, f"{name} no menciona el caso {case['name']}"


def test_both_surfaces_render_every_capability(surfaces, portfolio):
    for name, html in surfaces.items():
        for item in portfolio["capabilities"]["items"]:
            assert item["title"] in html, f"{name} no menciona {item['title']}"


def test_web_uses_absolute_static_urls(web_html):
    assert 'src="/static/' in web_html
    assert 'href="static/' not in web_html


def test_static_uses_relative_static_urls(static_html):
    assert 'src="static/' in static_html
    assert 'src="/static/' not in static_html


def test_static_has_no_link_to_flask_only_routes(static_html):
    """`/cafe/` y `/login` no existen en GitHub Pages: no pueden quedar como enlaces."""
    assert 'href="/cafe/"' not in static_html
    assert 'href="/login"' not in static_html
    assert "Disponible solo en la version web" not in static_html


def test_cafe_demo_has_no_button_without_a_verified_200(surfaces):
    """Sin 200 verificado en la demo desplegada no hay botón de demo de Café.

    El texto de no disponible es texto plano: sin atributos y sin envoltorios
    con `title`, `aria-disabled`, `aria-label` o `tabindex`.
    """
    for name, html in surfaces.items():
        assert 'href="/cafe/"' not in html, name
        for tag in re.findall(r'<span class="demo-unavailable"[^>]*>', html):
            assert tag == '<span class="demo-unavailable">', f"{name}: {tag}"
        assert ">Demo no disponible</span>" in html, name


def test_static_omits_private_access_link(static_html):
    assert "Acceso privado" not in static_html


def test_web_keeps_private_access_link(web_html, portfolio):
    assert portfolio["footer"]["private_access"]["icon"] in web_html


def test_both_surfaces_expose_the_same_navigation(surfaces, portfolio):
    for name, html in surfaces.items():
        for item in portfolio["nav"]:
            assert f'href="{item["href"]}"' in html, f"{name} sin enlace {item['href']}"


def test_unavailable_demos_are_never_clickable(surfaces, portfolio):
    for name, html in surfaces.items():
        for project in portfolio["projects"]["items"]:
            for link in project["links"]:
                if link["available"] or not link["href"].startswith("http"):
                    continue
                assert f'href="{link["href"]}"' not in html, (
                    f"{name} renderiza como enlace clicable una demo caida: {link['href']}"
                )


def test_available_demos_are_clickable(web_html, portfolio):
    for project in portfolio["projects"]["items"]:
        for link in project["links"]:
            if link["available"] and link["href"].startswith("http"):
                assert f'href="{link["href"]}"' in web_html


def test_external_links_open_safely(surfaces):
    for name, html in surfaces.items():
        for match in re.finditer(r'<a [^>]*href="https://[^"]+"[^>]*>', html):
            tag = match.group(0)
            assert 'rel="noopener noreferrer"' in tag, f"{name}: {tag}"
            assert 'target="_blank"' in tag, f"{name}: {tag}"


def test_static_home_link_is_relative(static_html):
    assert 'href="./" class="nav-name"' in static_html


# ─── login / session ───


def test_login_form_has_csrf_field(client):
    body = client.get("/login").data.decode("utf-8")
    assert 'name="csrf_token"' in body


def test_login_without_csrf_is_rejected(client):
    response = client.post(
        "/login", data={"username": "test-user", "password": TEST_PASSWORD}
    )
    assert response.status_code == 400


def test_login_with_wrong_csrf_is_rejected(client, csrf):
    response = client.post(
        "/login",
        data={
            "username": "test-user",
            "password": TEST_PASSWORD,
            "csrf_token": "not-the-token",
        },
    )
    assert response.status_code == 400


def test_login_with_bad_password_shows_error(client, csrf):
    response = client.post(
        "/login",
        data={"username": "test-user", "password": "wrong", "csrf_token": csrf},
    )
    assert response.status_code == 200
    assert "Credenciales inválidas" in response.data.decode("utf-8")


def test_login_with_valid_credentials_grants_access(logged_in):
    private = logged_in.get("/familia")
    assert private.status_code == 200


def test_login_clears_previous_session(client, csrf):
    """`session.clear()` tras autenticar evita fijacion de sesion."""
    with client.session_transaction() as session:
        session["preexistente"] = "debe desaparecer"

    response = client.post(
        "/login",
        data={"username": "test-user", "password": TEST_PASSWORD, "csrf_token": csrf},
    )
    assert response.status_code == 302

    with client.session_transaction() as session:
        assert "preexistente" not in session
        assert session["authenticated"] is True


def test_logout_clears_the_whole_session(logged_in):
    with logged_in.session_transaction() as session:
        session["preexistente"] = "debe desaparecer"
    logged_in.get("/logout")
    with logged_in.session_transaction() as session:
        assert "preexistente" not in session
        assert "authenticated" not in session
        assert "csrf_token" not in session


def test_logout_revokes_access(logged_in):
    assert logged_in.get("/familia").status_code == 200
    logged_in.get("/logout")
    assert logged_in.get("/familia").status_code == 302


def test_authenticated_user_is_redirected_away_from_login(logged_in):
    response = logged_in.get("/login")
    assert response.status_code == 302
    assert "/familia" in response.headers["Location"]


def test_session_cookie_is_hardened(client, csrf):
    cookie = client.post(
        "/login",
        data={"username": "test-user", "password": TEST_PASSWORD, "csrf_token": csrf},
    ).headers.get("Set-Cookie", "")
    assert "HttpOnly" in cookie
    assert "SameSite=Lax" in cookie


def test_login_is_rate_limited(client):
    statuses = []
    for _ in range(8):
        token = re.search(
            r'name="csrf_token" value="([^"]+)"',
            client.get("/login").data.decode("utf-8"),
        ).group(1)
        response = client.post(
            "/login",
            data={"username": "x", "password": "y", "csrf_token": token},
        )
        statuses.append(response.status_code)
    assert 429 in statuses, f"el login nunca se limito: {statuses}"


def test_rate_limited_response_is_a_friendly_page(client):
    for _ in range(8):
        token = re.search(
            r'name="csrf_token" value="([^"]+)"',
            client.get("/login").data.decode("utf-8"),
        ).group(1)
        response = client.post(
            "/login", data={"username": "x", "password": "y", "csrf_token": token}
        )
        if response.status_code == 429:
            body = response.data.decode("utf-8")
            assert "Demasiados intentos" in body
            assert "Volver al portafolio" in body
            return
    pytest.fail("no se alcanzo el limite de 5 por minuto")


# ─── shared render helpers ───


def test_unknown_surface_is_rejected(portfolio, tmp_path):
    with pytest.raises(ValueError, match="superficie"):
        render.build_environment(tmp_path, "pdf", lambda p: p, portfolio["site"]["origin"])


def test_unknown_tier_is_rejected(portfolio, tmp_path):
    env = render.build_environment(
        tmp_path, render.SURFACE_STATIC, lambda p: p, portfolio["site"]["origin"]
    )
    with pytest.raises(ValueError, match="categoria"):
        env.globals["tier"]({"category": "ategoria inventada"})


def test_unknown_accent_is_rejected(portfolio, tmp_path):
    env = render.build_environment(
        tmp_path, render.SURFACE_STATIC, lambda p: p, portfolio["site"]["origin"]
    )
    with pytest.raises(ValueError, match="accent"):
        env.globals["accent"]({"accent": "rosa"})


def test_absolute_filter_keeps_absolute_urls(portfolio):
    helpers, absolute = render._make_helpers(
        render.SURFACE_STATIC, lambda p: f"static/{p}", portfolio["site"]["origin"]
    )
    origin = portfolio["site"]["origin"]
    assert absolute(f"/static/hero-poster.jpg") == f"{origin}/static/hero-poster.jpg"
    assert absolute("https://example.com/a.png") == "https://example.com/a.png"


def test_both_surfaces_share_the_same_css(surfaces):
    css_sets = set()
    for html in surfaces.values():
        blocks = re.findall(r"<style>(.*?)</style>", html, re.S)
        css_sets.add(hash("\n".join(blocks)))
    assert len(css_sets) == 1, "las superficies divergieron en el CSS embebido"


def test_render_helpers_are_html_escaped(portfolio):
    helpers, _ = render._make_helpers(
        render.SURFACE_STATIC, lambda p: p, portfolio["site"]["origin"]
    )
    rendered = helpers["action_link"](
        {"label": "<script>x</script>", "href": "https://e.com", "available": True}
    )
    assert "<script>" not in rendered
    assert "&lt;script&gt;" in rendered
