# Quality Gates & Accessibility (`14-technical-quality-gates-and-accessibility`)

## 1. Core Web Vitals Budgets
- **LCP**: `< 2.5s` at 75th percentile.
- **INP**: `< 200ms`.
- **CLS**: `< 0.1`.

## 2. Nuanced Accessibility & Form Mechanics
- **WCAG 2.2 AA Contrast**: `≥ 4.5:1` body text, `≥ 3:1` display text & UI borders.
- **Focus Rings**: Mandatory `:focus-visible` outline rings with `3px` offset.
- **Disabled Buttons Guidance**:
  - Use `aria-disabled="true"` on submission buttons when keeping the button keyboard-focusable to surface contextual validation tooltips (`aria-describedby`) to screen readers.
  - Native `<button disabled>` is permissible for static non-interactive or native browser form constraints where tooltips are not used.


## Expanded reference material (historical research synthesis)

The following preserved material supplies detailed examples and rationale. Where it uses absolute ratios, technology defaults, or mandated flows, interpret these as proposals subject to the current SKILL.md evidence and context rules. Do not enforce outdated universal rules.

## Reference Module 14: Technical Quality Gates & Accessibility (`technical-quality-gates`)

### 1. Core Web Vitals Benchmarks
Performance criteria are evaluated strictly at the 75th percentile of production user loads:
*   **Largest Contentful Paint (LCP)**: `< 2.5 seconds` (ensuring hero media and room imagery render almost instantly).
*   **Interaction to Next Paint (INP)**: `< 200 milliseconds` (guaranteeing zero-friction interaction responses).
*   **Cumulative Layout Shift (CLS)**: `< 0.1` (eliminating layout jumping as dynamic rates hydrate).

### 2. Universal Accessibility (WCAG 2.2 Level AA)
*   **Contrast Thresholds**: Body copy strictly complies with WCAG AA standards (`≥ 4.5:1` contrast ratio); large display headers (`≥ 18pt` or `≥ 14pt` bold) and UI component boundaries (form inputs, button borders) require `≥ 3:1`.
*   **Button State Mechanics (`aria-disabled="true"`)**: Native `<button disabled>` HTML attributes remove elements from the browser tab order and trap screen reader users. Interfaces utilize `aria-disabled="true"` to keep buttons focusable while communicating disabled state clearly, paired with explicit `:focus-visible` focus rings.
*   **Data Preference Overrides**: Systems respect user network conditions via `@media (prefers-reduced-data: reduce)`. When active, auto-playing background videos are automatically suppressed and substituted with static compressed image crops.

---
