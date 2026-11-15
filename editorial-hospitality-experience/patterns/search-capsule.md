# UI Pattern: Floating Search Capsule & Overlay Drawer
Bottom-anchored mobile search pill (>= 44x44 pt) with dual-month calendar displaying starting rates per night.


## Expanded pattern specification

## 3. Floating Search Capsule & Progressive Overlay Drawer (`search-capsule`)

### Capsule Interface Specification
* **Mobile Layout**: Anchored pill fixed at the bottom viewport center (`bottom: 24px`, `height: 52px`, `z-index: 100`). Touch target measures `≥ 44×44 pt`.
* **Sub-Fields**: Three interactive segment buttons:
  1. *Location/Property*: Text string display (`e.g., Kyoto Estate`).
  2. *Dates*: Dual-date range string (`e.g., Oct 14 – Oct 18`).
  3. *Guests/Rooms*: Occupancy summary string (`e.g., 2 Guests, 1 Room`).

### Drawer Expansion Flow
* Clicking any segment opens the **Progressive Disclosure Search Overlay** (`min-height: 60vh`).
* **Segment Tabs**: Active field highlighted with clean underline or subtle background shift.
* **Interactive Calendar**: Dual-month desktop / single-month scrollable mobile calendar showing starting rates per night directly inside date cells using tabular numerals (`font-variant-numeric: tabular-nums`).

### Data & State Handling
* State changes update instantly across all views without page refresh.
* Unused input selections persist across navigation sessions using local state / URL query params.

---
