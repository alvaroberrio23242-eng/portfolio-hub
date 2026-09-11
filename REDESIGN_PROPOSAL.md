# REDESIGN PROPOSAL — Portfolio Hub

**Fecha:** 2026-09-09
**Objetivo:** Propuesta completa de rediseño para transformar el Portfolio Hub en una Digital Sales + Professional Credibility Platform.

---

## 1. FILOSOFÍA DEL REDISEÑO

### Principio rector

```
CLAIM → PROOF → CASE → VALUE → CTA
```

El visitante debe entender en este orden:
1. **Qué hago** (claim)
2. **Mira lo que construí** (proof)
3. **Mira cómo lo construí** (case)
4. **Mira qué problema resolví** (value)
5. **Si tienes un problema parecido, hablemos** (CTA)

### Objetivo de negocio

Optimizar: **ATTENTION → UNDERSTANDING → TRUST → PROOF → ACTION**

No optimizar "que se vea moderno". Optimizar conversión.

---

## 2. ARQUITECTURA DEL SITIO

### Estructura de navegación

```
INICIO (/)
├── Hero + Evidencia
├── Featured Case Study (SalsaQuest)
├── Capacidades
├── Proyectos (Tier 1-3)
├── Sobre mí
└── Contacto

PROYECTOS (/proyectos) — opcional, puede ser scroll en una página
├── Tier 1: Business Proof
├── Tier 2: Product Proof
├── Tier 3: Technical Proof
└── Trabajo para otros
```

### Máximo 5 secciones en la página principal:

1. **Hero** (quién soy + qué hago + evidencia inmediata)
2. **Featured Case Study** (SalsaQuest / Son Havana)
3. **Qué puedo hacer** (capacidades orientadas a problemas)
4. **Proyectos** (jerarquizados, no todos iguales)
5. **Sobre mí** (historia + credenciales)
6. **Contacto** (visible pero no agresivo)

---

## 3. HERO — PROPUESTA DETALLADA

### Alternativa A (Recomendada): Evidencia + Claridad

```
EYEBROW: SOFTWARE · IA · PRODUCTOS DIGITALES

HEADLINE: Construyo software y soluciones digitales
que convierten problemas reales en productos funcionales.

LEAD: Aplicaciones web, automatización e IA aplicada
para crear experiencias digitales útiles, rápidas y escalables.

CTA PRINCIPAL: VER PROYECTOS
CTA SECUNDARIO: HABLEMOS

EVIDENCIA ABOVE THE FOLD:
[3 screenshots de proyectos destacados con status "En producción"]
- SalsaQuest → En producción
- EduPack Builder → En producción
- OSINT Search Pro → En producción
```

**Por qué funciona:**
- Responde inmediatamente: ¿qué hace? → construye software
- Muestra evidencia real (screenshots de apps funcionando)
- CTA de bajo compromiso ("ver proyectos") antes del CTA de alto compromiso ("hablemos")
- No promete cosas que no puede demostrar

### Alternativa B: Orientada a problemas

```
EYEBROW: DESARROLLO WEB · AUTOMATIZACIÓN · IA

HEADLINE: Transformo problemas reales en
soluciones digitales que funcionan.

LEAD: Desde aplicaciones web hasta agentes de IA —
construyo productos digitales con evidencia, no promesas.

CTA PRINCIPAL: VER CASOS DE ESTUDIO
CTA SECUNDARIO: CONOCER MÁS SOBRE MÍ
```

### Alternativa C: Orientada a resultados

```
EYEBROW: SOFTWARE ENGINEER · AI · AUTOMATION

HEADLINE: Mira lo que construí.

LEAD: Aplicaciones web en producción, agentes de IA funcionando,
y sistemas que resuelven problemas reales. Sin humo.

CTA PRINCIPAL: VER PROYECTOS
CTA SECUNDARIO: CONTACTARME
```

### Selección recomendada: **Alternativa A**

Es la que mejor equilibra claridad, evidencia y conversión.

---

## 4. SECCIONES DETALLADAS

### 4.1 HERO

