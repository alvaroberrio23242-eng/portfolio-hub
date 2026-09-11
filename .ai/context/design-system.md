# Berrío Design System — Contexto

## Identidad

- **Nombre**: Berrío Design System
- **Marca**: Berrio Digital Lab
- **Propietario**: Alvaro Berrio — AI Engineer & Automation Developer
- **Alcance**: Tokens, documentación y (futuros) componentes compartidos para todos los proyectos del ecosistema Berrio.

## Proyectos del ecosistema

| Proyecto | Tipo | Stack | Estado |
|----------|------|-------|--------|
| Portfolio Hub | Portfolio web | Flask + Jinja2 + CSS inline | Activo |
| SalsaQuest | Juego educativo | Por definir | Fase de diseño |
| RockQuest | Juego educativo | Por definir | Fase de diseño |
| OSINT Search Pro | Herramienta OSINT | Por definir | Fase de diseño |
| EduPack Builder | Builder educativo | Por definir | Fase de diseño |
| CodeAudit | Auditoría de código | Por definir | Fase de diseño |
| Aventura Web | Experiencia narrativa | Por definir | Fase de diseño |
| ProyectoGatico | Proyecto experimental | Por definir | Fase de diseño |

## Tema visual

El sistema es **dark-mode only**. No existe variante light.

### Paleta de colores

| Token | Valor | Rol |
|-------|-------|-----|
| `--bg` | `#0B0D12` | Fondo de página (near-black) |
| `--surface` | `#13161D` | Fondo de tarjeta/panel |
| `--surface-2` | `#1B1F29` | Fondo de tarjeta elevada/abierta |
| `--line` | `#262B36` | Bordes y divisores |
| `--text` | `#EDEAE2` | Texto primario (off-white cálido) |
| `--muted` | `#8A8F9C` | Texto secundario |
| `--amber` | `#E3A24C` | Acento primario (CTA, Territorio) |
| `--teal` | `#46D7C0` | Acento secundario (Talento, focus ring) |
| `--magenta` | `#E34C9E` | Acento terciario (Comunicación, errores) |

Colores hardcoded secundarios:
| Valor | Uso |
|-------|-----|
| `#05070a` | Fondos de embed/terminal/filetree |
| `#B9F5E8` | Texto `<pre>` en terminal (mint brillante) |

### Tipografía

| Fuente | Familia CSS | Pesos | Rol |
|--------|-------------|-------|-----|
| Fraunces | `'Fraunces', serif` | 300, 500, 600, 700 | Display, títulos (h1, .card-title, .lab-name) |
| Inter | `'Inter', system-ui, sans-serif` | 400, 500, 600 | Texto cuerpo, UI general |
| JetBrains Mono | `'JetBrains Mono', monospace` | 400, 500, 600 | Monoespaciado (badges, pills, terminal, labels) |

### Escala de espaciado

Basada en incrementos de 2px: `0, 2, 4, 5, 6, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 28, 30, 32, 40, 46, 48, 50, 56, 60, 70, 80`

### Border-radius

| Valor | Uso |
|-------|-----|
| `2px` | Barras de waveform |
| `4px` | Why-note |
| `8px` | Inputs, botones, case-study |
| `10px` | Embeds, terminal, filetree |
| `14px` | Tarjetas principales |
| `20px` | Pills, links, badges (pill-shaped) |
| `50%` | Círculos (dots de terminal) |

### Transiciones

| Propiedad | Duración | Timing |
|-----------|----------|--------|
| border-color, background | .25s | ease |
| background, color | .2s | ease |
| transform | .3s | ease |
| max-height (accordion) | .4s | ease |

### Breakpoints

| Breakpoint | Uso |
|------------|-----|
| `560px` | Único breakpoint responsive (mobile) |
| `prefers-reduced-motion: reduce` | Accesibilidad — desactiva animaciones |

### Mapeo de acento por categoría

| Categoría | Accent | Token |
|-----------|--------|-------|
| Territorio | Amber | `--amber` |
| Ingeniería (01, 02) | Amber | `--amber` |
| Talento | Teal | `--teal` |
| Ingeniería (03, 05, 06, 07) | Teal | `--teal` |
| Comunicación | Magenta | `--magenta` |
| Ingeniería (04) | Magenta | `--magenta` |

## Estructura del monorepo (objetivo)

```
packages/
  berrio-ui/
    tokens/         ← FASE 1.0 (actual)
    components/     ← FASE 1.1+
```

## Estado actual de FASE 1.0

- [x] Tokens CSS extraídos de auditoría
- [x] Documentación de diseño creada
- [x] ADR-002 registrada
- [ ] Componentes reutilizables (FASE 1.1)
- [ ] Integración con proyectos existentes (FASE 2.0+)

## Reglas de FASE 1.0

1. **NO** modificar Portfolio Hub visual ni funcionalmente.
2. **NO** modificar ningún proyecto existente.
3. **NO** eliminar CSS inline existente.
4. **NO** instalar dependencias nuevas.
5. **NO** crear componentes aún (eso es FASE 1.1).
6. Solo crear tokens y documentación.
