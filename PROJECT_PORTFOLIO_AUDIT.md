# PROJECT PORTFOLIO AUDIT — Portfolio Hub

**Fecha:** 2026-09-09
**Objetivo:** Clasificar todos los proyectos por impacto, evidencia, calidad, relevancia y valor para crear una jerarquía estratégica.

---

## 1. INVENTARIO COMPLETO DE PROYECTOS

### Proyectos en base.html (Flask template — versión principal)

| # | Proyecto | Categoría | Estado | Deploy |
|---|----------|-----------|--------|--------|
| 01 | SalsaQuest | web, ingeniería | En producción | PythonAnywhere |
| 02 | EduPack Builder | web, ia, ingeniería | En producción | Railway |
| 03 | OSINT Search Pro | web, ingeniería | En producción | Railway |
| 04 | RockQuest | juego, ingeniería | En producción | PythonAnywhere |
| 05 | Aventura Antioqueña | juego, ingeniería | En producción | GitHub Pages + itch.io |
| 06 | Portfolio Engine | web, ingeniería, ia | En desarrollo | Privado (sin deploy) |
| 07 | CodeAudit | web, ingeniería | En desarrollo | Local (sin deploy) |
| 01-04 | Portafolios creados | portafolios | En producción | Render |

### Productos "en construcción" (15 items)

| Lab | Producto | ¿Existe? |
|-----|----------|----------|
| Territorio | SurveyForge | No |
| Territorio | ThesisLab Social | No |
| Territorio | Research Builder | No |
| Territorio | Social Insight AI | No |
| Territorio | Community Pulse | No |
| Talento | Assessment Builder | No |
| Talento | MicroLearning Factory | No |
| Talento | Onboarding AI | No |
| Talento | LearningPath AI | No |
| Talento | CulturePulse | No |
| Comunicación | Storytelling AI | No |
| Comunicación | CopyLab | No |
| Comunicación | Content Planner AI | No |
| Comunicación | BrandDNA | No |
| Comunicación | PhotoLab | No |

### Otros proyectos (en directorios separados)

| Proyecto | Directorio | Estado |
|----------|-----------|--------|
| Aventura Web | aventura-web/ | En desarrollo |
| ProyectoGatico | ProyectoGatico/ | Desconocido |
| CodeAudit | codeaudit/ | En desarrollo |
| OSINT Search Pro | OSINT_Search_Pro/ | En desarrollo |
| EduPack Builder | EduPack_Builder/ | En desarrollo |
| Landing Lisbeth | landing-lisbeth/ | En producción (Render) |
| Son Havana (game) | sonhavanagame/ | En producción (PythonAnywhere) |
| Berrio AI Platform | berrio-ai-platform/ | Desconocido |
| Lab Video | labvideo/ | Desconocido |

---

## 2. ANÁLISIS INDIVIDUAL POR PROYECTO

### TIER 1 — BUSINESS PROOF (Mayor evidencia de aplicación real)

---

#### SalsaQuest

**¿Qué problema resuelve?**
Ningún negocio de salsa ofrecía una experiencia digital interactiva — la mayoría se queda en menú digital o directorio básico.

**¿Quién lo necesita?**
Negocios de cultura/salsa que quieren diferenciarse con experiencias interactivas para turistas.

**¿Qué construí?**
Aplicación web Flask con storytelling gamificado, trivia interactiva, biografías de artistas, línea de tiempo, leaderboard, registro de usuarios, y estética glassmorphism sobre video de fondo.

**¿Qué tecnología demuestra?**
Python, Flask, SQLAlchemy, SQLite, JavaScript, CSS glassmorphism, integración de APIs (Spotify), autenticación de usuarios, diseño responsive.

**¿Qué habilidad comercial demuestra?**
Capacidad de crear productos digitales para un negocio real (Son Havana).

**¿Qué evidencia existe?**
- ✅ Deploy en PythonAnywhere (funcionando)
- ✅ Código en GitHub
- ✅ App funcional con múltiples módulos
- ✅ Integración con Spotify API
- ✅ Sistema de usuarios y leaderboard

