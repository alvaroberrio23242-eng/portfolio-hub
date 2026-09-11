# CAFÉ LA PROTECTORA — UX AUDIT

**Fecha:** Septiembre 2026
**Fase:** 4 — UX AUDIT

---

## 1. USUARIOS IDENTIFICADOS

### Persona 1: Consumidor curious

> "Quiero conocer este café. ¿De dónde viene? ¿Qué lo hace especial?"

- **Necesita:** Historia, origen, proceso, calidad
- **Ruta actual:** Home → Quiénes Somos → (se pierde)
- **Problema:** No hay narrativa visual que lo mantenga enganchado

### Persona 2: Comprador

> "Quiero comprar este café. ¿Dónde lo consigo? ¿Cuánto cuesta?"

- **Necesita:** Precio, distribuidores, disponibilidad
- **Ruta actual:** Home → Productos → (sin precio) → Encuéntranos → (vacío)
- **Problema:** No puede completar la compra. Directorio vacío.

### Persona 3: Distribuidor/Minorista

> "Quiero vender este café en mi negocio. ¿Cómo contacto?"

- **Necesita:** Información comercial, condiciones, contacto
- **Ruta actual:** Home → Encuéntranos → Relaciones Comerciales → (solo imágenes)
- **Problema:** No hay información de negocio clara

### Persona 4: Cafetería/Emprendedor

> "Quiero ofrecer este café en mi cafetería. ¿Es gourmet? ¿Tiene certificaciones?"

- **Necesita:** Certificaciones, perfil de taza, presentaciones, contacto B2B
- **Ruta actual:** Home → Productos → (sin descripción) → Contacto → (formulario genérico)
- **Problema:** No hay información técnica ni de negocio

### Persona 5: Investigador/Curioso

> "Quiero conocer la historia completa de esta marca venezolana."

- **Necesita:** Cronología, contexto cultural, impacto
- **Ruta actual:** Home → Quiénes Somos → (historia limitada)
- **Problema:** No hay contenido profundo ni contexto cultural

### Persona 6: Portfolio Reviewer

> "¿Qué puede hacer Álvaro con un caso de marca real?"

- **Necesita:** Ver investigación, estrategia, implementación técnica
- **Ruta actual:** No existe (proyecto nuevo)
- **Problema:** Este es el proyecto que construiremos

---

## 2. JOURNEYS ACTUALES (AS-IS)

### Journey 1: Descubrir el café

```
1. Llega al home
2. Ve hero con imagen de café
3. Lee "Auténtico Sabor Venezolano"
4. Hace clic en "VER PRODUCTOS"
5. Ve 5 productos sin descripción
6. No sabe cuál elegir
7. Abandona
```

**Tasa de éxito estimada:** 20%
**Punto de fricción:** Sin contexto, sin diferenciación entre productos

### Journey 2: Encontrar dónde comprar

```
1. Llega al home
2. Hace clic en "Encuéntranos"
3. Ve dropdown con 2 opciones
4. Hace clic en "Centros de Distribución"
5. Ve "Nro. Distribuidores: 0"
6. Piensa que no hay distribución
7. Abandona
```

**Tasa de éxito estimada:** 5%
**Punto de fricción:** Directorio digitalmente roto

### Journey 3: Conocer la historia

```
1. Llega al home
2. Hace clic en "QUIÉNES SOMOS"
3. Lee historia breve
4. Ve proceso (tabs)
5. Ve garantía de calidad
6. No hay más contenido
7. Abandona
```

**Tasa de éxito estimada:** 40%
**Punto de fricción:** Historia incompleta, sin línea de tiempo

---

## 3. PROBLEMAS UX IDENTIFICADOS

### Críticos (bloquean conversión)

| # | Problema | Impacto | Solución propuesta |
|---|----------|---------|-------------------|
| C1 | Directorio de distribución vacío | El comprador no puede encontrar el producto | "Find Where to Buy" con datos reales o propuesta |
| C2 | Sin precios en el sitio | El comprador no puede evaluar | Mostrar precios o indicar "Disponible en puntos de venta" |
| C3 | Productos sin descripción | No hay diferenciación ni copy de venta | Descripción única por presentación |
| C4 | CTA "VER PRODUCTOS" sin contexto | Click ciego sin expectativa | CTA contextual por sección |

### Importantes (degradan experiencia)

| # | Problema | Impacto | Solución propuesta |
|---|----------|---------|-------------------|
| I1 | Navegación confusa "Encuéntranos" | El usuario no sabe qué buscar | Renombrar a "Dónde Comprar" |
| I2 | Misión = Visión | Credibilidad comprometida | Corregir o eliminar duplicado |
| I3 | Sin Schema.org | SEO comprometido | Implementar Product, Organization, BreadcrumbList |
| I4 | Imágenes sin alt text | Accesibilidad comprometida | Agregar alt descriptivos |
| I5 | Sin mobile optimization | Experiencia móvil deficiente | Rediseñar para mobile-first |

### Menores (mejoran experiencia)

| # | Problema | Impacto | Solución propuesta |
|---|----------|---------|-------------------|
| M1 | Sin blog/content | No hay engagement | Sección de cultura/café |
| M2 | Sin recetas | No hay uso | Sección de preparación |
| M3 | Sin FAQ | No hay resolución de dudas | FAQ schema |
| M4 | Sin newsletter funcional | No hay captación | Formulario funcional |
| M5 | Copyright 2023 | Desactualizado | Actualizar |

