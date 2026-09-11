# Architecture Proposal: Fuente Única de Verdad para el Laboratorio Digital

**Estado:** Propuesta (Fase 0 — sin implementar)
**Fecha:** 2026-09-11
**Repos implicados:** `portfolio-hub-main` (catálogo público), `portfolio-engine` (perfiles individuales)

---

## 1. Problema actual

Hoy, los datos del "Laboratorio Digital" están duplicados entre dos repos sin ningún mecanismo de sincronización:

| Lugar | Contenido | Cómo se define |
|---|---|---|
| `portfolio-hub-main/templates/family.html` | 15 MVP cards (SurveyForge, Assessment Builder, etc.) como tuplas Jinja2 inline | Hardcoded en template |
| `portfolio-hub-main/templates/base.html` | 7 project cards del catálogo público | HTML estático hardcodeado |
| `portfolio-engine/app/services/seeding.py` | Perfiles de Gilberto, Lisbeth, Claudio, Rhonela con datos académicos/laborales | ORM seeding scripts |

**El gap:** Cuando se construya una app individual (ej. SurveyForge de Gilberto), habría que registrarla manualmente en `family.html` (el portafolio familiar) Y en el perfil de Gilberto dentro de `portfolio-engine`. Doble trabajo, riesgo de desactualización.

---

## 2. Opciones evaluadas

### Opción A: JSON compartido en portfolio-hub-main

Un archivo `apps.json` en portfolio-hub-main que ambos sitios lean.

**Pros:**
- Fácil de mantener (un solo archivo)
- portfolio-engine haría HTTP GET al JSON en cada request
- Sin necesidad de API en portfolio-engine

**Contras:**
- Portfolio-engine estaría acoplado a la disponibilidad de portfolio-hub-main
- Si portfolio-hub-main cae, los perfiles individuales no muestran apps
- Requiere fetch síncrono o caché complicada en portfolio-engine
- Los datos de negocio quedan en el repo de presentación, no en el dominio

### Opción B: API JSON en portfolio-engine

Portfolio-engine expone un endpoint tipo `GET /api/laboratorio` que devuelve todas las apps registradas. Portfolio-hub-main lo consume para renderizar sus tarjetas.

**Pros:**
- La fuente de verdad vive donde están los perfiles (portfolio-engine)
- Portfolio-hub-main es un simple consumidor
- Desacoplamiento natural: el catálogo depende del engine, no al revés
- Compatible con caché: portfolio-hub-main puede cachear el JSON con TTL

**Contras:**
- Requiere agregar un endpoint API a portfolio-engine
- Si portfolio-engine cae, portfolio-hub-main necesita caché local o fallback
- Más infraestructura que un JSON estático

### Opción C: Tabla SQLAlchemy en portfolio-engine con modelo dedicado

Nueva tabla `LabApp` en la base de datos de portfolio-engine, con seeding script dedicado. Portfolio-engine expone un endpoint JSON que la sirve.

**Pros:**
- Mismos beneficios que Opción B
- Integra con el sistema de verificación existente (verification_status)
- Permite relaciones con Profile (quién es dueño de qué app)
- Compatible con el panel de administración existente
- Aprovecha toda la infraestructura de modelos y seeding

**Contras:**
- Más trabajo inicial (nuevo modelo, migración, seeding)
- Mantiene la complejidad de SQLAlchemy para algo que podría ser un JSON

### Opción D: Archivo estático JSON generado por portfolio-engine

Portfolio-engine genera un archivo estático `laboratorio.json` en `/static/` (o `var/`) que portfolio-hub-main descarga al deploy o en runtime.

**Pros:**
- Simple de consumir (es un archivo estático)
- Portfolio-engine controla la generación
- Portfolio-hub-main no depende de un endpoint dinámico

**Contras:**
- Requiere trigger para regenerar el JSON cada vez que cambian los datos
- Si se genera al deploy, hay delay entre cambios en la DB y disponibilidad en el hub
- Complejidad oculta: cron job, hook post-seed, o similar

---

## 3. Opción recomendada: Opción C (Modelo dedicado + API)

### ¿Por qué?

