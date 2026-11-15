# Spatial Media & Photography Balance (`04-spatial-media-and-photography`)

## 1. Spatial Photography Guidelines
To balance emotional desire with physical spatial clarity, media selection follows an art-directed allocation model:
- **Editorial Detail Crops (~30% starting benchmark)**: Close-ups of natural materials, joinery, linens, and light vectors that communicate craftsmanship.
- **Spatial Comprehension Visuals (~70% starting benchmark)**: Wide architectural perspectives showing full room layouts, window sightlines, and terrace orientations.
- **Vector Floor Plan Overlays**: Interactive or scannable SVG floor plans showing square meters/footage, bed placement, and bathroom layouts.

*Note: The 30/70 ratio serves as a practical starting benchmark, not an inflexible dogma. Adjust allocation dynamically based on property inventory complexity and available visual assets.*


## Expanded reference material (historical research synthesis)

The following preserved material supplies detailed examples and rationale. Where it uses absolute ratios, technology defaults, or mandated flows, interpret these as proposals subject to the current SKILL.md evidence and context rules. Do not enforce outdated universal rules.

## Reference Module 4: Spatial Media Balance (`spatial-media-balance`)

### 1. The 30/70 Spatial Photography Allocation
Imagery in luxury hospitality serves a dual functional role that requires a strict 30/70 system allocation across property portfolios:
1.  **Editorial Detail Crops (30% System Allocation)**: Tightly cropped, evocative detail shots showcase physical luxury—focusing on raw architectural materials, textile textures, joinery, shadow interplay, and ambient lighting. These narrative hooks establish emotional resonance and brand maturity without resorting to bandwidth-heavy background video loops or disruptive animations.
2.  **Spatial Comprehension Visuals (70% System Allocation)**: To convert emotional desire into direct booking commitment, editorial crops are systematically paired with un-cropped wide-angle photography, precise architectural floor plans, window light orientation highlights, and explicit scale indicators. Guests committing to high-tier suite reservations require complete spatial clarity.

### 2. Asset Validation & Layout Tokens
*   **CMS Asset Validation**: Content management schemas mandate that every room category asset bundle contain a minimum of seven media assets, programmatically tagged as 30% detail crops (`detail_crop`) and 70% spatial overview images (`spatial_overview`).
*   **CSS Grid Tokens**: Templates utilize CSS Grid aspect-ratio tokens (`--aspect-editorial: 4/5`, `--aspect-spatial: 16/9`). Editorial crops are constrained to secondary support columns, while spatial comprehension assets occupy primary display slots.
*   **Accessible Overlay Seats**: Overlaid text must sit on solid background containers or achieve WCAG `4.5:1` contrast using localized linear gradient masks (`linear-gradient(rgba(0,0,0,0), rgba(0,0,0,0.6))`).

---
