import json, pathlib, re, urllib.request
OLD = "\u00c1lvaro Berr\u00edo"; NEW = "\u00c1lvaro Benjam\u00edn Berr\u00edo"
def fix(o):
    if isinstance(o, str): return o.replace(OLD, NEW)
    if isinstance(o, list): return [fix(x) for x in o]
    if isinstance(o, dict): return {k: fix(v) for k, v in o.items()}
    return o
p = pathlib.Path("data/portfolio.json")
d = fix(json.loads(p.read_text(encoding="utf-8")))
d["footer"]["updated"] = "octubre de 2026"
d["projects"]["items"] = [x for x in d["projects"]["items"] if "Protectora" not in x.get("name", "")]
ok = False
try: ok = urllib.request.urlopen("https://edupack-builder.onrender.com", timeout=60).status == 200
except Exception as e: print("AVISO EduPack no responde:", e)
if ok:
    for x in d["projects"]["items"]:
        for l in x["links"]:
            if "edupack-builder" in l["href"]: l["available"] = True
gh = {"name": "Perfil de GitHub", "url": "https://github.com/alvaroberrio23242-eng", "status": "Perfil p\u00fablico", "available": True, "media": {"kind": "image", "src": "img/profile-avatar.webp"}, "note": ""}
edu = {"name": "EduPack Builder", "url": "https://edupack-builder.onrender.com", "status": "En producci\u00f3n", "available": True, "media": {"kind": "image", "src": "img/thumbnails/edupack.png"}, "note": ""}
rest = [e for e in d["evidence"] if e["name"] not in (gh["name"], edu["name"])]
d["evidence"] = [gh] + rest + ([edu] if ok else [])
p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("OK carrusel:", len(d["evidence"]), "tarjetas")
t = pathlib.Path("templates/404.html")
s = t.read_bytes().decode("utf-8")
s = re.sub(r'[ \t]*<a class="btn" href="\{\{ site_origin \}\}/cafe/">[^<]*</a>\r?\n?', "", s).replace(OLD, NEW)
t.write_bytes(s.encode("utf-8"))
print("OK 404 y nombre")