1. **Alineada con la arquitectura existente.** Portfolio-engine ya tiene SQLAlchemy, modelos con verificación, seeding scripts, y un patrón establecido para todo tipo de datos. Agregar `LabApp` es seguir el mismo patrón, no inventar algo nuevo.

2. **La fuente de verdad vive en el dominio correcto.** Las apps del Laboratorio son datos del dominio "perfil profesional". El catálogo (portfolio-hub) es una vista presentacional de esos datos.

3. **El sistema de verificación ya existe.** Cada modelo en portfolio-engine tiene `verification_status`, `source`, `source_url`. Una app sin `demo_url` verificada queda automáticamente como "Próximamente" — exactamente la regla que se pide.

4. **El panel de administración se extiende naturalmente.** Portfolio-engine ya tiene un admin panel. Un campo nuevo en la DB es visible inmediatamente en el dashboard.

5. **Desacoplamiento correcto.** Portfolio-hub-main consume, portfolio-engine sirve. Si el hub cae, los perfiles individuales siguen funcionando. Si el engine cae, el hub puede cachear la última respuesta.

---

## 4. Modelo de datos propuesto

### 4.1 Nueva tabla: `lab_apps`

```python
class LabApp(db.Model):
    __tablename__ = "lab_apps"

    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(120), nullable=False)          # "SurveyForge"
    slug            = db.Column(db.String(140), unique=True, nullable=False)  # "surveyforge"
    tagline         = db.Column(db.String(250))                          # "Constructor de encuestas..."
    description     = db.Column(db.Text)                                 # Descripción completa
    category        = db.Column(db.String(60), nullable=False)           # "territorio" | "talento" | "comunicacion"
    tier            = db.Column(db.String(30), default="TECHNICAL")      # "BUSINESS" | "PRODUCT" | "TECHNICAL"
    demo_url        = db.Column(db.String(500))                          # URL de demo pública (nullable)
    code_url        = db.Column(db.String(500))                          # URL del repositorio (nullable)
    tech_stack      = db.Column(db.String(300))                          # "Python, Flask, SQLAlchemy"
    accent_color    = db.Column(db.String(30))                           # CSS variable name: "var(--amber)"

    # Relación con el dueño
    profile_id      = db.Column(db.Integer, db.ForeignKey("profiles.id"), nullable=False)
    profile         = db.relationship("Profile", backref=db.backref("lab_apps", lazy="dynamic"))

    # Control de visibilidad
    status          = db.Column(db.String(20), default="COMING_SOON")    # "COMING_SOON" | "AVAILABLE" | "ARCHIVED"
    position        = db.Column(db.Integer, default=0)                   # Orden de aparición

    # Sistema de veración (hereda del patrón existente)
    verification_status  = db.Column(db.String(20), default="UNVERIFIED")
    verification_notes   = db.Column(db.Text)
    source               = db.Column(db.String(255))
    source_url           = db.Column(db.String(500))

    # Timestamps
    created_at = db.Column(db.DateTime, nullable=False, default=_utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=_utcnow, onupdate=_utcnow)
```

### 4.2 Campos mínimos (respuesta a pregunta 3)

| Campo | Obligatorio | Notas |
|---|---|---|
| `name` | Sí | Nombre de la app |
| `slug` | Sí | Identificador URL-friendly, único |
| `tagline` | No | Descripción corta (una línea) |
| `description` | No | Descripción completa (para ficha detallada) |
| `category` | Sí | "territorio", "talento", "comunicacion" |
| `tier` | No | BUSINESS / PRODUCT / TECHNICAL |
| `demo_url` | No | Si es `None`, status = COMING_SOON automáticamente |
| `code_url` | No | Repositorio fuente |
| `tech_stack` | No | Tecnologías usadas |
| `accent_color` | No | Para consistencia visual |
| `profile_id` | Sí | Quién es el dueño |
| `status` | Sí | COMING_SOON / AVAILABLE / ARCHIVED |
| `verification_status` | Sí | UNVERIFIED / NEEDS_REVIEW / VERIFIED |

### 4.3 Lógica de visibilidad (regla establecida)

```python
@property
def is_available(self):
    return (
        self.status == "AVAILABLE"
        and self.demo_url is not None
        and self.verification_status == "VERIFIED"
    )

@property
def display_status(self):
    if self.is_available:
        return "Disponible"
    return "Próximamente"
```

