# SALES AUDIT — Portfolio Hub

**Fecha:** 2026-09-09
**Objetivo:** Analizar el funnel de conversión, CTAs, confianza, objeciones y fricción del sitio actual.

---

## 1. FUNNEL ACTUAL

```
VISITANTE LLEGA
    ↓
VE HERO (Agentes de IA para escalar tu negocio)
    ↓
DECIDE: ¿Soy el público? → Si no es dueño de negocio → SALE
    ↓
HACE SCROLL → VE "Índice · 10 fichas"
    ↓
VE FILTROS (Todos | Web apps | Agentes IA | Juegos | Profesionales | Marcas | Portafolios)
    ↓
ABRE UNA CARD (o no)
    ↓
¿QUÉ SIGUE? → No hay ruta clara
    ↓
¿CONTACTA? → Solo si busca WhatsApp/Cal.com
```

### Problemas del funnel

1. **El Hero filtra mal** — expulsa a reclutadores y desarrolladores
2. **No hay puente entre el Hero y los proyectos** — no hay sección intermedia
3. **Los filtros confunden** — 7 categorías, algunas vacías para ciertos públicos
4. **No hay "Sobre mí"** — el visitante no sabe quién es la persona
5. **No hay sección de servicios/capacidades** — ¿qué puede hacer por mí?
6. **No hay evidencia above the fold** — solo texto y CTAs de venta
7. **El accordion no guía** — abre la primera card y ya, sin narrativa

---

## 2. CTAs ACTUALES

| CTA | Ubicación | Tipo | Evaluación |
|-----|-----------|------|------------|
| "💬 Agendar asesoría por WhatsApp" | Hero (principal) | Conversión directa | Demasiado agresivo para visitante frío |
| "📅 Agendar demo de 15 min" | Hero (secundario) | Conversión directa | Demasiado compromiso para visitante nuevo |
| "Abrir app ↗" | Cada card | Exploración | Funcional pero no guía al siguiente paso |
| "Abrir portafolio ↗" | Cards de portafolios | Exploración | OK |
| "Jugar en el navegador ↗" | Aventura Antioqueña | Exploración | OK |
| "💬 Unirme a la lista de espera" | Productos en construcción | Lead capture | Repetido 15 veces → pierde impacto |
| "🔗 github.com/alvaroberrio23242-eng" | Header | Prueba técnica | OK pero bajo perfil |
| Login 🔐 | Footer | Acceso privado | Irrelevante para visitante público |

### Evaluación de CTAs

**Problemas:**
- Solo hay 2 tipos de CTA: "agendar" (alto compromiso) y "abrir" (exploración)
- No hay CTA de bajo compromiso: "ver caso de estudio", "ver mi trabajo", "conocer más"
- No hay CTA diferenciado por público (reclutador vs cliente)
- "Unirme a la lista de espera" × 15 = spam visual
- No hay CTA hacia "Sobre mí" o "Capacidades"

**Recomendaciones:**
- CTA principal de Hero: "VER PROYECTOS" (bajo compromiso)
- CTA secundario: "HABLEMOS" (para quien ya está interesado)
- CTAs contextuales en cada sección
- CTA de reclutador: "VER MI TRAYECTORIA"
- CTA de cliente: "VER CASOS DE ESTUDIO"

---

## 3. CONFIANZA

### ¿Qué genera confianza actualmente?

| Elemento | ¿Existe? | Evaluación |
|----------|----------|------------|
| Proyectos funcionales con link | ✅ Sí | Fuerte — apps reales en producción |
| Código en GitHub | ⚠️ Parcial | Link visible pero no promovido |
| Screenshots | ❌ No | Solo iframes que pueden no cargar |
| Demo en vivo | ⚠️ Parcial | iframes con nota de "puede tardar en despertar" |
| Testimonios | ❌ No | Ninguno |
| Métricas de negocio | ❌ No | Ninguna |
| Casos de estudio | ⚠️ Parcial | Mini casos dentro del accordion, no destacados |
| "Sobre mí" | ❌ No | No existe |
| Formación académica | ❌ No | No mencionada |
| Experiencia laboral | ❌ No | No mencionada |
| Clientes reales | ⚠️ Implícito | Son Havana aparece como "portafolio", no como "cliente" |

### Nivel de confianza actual: BAJO-MEDIO

El sitio tiene evidencia técnica (apps funcionando) pero no la utiliza estratégicamente para generar confianza.

---

## 4. PRUEBA SOCIAL

### ¿Qué prueba social existe?

**Ninguna verificable.**

- No hay testimonios
- No hay logos de clientes
- No hay métricas de negocio
- No hay referencias
- No hay badges de plataformas
- No hay menciones de prensa

### ¿Qué se puede utilizar como prueba social?

- Apps en producción (SalsaQuest, EduPack Builder, OSINT Search Pro, RockQuest)
- Portafolios funcionales para otras personas
- Código en GitHub
- Deploy en plataformas reales (PythonAnywhere, Railway, Render)

### Recomendación

Usar **Proof of Work** como mecanismo principal de confianza:
- "X proyectos en producción"
- "Aplicaciones funcionando en X plataformas"
- Screenshots de apps reales
- Métricas técnicas (tests pasando, uptime, etc.)

**NO inventar testimonios.** Si no existen, no mostrarlos.

---

## 5. OBJECIONES DEL VISITANTE

### Para un dueño de negocio:

