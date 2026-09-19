# Case Study Videos Checklist

> Convención de nombres: `static/case-studies/<slug>-bg.mp4` (kebab-case, ASCII, sin acentos)
> Recomendación: 8–15s loop seamless, <2MB ideal (<5MB máx), 1280×720 o 1920×1080, H.264 High Profile, 24-30fps, 1.5–3 Mbps, sin audio.
> Poster opcional: `static/case-studies/<slug>-poster.jpg` (frame representativo)

| # | Ficha (título visible) | Slug usado | Video esperado | Poster opcional | Estado |
|---|------------------------|------------|----------------|-----------------|--------|
| 1 | Ruta Salsera | `ruta-salsera` | `static/case-studies/ruta-salsera-bg.mp4` | `static/case-studies/ruta-salsera-poster.jpg` | ⬜ Pendiente |
| 2 | Café La Protectora | `cafe-la-protectora` | `static/case-studies/cafe-la-protectora-bg.mp4` | `static/case-studies/cafe-la-protectora-poster.jpg` | ⬜ Pendiente |

> **Nota:** Al agregar nuevas fichas a "Casos de estudio destacados", añade una fila aquí con el mismo patrón.
> El video se carga automáticamente cuando la ficha entra en viewport (IntersectionObserver).
> Si el archivo no existe, se muestra el fallback (emoji + texto) sin error visual.
> `prefers-reduced-motion: reduce` → fallback directo, sin request de video.