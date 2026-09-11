from flask import Blueprint, render_template, jsonify, request

cafe_bp = Blueprint(
    'cafe',
    __name__,
    template_folder='templates/cafe',
    static_folder='static/cafe',
    static_url_path='/static/cafe'
)

PRODUCTS = [
    {
        "slug": "cafe-molido-50g",
        "name": "Café Molido de 50g",
        "weight": "50 g",
        "description": "Nuestra presentación más compacta. Ideal para probar Café La Protectora o para quienes prefieren consumo ocasional. Mismo café de calidad, mismo origen andino.",
        "format": "Café molido",
        "packaging": "Polipropileno Biorentado 25μ + Metalizado 20μ, termosellado",
        "origin": "Santa Ana, Municipio Pampán, Estado Trujillo",
        "availability": "Disponible en distribuidores autorizados",
        "image": "/static/cafe/img/products-50g.png",
        "badge": "Para probar"
    },
    {
        "slug": "cafe-molido-100g",
        "name": "Café Molido de 100g",
        "weight": "100 g",
        "description": "Presentación práctica para el consumo diario. Conserva todo el aroma y sabor del café cultivado en la Cordillera Andina de Trujillo.",
        "format": "Café molido",
        "packaging": "Polipropileno Biorentado 25μ + Metalizado 20μ, termosellado",
        "origin": "Santa Ana, Municipio Pampán, Estado Trujillo",
        "availability": "Disponible en distribuidores autorizados",
        "image": "/static/cafe/img/products-100g.png",
        "badge": "Consumo diario"
    },
    {
        "slug": "cafe-molido-200g",
        "name": "Café Molido de 200g",
        "weight": "200 g",
        "description": "El equilibrio perfecto entre duración y frescura. Para quienes disfrutan del café como parte de su rutina diaria.",
        "format": "Café molido",
        "packaging": "Polipropileno Biorentado 25μ + Metalizado 20μ, termosellado",
        "origin": "Santa Ana, Municipio Pampán, Estado Trujillo",
        "availability": "Disponible en distribuidores autorizados",
        "image": "/static/cafe/img/products-200g.png",
        "badge": "Equilibrado"
    },
    {
        "slug": "cafe-molido-500g",
        "name": "Café Molido de 500g",
        "weight": "500 g",
        "description": "Nuestra presentación más popular. Para hogares que disfrutan del café con regularidad. Calidad gourmet a buen precio.",
        "format": "Café molido",
        "packaging": "Polipropileno Biorentado 25μ + Metalizado 20μ, termosellado",
        "origin": "Santa Ana, Municipio Pampán, Estado Trujillo",
        "availability": "Disponible en distribuidores autorizados",
        "image": "/static/cafe/img/products-500g.png",
        "badge": "Más popular"
    },
    {
        "slug": "cafe-molido-1kg",
        "name": "Café Molido de 1Kg",
        "weight": "1 kg",
        "description": "Para los verdaderos amantes del café. La mejor relación calidad-cantidad para hogares y oficinas.",
        "format": "Café molido",
        "packaging": "Polipropileno Biorentado 25μ + Metalizado 20μ, termosellado",
        "origin": "Santa Ana, Municipio Pampán, Estado Trujillo",
        "availability": "Disponible en distribuidores autorizados",
        "image": "/static/cafe/img/products-1kg.png",
        "badge": "Mayor volumen"
    }
]