**Función:** Comunicar quién soy, qué construyo, y mostrar evidencia inmediata.

**Contenido:**
- Nombre: Álvaro Berrío
- Título: Software Developer · IA Aplicada · Productos Digitales
- Headline: Construyo software y soluciones digitales que convierten problemas reales en productos funcionales.
- Lead: Aplicaciones web, automatización e IA aplicada para crear experiencias digitales útiles, rápidas y escalables.
- CTAs: VER PROYECTOS (principal) + HABLEMOS (secundario)
- Evidencia: 3 proyectos destacados con screenshots y status

**Diseño:**
- Sin video de fondo (consume performance, no agrega valor)
- Fondo oscuro sólido con textura sutil
- Jerarquía clara: headline > lead > CTAs > evidencia
- Los 3 proyectos destacados como mini-cards con screenshot + nombre + status

**Mobile:**
- Headline más corto en móvil
- 2 proyectos visibles, scroll horizontal para el tercero
- CTAs apilados verticalmente

### 4.2 FEATURED CASE STUDY — SalsaQuest / Son Havana

**Función:** Demostrar capacidad de crear valor para un negocio real.

**Contenido:**

```
CASO DE ESTUDIO: SalsaQuest
Experiencia digital interactiva para Son Havana

CONTEXTO
Son Havana es un bar de salsa y son cubano en Medellín.
Necesitaba una experiencia digital que diferenciara su propuesta
de la competencia (menús digitales y directorios básicos).

PROBLEMA
Ningún negocio de salsa en la ciudad ofrecía una experiencia
digital interactiva para turistas.

SOLUCIÓN
Construí una aplicación web con:
- Storytelling interactivo sobre la historia de la salsa
- Trivia gamificada con leaderboard
- Biografías de artistas con modal de detalle
- Línea de tiempo filtrable por década
- Registro de usuarios con captura de datos
- Reproductor de Spotify embebido

TECNOLOGÍAS
Python · Flask · SQLAlchemy · JavaScript · CSS Glassmorphism

RESULTADO
Aplicación en producción funcionando en PythonAnywhere.
Experiencia única que ningún otro negocio de salsa ofrece en la ciudad.

DEMO
[Screenshot + link a la app en vivo]

CÓDIGO
[Link a GitHub]
```

**Diseño:**
- Sección dedicada, no una card más en el accordion
- Layout de 2 columnas: contenido a la izquierda, demo/screenshot a la derecha
- En móvil: apilado verticalmente
- CTA: "Ver caso completo" (si se crea página dedicada) o "Ver demo" + "Ver código"

### 4.3 QUÉ PUEDO HACER (Capacidades)

**Función:** Comunicar capacidades de forma orientada a problemas, no solo tecnologías.

**Contenido:**

```
CAPACIDADES

DESARROLLO WEB
Transformo procesos o ideas en aplicaciones web funcionales.
→ Python · Flask · SQLAlchemy · JavaScript · HTML/CSS

AUTOMATIZACIÓN
Reduzco tareas repetitivas mediante flujos automatizados.
→ APIs · Scraping · Procesamiento de datos · Integraciones

IA APLICADA
Integro IA cuando aporta valor real al producto o proceso.
→ Modelos · APIs · Agentes · Análisis de datos

SISTEMAS DIGITALES
Diseño soluciones que conectan usuarios, información y procesados.
→ Arquitectura · Bases de datos · Auth · Testing
```

**Diseño:**
- Grid de 2×2 en desktop, 1 columna en móvil
- Cada capacidad: título + descripción breve + tecnologías como pills
- Sin cards excesivas, sin animaciones sin función
- Colores: amber para web, teal para automatización, magenta para IA, mixto para sistemas

### 4.4 PROYECTOS

**Función:** Mostrar evidencia de trabajo real, jerarquizada por impacto.

**Contenido:**

