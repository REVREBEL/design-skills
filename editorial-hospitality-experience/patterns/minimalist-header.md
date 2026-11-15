# UI Pattern: Minimalist Sticky Header & Persistent Booking Capsule
Fixed 80px header collapsing to 64px on scroll with single-line floating action pill.


## Expanded pattern specification

## 1. Minimalist Sticky Header & Persistent Booking Capsule (`minimalist-header`)

### Structural Blueprint
* **Desktop Layout**: A fixed, semi-transparent header (`backdrop-filter: blur(12px)`) with a height of `80px`. Contains property mark/logo (left), navigation links (center), and a compact persistent booking trigger pill (right).
* **Scroll Mechanics**: Collapses from `80px` to `64px` on scroll (`window.scrollY > 100px`). The logo scales down smoothly (`scale(0.85)`), and secondary nav items fade out, keeping only the booking trigger capsule and essential brand mark visible.
* **Persistent Booking Capsule**: A single-line floating action pill (`height: 44px`) displaying default or selected query state: `[ Destination / Property | Dates | Guests ]` followed by a discreet CTA button (`Check Availability` or `Reserve`).

### Interaction & Progressive Disclosure
* Clicking anywhere on the booking capsule triggers a smooth, non-blocking slide-down drawer or centered modal overlay without reloading the page.
* Keyboard focus traps inside the expanded drawer until closed (`Escape` key closes drawer and returns focus to capsule trigger).

### ARIA & Accessibility Contracts
* Nav container wrapped in `<header>` with `<nav aria-label="Main Navigation">`.
* Booking capsule trigger rendered as `<button aria-expanded="false" aria-controls="global-booking-drawer">`.
* Focus indicator uses explicit high-contrast offset ring (`outline: 2px solid var(--color-focus); outline-offset: 4px;`).

---
