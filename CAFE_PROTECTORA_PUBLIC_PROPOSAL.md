# CAFÉ LA PROTECTORA — PUBLIC EXPERIENCE PROPOSAL

**Fecha:** Septiembre 2026
**Fase:** 6 — PUBLIC EXPERIENCE PROPOSAL

---

## 1. ARQUITECTURA TÉCNICA

### Stack propuesto

| Capa | Tecnología | Justificación |
|------|-----------|---------------|
| Backend | Flask (sub-app) | Consistente con Portfolio Hub existente |
| Templates | Jinja2 | Consistente con Hub |
| Frontend | Vanilla CSS + JS | Sin dependencias, performance |
| Data | Python dict/JSON | Sin base de datos necesaria |
| Fonts | Google Fonts | Fraunces + Inter + JetBrains Mono |
| Icons | SVG inline | Sin librería externa |
| Maps | Leaflet (CDN) | Mapa interactivo liviano |

### Estructura de archivos

```
portfolio-hub-main/
├── app.py                          # Registro de sub-app
├── cafe_app.py                     # Sub-app Flask
├── templates/
│   └── cafe/
│       ├── base.html               # Base template café
│       ├── index.html              # Home/landing
│       ├── historia.html           # Historia
│       ├── origen.html             # Origen geográfico
│       ├── proceso.html            # Proceso productivo
│       ├── productos.html          # Catálogo
│       ├── producto.html           # Detalle de producto
│       ├── donde-comprar.html      # Directorio
│       ├── cultura.html            # Café y cultura
│       └── contacto.html           # Contacto
├── static/
│   └── cafe/
│       ├── css/
│       │   └── style.css           # Estilos encapsulados
│       ├── js/
│       │   └── app.js              # Interacciones
│       ├── img/
│       │   ├── products/           # Imágenes de producto
│       │   ├── process/            # Imágenes de proceso
│       │   ├── origin/             # Imágenes de origen
│       │   └── og-image.jpg        # Open Graph image
│       └── data/
│           ├── products.json       # Datos de productos
│           ├── distributors.json   # Datos de distribuidores (propuesto)
│           └── timeline.json       # Línea de tiempo
└── CAFE_PROTECTORA_*.md            # Documentación
```

### Rutas

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/cafe/` | GET | Home/landing |
| `/cafe/historia` | GET | Historia de la marca |
| `/cafe/origen` | GET | Origen geográfico |
| `/cafe/proceso` | GET | Proceso productivo |
| `/cafe/productos` | GET | Catálogo de productos |
| `/cafe/productos/<slug>` | GET | Detalle de producto |
| `/cafe/donde-comprar` | GET | Directorio de distribución |
| `/cafe/cultura` | GET | Café y cultura |
| `/cafe/contacto` | GET/POST | Formulario de contacto |

---

## 2. DISEÑO VISUAL

### Paleta de colores (propuesta)

| Token | Valor | Uso |
|-------|-------|-----|
| `--cafe-bg` | `#0C0A08` | Fondo principal |
| `--cafe-surface` | `#1A1612` | Fondo de tarjeta |
| `--cafe-surface-2` | `#2A241C` | Fondo elevado |
| `--cafe-line` | `#3D352A` | Bordes |
| `--cafe-text` | `#F5F0E8` | Texto primario |
| `--cafe-muted` | `#A69882` | Texto secundario |
| `--cafe-accent` | `#C4783A` | Acento principal (dorado/café) |
| `--cafe-green` | `#5A7A4A` | Acento secundario (naturaleza) |
| `--cafe-red` | `#8B3A3A` | Acento terciario (tradición) |

### Inspiración

- **Café** — Tonos cálidos, dorados, marrones profundos
- **Tierra** — Colores naturales, orgánicos
- **Montaña** — Verdes profundos, azules lejanos
- **Grano** — Texturas, profundidad
- **Venezuela** — Bandera sutil (rojo, azul, amarillo como acentos)

### No caer en

- Exceso de marrón genérico
- Texturas de madera/fondo
- Estética vintage artificial
- Glassmorphism excesivo
- Animaciones que destruyan performance

### Tipografía

| Fuente | Uso | Peso |
|--------|-----|------|
| Fraunces | Headlines, display | 500, 600, 700 |
| Inter | Body text | 400, 500 |
| JetBrains Mono | Labels, badges, mono | 400, 500 |

