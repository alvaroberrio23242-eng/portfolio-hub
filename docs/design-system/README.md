# Berrío Design System

Sistema de diseño centralizado para el ecosistema Berrio Digital Lab.

## Estado

**FASE 1.0** — Design Tokens + Documentación

Los componentes reutilizables (Button, Card, Navbar, etc.) se crearán en FASE 1.1+.

## Estructura

```
packages/berrio-ui/
  tokens/
    colors.css       ← Paleta de colores (dark-mode only)
    typography.css   ← Fuentes, tamaños, pesos, line-heights
    spacing.css      ← Escala de espaciado
    radius.css       ← Border-radius tokens
    motion.css       ← Transiciones y animaciones
    breakpoints.css  ← Media queries
```

## Uso

### Importar tokens

```html
<link rel="stylesheet" href="packages/berrio-ui/tokens/colors.css">
<link rel="stylesheet" href="packages/berrio-ui/tokens/typography.css">
<link rel="stylesheet" href="packages/berrio-ui/tokens/spacing.css">
<link rel="stylesheet" href="packages/berrio-ui/tokens/radius.css">
<link rel="stylesheet" href="packages/berrio-ui/tokens/motion.css">
<link rel="stylesheet" href="packages/berrio-ui/tokens/breakpoints.css">
```

### Importar todo de una vez

```html
<link rel="stylesheet" href="packages/berrio-ui/tokens/tokens.css">
```

### Uso en CSS

```css
.my-component {
  background: var(--surface);
  color: var(--text);
  padding: var(--space-4);
  border-radius: var(--radius-card);
  font-family: var(--font-body);
  font-size: var(--text-base);
  transition: background var(--transition-fast);
}
```

## Tokens disponibles

### Colores (`colors.css`)

| Token | Valor | Descripción |
|-------|-------|-------------|
| `--bg` | `#0B0D12` | Fondo de página |
| `--surface` | `#13161D` | Fondo de tarjeta |
| `--surface-2` | `#1B1F29` | Fondo elevado |
| `--line` | `#262B36` | Bordes |
| `--text` | `#EDEAE2` | Texto primario |
| `--muted` | `#8A8F9C` | Texto secundario |
| `--amber` | `#E3A24C` | Acento primario |
| `--teal` | `#46D7C0` | Acento secundario |
| `--magenta` | `#E34C9E` | Acento terciario |
| `--embed-bg` | `#05070a` | Fondo de embed/terminal |
| `--terminal-text` | `#B9F5E8` | Texto de terminal |

### Colores semánticos (derivados)

| Token | Valor base | Descripción |
|-------|------------|-------------|
| `--error-bg` | `rgba(227,76,158,.1)` | Fondo de error (10% magenta) |
| `--overlay-top` | `rgba(11,13,18,.82)` | Overlay gradiente superior |
| `--overlay-bottom` | `rgba(11,13,18,.9)` | Overlay gradiente inferior |
| `--tint-white-3` | `rgba(255,255,255,.03)` | Tinte sutil why-note |
| `--tint-white-2` | `rgba(255,255,255,.02)` | Tinte sutil case-study |

### Tipografía (`typography.css`)

| Token | Valor | Descripción |
|-------|-------|-------------|
| `--font-display` | `'Fraunces', serif` | Fuente display |
| `--font-body` | `'Inter', system-ui, sans-serif` | Fuente cuerpo |
| `--font-mono` | `'JetBrains Mono', monospace` | Fuente monoespaciada |
| `--text-xs` | `11px` | Pills, badges |
| `--text-sm` | `12px` | Labels, footer, eyebrow |
| `--text-base-sm` | `13px` | Monospace UI, card links |
| `--text-base` | `14px` | Feature lists, tags |
| `--text-md` | `15px` | Body text |
| `--text-lg` | `17px` | Lead text |
| `--text-xl` | `21px` | Card titles |
| `--text-2xl` | `26px` | Lab names |
| `--text-3xl` | `clamp(34px, 6vw, 58px)` | H1 responsive |

### Espaciado (`spacing.css`)

| Token | Valor | Descripción |
|-------|-------|-------------|
| `--space-1` | `2px` | |
| `--space-2` | `4px` | |
| `--space-3` | `6px` | |
| `--space-4` | `8px` | Gap pills, filter bar |
| `--space-5` | `10px` | Card head gap, footer |
| `--space-6` | `12px` | |
| `--space-7` | `14px` | Cards gap, features gap |
| `--space-8` | `16px` | |
| `--space-9` | `18px` | |
| `--space-10` | `20px` | |
| `--space-11` | `22px` | Card head padding, card-body margin |
| `--space-12` | `24px` | Card body padding, login margin |
| `--space-14` | `28px` | Page gutters (horizontal) |
| `--space-16` | `32px` | |
| `--space-20` | `40px` | |
| `--space-24` | `48px` | |
| `--space-28` | `56px` | |
| `--space-32` | `64px` | |
| `--space-40` | `80px` | |

### Border-radius (`radius.css`)

| Token | Valor | Descripción |
|-------|-------|-------------|
| `--radius-xs` | `2px` | Waveform bars |
| `--radius-sm` | `4px` | Why-note |
| `--radius-md` | `8px` | Inputs, buttons |
| `--radius-lg` | `10px` | Embeds, terminal |
| `--radius-card` | `14px` | Cards principales |
| `--radius-pill` | `20px` | Pills, links, badges |
| `--radius-full` | `50%` | Círculos |

### Motion (`motion.css`)

| Token | Valor | Descripción |
|-------|-------|-------------|
| `--transition-fast` | `.2s ease` | Hovers simples |
| `--transition-base` | `.25s ease` | Borders, backgrounds |
| `--transition-medium` | `.3s ease` | Transform (chevron) |
| `--transition-slow` | `.4s ease` | Accordion expand |
| `--animation-pulse` | `2.6s ease-in-out infinite` | Waveform signature |

### Breakpoints (`breakpoints.css`)

| Token | Valor | Descripción |
|-------|-------|-------------|
| `--bp-mobile` | `560px` | Único breakpoint responsive |

## Reglas de FASE 1.0

1. No modificar ningún proyecto existente.
2. No crear componentes aún.
3. Solo tokens y documentación.
4. Verificación manual al finalizar.

## Próximas fases

- **FASE 1.1**: Componentes reutilizables (Button, Card, Navbar, Hero, Form)
- **FASE 1.2**: Componentes avanzados (Dashboard, Timeline, Modal, Tabs, Toast)
- **FASE 2.0**: Integración con Portfolio Hub
- **FASE 2.1+**: Integración con otros proyectos