```
PROYECTOS

[TIER 1 — BUSINESS PROOF]
SalsaQuest → Experiencia web interactiva para Son Havana
EduPack Builder → Agente autónomo de curación de datos con IA

[TIER 2 — PRODUCT PROOF]
OSINT Search Pro → Plataforma de ciberinteligencia
Portfolio Engine → Sistema multi-perfil con autenticación

[TIER 3 — TECHNICAL PROOF]
RockQuest → Enciclopedia interactiva de rock
Aventura Antioqueña → Juego educativo compilado a WebAssembly
CodeAudit → Auditor estático de repositorios Python

[TRABAJO PARA OTROS]
Portafolios profesionales · Landing Lisbeth
```

**Diseño:**
- NO usar accordion — usar cards expandidas o grid
- Cada proyecto: screenshot + nombre + descripción corta + tags + links
- Tier badges visuales (colores diferentes por tier)
- Filtros simplificados: Todos | Web | IA | Productos | Casos reales
- Máximo 7 proyectos visibles sin scroll excessivo

**Filtros propuestos:**
1. Todos
2. Web apps
3. IA & Automatización
4. Productos
5. Casos reales (SalsaQuest, portafolios)

### 4.5 SOBRE MÍ

**Función:** Conectar humanamente, contar la historia, generar confianza.

**Contenido:

```
SOBRE MÍ

[Foto profesional]

Soy Álvaro Berrío, estudiante de Ingeniería de Sistemas
en Medellín, Colombia.

Construyo software y soluciones digitales mientras
desarrollo mi carrera como desarrollador.

ME INTERESA RESOLVER:
- Problemas que se pueden resolver con tecnología
- Procesos que se pueden automatizar
- Ideas que se pueden convertir en productos digitales

QUÉ ESTUDIO:
Ingeniería de Sistemas

QUÉ CONSTRUYO:
Aplicaciones web, automatización, IA aplicada,
y productos digitales para negocios y profesionales.

HACIA DÓNDE VOY:
Evolucionar hacia desarrollo de software profesional,
IA aplicada y soluciones digitales para negocios.

GitHub: [link]
LinkedIn: [link]
Email: [link]
```

**Diseño:**
- Layout de 2 columnas: foto a la izquierda, contenido a la derecha
- En móvil: apilado
- Tono: profesional pero humano, sin exagerar
- Sin "AI Engineer & Automation Developer" como título — suena a exageración para un estudiante

### 4.6 CONTACTO

**Función:** Facilitar la comunicación sin ser agresivo.

**Contenido:**

```
CONTACTO

¿Tienes un problema que se puede resolver con tecnología?
¿Necesitas un desarrollador para tu proyecto?
¿Quieres conocer mi trabajo?

HABLEMOS

[Email]
[LinkedIn]
[GitHub]
[WhatsApp — solo si corresponde]
```

**Diseño:**
- Sección limpia, sin formulario (el formulario genera fricción)
- Links a canales de contacto directos
- CTA: "Hablemos" (simple, directo)
- No mostrar número de WhatsApp como CTA principal — solo como opción

---

## 5. NAVEGACIÓN

### Estado actual

No hay navegación. Solo el header con nombre + GitHub link.

### Propuesta

```
HEADER FIJO (sticky):
[Álvaro Berrío] ← [Proyectos] [Capacidades] [Sobre mí] [Contacto]

En móvil: hamburger menu
```

**Reglas:**
- Header minimalista: nombre a la izquierda, links a la derecha
- Sin logo complejo — el nombre es la marca
- Header se vuelve más compacto al hacer scroll
- CTA "Hablemos" en el header como botón destacado

---

## 6. DISEÑO VISUAL

### Principios

- **Premium digital product**, no template portfolio
- Jerarquía clara con whitespace
- Sin glassmorphism excesivo
- Sin gradients neón
- Sin video de fondo (consumo innecesario)
- Fondo oscuro sólido con textura sutil
- Contraste alto para legibilidad
- Motion design con función (no decorativo)

### Paleta (mantener la actual)

| Token | Valor | Uso |
|-------|-------|-----|
| --bg | #0B0D12 | Fondo |
| --surface | #13161D | Cards |
| --surface-2 | #1B1F29 | Cards elevadas |
| --line | #262B36 | Bordes |
| --text | #EDEAE2 | Texto primario |
| --muted | #8A8F9C | Texto secundario |
| --amber | #E3A24C | Acento primario |
| --teal | #46D7C0 | Acento secundario |
| --magenta | #E34C9E | Acento terciario |