---

## 3. DISEÑO POR SECCIÓN

### Hero

```
┌─────────────────────────────────────────────┐
│                                             │
│  [FONDO: imagen de café/trujillo con        │
│   overlay gradiente oscuro]                 │
│                                             │
│  CAFÉ LA PROTECTORA                         │
│  Café venezolano de origen andino.          │
│  Tradición del grano a tu taza.             │
│                                             │
│  [CONOCE NUESTRO CAFÉ]  [DÓNDE COMPRAR]    │
│                                             │
│  ┌──────┐ ┌──────┐ ┌──────┐                │
│  │ORIGEN│ │PROCESO│ │CALIDAD│               │
│  └──────┘ └──────┘ └──────┘                │
│                                             │
└─────────────────────────────────────────────┘
```

**Headline:** "Del Origen a Tu Taza"
**Supporting:** "Café venezolano de los Andes de Trujillo. Tradición, calidad y sabor en cada grano."
**CTAs:** "Conoce Nuestro Café" (primario) + "Dónde Comprar" (secundario)

### Historia

```
┌─────────────────────────────────────────────┐
│  NUESTRA HISTORIA                           │
│                                             │
│  LÍNEA DE TIEMO:                            │
│  ● Café La India → ● Café La Pastora →      │
│  ● Café La Protectora (2005)                │
│                                             │
│  [FOTO: imagen de la marca/origen]          │
│                                             │
│  "A través de los años, nos esforzamos..."  │
│                                             │
│  [FOTOS DE PROCESO]                         │
│                                             │
└─────────────────────────────────────────────┘
```

### Origen

```
┌─────────────────────────────────────────────┐
│  DEL ORIGEN A TU TAZA                       │
│                                             │
│  [MAPA INTERACTIVO]                         │
│  Venezuela → Trujillo → Pampán → Santa Ana  │
│                                             │
│  ALTURA: 900-1,200 m.s.n.m.               │
│  CLIMA: Sombras, Cordillera Andina          │
│                                             │
│  [INFOGRAFÍA: condiciones de cultivo]       │
│                                             │
└─────────────────────────────────────────────┘
```

### Proceso

```
┌─────────────────────────────────────────────┐
│  NUESTROS PROCESOS                          │
│                                             │
│  CULTIVO → ALMACENAMIENTO → TORREFACCIÓN →  │
│  MOLIDO → EMPACADO → DISTRIBUCIÓN           │
│                                             │
│  [CADA ETAPA: imagen + descripción +        │
│   datos técnicos]                           │
│                                             │
│  [ANIMACIÓN: scroll → proceso]              │
│                                             │
└─────────────────────────────────────────────┘
```

### Productos

```
┌─────────────────────────────────────────────┐
│  NUESTROS PRODUCTOS                         │
│                                             │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │
│  │ 50g │ │100g │ │200g │ │500g │ │ 1Kg │  │
│  │     │ │     │ │     │ │     │ │     │  │
│  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘  │
│                                             │
│  [CADA PRODUCTO: imagen + nombre +          │
│   descripción + formato + CTA]              │
│                                             │
│  NOTA: "Todos nuestros productos son café   │
│  molido de calidad, seleccionado de la      │
│  parte alta del estado Trujillo."           │
│                                             │
└─────────────────────────────────────────────┘
```

### Dónde Comprar (PROPUESTO)

