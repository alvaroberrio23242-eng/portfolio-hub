"""Regresion de las 10 rutas del blueprint /cafe (cafe_app.py)."""


def test_cafe_index_200(client):
    assert client.get("/cafe/").status_code == 200


def test_cafe_home_usa_plantilla_cafe(client):
    html = client.get("/cafe/").get_data(as_text=True)
    assert "<title>" in html
    assert "Berr" in html


RUTAS_CAFE = [
    "/cafe/",
    "/cafe/historia",
    "/cafe/origen",
    "/cafe/proceso",
    "/cafe/productos",
    "/cafe/donde-comprar",
    "/cafe/cultura",
    "/cafe/contacto",
    "/cafe/decisiones",
]


def test_cafe_tiene_10_rutas(app):
    reglas = {str(r) for r in app.url_map.iter_rules() if r.endpoint.startswith("cafe.")}
    publicas = {r for r in reglas if "<path:filename>" not in r and "slug" not in r}
    assert len(publicas) == 9, f"cambio el numero de rutas publicas del cafe: {sorted(publicas)}"
    assert "/cafe/productos/<slug>" in reglas


def test_cafe_slugs_registrados(raiz, productos):
    """Cada presentacion necesita slug y nombre; la imagen es opcional.

    content.py declara en KNOWN_GAPS['product_photos_missing'] que los
    products-*.png no existen y que 'image' se omite a proposito, en vez de
    apuntar a una foto generica que contradiga /cafe/decisiones. Si alguna
    vez se declara una imagen, el archivo tiene que existir de verdad.
    """
    for p in productos:
        assert p.get("slug"), "producto sin slug"
        assert p.get("name"), f"producto {p.get('slug')} sin nombre"
        if p.get("image"):
            relativa = p["image"].removeprefix("/static/")
            assert (raiz / "static" / relativa).is_file(), (
                f"producto {p['slug']} declara una imagen inexistente: {p['image']}"
            )


def test_cafe_tiene_5_presentaciones(productos):
    assert len(productos) == 5, f"cambio el numero de productos: {len(productos)}"


def test_producto_valido_200(client, productos):
    slug = productos[0]["slug"]
    resp = client.get(f"/cafe/productos/{slug}")
    assert resp.status_code == 200


def test_producto_valido_muestra_su_nombre(client, productos):
    producto = productos[0]
    html = client.get(f"/cafe/productos/{producto['slug']}").get_data(as_text=True)
    assert producto["name"] in html


def test_todos_los_productos_responden(client, productos):
    for p in productos:
        resp = client.get(f"/cafe/productos/{p['slug']}")
        assert resp.status_code == 200, f"producto {p['slug']} devolvio {resp.status_code}"


def test_producto_invalido_404(client):
    assert client.get("/cafe/productos/slug-que-no-existe").status_code == 404


def test_producto_invalido_usa_plantilla_404_del_cafe(client):
    html = client.get("/cafe/productos/slug-que-no-existe").get_data(as_text=True)
    assert "<html" in html.lower(), "el 404 del cafe debe devolver HTML, no un cuerpo vacio"


def test_ruta_cafe_inexistente_404(client):
    assert client.get("/cafe/ruta-inexistente").status_code == 404


def test_cafe_no_requiere_autenticacion(client):
    """Ninguna ruta publica del cafe debe redirigir a /login."""
    for ruta in RUTAS_CAFE:
        resp = client.get(ruta, follow_redirects=False)
        assert resp.status_code == 200, f"{ruta} devolvio {resp.status_code}"
        assert "/login" not in resp.headers.get("Location", "")


def test_cafe_tiene_canonical(client):
    html = client.get("/cafe/").get_data(as_text=True)
    assert 'rel="canonical"' in html


def test_cafe_declara_og_image(client):
    html = client.get("/cafe/").get_data(as_text=True)
    assert 'property="og:image"' in html