**¿Qué NO está documentado?**
- No hay métricas de uso del negocio
- No hay testimonio de Son Havana
- No se sabe si el negocio lo está usando activamente

**Tier recomendado:** TIER 1 — BUSINESS PROOF
**Posición en portada:** FEATURED CASE STUDY

---

#### Portfolio Engine (berrio-ai-platform)

**¿Qué problema resuelve?**
Necesidad de un sistema que permita gestionar portfolios académicos/profesionales privados con datos verificables, sin exponer información personal en URLs públicas.

**¿Quién lo necesita?**
Profesionales, académicos, instituciones que necesitan portfolios privados y verificables.

**¿Qué construí?**
Backend Flask multi-perfil con autenticación Flask-Login, 16 tablas SQLAlchemy, sistema de roles (Admin/Owner/Reviewer), verificación por campo, panel administrativo, 39+ tests automatizados.

**¿Qué tecnología demuestra?**
Arquitectura backend seria: SQLAlchemy, Flask-Login, sistema de roles, testing, diseño de base de datos relacional, integridad referencial.

**¿Qué habilidad comercial demuestra?**
Capacidad de diseñar y construir sistemas complejos con lógica de negocio real.

**¿Qué evidencia existe?**
- ✅ 16 tablas documentadas
- ✅ 39+ tests automatizados
- ✅ Código en GitHub
- ⚠️ Sin deploy público

**Tier recomendado:** TIER 2 — PRODUCT PROOF (arquitectura seria, sin deploy)
**Posición en portada:** Segundo nivel, destacado como prueba técnica

---

### TIER 2 — PRODUCT PROOF (Productos funcionales que demuestran capacidad)

---

#### EduPack Builder

**¿Qué problema resuelve?**
Compilar material educativo con licencia libre desde múltiples fuentes tomaba horas de búsqueda manual.

**¿Quién lo necesita?**
Educadores, creadores de contenido educativo, organizaciones que distribuyen material formativo.

**¿Qué construí?**
Agente autónomo Flask que busca en 5 APIs (Wikimedia, Openverse, GitHub, Wikipedia, Internet Archive), filtra por licencia, genera documentación y empaqueta en .zip.

**¿Qué tecnología demuestra?**
Consumo de APIs externas, scraping, procesamiento de datos, generación de documentación, IA (Anthropic API).

**¿Qué evidencia existe?**
- ✅ Deploy en Railway
- ✅ Código en GitHub
- ✅ Métrica: "3 horas → 15 segundos"
- ✅ App funcional

**Tier recomendado:** TIER 2 — PRODUCT PROOF
**Posición en portada:** Segundo nivel

---

#### OSINT Search Pro

**¿Qué problema resuelve?**
Necesidad de una herramienta que agregue información pública de múltiples fuentes OSINT en una sola interfaz, sin pagar licencias costosas.

**¿Quién lo necesita?**
Profesionales de ciberseguridad, investigadores, analistas de inteligencia.

**¿Qué construí?**
Plataforma Flask con 7 motores de búsqueda en paralelo, módulos especializados (emails, dominios, IPs, usernames), interfaz "Recon Console".

**¿Qué tecnología demuestra?**
Scraping, consumo de APIs, arquitectura modular, diseño de interfaz especializada.

**¿Qué evidencia existe?**
- ✅ Deploy en Railway
- ✅ Código en GitHub
- ✅ App funcional
- ✅ Arquitectura extensible documentada

**Tier recomendado:** TIER 2 — PRODUCT PROOF
**Posición en portada:** Segundo nivel

---

### TIER 3 — TECHNICAL PROOF (Demuestran habilidades técnicas específicas)

---

#### RockQuest

**¿Qué problema resuelve?**
No existía una enciclopedia interactiva de rock con estética inmersiva que combinara línea de tiempo, trivia y base de datos de bandas reales.

**¿Quién lo necesita?**
Fans de rock, educadores musicales, curiosos.

**¿Qué construí?**
App Flask/SQLAlchemy con glassmorphism, fondo de video rotativo, línea de tiempo, décadas, subgéneros, trivia, base de datos SQL de bandas y artistas.

