"""Consistencia de URLs entre los dos targets de despliegue.

Targets:
  - GitHub Pages -> index.html   (raiz del repo, se publica tal cual)
  - Flask        -> templates/base.html (Jinja)

Este archivo documenta la linea base real. Los fallos observados son
intencionales: equivalen a los problemas de URL pendientes de correccion.
NO se corrige ninguna URL aqui; solo se mide.
"""

import re
from pathlib import Path

import pytest

import content

INDEX = "index.html"
BASE = "templates/base.html"
CAFE_BASE = "templates/cafe/base.html"

# Dominios que el proyecto ya dejo de usar.
DOMINIOS_OBSOLETOS = [
    "benjaminberrio16.pythonanywhere.com",
    "alvaro345673344.pythonanywhere.com",
]

# URL verificada en produccion el 2026-09-25 (HTTP 200).
ROCKQUEST_CANONICO = "https://rockquest.onrender.com/"

# Dominio retirado: NXDOMAIN confirmado el 2026-09-25.
DOMINIO_NXDOMAIN = "alvaroberrio.dev"

# Canonical oficial (decision N-3). Sin barra final: `site.origin` se compara
# con `rstrip("/")` en content.py y las plantillas aportan la barra final.
CANONICO_APROBADO = "https://portfolio-hub-app.onrender.com"

TARGETS = [INDEX, BASE, CAFE_BASE]


def _leer(raiz, rel):
    return (raiz / rel).read_text(encoding="utf-8")


def _html_renderizado(client, ruta="/"):
    return client.get(ruta).get_data(as_text=True)


def _canonical(html):
    """Extrae el href del canonical de un documento ya renderizado."""
    match = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    assert match, 'el documento no declara <link rel="canonical">'
    return match.group(1)


@pytest.mark.parametrize("dominio", DOMINIOS_OBSOLETOS)
@pytest.mark.parametrize("fuente", TARGETS)
def test_sin_dominios_pythonanywhere(raiz, fuente, dominio):
    """Linea base: FALLA. PythonAnywhere fue retirado en la migracion a Render."""
    assert dominio not in _leer(raiz, fuente), (
        f"{fuente} todavia referencia {dominio}, que devuelve HTTP 404"
    )


def test_rockquest_usa_url_verificada(portfolio, surfaces):
    """RockQuest debe apuntar a la URL verificada en la fuente de verdad.

    El proyecto es data-driven: la URL se declara en data/portfolio.json y
    llega al HTML por renderizado, tanto en Flask como en el artefacto estatico
    que produce scripts/build_static.py. templates/base.html no la contiene a
    proposito, asi que exigir el literal ahi seria medir la capa equivocada y
    obligaria a hardcodear un dato que ya tiene una unica fuente.
    """
    proyecto = next(
        (p for p in portfolio["projects"]["items"] if p["name"] == "RockQuest"), None
    )
    assert proyecto is not None, "data/portfolio.json no declara el proyecto RockQuest"

    demo = next((l for l in proyecto["links"] if l["label"] == "Demo"), None)
    assert demo is not None, "RockQuest no declara un enlace de demo"
    assert demo["href"] == ROCKQUEST_CANONICO, (
        f"la fuente de verdad declara {demo['href']!r} en vez de {ROCKQUEST_CANONICO}"
    )
    assert demo.get("available") is True, "la demo verificada de RockQuest no debe marcarse caida"

    for nombre, html in surfaces.items():
        assert ROCKQUEST_CANONICO in html, (
            f"la superficie {nombre} no expone la URL verificada de RockQuest"
        )


def test_rockquest_no_tiene_dominio_retirado(client):
    html = _html_renderizado(client)
    for dominio in DOMINIOS_OBSOLETOS:
        assert dominio not in html, f"la pagina renderizada expone {dominio}"


def test_canonical_no_usa_dominio_nxdomain(portfolio, surfaces, client):
    """Decision del usuario: el canonical oficial es el despliegue de Render.

    El proyecto es data-driven: el canonical no vive en las plantillas, sale de
    `site.origin` en data/portfolio.json y las plantillas solo aportan la barra
    final. Exigir el literal en templates/*.html mediria la capa equivocada y
    obligaria a hardcodear un dato que ya tiene una unica fuente, asi que se
    validan la fuente de verdad y el HTML ya renderizado: el que produce Flask
    y el artefacto de scripts/build_static.py.
    """
    origin = portfolio["site"]["origin"]

    assert DOMINIO_NXDOMAIN not in origin, (
        f"site.origin declara {DOMINIO_NXDOMAIN}, que no existe en DNS"
    )
    assert origin == CANONICO_APROBADO, (
        f"site.origin es {origin!r} y no el canonical aprobado {CANONICO_APROBADO!r}"
    )
    assert origin.rstrip("/") == content.APPROVED_ORIGIN, (
        f"lockstep roto: site.origin={origin!r} vs APPROVED_ORIGIN="
        f"{content.APPROVED_ORIGIN!r}"
    )
    assert content.APPROVED_ORIGIN == CANONICO_APROBADO, (
        f"content.APPROVED_ORIGIN quedo en {content.APPROVED_ORIGIN!r}"
    )

    esperado = f"{CANONICO_APROBADO}/"
    for nombre, html in surfaces.items():
        assert DOMINIO_NXDOMAIN not in html, (
            f"la superficie {nombre} declara canonical {DOMINIO_NXDOMAIN}, que no existe en DNS"
        )
        assert _canonical(html) == esperado, (
            f"la superficie {nombre} declara canonical {_canonical(html)!r} "
            f"y deberia declarar {esperado!r}"
        )

    cafe = _html_renderizado(client, "/cafe/")
    assert DOMINIO_NXDOMAIN not in cafe, f"/cafe/ declara canonical {DOMINIO_NXDOMAIN}"
    assert _canonical(cafe) == f"{esperado}cafe/", (
        f"/cafe/ declara canonical {_canonical(cafe)!r} y deberia declarar "
        f"{esperado + 'cafe/'!r}"
    )


