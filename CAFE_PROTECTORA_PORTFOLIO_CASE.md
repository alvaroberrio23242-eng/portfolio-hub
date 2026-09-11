# CAFÉ LA PROTECTORA — PORTFOLIO INTEGRATION

**Fecha:** Septiembre 2026
**Fase:** 7 — PORTFOLIO INTEGRATION

---

## 1. CONTEXTO: PORTFOLIO HUB

### Estructura actual del Hub

El Portfolio Hub de Álvaro Berrío presenta proyectos organizados por tiers:

| Tier | Nombre | Proyectos |
|------|--------|-----------|
| Tier 1 | Business Proof | SalsaQuest, EduPack Builder |
| Tier 2 | Product Proof | OSINT Search Pro, Portfolio Engine |
| Tier 3 | Technical Proof | RockQuest, Aventura Antioqueña, CodeAudit |

### Problema de jerarquía actual

Todos los proyectos se presentan con la misma importancia visual. No hay distinción entre:
- Un caso de marca completo (Son Havana / SalsaQuest)
- Un proyecto técnico (CodeAudit)
- Un proyecto experimental

---

## 2. NUEVA JERARQUÍA PROPUESTA

### TIER 0 — BRAND & BUSINESS CASES

| Proyecto | Industria | Tipo | Status |
|----------|-----------|------|--------|
| **Son Havana** | Cultura · Turismo · Entretenimiento | Experiencia digital interactiva | En producción |
| **Café La Protectora** | Producto · Marca · Retail · Cultura | Digital brand experience | Concepto independiente |

### TIER 1 — PRODUCT PROOF

| Proyecto | Tipo | Status |
|----------|------|--------|
| SalsaQuest | Experiencia web interactiva | En producción |
| EduPack Builder | Agente autónomo IA | En producción |

### TIER 2 — TECHNICAL PROOF

| Proyecto | Tipo | Status |
|----------|------|--------|
| OSINT Search Pro | Plataforma de ciberinteligencia | En producción |
| Portfolio Engine | Sistema multi-perfil | En desarrollo |

### TIER 3 — EXPERIMENTAL

| Proyecto | Tipo | Status |
|----------|------|--------|
| RockQuest | Enciclopedia interactiva | En producción |
| Aventura Antioqueña | Juego WebAssembly | En producción |
| CodeAudit | Auditor estático | En desarrollo |

---

## 3. NARRATIVA DEL PORTFOLIO

### Claim principal

> Diferentes industrias. Mismo enfoque: entender el problema y construir una solución digital.

### Proof structure

```
CLAIM
↓
"Construyo software y soluciones digitales que convierten
problemas reales en productos funcionales."

↓ PROOF

SON HAVANA
Cultura · Turismo · Entretenimiento
Experiencia interactiva con storytelling gamificado

↓ CASE

CAFÉ LA PROTECTORA
Producto · Marca · Retail · Cultura
Digital brand experience con investigación documentada

↓ VALUE

SALSAQUEST / EDUPACK BUILDER / OSINT SEARCH PRO
Productos funcionales en producción

↓ CTA

¿Tienes un problema que se puede resolver con tecnología?
Hablemos.
```

---

## 4. INTEGRACIÓN EN EL HUB

### Cambios en base.html

#### 1. Featured Case Study — Dual

```html
<!-- Actual: solo SalsaQuest -->
<!-- Propuesto: Son Havana + Café La Protectora -->

<div class="section-label">Casos de estudio destacados</div>

<!-- Son Havana -->
<article class="case-study-section">
  <div class="case-grid">
    <div class="case-content">
      <p class="case-badge">Brand & Business Case</p>
      <h2>Son Havana</h2>
      <p class="case-subtitle">Cultura · Turismo · Entretenimiento</p>
      <!-- ... -->
    </div>
  </div>
</article>

<!-- Café La Protectora -->
<article class="case-study-section">
  <div class="case-grid">
    <div class="case-content">
      <p class="case-badge">Brand & Business Case</p>
      <h2>Café La Protectora</h2>
      <p class="case-subtitle">Producto · Marca · Retail · Cultura</p>
      <!-- ... -->
    </div>
  </div>
</article>
```

#### 2. Projects section — Tier 0