| Objeción | ¿Se responde actualmente? |
|----------|--------------------------|
| "¿Puede resolver mi problema?" | Parcialmente — el Hero dice que sí, pero no muestra cómo |
| "¿Tiene experiencia con negocios reales?" | Sí, pero enterrado (Son Havana es proyecto #09) |
| "¿Es una persona o una empresa?" | Confuso — "Berrío Digital Lab" suena a empresa |
| "¿Cuánto cuesta?" | No mencionado |
| "¿Cuánto tarda?" | No mencionado |
| "¿Y si no funciona?" | No abordado |
| "¿Tiene otros clientes?" | No demostrado claramente |

### Para un reclutador:

| Objeción | ¿Se responde actualmente? |
|----------|--------------------------|
| "¿Quién es?" | No — no hay "Sobre mí" |
| "¿Qué sabe hacer?" | Parcialmente — el Hero dice "IA y automatización" |
| "¿Tiene experiencia laboral?" | No mencionada |
| "¿Dónde está el código?" | Link en header, pero bajo perfil |
| "¿Qué tecnologías domina?" | Implícito en los proyectos, no listado |
| "¿Tiene formación?" | No mencionada |
| "¿Dónde está el CV?" | No existe |

### Para un desarrollador:

| Objeción | ¿Se responde actualmente? |
|----------|--------------------------|
| "¿Es buen desarrollador?" | Parcialmente — la calidad de código se infiere |
| "¿Usa buenas prácticas?" | No demostrado |
| "¿Conoce arquitectura?" | Portfolio Engine lo demuestra, pero enterrado |
| "¿Conoce IA de verdad?" | EduPack Builder muestra Anthropic API, pero no destacado |

---

## 6. FRICCIÓN

### Fricciones de alto impacto:

1. **Video de fondo** → carga pesada, puede causar lag en móviles
2. **10+ iframes embebidos** → cada uno carga una app completa, lento
3. **Accordion como única forma de explorar** → el visitante debe hacer click en cada card
4. **Sin navegación** → no hay menú, no hay "Sobre mí", no hay "Servicios"
5. **Sin búsqueda** → con 25+ items, encontrar algo específico es difícil
6. **Filtros confusos** → "Juegos" y "Portafolios" no ayudan a entender el valor
7. **CTAs de alto compromiso** → WhatsApp y Cal.com asustan al visitante nuevo
8. **Sin "Sobre mí"** → el visitante no sabe con quién está hablando
9. **Texto denso en el Hero** → 3 líneas de lead que nadie lee completo

### Fricciones de medio impacto:

1. **No hay lazy loading en imágenes** → todas cargan de golpe
2. **No hay prefetch de fonts** → parpadeo de texto
3. **No hay meta tags de SEO** → no aparece en búsquedas
4. **No hay Open Graph tags** → compartir en redes muestra info genérica
5. **No hay sitemap** → SEO dañado
6. **No hay analytics** → no se puede medir nada

---

## 7. BUYER JOURNEY ACTUAL

### Para dueño de negocio:

```
1. Llega al sitio
2. Ve "Agentes de IA para escalar tu negocio"
3. Piensa: "Suena interesante"
4. Hace scroll
5. Ve "Índice · 10 fichas"
6. Piensa: "¿Qué proyecto debo ver?"
7. Abre una card al azar
8. Lee la descripción
9. No sabe si esto aplica a su negocio
10. O se va, o busca WhatsApp
```

**Problema:** No hay narrativa que guíe al visitante de "interesado" a "listo para contactar".

### Para reclutador:

```
1. Llega al sitio (o le envían el link)
2. Ve "Agentes de IA para escalar tu negocio"
3. Piensa: "Esto no es un portfolio de desarrollador"
4. Hace scroll buscando evidencia técnica
5. Encuentra proyectos, pero no sabe cuáles son los más relevantes
6. No encuentra "Sobre mí", experiencia, formación
7. Se va
```

**Problema:** El sitio no está diseñado para reclutadores. No hay ruta para ellos.

---

## 8. MÉTRICAS SUGERIDAS (post-rediseño)

| Métrica | Herramienta | Objetivo |
|---------|-------------|----------|
| Tiempo en página | Analytics | > 2 min |
| Tasa de rebote | Analytics | < 60% |
| Scrolls hasta proyectos | Scroll tracking | > 80% llegan |
| Clicks en "Ver proyectos" | Event tracking | > 40% |
| Clicks en caso de estudio | Event tracking | > 20% |
| Clicks en contacto | Event tracking | > 10% |
| Tasa de conversión (contacto) | Form tracking | > 5% |

---

## 9. RESUMEN DE PRIORIDADES DE CONVERSIÓN

| # | Cambio | Impacto | Esfuerzo |
|---|--------|---------|----------|
| 1 | Hero con evidencia inmediata + CTA de bajo compromiso | Alto | Medio |
| 2 | Sección "Qué puedo hacer" orientada a problemas | Alto | Medio |
| 3 | Featured Case Study de Son Havana | Alto | Medio |
| 4 | Sección "Sobre mí" | Alto | Bajo |
| 5 | Ruta diferenciada (reclutador vs cliente) | Medio | Medio |
| 6 | Reducir iframes, usar screenshots + links | Medio | Medio |
| 7 | Agregar meta tags y SEO | Medio | Bajo |
| 8 | Agregar prueba social (proof of work) | Medio | Bajo |
| 9 | Simplificar navegación | Medio | Bajo |
| 10 | Agregar analytics | Bajo | Bajo |
