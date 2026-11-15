# Restrained Motion & Animation Tokens (`09-motion-and-restrained-animation`)

## 1. Performance-Conscious Animation Rules
- **Hardware Acceleration**: Use CSS properties optimized for GPU rendering (`transform`, `opacity`).
- **Timing Budgets**: Keep micro-interactions fast (`duration < 250ms`).
- **Reduced Motion Overrides**: Honor user OS preferences via `@media (prefers-reduced-motion: reduce)`, swapping smooth slide-overs with instant static display states.


## Expanded reference material (historical research synthesis)

The following preserved material supplies detailed examples and rationale. Where it uses absolute ratios, technology defaults, or mandated flows, interpret these as proposals subject to the current SKILL.md evidence and context rules. Do not enforce outdated universal rules.

## Reference Module 9: Restrained Motion & Animation Specs (`restrained-animation`)

### 1. Purposeful Animation Token Specs
Interface motion in luxury digital products is deployed exclusively to explain spatial state transitions (drawer reveals, date-picker expansions, floor-plan overlays) and reinforce navigation continuity.

```css
/* Restrained Motion Tokens */
:root {
  --ease-editorial: cubic-bezier(0.16, 1, 0.3, 1);
  --duration-fast: 150ms;
  --duration-medium: 240ms;
  --duration-drawer: 300ms;
}

.drawer-slide {
  transition: transform var(--duration-drawer) var(--ease-editorial),
              opacity var(--duration-drawer) ease-out;
  will-change: transform, opacity;
}
```

### 2. Motion Overrides & Reduced-Motion Contracts
*   **Execution Hardware**: All animations must rely exclusively on hardware-accelerated CSS properties (`transform`, `opacity`) to guarantee `60fps` execution and zero main-thread blocking.
*   **Mandatory Motion Overrides**: Systems must honor system accessibility flags via `@media (prefers-reduced-motion: reduce)`, instantly suppressing non-essential transitions and delivering static state changes.

---
