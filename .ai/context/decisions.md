# Architecture Decision Records (ADR)

## ADR-001: Monorepo para ecosistema Berrio

- **Fecha**: 2026-08-25
- **Estado**: Aprobada
- **Contexto**: Múltiples proyectos (Portfolio Hub, SalsaQuest, RockQuest, OSINT Search Pro, EduPack Builder, CodeAudit, Aventura Web, ProyectoGatico) comparten identidad visual y patrones de UI.
- **Decisión**: Adoptar estructura de monorepo con `packages/berrio-ui/` como paquete compartido de tokens y componentes.
- **Consecuencias**:
  - Tokens centralizados en un solo lugar.
  - Componentes reutilizables entre proyectos.
  - Posible overhead de build si los proyectos usan stacks diferentes.
  - Requiere estrategia de integración por proyecto (FASE 2.0+).

## ADR-002: Design Tokens como CSS Custom Properties

- **Fecha**: 2026-08-25
- **Estado**: Aprobada
- **Contexto**: El ecosistema usa CSS inline con `:root` variables. Los proyectos existentes (Portfolio Hub) ya definen 9 tokens base. No hay build pipeline ni preprocesadores CSS en producción.
- **Decisión**: Los design tokens se definen como **CSS Custom Properties** en archivos `.css` puros dentro de `packages/berrio-ui/tokens/`. No se usan herramientas de generación de tokens (Style Dictionary, Figma Tokens, etc.) en FASE 1.0.
- **Justificación**:
  - Compatibilidad directa con CSS inline existente.
  - Zero-dependency: no requiere build step.
  - Los proyectos pueden importar solo los tokens que necesiten.
  - Fácil migración futura a herramientas de generación si se requiere.
- **Consecuencias**:
  - No hay transformación automática a otros formatos (SCSS, JS, iOS, Android).
  - Mantenimiento manual de tokens (pero el set es pequeño: ~9 root + derivados).
  - Futuro: considerar Style Dictionary si se necesita multi-plataforma.

## ADR-003: Dark-mode only

- **Fecha**: 2026-08-25
- **Estado**: Aprobada
- **Contexto**: Todos los proyectos del ecosistema usan tema oscuro. No existe variante light en ningún proyecto.
- **Decisión**: El design system se diseña exclusivamente para dark mode. No se incluyen tokens light.
- **Consecuencias**:
  - Simplifica la paleta (9 tokens base, no 18+).
  - Si en el futuro se necesita light mode, habrá que crear una paleta completa nueva.
  - Los tokens de fondo (`--bg`, `--surface`, `--surface-2`) son específicos de dark mode.

## ADR-004: Tipografía de 3 fuentes

- **Fecha**: 2026-08-25
- **Estado**: Aprobada
- **Contexto**: Portfolio Hub usa Fraunces (display), Inter (body) y JetBrains Mono (mono). Son 3 roles tipográficos claros.
- **Decisión**: Mantener el sistema de 3 fuentes. Fraunces para títulos display, Inter para cuerpo, JetBrains Mono para elementos monoespaciados.
- **Consecuencias**:
  - 3 fuentes cargadas = más peso de carga (mitigado por Google Fonts woff2).
  - Fraunces aporta personalidad serif única al ecosistema.
  - JetBrains Mono refuerza la identidad "developer/engineering".