def test_canonical_unico_por_pagina(client):
    """Un solo canonical por pagina: los duplicados confunden a los buscadores."""
    for ruta in ["/", "/cafe/", "/cafe/productos"]:
        html = _html_renderizado(client, ruta)
        assert html.count('rel="canonical"') == 1, f"{ruta} no tiene exactamente un canonical"


@pytest.mark.parametrize("ruta", ["/", "/cafe/"])
def test_sin_email_placeholder(client, ruta):
    """Linea base: FALLA. Hay un mailto: de ejemplo en produccion."""
    html = _html_renderizado(client, ruta)
    assert "example.com" not in html, f"{ruta} expone un email de ejemplo (RFC 2606)"


@pytest.mark.parametrize("ruta", ["/", "/cafe/"])
def test_sin_linkedin_generico(client, ruta):
    """Ninguna pagina debe enlazar a la portada de LinkedIn.

    Decision N-2 del usuario: la URL real se proporciono y quedo en
    `contact.linkedin` (data/portfolio.json). El proyecto es data-driven, asi
    que el perfil se propaga solo a las dos superficies; este test vigila que
    ningun href vuelva a la portada generica `https://linkedin.com`, que no
    lleva a ningun perfil.
    """
    html = _html_renderizado(client, ruta)
    assert not re.search(r'href="https://linkedin\.com/?["?]', html), (
        f"{ruta} enlaza a la portada de LinkedIn en vez de a un perfil"
    )


def test_enlaces_de_codigo_no_apuntan_al_perfil_generico(raiz):
    """Linea base: FALLA. 4 code-links por target caen en el perfil generico."""
    perfil = "https://github.com/alvaroberrio23242-eng"
    patron = re.compile(rf'href="{re.escape(perfil)}"[^>]*>\s*(C[^<]*odigo|Ver c[^<]*)', re.I)
    for fuente in [INDEX, BASE]:
        html = _leer(raiz, fuente)
        coincidencias = patron.findall(html)
        assert not coincidencias, (
            f"{fuente}: {len(coincidencias)} boton(es) de 'Codigo' apuntan al perfil "
            f"generico en vez de al repositorio del proyecto"
        )


def test_pages_no_usa_rutas_absolutas_raiz(raiz):
    """Linea base: FALLA con 4 referencias.

    GitHub Pages sirve en /portfolio-hub/, por lo que una ruta absoluta
    /static/... resuelve fuera del proyecto y devuelve 404. Verificado por
    HTTP el 2026-09-25.
    """
    html = _leer(raiz, INDEX)
    absolutas = re.findall(r'(?:src|href|poster)="/(?!/)[^"]*"', html)
    assert not absolutas, (
        "index.html usa rutas absolutas que rompen en GitHub Pages: "
        + ", ".join(sorted(set(absolutas)))
    )


def test_pages_tiene_almenos_un_assets_correcto(raiz):
    """Linea base: FALLA. Ningun thumbnail del evidence-strip carga hoy."""
    html = _leer(raiz, INDEX)
    relativa = re.search(r'src="(?!/|https?:|//)(static/[^"]+)"', html)
    assert relativa, (
        "index.html no referencia ningun asset con ruta relativa; "
        "las miniaturas del evidence-strip no cargan en Pages"
    )
    assert (raiz / relativa.group(1)).is_file(), f"no existe {relativa.group(1)}"


def test_urls_railway_consistentes(raiz):
    """Linea base: FALLA. Railway aparece con y sin barra final."""
    for fuente in [INDEX, BASE]:
        html = _leer(raiz, fuente)
        for m in re.finditer(r'https://[a-z0-9.\-]*\.up\.railway\.app(/)?["\s]', html):
            sin_slash = m.group(1) == ""
            ctx = html[max(0, m.start() - 200) : m.start()]
            etiqueta = "BROKEN" if "REQUIERE DECISI" in ctx else "Demo"
            assert not sin_slash or etiqueta == "BROKEN", (
                f"{fuente}: URL de Railway sin barra final: {m.group(0).strip()}"
            )


def test_demos_caidas_estan_marcadas(raiz):
    """Linea base: FALLA. EduPack y OSINT devuelven 404 y no lo declaran.

    Decision del usuario: marcarlos como 'BROKEN / REQUIERE DECISION' sin
    cambiar la URL.
    """
    for fuente in [INDEX, BASE]:
        html = _leer(raiz, fuente)
        for host in ["web-production-0f3c8.up.railway.app", "osintsearchpro-production"]:
            if host in html:
                idx = html.find(host)
                contexto = html[max(0, idx - 400) : idx + 400]
                assert "BROKEN" in contexto, (
                    f"{fuente}: {host} devuelve 404 pero no se marca como roto"
                )


def test_sin_urls_de_archivos_locales(raiz):
    """Ningun target debe enlazar a rutas de desarrollo."""
    for fuente in TARGETS:
        html = _leer(raiz, fuente)
        for patron in [r'href="/?[A-Za-z]:\\', r'href="/?Users/', r'href="/?home/']:
            assert not re.search(patron, html), f"{fuente} expone una ruta local"