**¿Qué tecnología demuestra?**
SQLAlchemy, diseño de base de datos, glassmorphism, responsive design.

**¿Qué evidencia existe?**
- ✅ Deploy en PythonAnywhere
- ✅ Código en GitHub
- ✅ Base de datos con datos reales

**Tier recomendado:** TIER 3 — TECHNICAL PROOF
**Posición en portada:** Tercer nivel

---

#### Aventura Antioqueña

**¿Qué problema resuelve?**
Faltaba un juego educativo accesible desde el navegador que enseñara cultura antioqueña de forma interactiva.

**¿Quién lo necesita?**
Educadores, turistas, personas interesadas en cultura antioqueña.

**¿Qué construí?**
Juego Python/Pygame compilado a WebAssembly con Pygbag, desplegado en GitHub Pages y itch.io.

**¿Qué tecnología demuestra?**
Python, Pygame, WebAssembly, pygbag, compilación cross-platform.

**¿Qué evidencia existe?**
- ✅ Deploy en GitHub Pages
- ✅ Disponible en itch.io
- ✅ Código en GitHub

**Tier recomendado:** TIER 3 — TECHNICAL PROOF
**Posición en portada:** Tercer nivel

---

#### CodeAudit

**¿Qué problema resuelve?**
No existía una herramienta local que auditara repositorios Python/Flask de forma segura, sin ejecutar código ajeno.

**¿Quién lo necesita?**
Desarrolladores Python, equipos de código, empresas que revisan PRs.

**¿Qué construí?**
Motor Flask con análisis regex/AST en subproceso aislado, rate limiting, caché, rúbrica A–F.

**¿Qué tecnología demuestra?**
Análisis estático, AST, seguridad, arquitectura modular, testing.

**¿Qué evidencia existe?**
- ✅ Tests pasando con pytest
- ⚠️ Sin deploy público
- ⚠️ Solo local

**Tier recomendado:** TIER 3 — TECHNICAL PROOF
**Posición en portada:** Tercer nivel (sin deploy = menor impacto)

---

### TIER 4 — EXPERIMENTAL / SECUNDARY

---

#### Portafolios creados (Gilberto, Claudio, Rhonela, Son Havana, Lisbeth)

**Evaluación general:**
Son trabajos de desarrollo web para otras personas, pero no son "productos" de Álvaro. Son servicios.

**Valor para el portafolio:**
- Demuestran capacidad de entregar trabajo a clientes reales
- Demuestran versatilidad (sociólogo, fisioterapeuta, bar)
- Son evidencia de que alguien confió en su trabajo

**Problema:**
- No se documentan como "clientes" (solo "portafolios creados")
- Son Havana aparece como "portafolio" cuando debería ser "caso de estudio de negocio"
- La mayoría son para familiares, no clientes pagados

**Tier recomendado:** TIER 4 — EXPERIMENTAL (como portfolio de servicios)
**Posición en portada:** Agrupados en sección "Trabajo para otros"

---

#### Productos en construcción (15 items)

**Evaluación:**
Ninguno de estos 15 productos existe. Son ideas documentadas. No aportan credibilidad — la restan.

**Problema:**
- 15 cards "en construcción" = el 60% del contenido del sitio no existe
- Genera la impresión de que el sitio es un brainstorm, no un portafolio
- Cada card tiene un CTA "Unirme a la lista de espera" que nadie usaría

**Recomendación:** NO mostrar estos productos en el portafolio público. Si se quieren mantener, moverlos a una sección interna o privada.

---

## 3. JERARQUÍA FINAL RECOMENDADA

### PORTADA (Above the fold + primer scroll)