```html
{# ─── TIER 0: BRAND & BUSINESS CASES ─── #}
<article class="project-card" style="--card-accent: var(--amber);">
  <div class="project-top">
    <span class="project-tier" style="border-color: #C4783A; color: #C4783A;">Brand & Business</span>
    <div class="project-info">
      <p class="project-name">Son Havana</p>
      <p class="project-tag">Cultura · Turismo · Entretenimiento</p>
    </div>
  </div>
</article>

<article class="project-card" style="--card-accent: var(--amber);">
  <div class="project-top">
    <span class="project-tier" style="border-color: #C4783A; color: #C4783A;">Brand & Business</span>
    <div class="project-info">
      <p class="project-name">Café La Protectora</p>
      <p class="project-tag">Producto · Marca · Retail · Cultura</p>
    </div>
  </div>
</article>
```

#### 3. Evidence strip — Add Café La Protectora

```html
<div class="evidence-strip">
  <!-- SalsaQuest -->
  <!-- EduPack Builder -->
  <!-- Café La Protectora -->
  <a href="/cafe/" class="evidence-card">
    <div class="evidence-thumb" style="background: linear-gradient(135deg, #1a1510, #2a1a15);">
      <span style="font-size:48px;">☕</span>
    </div>
    <div class="evidence-info">
      <p class="evidence-name">Café La Protectora</p>
      <p class="evidence-status">Brand Experience</p>
    </div>
  </a>
</div>
```

---

## 5. CASO DE ESTUDIO: /projects/cafe-la-protectora

### Estructura del caso

```html
<!-- templates/projects/cafe-la-protectora.html -->

<section class="case-study-page">
  <header>
    <span class="case-badge">Brand & Business Case</span>
    <h1>Café La Protectora</h1>
    <p class="case-subtitle">Digital Brand Experience — Independent Case Study</p>
  </header>

  <!-- 01 — CONTEXTO -->
  <section id="contexto">
    <h2>01 — Contexto</h2>
    <p>Café La Protectora es una marca venezolana de café fundada en 2005 en Santa Ana, Municipio Pampán, estado Trujillo...</p>
  </section>

  <!-- 02 — INVESTIGACIÓN -->
  <section id="investigacion">
    <h2>02 — Investigación</h2>
    <p>Se investigaron múltiples fuentes primarias y secundarias...</p>
  </section>

  <!-- 03 — PROBLEMA -->
  <section id="problema">
    <h2>03 — Problema</h2>
    <p>La experiencia digital de la marca no reflejaba su calidad ni facilitaba la conexión con el consumidor...</p>
  </section>

  <!-- 04 — INSIGHT -->
  <section id="insight">
    <h2>04 — Insight</h2>
    <p>La brecha digital de Café La Protectora representaba una oportunidad para demostrar cómo la tecnología puede transformar la experiencia de una marca de producto real...</p>
  </section>

  <!-- 05 — SOLUCIÓN -->
  <section id="solucion">
    <h2>05 — Solución</h2>
    <p>Se construyó una Public Digital Brand Experience que cuenta la historia de la marca de forma moderna, clara y memorable...</p>
  </section>

  <!-- 06 — UX -->
  <section id="ux">
    <h2>06 — UX</h2>
    <p>Se diseñaron journeys para 6 tipos de usuario con rutas claras...</p>
  </section>

  <!-- 07 — TECHNOLOGY -->
  <section id="tecnologia">
    <h2>07 — Technology</h2>
    <p>Sub-app Flask encapsulada con CSS vanilla optimizado...</p>
  </section>

  <!-- 08 — PERFORMANCE -->
  <section id="performance">
    <h2>08 — Performance</h2>
    <p>LCP < 2.5s, CLS < 0.1, peso total < 350KB...</p>
  </section>

  <!-- 09 — EVIDENCE -->
  <section id="evidencia">
    <h2>09 — Evidence</h2>
    <p>30 claims documentados con fuente, fecha, status y confianza...</p>
  </section>

  <!-- 10 — LIMITATIONS -->
  <section id="limitaciones">
    <h2>10 — Limitations</h2>
    <p>Sin relación con la marca, sin acceso a datos internos, contenido con placeholders...</p>
  </section>

  <!-- 11 — RESULTS -->
  <section id="resultados">
    <h2>11 — Results</h2>
    <p>Lighthouse ≥ 90 en todas las categorías...</p>
  </section>

  <!-- 12 — DEMO -->
  <section id="demo">
    <h2>12 — Demo</h2>
    <a href="/cafe/" class="btn btn-primary">Ver Demo ↗</a>
  </section>

  <!-- 13 — CODE -->
  <section id="codigo">
    <h2>13 — Code</h2>
    <a href="https://github.com/..." class="btn">Ver Código ↗</a>
  </section>

  <!-- 14 — CONTACT -->
  <section id="contacto">
    <h2>14 — Contact</h2>
    <p>Álvaro Berrío — alvaroberrio.dev</p>
  </section>
</section>
```

