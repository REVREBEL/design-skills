# UI Pattern: Story Cards & Slide-Over Spatial Overview Panel
Level 1 story cards linking to Level 2 slide-over drawers with SVG floor plan vector overlays.


## Expanded pattern specification

## 4. Story Cards & Slide-Over Spatial Overview Panel (`spatial-overview-panel`)

### Level 1: Story Card Specification
* **Media Container**: 3:2 ratio aspect box displaying a hero spatial photograph. Hover triggers smooth scale transition (`scale(1.03)` over `400ms cubic-bezier(0.25, 1, 0.5, 1)`).
* **Card Metadata**: Category title (e.g., *Garden Villa with Private Onsen*), exact floor area (`120 sq m / 1,290 sq ft`), bed configuration (*King Bed*), view orientation (*West Facing / Forest View*), and transparent total starting rate.
* **Primary Action**: "Explore Space" button triggering the Level 2 Panel.

### Level 2: Slide-Over Spatial Overview Panel
* **Drawer Mechanics**: 600px wide panel sliding from right viewport edge (`transform: translateX(0)` over `300ms`).
* **Content Hierarchy**:
  1. *Wide-Angle Hero Photography*: Wide architectural view of room interior.
  2. *Interactive Vector Floor Plan*: SVG vector floor plan overlay with clickable hotspot pins revealing localized photos (bathroom, terrace, bed orientation).
  3. *Spatial Details List*: Ceiling height, natural light orientation, bathroom specs, material finishes.
  4. *Direct Rate Action*: Inline button to select room and proceed to rate plan selection.

---
