"""Carga y validacion de la fuente de verdad del contenido del hub.

Los datos viven en `data/portfolio.json`. Tanto la app Flask como el generador
estatico (`scripts/build_static.py`) los consumen desde aqui, de modo que
ninguna superficie puede desincronizarse del contenido.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "portfolio.json"

SECTIONS = (
    "site",
    "nav",
    "hero",
    "capabilities",
    "evidence",
    "case_studies",
    "projects",
    "about",
    "contact",
    "footer",
)

APPROVED_ORIGIN = "https://portfolio-hub-app.onrender.com"

# `contact.linkedin` debe apuntar al perfil, nunca a la portada: un boton que
# lleva a linkedin.com no identifica a nadie y ademas engines lo pueden leer como
# un perfil duplicado. El placeholder se elimino de data/portfolio.json cuando se
# confirmo la URL real, asi que la regresion debe romper aqui y no en el sitio.
PERFILO_LINKEDIN = re.compile(r"^https://([a-z]{2,3}\.)?linkedin\.com/in/[A-Za-z0-9_-]+/?$")

# Deuda conocida que la verificacion del 2026-09-26 dejo pendiente de confirmar
# con el usuario. No se inventan valores: se declaran para que los tests fallen
# si alguien los reintroduce como enlaces utilizables.
UNAVAILABLE_URLS = frozenset(
    {
        "https://web-production-0f3c8.up.railway.app",
        "https://osintsearchpro-production.up.railway.app/",
        "https://alvaro345673344.pythonanywhere.com/",
        "https://benjaminberrio16.pythonanywhere.com/",
    }
)

KNOWN_GAPS = {
    "unavailable_urls": tuple(sorted(UNAVAILABLE_URLS)),
    "og_image_placeholder": (
        "site.og_image reutiliza hero-poster.jpg; falta una tarjeta social 1200x630 propia."
    ),
    "cafe_og_image_placeholder": (
        "Las fotos de /cafe/ son genericas y documentadas como tales en /cafe/decisiones; "
        "falta una imagen de marca propia para Open Graph."
    ),
    "product_photos_missing": (
        "Los 5 products-*.png no existen; se omite 'image' en el JSON-LD de producto en vez "
        "de apuntar a una foto generica que contradiga /cafe/decisiones."
    ),
}


class ContentError(ValueError):
    """La fuente de verdad no cumple el contrato minimo."""


def _require(mapping, key, path):
    if not isinstance(mapping, dict):
        raise ContentError(f"'{path}' debe ser un objeto, no {type(mapping).__name__}")
    if key not in mapping:
        raise ContentError(f"Falta '{path}.{key}' en {DATA_PATH.name}")
    return mapping[key]


def _require_list(mapping, key, path, min_len=1):
    value = _require(mapping, key, path)
    if not isinstance(value, list) or len(value) < min_len:
        raise ContentError(f"'{path}.{key}' debe ser una lista con al menos {min_len} elemento(s)")
    return value


def _check_media(media, path):
    kind = _require(media, "kind", path)
    if kind not in ("image", "video"):
        raise ContentError(f"'{path}.kind' debe ser 'image' o 'video', no {kind!r}")
    _require(media, "src", path)
    if kind == "video":
        _require(media, "poster", path)


def _check_links(links, path):
    for i, link in enumerate(links):
        where = f"{path}[{i}]"
        label = _require(link, "label", where)
        href = _require(link, "href", where)
        if not isinstance(label, str) or not label.strip():
            raise ContentError(f"'{where}.label' no puede estar vacio")
        if not isinstance(href, str) or not href:
            raise ContentError(f"'{where}.href' no puede estar vacio")
        if "available" not in link:
            raise ContentError(f"'{where}.available' es obligatorio (los enlaces caidos se declaran, no se ocultan)")
        if link["available"] is False and not (link.get("note") or "").strip():
            raise ContentError(
                f"'{where}' se declara no disponible y debe explicar por que en 'note'; "
                "un enlace caido sin explicacion se pierde en silencio"
            )


def validate(data):
    """Valida el contrato minimo. Lanza ContentError si algo falta."""
    if not isinstance(data, dict):
        raise ContentError("La raiz del JSON debe ser un objeto")

    for key in SECTIONS:
        _require(data, key, "<root>")

    site = data["site"]
    for key in ("origin", "locale", "title", "description", "og_title", "og_description", "og_image"):
        _require(site, key, "site")
    if not str(site["origin"]).startswith("https://"):
        raise ContentError("site.origin debe ser una URL https://")
    if site["origin"].rstrip("/") != APPROVED_ORIGIN:
        raise ContentError(
            f"site.origin cambio respecto al dominio oficial autorizado ({APPROVED_ORIGIN}): {site['origin']!r}"
        )

    nav = _require_list(data, "nav", "<root>")
    for i, item in enumerate(nav):
        _require(item, "label", f"nav[{i}]")
        href = _require(item, "href", f"nav[{i}]")
        if not href.startswith("#"):
            raise ContentError(f"nav[{i}].href debe ser un ancla interna, no {href!r}")

    hero = data["hero"]
    for key in ("eyebrow", "headline", "headline_emphasis", "lead", "avatar", "actions", "media"):
        _require(hero, key, "hero")
    _check_media(hero["media"], "hero.media")
    _check_links(hero["actions"], "hero.actions")

    caps = data["capabilities"]
    _require(caps, "heading", "capabilities")
    for i, item in enumerate(_require_list(caps, "items", "capabilities")):
        for key in ("icon", "title", "text", "pills", "accent"):
            _require(item, key, f"capabilities.items[{i}]")
        if item["accent"] not in ("amber", "teal", "magenta", "muted"):
            raise ContentError(f"'capabilities.items[{i}].accent' debe ser amber, teal, magenta o muted")

    for i, item in enumerate(_require_list(data, "evidence", "<root>")):
        where = f"evidence[{i}]"
        for key in ("name", "url", "status", "available", "media", "note"):
            _require(item, key, where)
        _check_media(item["media"], f"{where}.media")
        if not isinstance(item["available"], bool):
            raise ContentError(f"'{where}.available' debe ser booleano")
        if not item["available"] and not item["note"]:
            raise ContentError(f"'{where}' no disponible exige una nota que explique por que")

    cases = data["case_studies"]
    _require(cases, "heading", "case_studies")
    seen_cases = set()
    for i, case in enumerate(_require_list(cases, "items", "case_studies")):
        where = f"case_studies.items[{i}]"
        for key in ("name", "icon", "badge", "caption", "context", "problem", "solution", "features", "tech", "links", "media"):
            _require(case, key, where)
        if case["name"] in seen_cases:
            raise ContentError(f"Caso de estudio duplicado: {case['name']}")
        seen_cases.add(case["name"])
        _require_list(case, "features", where, min_len=0)
        _require_list(case, "tech", where)
        _check_links(case["links"], f"{where}.links")
        _check_media(case["media"], f"{where}.media")

    projects = data["projects"]
    _require(projects, "heading", "projects")
    seen = set()
    for i, project in enumerate(_require_list(projects, "items", "projects")):
        where = f"projects.items[{i}]"
        for key in ("name", "category", "status", "accent", "tag", "description", "features", "tech", "links"):
            _require(project, key, where)
        if project["name"] in seen:
            raise ContentError(f"Proyecto duplicado en projects.items: {project['name']}")
        seen.add(project["name"])
        if project["accent"] not in ("amber", "teal", "muted"):
            raise ContentError(f"'{where}.accent' debe ser amber, teal o muted")
        _require_list(project, "features", where, min_len=0)
        _require_list(project, "tech", where)
        _check_links(project["links"], f"{where}.links")

    about = data["about"]
    for key in ("name", "avatar", "paragraphs", "list"):
        _require(about, key, "about")
    _require_list(about, "paragraphs", "about")
    for i, item in enumerate(about["list"]):
        _require(item, "label", f"about.list[{i}]")
        _require(item, "value", f"about.list[{i}]")

    contact = data["contact"]
    for key in ("headline", "sub", "email", "whatsapp", "github", "linkedin"):
        _require(contact, key, "contact")
    if "@" not in contact["email"] or contact["email"].endswith("@example.com"):
        raise ContentError("contact.email debe ser una direccion real, no un placeholder")
    if not contact["whatsapp"].startswith("https://wa.me/"):
        raise ContentError("contact.whatsapp debe usar el formato https://wa.me/<pais><numero>")
    if not contact["github"].startswith("https://github.com/"):
        raise ContentError("contact.github debe apuntar a un perfil de GitHub")
    if not PERFILO_LINKEDIN.match(contact["linkedin"]):
        raise ContentError(
            "contact.linkedin debe apuntar al perfil (https://www.linkedin.com/in/<slug>), "
            f"no a la portada: {contact['linkedin']!r}"
        )

    footer = data["footer"]
    for key in ("copyright", "updated"):
        _require(footer, key, "footer")
    _require(footer, "private_access", "footer")
    for key in ("label", "href", "icon"):
        _require(footer["private_access"], key, "footer.private_access")

    return data


def load(path=None):
    """Lee, parsea y valida la fuente de verdad."""
    target = Path(path) if path else DATA_PATH
    try:
        raw = target.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ContentError(f"No existe la fuente de verdad: {target}") from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ContentError(f"{DATA_PATH.name} no es JSON valido: {exc}") from exc
    return validate(data)