### Tipografía (mantener)

| Fuente | Rol |
|--------|-----|
| Fraunces | Display, títulos |
| Inter | Body text |
| JetBrains Mono | Monospace, badges, pills |

### Componentes clave

1. **Hero**: Full-width, fondo sólido, headline grande + lead + CTAs + mini-cards de evidencia
2. **Featured Case Study**: 2 columnas (contenido + demo), fondo ligeramente elevado
3. **Capacidades**: Grid 2×2, cada item con título + descripción + pills
4. **Proyectos**: Cards con screenshot + meta info, no accordion
5. **Sobre mí**: 2 columnas (foto + contenido)
6. **Contacto**: Links directos, sin formulario

---

## 7. MOBILE FIRST

### Breakpoints

| Breakpoint | Uso |
|------------|-----|
| 320px | Mínimo absoluto |
| 375px | iPhone SE/Mini |
| 390px | iPhone estándar |
| 430px | iPhone Plus/Max |
| 768px | Tablet |
| 1024px | Desktop pequeño |
| 1280px | Desktop estándar |
| 1440px | Desktop grande |
| 1920px | Full HD |

### Estrategia mobile

- **No** versión reducida de desktop
- **Sí** experiencia diseñada para cada tamaño
- En móvil: todo apilado verticalmente
- CTAs stacked, no side-by-side
- Screenshots más pequeños, scroll horizontal para proyectos
- Navegación hamburger

---

## 8. SEO

### Meta tags

```html
<title>Álvaro Berrío — Software Developer | IA Aplicada | Productos Digitales</title>
<meta name="description" content="Desarrollador de software especializado en aplicaciones web, automatización e IA aplicada. Proyectos en producción con Python, Flask y más.">
<meta name="keywords" content="desarrollador web, desarrollador Python, Flask, software, IA aplicada, automatización, Medellín, Colombia">
```

### Open Graph

```html
<meta property="og:title" content="Álvaro Berrío — Software Developer">
<meta property="og:description" content="Construyo software y soluciones digitales que convierten problemas reales en productos funcionales.">
<meta property="og:type" content="website">
<meta property="og:image" content="[screenshot del portfolio]">
```

### Estructura semántica

- `<header>` con nav
- `<main>` con secciones
- `<section>` para cada área
- `<article>` para proyectos
- `<footer>` con links

---

## 9. PERFORMANCE

### Prioridades

1. **Eliminar video de fondo** → ahorra ~20MB de carga
2. **Eliminar iframes embebidos** → cada iframe carga una app completa
3. **Usar screenshots + links** → mucho más ligero que iframes
4. **Lazy loading en imágenes** → carga diferida
5. **Prefetch de fonts** → evitar FOIT
6. **Minimizar CSS inline** → extraer a archivo externo si es posible
7. **Eliminar animaciones innecesarias** → waveform animado no agrega valor

### Métricas objetivo

| Métrica | Objetivo |
|---------|----------|
| LCP | < 2.5s |
| INP | < 200ms |
| CLS | < 0.1 |
| Peso total | < 500KB (sin imágenes pesadas) |
| Requests | < 15 |

---

## 10. SEGURIDAD

### Auditoría de seguridad actual

| Problema | Severidad | Ubicación |
|----------|-----------|-----------|
| `debug=True` en app.py | Alta | app.py:47 |
| Secret key hardcodeada | Alta | app.py:5 |
| Admin credentials en env vars con defaults | Media | app.py:7-8 |
| .env.example con valores placeholder | Baja | .env.example |
| Sin CSRF protection | Media | Formularios |
| Sin rate limiting | Media | Login |
| Sin HTTPS enforcement | Media | Deploy |

### Acciones requeridas (antes de deploy)

