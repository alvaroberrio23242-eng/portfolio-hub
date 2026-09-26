"""`index.html` es un artefacto: debe estar siempre regenerado desde la fuente."""

import re

from conftest import BASE_DIR
from scripts import build_static

INDEX = BASE_DIR / "index.html"


def test_index_is_regenerated_up_to_date():
    assert build_static.build(check=True) == 0


def test_index_exists_and_is_not_empty():
    assert INDEX.is_file()
    assert INDEX.stat().st_size > 20_000


def test_index_declares_itself_generated():
    head = INDEX.read_text(encoding="utf-8")[:400]
    assert "scripts/build_static.py" in head
    assert "data/portfolio.json" in head


def test_index_has_no_unrendered_jinja(static_html):
    assert "{{" not in static_html
    assert "{%" not in static_html


def test_index_has_no_flask_only_helpers(static_html):
    for helper in ("url_for", "csrf_token", "STATIC_ONLY_NOTE"):
        assert helper not in static_html


def test_index_has_no_dead_mp4_references(static_html, portfolio):
    """Los .mp4 de caso que se rompian (404 en el sitio) ya no se referencian."""
    assert "case-studies/" not in static_html
    declared = {src for _, src in _media_paths(portfolio)}
    for src in re.findall(r'static/([\w./-]+\.mp4)', static_html):
        assert src in declared, f"index.html referencia un mp4 no declarado: {src}"


def _media_paths(portfolio):
    from conftest import iter_media

    return iter_media(portfolio)


def test_template_and_data_are_the_only_sources():
    """No debe quedar copy del hub escrito a mano en el template."""
    template = (BASE_DIR / "templates" / "base.html").read_text(encoding="utf-8")
    body = template.split("</style>", 1)[-1]
    for leaked in (
        "Python",
        "Flask",
        "SQLAlchemy",
        "berriobenjamin16",
        "SalsaQuest",
        "RockQuest",
    ):
        assert leaked not in body, f"copy hardcodeado en el template: {leaked}"


def test_template_has_no_dead_conditional_blocks():
    template = (BASE_DIR / "templates" / "base.html").read_text(encoding="utf-8")
    assert "{% if False %}" not in template
    assert "OCULTA DESDE" not in template


def test_build_is_deterministic():
    assert build_static.render_html() == build_static.render_html()
