"""Integridad de los enlaces: nada de URLs rotas presentadas como utilizables."""

import re

import pytest

import content
from conftest import iter_links

EXTERNAL_PREFIXES = ("https://",)


def test_no_external_uses_insecure_http(surfaces):
    for name, html in surfaces.items():
        for match in re.finditer(r'href="(http://[^"]+)"', html):
            pytest.fail(f"{name} enlaza por http sin cifrar: {match.group(1)}")


def test_no_usable_link_points_to_a_known_dead_url(portfolio):
    for where, link in iter_links(portfolio):
        if link["available"]:
            assert link["href"] not in content.UNAVAILABLE_URLS, (
                f"{where} marco como disponible una URL verificada como caída: {link['href']}"
            )


def test_no_usable_link_points_to_a_dead_internal_route(client, portfolio):
    known = {rule.rule for rule in client.application.url_map.iter_rules()}
    for where, link in iter_links(portfolio):
        href = link["href"]
        if not href.startswith("/") or not link["available"]:
            continue
        assert href in known, f"{where} apunta a una ruta inexistente: {href}"


def test_mail_targets_the_approved_address(portfolio):
    assert portfolio["contact"]["email"] == "berriobenjamin16@gmail.com"
    assert "@gmail.com" in portfolio["contact"]["email"]


def test_whatsapp_number_is_the_approved_one(portfolio):
    assert portfolio["contact"]["whatsapp"] == "https://wa.me/573165192825"


def test_github_links_are_absolute(surfaces):
    for name, html in surfaces.items():
        for match in re.finditer(r'href="([^"]*github\.com[^"]*)"', html):
            assert match.group(1).startswith(EXTERNAL_PREFIXES), f"{name}: {match.group(1)}"


def test_no_link_points_to_a_local_file(surfaces):
    for name, html in surfaces.items():
        for match in re.finditer(r'href="([^"]+\.(?:py|json|md|yml|ini|txt))"', html):
            pytest.fail(f"{name} enlaza a un archivo del repositorio: {match.group(1)}")


def test_repo_links_are_specific_or_explicitly_profiled(portfolio):
    """Los enlaces 'Codigo' apuntan al repo real o declaran que es privado."""
    for project in portfolio["projects"]["items"]:
        for link in project["links"]:
            if link["label"] != "Código":
                continue
            if link["href"].rstrip("/") == portfolio["contact"]["github"]:
                assert link.get("note"), (
                    f"{project['name']} apunta al perfil de GitHub sin explicar por que"
                )


def test_verified_working_demos_are_marked_available(portfolio):
    """Estas tres respondieron 200 en la verificacion del 2026-09-26."""
    working = {
        "https://salsaquest-1.onrender.com/",
        "https://rockquest.onrender.com/",
        "https://alvaroberrio23242-eng.github.io/aventura-antioquena-web/",
        "https://alvaroberrio23242-eng.itch.io/aventura-antioquea",
    }
    for where, link in iter_links(portfolio):
        if link["href"] in working:
            assert link["available"], f"{where} declara caida una URL verificada: {link['href']}"


def test_evidence_cards_match_their_destination(portfolio):
    for item in portfolio["evidence"]:
        assert item["url"].startswith(("http://", "https://", "/")), item["name"]
        assert item["status"].strip()


def test_static_renders_no_anchor_to_a_missing_page(static_html):
    for match in re.finditer(r'href="(#[^"]+)"', static_html):
        anchor = match.group(1)
        assert f'id="{anchor[1:]}"' in static_html, f"ancla rota: {anchor}"


def test_no_trailing_whitespace_in_generated_output(static_html):
    for number, line in enumerate(static_html.splitlines(), start=1):
        assert line == line.rstrip(), f"index.html linea {number} con espacios al final"


def test_generated_output_ends_with_newline(static_html):
    assert static_html.endswith("\n")