---

## 6. RELACIÓN CON SON HAVANA

### Cómo presentarlas juntas

**NO** como un mismo cliente.
**NO** como una relación artificial.
**SÍ** como dos casos independientes en la misma categoría.

### Narrativa

> **Son Havana** — Cultura, Turismo, Entretenimiento
> Experiencia web interactiva con storytelling gamificado para un bar de salsa en Medellín.
>
> **Café La Protectora** — Producto, Marca, Retail, Cultura
> Digital brand experience con investigación documentada para una marca de café venezolana.
>
> **Diferentes industrias. Mismo enfoque: entender el problema y construir una solución digital.**

### Visual

```
┌─────────────────────────────────────────────────┐
│  BRAND & BUSINESS CASES                         │
│                                                 │
│  ┌───────────────────┐ ┌───────────────────┐    │
│  │   🎵 SON HAVANA   │ │  ☕ CAFÉ LA PROT. │    │
│  │                   │ │                   │    │
│  │ Cultura           │ │ Producto          │    │
│  │ Turismo           │ │ Marca             │    │
│  │ Entretenimiento   │ │ Retail            │    │
│  │                   │ │ Cultura           │    │
│  │ [Demo] [Código]   │ │ [Demo] [Código]   │    │
│  └───────────────────┘ └───────────────────┘    │
│                                                 │
│  Diferentes industrias.                         │
│  Mismo enfoque: entender el problema            │
│  y construir una solución digital.              │
└─────────────────────────────────────────────────┘
```

---

## 7. POSICIONAMIENTO DE ÁLVARO

### El Portfolio Hub comunica

> **Álvaro Berrío**
> Software · AI · Digital Products · Business Problem Solving
>
> Construyo software y soluciones digitales que convierten
> problemas reales en productos funcionales.

### La evidencia demuestra

| Capacidad | Evidencia |
|-----------|-----------|
| Investigación | 30 claims documentados, 6 fuentes |
| Brand Strategy | Brand audit completo |
| UX | 6 journeys, arquitectura propuesta |
| Product Thinking | Business case, propuesta de valor |
| Software | Sub-app Flask funcional |
| SEO | Schema.org, meta tags, breadcrumbs |
| Performance | Budget y optimización |
| Security | Headers, CSP, sin secrets |
| Business Understanding | Análisis de mercado y competencia |

### La regla fundamental

> **NO** vender: "Soy el mejor."
>
> **SÍ** demostrar:
> MIRA LO QUE INVESTIGUÉ.
> ↓
> MIRA LO QUE CONSTRUÍ.
> ↓
> MIRA CÓMO LO CONSTRUÍ.
> ↓
> MIRA QUÉ PROBLEMA RESUELVE.
> ↓
> SI TIENES UN PROBLEMA PARECIDO, HABLEMOS.

---

## 8. CAMBIOS NECESARIOS EN EL HUB

### Archivos a modificar

| Archivo | Cambio | Impacto |
|---------|--------|---------|
| `templates/base.html` | Agregar Tier 0, Featured dual, Evidence strip | Bajo |
| `app.py` | Registrar sub-app café | Bajo |
| `static/` | Agregar assets café | Ninguno (adicional) |
| `templates/cafe/` | Crear templates café | Ninguno (nuevo) |

### Archivos NO modificados

| Archivo | Razón |
|---------|-------|
| `templates/family.html` | Portal privado, no relacionado |
| `templates/login.html` | Auth, no relacionado |
| `.env` | Seguridad |
| `requirements.txt` | Sin nuevas dependencias necesarias |
| Otros templates de proyecto | Proyectos independientes |

---

**Portfolio Integration completada. Lista para Approval Gate.**
