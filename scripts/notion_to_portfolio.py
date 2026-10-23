"""Actualiza data/portfolio.json desde la base Proyectos de Notion.

Solo toca lo que Notion puede comprobar: el enlace de demo de cada proyecto (disponible o no) y,
para que no se contradigan, la etiqueta de estado entre "Demo no disponible" y "Demo en línea".
Textos, descripciones, funciones y tecnologías siguen en el JSON. Nunca baja una demo por un
fallo de verificación (solo avisa) y nunca agrega proyectos.

Uso:
    python scripts/notion_to_portfolio.py            muestra qué cambiaría (no escribe)
    python scripts/notion_to_portfolio.py --aplicar  escribe el JSON, regenera index.html y corre los tests;
                                                     si algo falla, revierte

Variable: NOTION_TOKEN (o archivo .env en este repo o en ../notion-sync).
"""
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
JSON_PATH = BASE_DIR / "data" / "portfolio.json"
API = "https://api.notion.com/v1"
VERSION = "2022-06-28"
PREFIJO = "Verificación de deploy: "
APLICAR = "--aplicar" in sys.argv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def cargar_token():
    t = os.environ.get("NOTION_TOKEN")
    if t:
        return t.strip()
    for ruta in (BASE_DIR / ".env", BASE_DIR.parent / "notion-sync" / ".env"):
        if ruta.exists():
            for linea in ruta.read_text(encoding="utf-8-sig").splitlines():
                linea = linea.strip()
                if linea.startswith("NOTION_TOKEN") and "=" in linea:
                    return linea.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("Falta NOTION_TOKEN (variable de entorno o .env)")


HEAD = {
    "Authorization": f"Bearer {cargar_token()}",
    "Notion-Version": VERSION,
    "Content-Type": "application/json",
}


def notion(metodo, ruta, cuerpo=None):
    datos = json.dumps(cuerpo).encode("utf-8") if cuerpo is not None else None
    req = urllib.request.Request(API + ruta, data=datos, method=metodo, headers=HEAD)
    for _ in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                time.sleep(0.35)
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(float(e.headers.get("Retry-After", 1)))
                continue
            sys.exit(f"Error de Notion {e.code} en {metodo} {ruta}: {e.read().decode('utf-8', 'ignore')[:300]}")
    sys.exit("Notion limitó las peticiones; vuelve a intentar en un minuto")


def consultar(db_id):
    out, cursor = [], None
    while True:
        cuerpo = {"page_size": 100}
        if cursor:
            cuerpo["start_cursor"] = cursor
        r = notion("POST", f"/databases/{db_id}/query", cuerpo)
        out += r["results"]
        if not r.get("has_more"):
            return out
        cursor = r["next_cursor"]


def texto(prop):
    t = prop["type"]
    if t in ("title", "rich_text"):
        return "".join(x.get("plain_text", "") for x in prop[t]).strip()
    if t == "url":
        return (prop["url"] or "").strip()
    return ""


def titulo_fila(fila):
    for p in fila["properties"].values():
        if p["type"] == "title":
            return texto(p)
    return ""


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


def norm_url(u):
    return re.sub(r"^https?://", "", u.strip().lower()).rstrip("/")


def es_demo(link):
    e = str(link.get("label", "")).lower()
    return "demo" in e or e.startswith("jugar")


def leer_notion():
    bases, cursor = [], None
    while True:
        cuerpo = {"filter": {"property": "object", "value": "database"}, "page_size": 100}
        if cursor:
            cuerpo["start_cursor"] = cursor
        r = notion("POST", "/search", cuerpo)
        bases += r["results"]
        if not r.get("has_more"):
            break
        cursor = r["next_cursor"]
    regs = [b for b in bases
            if "".join(t.get("plain_text", "") for t in b.get("title", [])).strip().lower() == "registro de cambios"
            and "Proyecto" in b["properties"] and "Fecha" in b["properties"]]
    if not regs:
        sys.exit("No encontré la base 'Registro de cambios'. ¿La conexión tiene acceso?")
    regs.sort(key=lambda b: b.get("last_edited_time", ""), reverse=True)
    registro = regs[0]
    proy_id = registro["properties"]["Proyecto"]["relation"]["database_id"]

    ultimo = {}
    for f in sorted(consultar(registro["id"]), key=lambda x: x.get("created_time", "")):
        t = titulo_fila(f)
        if not t.startswith(PREFIJO):
            continue
        estado = "OK" if t.endswith("(OK)") else "FALLÓ" if t.endswith("(FALLÓ)") else None
        if estado:
            for rel in f["properties"].get("Proyecto", {}).get("relation", []):
                ultimo[rel["id"]] = estado

    filas = {}
    for f in consultar(proy_id):
        p = f["properties"]
        nombre = titulo_fila(f)
        fecha = (p.get("Última verificación", {}).get("date") or {}).get("start", "")
        filas[norm(nombre)] = {
            "nombre": nombre,
            "url": texto(p["Deploy (URL)"]) if "Deploy (URL)" in p else "",
            "estado": ultimo.get(f["id"]),
            "verificado": fecha,
            "publicar": p.get("Publicar", {}).get("checkbox", False),
        }
    return filas