1. Quitar `debug=True`
2. Usar secrets de entorno reales
3. Agregar CSRF protection
4. Agregar rate limiting al login
5. Forzar HTTPS
6. No exponer `.env` en repositorio

---

## 11. CONTENIDO A PRESERVAR

### NO modificar

- Perfiles de Gilberto Berrío Serrano
- Perfiles de Lisbeth Ibelice Cabello
- Perfiles de Claudio José Berrío
- Perfiles de Rhonela Martínez Cabello
- Contenido de Son Havana (sitio del negocio)
- Funcionalidad de login/logout
- Ruta /familia (portal familiar privado)

### Puede modificar

- Hero principal
- Estructura de navegación
- Jerarquía de proyectos
- Copy del sitio
- Diseño visual
- Filtros
- CTAs
- Meta tags
- CSS

---

## 12. IMPLEMENTACIÓN RECOMENDADA

### Orden de ejecución

1. **Crear nueva versión de base.html** con la estructura propuesta
2. **Implementar Hero** con alternativa A
3. **Implementar Featured Case Study** de SalsaQuest
4. **Implementar sección Capacidades**
5. **Implementar sección Proyectos** con jerarquía
6. **Implementar sección Sobre mí**
7. **Implementar sección Contacto**
8. **Implementar navegación**
9. **Optimizar performance** (quitar video, iframes)
10. **Agregar SEO** (meta tags, Open Graph)
11. **Corregir seguridad** (debug, secrets, CSRF)
12. **QA completo** (responsive, accessibility, links)

### NO hacer

- No crear archivos nuevos innecesarios
- No modificar /familia ni login
- No modificar perfiles de familiares
- No agregar dependencias nuevas
- No hacer commits
- No hacer push
- No inventar contenido
- No exagerar capacidades

---

## 13. MÉTRICAS DE ÉXITO

### 5-SECOND TEST

Un visitante debería poder responder:
- ✅ ¿Qué hago? → Construyo software y soluciones digitales
- ✅ ¿Qué construyo? → Aplicaciones web, automatización, IA
- ✅ ¿Por qué debería confiar? → Proyectos en producción, screenshots, código
- ✅ ¿Qué puedo ver? → Proyectos destacados, caso de estudio
- ✅ ¿Cómo contacto? → Hablemos (email, LinkedIn, GitHub)

### 30-SECOND TEST

Debe poder identificar:
- ✅ Especialidad: Software + IA + Productos digitales
- ✅ Proyectos principales: SalsaQuest, EduPack, OSINT
- ✅ Evidencia: Apps en producción, código en GitHub
- ✅ Propuesta de valor: Convierto problemas en productos funcionales

### 2-MINUTE TEST

Debe poder explorar:
- ✅ Caso de estudio de SalsaQuest
- ✅ Código en GitHub
- ✅ Demo de apps en vivo
- ✅ Capacidades y tecnologías
- ✅ Contacto

---

## 14. CRITERIOS DE ACEPTACIÓN

El rediseño se considera completo SI:

- [ ] El Hero comunica claramente qué hace Álvaro
- [ ] SalsaQuest aparece como Featured Case Study
- [ ] Los proyectos están jerarquizados por impacto
- [ ] Existe una sección "Sobre mí"
- [ ] Los CTAs tienen jerarquía clara
- [ ] El visitante entiende en 5 segundos qué hace
- [ ] El sitio funciona en mobile (320px - 1920px)
- [ ] No hay claims sin evidencia
- [ ] No se inventaron resultados
- [ ] No se modificaron perfiles ajenos
- [ ] No se rompieron funcionalidades existentes
- [ ] El rendimiento es aceptable (LCP < 2.5s)
- [ ] No hay enlaces rotos
- [ ] Los meta tags están optimizados
- [ ] La seguridad está corregida

---

## 15. PRINCIPIO FINAL

No intentar convencer al visitante de que Álvaro es "el mejor desarrollador".

Demostrar:

> **"Mira lo que construí."**

Después:

> **"Mira cómo lo construí."**

Después:

> **"Mira qué problema resolví."**

Y finalmente:

> **"Si tienes un problema parecido, hablemos."**
