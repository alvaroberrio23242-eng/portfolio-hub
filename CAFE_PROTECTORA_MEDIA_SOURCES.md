# CAFÉ LA PROTECTORA — FUENTES DE MEDIOS

**Fecha:** 11 Sep 2026
**Propósito:** Documentar imágenes genéricas de café con licencia libre de uso comercial para las secciones del sub-app Flask.

---

## REGLA DE DERECHOS DE AUTOR

**NO se utiliza ninguna imagen del sitio oficial real (cafelaprotectora.com.ve).**
Todas las imágenes son genéricas (no identificables como Café La Protectora ni como la marca real).
Se privilegia contenido de Wikimedia Commons (CC0/CC-BY/CC-BY-SA) y Pexels (licencia propia, uso comercial sin atribución).

---

## IMÁGENES SELECCIONADAS

### 1. SECCIÓN: ORIGEN — Paisaje de montaña/finca cafetera

| Campo | Valor |
|-------|-------|
| **Archivo** | `Coffee_Farm.jpg` |
| **URL de descarga** | `https://upload.wikimedia.org/wikipedia/commons/7/79/Coffee_Farm.jpg` |
| **Página de origen** | `https://commons.wikimedia.org/wiki/File:Coffee_Farm.jpg` |
| **Autor** | Frank_am_Main |
| **Licencia** | CC-BY-SA-2.0 (Creative Commons Attribution-Share Alike 2.0 Generic) |
| **Condición** | Atribución obligatoria + ShareAlike |
| **Descripción** | Vista general de una pequeña finca cafetera (Colombia, 2009) |
| **Uso en el proyecto** | Sección Origen (`/cafe/origen`) — hero/banner |
| **Resolución original** | 1,280 × 851 px (282 KB) |
| **Optimización** | Redimensionar a 1,200px ancho, convertir a WebP, lazy loading |

---

### 2. SECCIÓN: PROCESO — Tueste de café

| Campo | Valor |
|-------|-------|
| **Archivo** | `Coffee_Roaster-1.jpg` |
| **URL de descarga** | `https://upload.wikimedia.org/wikipedia/commons/c/cc/Coffee_Roaster-1.jpg` |
| **Página de origen** | `https://commons.wikimedia.org/wiki/File:Coffee_Roaster-1.jpg` |
| **Autor** | Visitor7 |
| **Licencia** | CC-BY-SA-3.0 (Creative Commons Attribution-Share Alike 3.0 Unported) |
| **Condición** | Atribución obligatoria + ShareAlike |
| **Descripción** | Granos de café being discharged and cooled at end of roasting cycle. Victrola Coffee Roasters, Seattle (2013) |
| **Uso en el proyecto** | Sección Proceso (`/cafe/proceso`) — paso de torrefacción |
| **Resolución original** | 4,301 × 3,072 px (1.76 MB) |
| **Optimización** | Redimensionar a 1,200px ancho, convertir a WebP, lazy loading |

---

### 3. SECCIÓN: PRODUCTOS — Granos de café molido

| Campo | Valor |
|-------|-------|
| **Archivo** | `Coffee_beans_(Unsplash).jpg` |
| **URL de descarga** | `https://upload.wikimedia.org/wikipedia/commons/9/99/Coffee_beans_%28Unsplash%29.jpg` |
| **Página de origen** | `https://commons.wikimedia.org/wiki/File:Coffee_beans_(Unsplash).jpg` |
| **Autor** | Mark Daynes (Unsplash, pre-2017) |
| **Licencia** | CC0 1.0 Universal (Public Domain Dedication) |
| **Condición** | Sin atribución requerida |
| **Descripción** | Granos de café marrón, close-up |
| **Uso en el proyecto** | Sección Productos (`/cafe/productos`) — banner o fondo |
| **Resolución original** | 5,472 × 3,648 px (546 KB) |
| **Optimización** | Redimensionar a 1,200px ancho, convertir a WebP, lazy loading |

---

### 4. SECCIÓN: PRODUCTOS — Taza de café

| Campo | Valor |
|-------|-------|
| **Archivo** | `Brown_cup_of_coffee.jpg` |
| **URL de descarga** | `https://upload.wikimedia.org/wikipedia/commons/1/1f/Brown_cup_of_coffee.jpg` |
| **Página de origen** | `https://commons.wikimedia.org/wiki/File:Brown_cup_of_coffee.jpg` |
| **Autor** | DocteurCosmos |
| **Licencia** | CC-BY-3.0 + GFDL (dual license) |
| **Condición** | Atribución obligatoria |
| **Descripción** | Taza de café negro en taza parda |
| **Uso en el proyecto** | Sección Productos (`/cafe/productos`) — tarjeta o detalle |
| **Resolución original** | 2,272 × 1,704 px (551 KB) |
| **Optimización** | Redimensionar a 1,200px ancho, convertir a WebP, lazy loading |