def revisar(data, filas):
    cambios, avisos, sin_publicar = [], [], []
    secciones = [("projects", data["projects"]["items"]), ("case_studies", data["case_studies"]["items"])]
    print(f"{'sección':13} {'proyecto':22} {'Notion':7} {'verificado':11} {'Publicar':9} demo en el JSON")
    for seccion, items in secciones:
        for it in items:
            n = it["name"]
            fila = filas.get(norm(n))
            links = it.get("links") if isinstance(it.get("links"), list) else []
            demo = next((l for l in links if es_demo(l)), None)
            if demo is None:
                desc = "(sin enlace de demo)"
            else:
                desc = ("disponible " if demo.get("available", True) else "NO disponible ") + str(demo.get("href", ""))
            if not fila:
                print(f"{seccion:13} {n:22} {'--':7} {'--':11} {'--':9} {desc}")
                avisos.append(f"{n}: no existe en la base de Notion")
                continue
            est = fila["estado"] or ("?" if fila["url"] else "--")
            print(f"{seccion:13} {n:22} {est:7} {fila['verificado'] or '--':11} {'sí' if fila['publicar'] else 'no':9} {desc} | status: {it.get('status', '-')}")
            if not fila["publicar"]:
                sin_publicar.append(n)
            url, estado = fila["url"], fila["estado"]
            disponible = demo is not None and demo.get("available", True)
            href = str(demo.get("href", "")) if demo is not None else ""
            if disponible and not url:
                avisos.append(f"{n}: el JSON muestra demo disponible ({href}) pero Notion no tiene URL verificada")
            if url and estado == "OK":
                if demo is None:
                    avisos.append(f"{n}: Notion tiene URL verificada ({url}) pero el JSON no tiene enlace de demo")
                elif norm_url(href) == norm_url(url):
                    if not disponible:
                        cambios.append({"item": it, "demo": demo, "href": None,
                                        "texto": f"{n}: habilitar el enlace de demo (ya apunta a la URL verificada {url})"})
                    elif it.get("status") == "Demo no disponible":
                        cambios.append({"item": it, "demo": demo, "href": None,
                                        "texto": f"{n}: la demo ya está disponible y verificada, pero la etiqueta dice 'Demo no disponible'; cambiar a 'Demo en línea'"})
                elif disponible:
                    avisos.append(f"{n}: la demo del JSON ({href}) difiere de la URL de Notion ({url}); no la toco")
                else:
                    cambios.append({"item": it, "demo": demo, "href": url,
                                    "texto": f"{n}: reemplazar href '{href}' por '{url}' y habilitar la demo"})
            elif url and disponible and norm_url(href) == norm_url(url):
                avisos.append(f"{n}: la URL no está verificada OK en Notion (estado: {estado or 'sin verificar'}) pero el JSON la muestra disponible")
    return cambios, avisos, sin_publicar


def aplicar_cambio(c):
    if c["href"]:
        c["demo"]["href"] = c["href"]
    c["demo"]["available"] = True
    if c["item"].get("status") == "Demo no disponible":
        c["item"]["status"] = "Demo en línea"


def correr(cmd):
    env = {**os.environ, "PYTHONUTF8": "1"}
    return subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", env=env)


def aplicar(data, cambios):
    if not cambios:
        print("Nada que aplicar.")
        return
    sucio = correr(["git", "status", "--porcelain", "data/portfolio.json", "index.html"]).stdout.strip()
    if sucio:
        sys.exit("data/portfolio.json o index.html tienen cambios sin commit; no aplico para poder revertir limpio.")
    for c in cambios:
        aplicar_cambio(c)
    with open(JSON_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    for nombre, cmd in (("regenerar index.html", ["python", "scripts/build_static.py"]),
                        ("tests", ["python", "-m", "pytest", "-q"])):
        r = correr(cmd)
        if r.returncode != 0:
            correr(["git", "checkout", "--", "data/portfolio.json", "index.html"])
            print(f"FALLÓ {nombre}; cambios revertidos.")
            print(((r.stdout or "") + (r.stderr or ""))[-1500:])
            sys.exit(1)
    print("Aplicado: JSON actualizado, index.html regenerado y tests en verde.")


def main():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8-sig"))
    filas = leer_notion()
    print(f"Modo: {'APLICAR' if APLICAR else 'SOLO MOSTRAR (no escribe)'}\n")
    cambios, avisos, sin_publicar = revisar(data, filas)
    pub = lambda c: filas.get(norm(c["item"]["name"]), {}).get("publicar")
    for c in [c for c in cambios if not pub(c)]:
        avisos.append(f"{c['item']['name']}: hay un cambio pendiente pero 'Publicar' no está marcado en Notion")
    cambios = [c for c in cambios if pub(c)]
    print("\n===== CAMBIOS PROPUESTOS =====")
    for c in cambios:
        print("  *", c["texto"])
    if not cambios:
        print("  (ninguno)")
    print("\n===== AVISOS (no se tocan) =====")
    for a in avisos:
        print("  !", a)
    if not avisos:
        print("  (ninguno)")
    if sin_publicar:
        print("\nEn el portafolio pero con 'Publicar' sin marcar en Notion:", ", ".join(sin_publicar))
    if APLICAR:
        aplicar(data, cambios)


if __name__ == "__main__":
    main()