```
┌─────────────────────────────────────────────┐
│  ENCUENTRA TU CAFÉ                          │
│                                             │
│  [FILTROS: Estado → Ciudad → Tipo]          │
│                                             │
│  [MAPA: distribuidores propuestos]          │
│                                             │
│  [LISTA: distribuidores por zona]           │
│                                             │
│  NOTA: "Directorio propuesto. Los datos     │
│  mostrados son una propuesta basada en      │
│  información pública disponible."           │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 4. SEO IMPLEMENTATION

### Tags por página

| Página | Title | Meta Description |
|--------|-------|------------------|
| Home | Café La Protectora — Café Venezolano de Origen Andino | Del origen andino de Trujillo a tu taza. Conoce la historia, el proceso y los productos de Café La Protectora. |
| Historia | Nuestra Historia — Café La Protectora | Desde Café La India hasta Café La Protectora. Una historia de tradición cafetera en los Andes venezolanos. |
| Origen | Origen — Café La Protectora | Café cultivado en la Cordillera Andina de Trujillo, a 900-1,200 metros de altura. Conoce de dónde viene nuestro café. |
| Proceso | Proceso — Café La Protectora | Del cultivo a la distribución. Conoce las 6 etapas que hacen posible cada taza de Café La Protectora. |
| Productos | Productos — Café La Protectora | Café molido venezolano en presentaciones de 50g a 1Kg. Calidad gourmet de los Andes de Trujillo. |
| Dónde Comprar | Dónde Comprar — Café La Protectora | Encuentra Café La Protectora en supermercados y distribuidores autorizados en toda Venezuela. |
| Cultura | Café y Cultura — Café La Protectora | El café como parte de la identidad venezolana. Historias, tradiciones y recetas. |
| Contacto | Contacto — Café La Protectora | Contáctanos para información comercial, distribución o consultas generales. |

### Schema.org

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Café La Protectora",
  "url": "https://cafelaprotectora.com.ve",
  "logo": "...",
  "description": "Café venezolano de origen andino, cultivado en la Cordillera Andina de Trujillo.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Santa Ana",
    "addressRegion": "Trujillo",
    "addressCountry": "VE"
  },
  "sameAs": [
    "https://www.instagram.com/cafelaprotectora/",
    "https://www.facebook.com/CafeLaProtectora"
  ]
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Café Molido de 500g",
  "brand": {
    "@type": "Brand",
    "name": "Café La Protectora"
  },
  "description": "Café molido gourmet de origen trujillano...",
  "image": "...",
  "offers": {
    "@type": "Offer",
    "availability": "InStock",
    "priceCurrency": "USD",
    "price": "6.90"
  }
}
```

### Breadcrumb

```
Home > Café La Protectora > [Sección]
```

---

## 5. PERFORMANCE BUDGET

| Recurso | Target | Estrategia |
|---------|--------|------------|
| CSS | < 30KB | Un solo archivo, sin framework |
| JS | < 15KB | Vanilla, sin librerías |
| Imágenes | < 200KB total | WebP, lazy loading, responsive |
| Fuentes | < 100KB | Subset, preload 2 pesos críticos |
| Total | < 350KB | Sin video, sin animaciones pesadas |

### Optimizaciones

- Lazy loading en imágenes below the fold
- Preload de fuentes críticas
- CSS inline en critical path
- Imágenes WebP con fallback
- Sin framework CSS (custom properties)
- Sin framework JS
- SVG inline para iconos

---

## 6. SEGURIDAD

### Headers

```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline' fonts.googleapis.com; font-src fonts.gstatic.com; img-src 'self' data:
```

### Checklist

- [ ] Sin secrets en código
- [ ] Sin .env en repositorio
- [ ] Sin API keys expuestas
- [ ] Sin uploads de usuario
- [ ] Sin formularios con datos sensibles
- [ ] CSP configurado
- [ ] HTTPS forzado

---

## 7. DEPLOYMENT

### Opción recomendada: Railway

| Criterio | Evaluación |
|----------|------------|
| Costo | Free tier disponible |
| HTTPS | Sí, automático |
| Custom domain | Sí |
| Flask support | Nativo |
| Performance | Buena |
| Mantenimiento | Bajo |

### URLs

| Entorno | URL |
|---------|-----|
| Producción | cafe.alvaroberrio.dev (o similar) |
| Portfolio | alvaroberrio.dev/projects/cafe-la-protectora |
| Demo | cafe-la-protectora-production.up.railway.app |

---

## 8. ESTRATEGIA DE CONTENIDO

### Contenido original vs. placeholder

| Tipo | Decisión | Razón |
|------|----------|-------|
| Fotos de producto | Placeholder con estilo | Derechos no verificados |
| Fotos de proceso | Placeholder con estilo | Derechos no verificados |
| Fotos de origen | Placeholder con estilo | Derechos no verificados |
| Textos | Originales del sitio | Texto público, atribuido |
| Datos | Documentados con fuente | Evidence matrix |
| Precios | Datos de terceros | Marca como tercero |

### Placeholder strategy

Para imágenes donde no se tienen derechos:
- Usar gradientes con colores de marca
- Usar iconos SVG representativos
- Usar ilustraciones estilo flat
- Texto descriptivo sobre fondo

**NUNCA** descargar y redistribuir imágenes protegidas.

---

**Public Experience Proposal completada. Lista para Approval Gate.**
