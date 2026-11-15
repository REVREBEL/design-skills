# Mobile Ergonomics & Touch Rules (`10-responsive-mobile-ergonomics`)

## 1. Natural Thumb-Zone Layouts
- **Persistent Search Pill**: Anchor persistent booking triggers near the bottom of mobile viewports within natural thumb reach.
- **Touch Targets**: Enforce minimum touch target sizing (`≥ 44×44 pt` / `48×48 dp`) via interior padding.
- **Single-Column Accordions**: Transform desktop side-by-side matrices into clean, single-column collapsible text accordions on mobile viewports (< 768px).
- **Map Pin Exception (WCAG SC 2.5.8)**: Interactive map pins anchored to real geographic coordinates observe the Essential Exception rule; always pair interactive maps with a synchronized list view toggle.


## Expanded reference material (historical research synthesis)

The following preserved material supplies detailed examples and rationale. Where it uses absolute ratios, technology defaults, or mandated flows, interpret these as proposals subject to the current SKILL.md evidence and context rules. Do not enforce outdated universal rules.

## Reference Module 10: Mobile Ergonomics & Thumb-Zone Layouts (`mobile-ergonomics`)

### 1. Architectural Adaptation Over Scaling
Desktop luxury layouts cannot simply be downscaled for mobile viewports; compressing multi-column grids reduces text legibility, shrinks touch targets below usable limits, and creates unorganized vertical scrolling. Mobile adaptation requires an explicit architectural redesign around native mobile ergonomics.

```
┌────────────────────────────────────────┐
│ MOBILE VIEWPORT DESIGN                 │
│ ┌────────────────────────────────────┐ │
│ │ Immersive Editorial Media / Specs  │ │
│ │ (Adaptive Single-Column Layout)    │ │
│ │                                    │ │
│ ├────────────────────────────────────┤ │
│ │ PERSISTENT BOTTOM SEARCH CAPSULE   │ │
│ │ [ Paris │ 12-16 Oct │ 2 Guests ]   │ │ ◄ Natural Thumb-Zone Reach
│ └────────────────────────────────────┘ │
└────────────────────────────────────────┘
```

### 2. Touch Target Standards & The WCAG Essential Exception
*   **Touch Target Sizing**: Interactive controls strictly observe WCAG 2.2 SC 2.5.8, enforcing a minimum target size of `24×24 CSS pixels`, while actively targeting native platform guidelines (`44×44 pt` on iOS, `48×48 dp` on Android). Target dimensions are padded using interior CSS padding rather than exterior margins to prevent accidental mis-taps on adjacent links.
*   **The WCAG Essential Exception**: Under WCAG SC 2.5.8, interactive spatial map pins (e.g., destination maps where pin accuracy is tied to exact geographic coordinates) are granted an explicit "Essential" exception. When pins cluster closely, enforcing 24px visual padding is geographically impossible. In these scenarios, the interface must provide an equivalent, highly accessible list or drawer view toggle immediately adjacent to the map container.

---