---

## 5. Cómo se sincroniza (respuesta a pregunta 2)

### Flujo de datos

```
                    ┌─────────────────────────────┐
                    │   portfolio-engine           │
                    │                              │
                    │  ┌─────────┐   ┌──────────┐  │
                    │  │ Profile │──▶│ LabApp   │  │
                    │  │ (Gilberto)  │(SurveyForge)│ │
                    │  └─────────┘  └──────────┘  │
                    │                              │
                    │  GET /api/laboratorio        │
                    │  → JSON con todas las apps   │
                    │  GET /api/laboratorio/<slug> │
                    │  → JSON de una app específica│
                    └──────────┬──────────────────┘
                               │
                    HTTP GET (con caché)
                               │
                    ┌──────────▼──────────────────┐
                    │   portfolio-hub-main          │
                    │                              │
                    │  /familia → family.html      │
                    │  (fichas del Laboratorio)     │
                    │                              │
                    │  / → base.html               │
                    │  (catálogo de proyectos)      │
                    └─────────────────────────────┘
```

### Estrategia de sincronización

1. **portfolio-engine expone `GET /api/laboratorio`**
   - Retorna JSON con todas las `LabApp` activas, agrupadas por categoría
   - Incluye datos del perfil dueño (nombre, slug, photo)
   - Disponible sin autenticación (es datos públicos)

2. **portfolio-hub-main consume con caché en memoria**
   - Flask almacena el JSON en `app.config["LAB_CACHE"]` con TTL de 5 minutos
   - Si el fetch falla, usa la última versión cacheada
   - Si nunca hubo caché, renderiza la sección como vacía ("Próximamente")

3. **Fallback graceful**
   - Si portfolio-engine está caído, el hub muestra las tarjetas que ya tiene en caché o, si no hay caché, un mensaje "Catálogo en actualización"
   - Los perfiles individuales (portfolio-engine) NUNCA dependen del hub

### Por qué NO sincronización bidireccional

El hub NO escribe al engine. El flujo es unidireccional:
- **Engine → Hub:** datos fluyen del engine al hub via API
- **Escritura:** solo se escribe en portfolio-engine (via panel admin o seeding)
- Esto evita conflictos de concurrencia y mantiene una fuente clara

---

## 6. Dónde vive la fuente de verdad (respuesta a pregunta 1)

**En portfolio-engine, en la tabla `lab_apps` de su base de datos SQLite.**

Razones:
- Portfolio-engine es el sistema de datos de los perfiles profesionales
- Ya tiene la relación `Profile` ↔ `LabApp` (un perfil tiene muchas apps)
- El sistema de verificación existente se aplica directamente
- El panel de administración permite gestionar las apps
- Portfolio-hub-main es solo una vista/presentación que consume datos

---

## 7. Endpoints API propuestos para portfolio-engine

### `GET /api/laboratorio`

```json
{
  "apps": [
    {
      "name": "SurveyForge",
      "slug": "surveyforge",
      "tagline": "Constructor de encuestas de investigación social con IA",
      "category": "territorio",
      "tier": "TECHNICAL",
      "demo_url": null,
      "tech_stack": "Python, Flask, React",
      "accent_color": "var(--amber)",
      "status": "COMING_SOON",
      "display_status": "Próximamente",
      "profile": {
        "full_name": "Gilberto Berrio Serrano",
        "slug": "gilberto-berrio-serrano"
      }
    }
  ],
  "categories": {
    "territorio": {
      "label": "Lab Territorio",
      "description": "Investigación social",
      "apps": ["surveyforge", "thesislab-social", ...]
    }
  }
}
```

### `GET /api/laboratorio/<slug>`

Retorna una sola app con todos los campos, incluyendo `description` completa.

---

## 8. Cómo se renderiza en cada sitio

### En portfolio-engine (perfil individual de Gilberto)

El template `profile.html` ya tiene lógica condicional por slug. Se agrega una sección:

