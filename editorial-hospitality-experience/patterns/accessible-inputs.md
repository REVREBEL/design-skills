# UI Pattern: Accessible Inputs & Skeleton Loaders
Form controls with aria-disabled focus mechanics and pulse animations ensuring zero layout shift (CLS = 0).


## Expanded pattern specification

## 10. Accessible Inputs & Skeleton Loaders (`accessible-inputs`)

### Accessible Form Controls
* **Form Controls**: Every input paired with an explicit `<label for="input-id">`.
* **Non-Blocking State**: Disabled or invalid states use `aria-disabled="true"` or `aria-invalid="true"` rather than native disabled attributes to preserve DOM focus order and screen reader availability.
* **Focus States**: High-contrast outline ring on all interactive elements (`:focus-visible`).

### Skeleton Loaders & Micro-Interactions
* Uses smooth, low-contrast pulse animations (`opacity 0.6` to `1.0` over `1.5s`) matching final layout shapes during async data fetching.
* Ensures zero layout shift (`CLS = 0`) when real data loads into the component container.

---
