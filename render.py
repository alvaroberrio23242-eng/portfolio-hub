"""Render compartido del hub: un unico template, dos superficies.

`templates/base.html` es la unica fuente de markup. La app Flask lo sirve con
`url_for('static', ...)` y el generador estatico lo renderiza con rutas
relativas a `static/`. Los helpers viven aqui para que ambas superficies
produzcan exactamente el mismo HTML salvo por las URLs.
"""

from markupsafe import Markup, escape
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATE = "base.html"
SURFACE_WEB = "web"
SURFACE_STATIC = "static"

ACCENTS = {
    "amber": "var(--amber)",
    "teal": "var(--teal)",
    "magenta": "var(--magenta)",
    "muted": "var(--muted)",
}

TIERS = {
    "Brand & Business": "tier-1",
    "Product Proof": "tier-2",
    "Technical Proof": "tier-3",
}

STATIC_ONLY_NOTE = "Disponible solo en la version web (portfolio-hub-app.onrender.com)."


def _make_helpers(surface, asset_url, origin):
    if surface not in (SURFACE_WEB, SURFACE_STATIC):
        raise ValueError(f"superficie desconocida: {surface!r}")

    def accent(item):
        try:
            return ACCENTS[item["accent"]]
        except KeyError as exc:
            raise ValueError(f"accent desconocido: {item.get('accent')!r}") from exc

    def tier(project):
        try:
            return TIERS[project["category"]]
        except KeyError as exc:
            raise ValueError(f"categoria desconocida: {project.get('category')!r}") from exc

    def media_tag(media, name, lazy=False):
        loading = ' loading="lazy" decoding="async"' if lazy else ' decoding="async"'
        alt = escape(name)
        if media["kind"] == "video":
            return Markup(
                '<video class="evidence-thumb" autoplay muted loop playsinline'
                ' preload="metadata"'
                f' poster="{escape(asset_url(media["poster"]))}" aria-hidden="true" tabindex="-1">'
                f'<source src="{escape(asset_url(media["src"]))}" type="video/mp4">'
                "</video>"
            )
        return Markup(
            f'<img class="evidence-thumb" src="{escape(asset_url(media["src"]))}"'
            f' alt="{alt}"{loading} width="480" height="300">'
        )

    def action_link(link, compact=False):
        base = "btn btn-compact" if compact else "btn"
        label = escape(link["label"])
        href = link.get("href") or ""
        note = link.get("note") or ""
        is_external = href.startswith(("http://", "https://"))

        if not link.get("available", True):
            text = link.get("unavailable_text") or f"{link['label']} no disponible"
            return Markup(f'<span class="demo-unavailable">{escape(text)}</span>')

        if href.startswith("/") and surface == SURFACE_STATIC:
            return Markup(
                f'<span class="{base} btn-disabled" role="link" aria-disabled="true"'
                f' title="{escape(STATIC_ONLY_NOTE)}">{label}</span>'
            )

        if is_external:
            attrs = ' target="_blank" rel="noopener noreferrer"'
        else:
            attrs = ""
        title_attr = f' title="{escape(note)}"' if note else ""
        return Markup(f'<a class="{base}" href="{escape(href)}"{attrs}{title_attr}>{label} ↗</a>')

    def absolute(url):
        if url.startswith(("http://", "https://")):
            return url
        return f"{origin.rstrip('/')}/{url.lstrip('/')}"

    return {
        "surface": surface,
        "home_url": "/",
        "asset": asset_url,
        "accent": accent,
        "tier": tier,
        "media_tag": media_tag,
        "action_link": action_link,
    }, absolute


def build_environment(templates_dir, surface, asset_url, origin, home_url="./"):
    """Entorno Jinja autonomouso, usado por el generador estatico."""
    helpers, absolute = _make_helpers(surface, asset_url, origin)
    helpers["home_url"] = home_url
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["absolute"] = absolute
    env.globals.update(helpers)
    return env


def configure_flask(app, data):
    """Inyecta los mismos helpers en el entorno Jinja de la app Flask."""
    from flask import url_for

    helpers, absolute = _make_helpers(
        SURFACE_WEB, lambda path: url_for("static", filename=path), data["site"]["origin"]
    )
    app.jinja_env.filters["absolute"] = absolute
    app.jinja_env.globals.update(helpers)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
