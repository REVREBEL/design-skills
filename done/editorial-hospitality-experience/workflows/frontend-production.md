# Frontend Production & Performance Engineering (`workflows/frontend-production`)
## Objective
Output clean, responsive code in the project's native framework (React, Vue, Next.js, static HTML) meeting Core Web Vitals.

## Execution Steps
1. **Framework Adaptation**: Inspect existing project setup and generate clean code compatible with the active codebase.
2. **Image & Font Optimization**: Serve responsive image `srcset` attributes and preconnect web fonts.
3. **Performance Audit**: Run `scripts/audit-performance.sh` to ensure `LCP < 2.5s`, `INP < 200ms`, and `CLS < 0.1`.


## Detailed execution procedure (preserved)

## Workflow 7: High-Performance Frontend Production (Next.js/React) (`frontend-production`)

### Objective
Output production-grade Next.js (App Router) and React code engineered for sub-second page rendering, strict Core Web Vitals compliance, and hardware-accelerated animations.

### Step-by-Step Execution

1. **Architecture & Rendering Strategy**
   - Leverage React Server Components (RSC) for static editorial content, property overviews, and CMS content blocks.
   - Isolate Client Components for interactive UI (search capsule, date pickers, room drawers, rate selectors).
   - Implement edge-rendered API routes for real-time PMS pricing and availability queries.

2. **Performance & Asset Optimization**
   - Utilize `next/image` with explicit `sizes`, priority flags on LCP hero assets, and WebP/AVIF formatting.
   - Implement `@media (prefers-reduced-data)` fallbacks to replace background hero videos with compressed static image crops.
   - Load custom brand fonts via `next/font` with `display: swap` to prevent Flash of Unstyled Text (FOUT).

3. **Hardware-Accelerated Motion Execution**
   - Restrict animations to hardware-accelerated properties (`transform`, `opacity`).
   - Limit animation durations to `< 300ms` using cubic-bezier easing (`cubic-bezier(0.16, 1, 0.3, 1)`).
   - Implement mandatory `@media (prefers-reduced-motion: reduce)` fallbacks disabling visual movement.

### Output Artifact
`frontend-architecture.md` containing React/Next.js code templates, server/client component boundaries, asset loading rules, and performance configuration.

---