PROCESS_STEPS = [
    {
        "id": "cultivo",
        "title": "Cultivo",
        "description": "Los granos provienen de la parte alta del estado Trujillo (Cordillera Andina), cultivados bajo sombra entre 900 y 1,200 metros de altura. En la mayoría de los casos no se utilizan fertilizantes tóxicos y se recoge el fruto 100% maduro.",
        "detail": "El café se lava como mínimo durante 4 horas, luego se seca al sol y se almacena en pergamino por 2 meses en sacos de sisal con menos del 12% de humedad.",
        "icon": "🌱"
    },
    {
        "id": "almacenamiento",
        "title": "Almacenamiento",
        "description": "Nuestro café es almacenado en galpones aptos para el mismo, donde no entra la luz solar directamente y su temperatura se puede mantener estable.",
        "detail": "El café no está expuesto a otros productos, preservando así su sabor y su aroma de forma óptima.",
        "icon": "🏚️"
    },
    {
        "id": "torrefaccion",
        "title": "Torrefacción",
        "description": "Cuando el café llega a la Planta Torrefactora, es sometido a una clasificación por peso, tamaño, forma y color.",
        "detail": "La clave del éxito es saber escoger el grano que se va a tostar y ser consistente en el tiempo en que estará expuesto al calor. El tostado del café desarrolla su aroma y le da su color oscuro.",
        "icon": "🔥"
    },
    {
        "id": "molido",
        "title": "Molido",
        "description": "El molido es uno de los procesos más delicados, pues la molienda permite que el sabor se pueda extraer con mayor facilidad al colarse.",
        "detail": "Una vez tostado y molido se lleva a las máquinas empacadoras garantizando el contenido de los mismos.",
        "icon": "⚙️"
    },
    {
        "id": "empacado",
        "title": "Empacado",
        "description": "En el empacado del café se debe garantizar el pleno hermetismo para evitar oxidación del contenido y protegerlo de la humedad, oxígeno y luz.",
        "detail": "El empaque es de Polipropileno Biorentado 25 micras y laminadas con Polipropileno Metalizado de 20 micras de espesor, y Termosellado, lo que conserva el Aroma, Pureza y Sabor del café.",
        "icon": "📦"
    },
    {
        "id": "distribucion",
        "title": "Distribución",
        "description": "Finalmente los empaques en las diferentes presentaciones son embalados en bultos de 5 kg y entregados a las distintas cadenas de comercialización y distribuidoras autorizadas a nivel nacional.",
        "detail": "Café La Protectora llega a pontos de venta en todo el país a través de su red de distribuidores autorizados.",
        "icon": "🚚"
    }
]

TIMELINE = [
    {"year": "Inicio", "event": "Café La India — Primer nombre del producto cafetalero"},
    {"year": "Evolución", "event": "Café La Pastora — Segunda etapa de la marca"},
    {"year": "2005", "event": "Café La Protectora C.A. — Constitución en Santa Ana, Pampán, Trujillo"},
    {"year": "Actual", "event": "5 presentaciones, distribución nacional, 85 puntos de venta"}
]


@cafe_bp.route('/')
def index():
    return render_template('cafe/index.html',
                         products=PRODUCTS,
                         process_steps=PROCESS_STEPS,
                         timeline=TIMELINE,
                         active_page='home')


@cafe_bp.route('/historia')
def historia():
    return render_template('cafe/historia.html',
                         timeline=TIMELINE,
                         active_page='historia')


@cafe_bp.route('/origen')
def origen():
    return render_template('cafe/origen.html',
                         active_page='origen')


@cafe_bp.route('/proceso')
def proceso():
    return render_template('cafe/proceso.html',
                         process_steps=PROCESS_STEPS,
                         active_page='proceso')


@cafe_bp.route('/productos')
def productos():
    return render_template('cafe/productos.html',
                         products=PRODUCTS,
                         active_page='productos')


@cafe_bp.route('/productos/<slug>')
def producto(slug):
    product = next((p for p in PRODUCTS if p['slug'] == slug), None)
    if not product:
        return render_template('cafe/404.html'), 404
    return render_template('cafe/producto.html',
                         product=product,
                         products=PRODUCTS,
                         active_page='productos')


@cafe_bp.route('/donde-comprar')
def donde_comprar():
    return render_template('cafe/donde-comprar.html',
                         active_page='donde-comprar')


@cafe_bp.route('/cultura')
def cultura():
    return render_template('cafe/cultura.html',
                         active_page='cultura')


@cafe_bp.route('/contacto')
def contacto():
    return render_template('cafe/contacto.html',
                         active_page='contacto')