---

### 5. SECCIÓN: CULTURA — Escena de cafetería

| Campo | Valor |
|-------|-------|
| **Fuente** | Pexels (pexels.com) |
| **IDs candidatos** | Photo 1833586, 2530586, 12570668 |
| **URL base** | `https://www.pexels.com/photo/1833586/` (u otra similar) |
| **Licencia** | Pexels License (uso comercial permitido, atribución no requerida pero recomendada) |
| **Condición** | Sin atribución requerida |
| **Descripción** | Interior de cafetería cálida y acogedora |
| **Uso en el proyecto** | Sección Cultura (`/cafe/cultura`) — hero/banner |
| **Optimización** | Descargar versión medium (≤1200px), convertir a WebP, lazy loading |
| **NOTA** | **PENDIENTE**: No se pudo acceder a pexels.com para verificar la licencia exacta de estos IDs específicos. Se recomienda verificar antes de implementar. Alternativa: usar solo las 4 imágenes de Wikimedia Commons ya confirmadas y dejar la sección Cultura con placeholder (emoji/CSS) hasta confirmar la fuente. |

---

## ATTRIBUTION TEXT (para incluir en templates)

### Opción A: Atribución en página (para CC-BY-SA)
```html
<p class="cafe-image-credit">
  Foto: <a href="https://commons.wikimedia.org/wiki/File:Coffee_Farm.jpg">Frank_am_Main</a>,
  licencia <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC BY-SA 2.0</a>
</p>
```

### Opción B: Atribución en footer o sección de créditos
```html
<div class="cafe-credits">
  <p>Imágenes: Coffee Farm (Frank_am_Main, CC BY-SA 2.0), Coffee Roaster (Visitor7, CC BY-SA 3.0),
  Coffee beans (Mark Daynes, CC0), Brown cup of coffee (DocteurCosmos, CC BY 3.0).
  Fuente: Wikimedia Commons.</p>
</div>
```

---

## RESUMEN DE LICENCIAS

| Imagen | Licencia | Atribución | ShareAlike | Uso comercial | Estado |
|--------|----------|------------|------------|---------------|--------|
| Coffee_Farm.jpg | CC-BY-SA-2.0 | Sí | Sí | Sí | **IMPLEMENTADO** en `/cafe/origen` |
| Coffee_Roaster-1.jpg | CC-BY-SA-3.0 | Sí | Sí | Sí | **IMPLEMENTADO** en `/cafe/proceso` |
| Brown_cup_of_coffee.jpg | CC-BY-3.0 | Sí | No | Sí | **IMPLEMENTADO** en `/cafe/productos` |
| Coffee_beans (Unsplash) | CC0 | No | No | Sí | **PENDIENTE** — rate-limited por Wikimedia, reintento necesario |
| Pexels (café) | Pexels License | No | No | Sí | **PENDIENTE** — sección Cultura |

---

## IMÁGENES PENDIENTES

### Coffee_beans_(Unsplash).jpg — Para sección Productos (detalle)
- **URL**: `https://commons.wikimedia.org/wiki/File:Coffee_beans_(Unsplash).jpg`
- **Licencia**: CC0 (dominio público)
- **Razón de pendiente**: Wikimedia devolvió error 429 (rate limit) durante la descarga
- **Acción**: Reintentar descarga cuando el rate limit se resuelva (~24h)
- **Uso previsto**: Fondo o tarjeta en la sección de productos

### Imágenes de Pexels — Para sección Cultura
- **URLs candidatas**: Photo 1833586, 2530586, 12570668
- **Licencia**: Pexels License (uso comercial permitido, atribución no requerida)
- **Razón de pendiente**: No se pudo verificar licencia exacta de IDs específicos
- **Acción**: Verificar en pexels.com antes de implementar
- **Alternativa**: Dejar placeholder (emoji/CSS) hasta confirmar

---

## DECISIÓN SOBRE CULTURA

Dado que no se pudo verificar la licencia exacta de las fotos de Pexels para la sección Cultura, hay dos opciones:

1. **Opción conservadora (recomendada)**: Dejar la sección Cultura con placeholder (emoji/CSS) y documentar que queda pendiente直到 que se confirme la fuente de Pexels.
2. **Opción progresiva**: Usar una de las fotos de Pexels ( Photo 1833586 — "Coffee Shop") con la URL documentada, asumiendo que la Pexels License permite uso comercial sin atribución.

**Recomendación**: Opción conservadora. Mejor un placeholder claro que una fuente dudosa.

---

**Documento creado. Imágenes listas para implementación tras aprobación del usuario.**
