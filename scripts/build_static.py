"""Genera `index.html` a partir de `templates/base.html` + `data/portfolio.json`.

La version estatica (GitHub Pages) no puede usar `url_for`, asi que los assets se
emiten con rutas relativas a `static/`. Es el unico lugar donde se produce
`index.html`: el archivo es un artefacto, no una fuente.

Uso:
    python scripts/build_static.py [--check] [--out index.html]
"""

import argparse
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

import content
import render

TEMPLATES_DIR = BASE_DIR / "templates"
DEFAULT_OUT = BASE_DIR / "index.html"

GENERATED_NOTICE = "<!-- Generado por scripts/build_static.py desde templates/base.html y data/portfolio.json. No editar a mano. -->"


def render_html():
    """Renderiza el sitio estatico completo y devuelve el HTML."""
    data = content.load()
    env = render.build_environment(
        templates_dir=TEMPLATES_DIR,
        surface=render.SURFACE_STATIC,
        asset_url=lambda path: f"static/{path}",
        origin=data["site"]["origin"],
        home_url="./",
    )
    html = env.get_template(render.TEMPLATE).render(
        site=data["site"],
        nav=data["nav"],
        hero=data["hero"],
        evidence=data["evidence"],
        case_studies=data["case_studies"],
        capabilities=data["capabilities"],
        projects=data["projects"],
        about=data["about"],
        contact=data["contact"],
        footer=data["footer"],
    )
    return GENERATED_NOTICE + "\n" + html.strip() + "\n"


def build(out_path=None, check=False):
    """Compara o escribe `index.html`. Con `check`, solo verifica."""
    body = render_html()
    target = Path(out_path) if out_path else DEFAULT_OUT

    if check:
        current = target.read_text(encoding="utf-8") if target.exists() else ""
        if current != body:
            print(f"DESACTUALIZADO: {target.name} no coincide con la fuente de verdad.")
            return 1
        print(f"OK: {target.name} esta sincronizado con data/portfolio.json.")
        return 0

    target.write_text(body, encoding="utf-8")
    print(f"Escrito {target} ({len(body):,} bytes) desde data/portfolio.json")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verifica sincronizacion sin escribir")
    parser.add_argument("--out", default=None, help="ruta de salida (por defecto index.html)")
    args = parser.parse_args(argv)
    return build(out_path=args.out, check=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