```html
{% if profile.lab_apps.all() %}
<section class="lab-section">
  <h2>Laboratorio Digital</h2>
  {% for app in profile.lab_apps|sort(attribute='position') %}
  <article class="lab-app-card">
    <h3>{{ app.name }}</h3>
    <p>{{ app.tagline }}</p>
    {% if app.is_available %}
      <a href="{{ app.demo_url }}">Ver demo</a>
    {% else %}
      <span class="badge">Próximamente</span>
    {% endif %}
  </article>
  {% endfor %}
</section>
{% endif %}
```

### En portfolio-hub-main (catálogo familiar)

`family.html` deja de tener datos hardcoded. En su lugar:

```python
# app.py
@app.route("/familia")
def family():
    if not session.get("authenticated"):
        return redirect(url_for("login"))
    lab_data = get_lab_apps()  # fetch con caché desde portfolio-engine
    return render_template("family.html", lab_data=lab_data)
```

```html
<!-- family.html -->
{% for member_slug, member_data in lab_data.items() %}
<section class="member-lab">
  <h2>{{ member_data.profile.full_name }}</h2>
  {% for app in member_data.apps %}
  <article class="lab-card">
    <span class="card-number">{{ loop.index | string | padstart(2, '0') }}</span>
    <h3>{{ app.name }}</h3>
    <p>{{ app.tagline }}</p>
    <span class="category-badge">{{ app.category }}</span>
    <span class="status-badge {{ 'available' if app.is_available else 'coming-soon' }}">
      {{ app.display_status }}
    </span>
  </article>
  {% endfor %}
</section>
{% endfor %}
```

---

## 9. Impacto en los 15 MVPs actuales de family.html

Los 15 apps que hoy están hardcoded en `family.html` se migrarían al seeding de portfolio-engine:

| # | App | Dueño (Profile) | Categoría |
|---|-----|-----------------|-----------|
| 01 | SurveyForge | Gilberto | territorio |
| 02 | ThesisLab Social | Gilberto | territorio |
| 03 | Research Builder | Gilberto | territorio |
| 04 | Social Insight AI | Gilberto | territorio |
| 05 | Community Pulse | Gilberto | territorio |
| 06 | Assessment Builder | Lisbeth | talento |
| 07 | MicroLearning Factory | Lisbeth | talento |
| 08 | Onboarding AI | Lisbeth | talento |
| 09 | LearningPath AI | Lisbeth | talento |
| 10 | CulturePulse | Lisbeth | talento |
| 11 | Storytelling AI | Claudio | comunicacion |
| 12 | CopyLab | Claudio | comunicacion |
| 13 | Content Planner AI | Claudio | comunicacion |
| 14 | BrandDNA | Claudio | comunicacion |
| 15 | PhotoLab | Claudio | comunicacion |

**Nota:** Estos MVPs no existen como apps funcionales hoy. Se registran como `COMING_SOON` con `verification_status: UNVERIFIED`. Aparecen como "Próximamente" en ambos sitios.

---

## 10. Plan de implementación (cuando se apruebe)

| Fase | Qué | Dónde |
|------|-----|-------|
| 1 | Crear modelo `LabApp` + migración | portfolio-engine |
| 2 | Agregar seeding de los 15 MVPs (COMING_SOON) | portfolio-engine |
| 3 | Crear endpoint `GET /api/laboratorio` | portfolio-engine |
| 4 | Agregar tests para el modelo y el endpoint | portfolio-engine |
| 5 | Modificar `app.py` del hub para consumir la API con caché | portfolio-hub-main |
| 6 | Reemplazar datos hardcoded en `family.html` por loop Jinja2 | portfolio-hub-main |
| 7 | Agregar sección "Laboratorio Digital" al template de perfil individual | portfolio-engine |
| 8 | Deploy y verificación en ambos entornos | Ambos repos |

---

## 11. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| portfolio-engine cae → hub no muestra apps | Caché en memoria con TTL 5min + fallback a "Catálogo en actualización" |
| Cambios en la API rompen el hub | Contrato de API estable (versionado: `/api/v1/laboratorio`) |
| 15 apps COMING_SOON llenan el catálogo | Filtro por `status` en el hub: mostrar solo AVAILABLE o un subset de COMING_SOON |
| Despliegue de portfolio-engine requiere migración | Script `init_db.py` ya maneja creación de tablas — `LabApp` se crea automáticamente |

---

*Este documento es una propuesta arquitectónica. No se implementa nada hasta aprobación explícita.*