---

## 4. ARQUITECTURA DE INFORMACIÓN PROPUESTA

### Estructura actual vs. propuesta

**ACTUAL:**
```
INICIO → QUIÉNES SOMOS → ENCUENTRANOS → PRODUCTOS → CONTACTO
```

**PROPUESTA:**
```
HOME
├── HISTORIA
│   ├── Origen
│   ├── Evolución de la marca
│   ├── Línea de tiempo
│   └── La gente (caficultores)
│
├── ORIGEN
│   ├── Trujillo
│   ├── Cordillera Andina
│   ├── Santa Ana / Pampán
│   ├── Altura y clima
│   └── Mapa interactivo
│
├── PROCESO
│   ├── Cultivo
│   ├── Almacenamiento
│   ├── Torrefacción
│   ├── Molido
│   ├── Empacado
│   └── Distribución
│
├── PRODUCTOS
│   ├── 50g
│   ├── 100g
│   ├── 200g
│   ├── 500g
│   └── 1Kg
│
├── DÓNDE COMPRAR
│   ├── Por estado
│   ├── Por ciudad
│   ├── Por tipo de establecimiento
│   └── Cómo llegar
│
├── CULTURA
│   ├── Café y Venezuela
│   ├── Recetas
│   └── Preparación
│
└── CONTACTO
    ├── General
    ├── Comercial
    └── Prensa
```

---

## 5. FLUJOS PROPUESTOS

### Flujo 1: Descubrir (Consumer)

```
HOME
↓
Hero: "Del Origen a Tu Taza"
↓
Scroll → Historia visual (3 slides)
↓
Scroll → Proceso animado (6 etapas)
↓
Scroll → Productos con descripción
↓
CTA: "Conoce tu Café" → Página de producto
↓
CTA: "Dónde Comprar" → Directorio
```

### Flujo 2: Comprar (Buyer)

```
HOME
↓
CTA: "Encuentra tu Café"
↓
DÓNDE COMPRAR
↓
Seleccionar Estado → Ciudad → Tipo
↓
Ver distribuidores
↓
Cómo llegar (mapa)
↓
Disponibilidad
```

### Flujo 3: Negocio (B2B)

```
HOME
↓
Footer: "Relaciones Comerciales"
↓
Página B2B
↓
Información comercial
↓
Contacto directo
↓
Formulario especializado
```

---

## 6. MÉTRICAS PROPUESTAS

### Previas al lanzamiento

| Métrica | Target | Método |
|---------|--------|--------|
| LCP | < 2.5s | Lighthouse |
| INP | < 200ms | Lighthouse |
| CLS | < 0.1 | Lighthouse |
| Accessibility | ≥ 90 | Lighthouse |
| SEO | ≥ 95 | Lighthouse |
| Mobile Usability | Pass | Google Search Console |

### Post-lanzamiento (si hay analytics)

| Métrica | Target | Método |
|---------|--------|--------|
| Bounce rate | < 50% | Analytics |
| Time on site | > 2 min | Analytics |
| Pages per session | > 3 | Analytics |
| CTA clicks | > 10% | Events |
| Mobile traffic | > 60% | Analytics |

---

## 7. ACCESIBILIDAD

### WCAG 2.2 AA — Checklist

| Criterio | Estado actual | Target |
|----------|---------------|--------|
| 1.1.1 Non-text Content | Fallido (sin alt) | Pass |
| 1.3.1 Info and Relationships | Parcial | Pass |
| 1.4.3 Contrast | No verificado | Pass (4.5:1) |
| 2.1.1 Keyboard | No verificado | Pass |
| 2.4.1 Bypass Blocks | No verificado | Pass |
| 2.4.3 Focus Order | No verificado | Pass |
| 2.4.6 Headings | Parcial | Pass |
| 2.5.5 Target Size | No verificado | Pass (24px) |
| 3.1.1 Language | Presente (es) | Pass |
| 4.1.2 Name, Role, Value | No verificado | Pass |

---

## 8. CONCLUSIÓN UX AUDIT

### El problema central

**El sitio actual de Café La Protectora falla en los 3 momentos críticos del viaje del usuario:**

1. **Descubrir** — Sin narrativa visual, sin contexto, sin diferenciación
2. **Decidir** — Sin descripciones, sin precios, sin social proof
3. **Comprar** — Directorio vacío, sin CTA de conversión

### La oportunidad

Construir una experiencia digital que responda rápidamente:
- **¿Qué es?** Café La Protectora — Café venezolano de origen andino
- **¿De dónde viene?** Trujillo, Cordillera Andina, 900-1,200m
- **¿Cómo se produce?** 6 etapas documentadas
- **¿Qué productos tiene?** 5 presentaciones de café molido
- **¿Dónde comprarlo?** Directorio funcional
- **¿Por qué confiar?** Calidad, tradición, proceso
- **¿Cómo conocer más?** Historia, cultura, recetas

---

**UX Audit completado. 3 journeys críticos, 4 problemas críticos, arquitectura propuesta.**