```
HERO
  ├── Eyebrow: SOFTWARE · IA · PRODUCTOS DIGITALES
  ├── Headline: Construyo software y soluciones digitales
  ├── Lead: Aplicaciones web, automatización e IA aplicada
  ├── CTA principal: VER PROYECTOS
  ├── CTA secundario: HABLEMOS
  └── Evidencia inmediata: 3 proyectos destacados con screenshots

FEATURED CASE STUDY — SalsaQuest / Son Havana
  ├── Problema
  ├── Solución
  ├── Resultado
  └── CTA: Ver caso completo

CAPACIDADES (Qué puedo hacer)
  ├── Desarrollo Web
  ├── Automatización
  ├── IA Aplicada
  └── Sistemas Digitales

SOBRE MÍ
  ├── Quién soy
  ├── Qué estudio
  ├── Qué construyo
  └── Hacia dónde voy
```

### SEGUNDO NIVEL

```
PROYECTOS — TIER 1-2
  ├── SalsaQuest (Featured)
  ├── EduPack Builder
  ├── OSINT Search Pro
  └── Portfolio Engine

PROYECTOS — TIER 3
  ├── RockQuest
  ├── Aventura Antioqueña
  └── CodeAudit

TRABAJO PARA OTROS
  ├── Portafolios profesionales
  └── Landing Lisbeth
```

### NO MOSTRAR EN PORTAFOLIO PÚBLICO

```
ELIMINADOS DE PORTADA
  ├── 15 productos en construcción (SurveyForge, ThesisLab, etc.)
  ├── Categorías "Territorio", "Talento", "Comunicación"
  └── Sección "Portafolios creados" como items principales
```

---

## 4. MATRIZ DE DECISIÓN POR PROYECTO

| Proyecto | Impacto | Evidencia | Calidad | Relevancia | Tier | ¿En portada? |
|----------|---------|-----------|---------|------------|------|--------------|
| SalsaQuest | Alto | Alta | Alta | Alta | T1 | Featured |
| Portfolio Engine | Alto | Media | Alta | Alta | T2 | Segundo nivel |
| EduPack Builder | Medio-Alto | Alta | Alta | Media-Alta | T2 | Segundo nivel |
| OSINT Search Pro | Medio | Alta | Alta | Media | T2 | Segundo nivel |
| RockQuest | Medio | Alta | Media-Alta | Media | T3 | Tercer nivel |
| Aventura Antioqueña | Medio | Alta | Media | Media-Baja | T3 | Tercer nivel |
| CodeAudit | Medio | Baja | Media-Alta | Media-Baja | T3 | Tercer nivel |
| Portafolios creados | Bajo-Medio | Media | Media | Media | T4 | Agrupados |
| 15 productos en construcción | Nulo | Nula | N/A | Nula | ELIMINAR | No |

---

## 5. RECOMENDACIONES ESPECÍFICAS

### SalsaQuest → Featured Case Study

El proyecto debe tener su propia sección dedicada, no ser "proyecto #01" en un accordion.

**Estructura recomendada:**
```
CASO DE ESTUDIO: SalsaQuest
  ├── Contexto: Son Havana, bar de salsa en Medellín
  ├── Problema: Sin experiencia digital interactiva
  ├── Solución: App Flask con storytelling + trivia
  ├── Tecnología: Python/Flask/SQLAlchemy/JS
  ├── Resultado: En producción, funcionando
  ├── Demo: Screenshot + link
  ├── Código: GitHub link
  └── CTA: Ver demo / Ver código
```

### Son Havana → Contexto del caso, no proyecto separado

Son Havana no es un "proyecto" — es el contexto comercial de SalsaQuest. Debe aparecer como parte del caso de estudio, no como una card separada.

### Portfolio Engine → Prueba técnica destacada

Es la prueba más fuerte de capacidad de arquitectura. Debe destacarse aunque no tenga deploy público. Mostrar:
- 16 tablas documentadas
- 39+ tests
- Sistema de roles
- Verificación por campo

### Productos en construcción → ELIMINAR de portada

No aportan credibilidad. Son ideas, no productos. Si se quieren mantener, crear una sección privada (detrás del login de /familia).

### Portafolios creados → Reconfigurar como "Servicios"

No mostrar como "portafolios creados" (suena amateur). Mostrar como "Proyectos para otros" o "Trabajo entregado", con énfasis en Son Havana como caso de negocio real.
