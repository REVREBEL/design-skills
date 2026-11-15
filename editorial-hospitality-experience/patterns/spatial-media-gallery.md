# UI Pattern: Spatial Media Gallery & Floor Plan Viewer
Spatial photography balance with interactive vector floor plan nodes and thumbnail previews.


## Expanded pattern specification

## 7. Spatial Media Gallery & SVG Floor Plan Viewer (`spatial-media-gallery`)

### Media Balance Rule
* Enforces the **30/70 Spatial Photography Allocation**:
  * 30% of gallery allocation dedicated to detail crops (material joinery, stone textures, ambient light reflection).
  * 70% dedicated to spatial comprehension shots (wide architectural room views, view vectors, window orientations).

### Interactive Vector Floor Plan Overlay
* Inline SVG floor plan diagram rendering room geometry accurately to scale.
* Hotspot nodes overlaid on vector room areas (Bedroom, Bathroom, Private Balcony). Clicking a node updates the adjacent photo viewer to show that specific space.
* Keyboard nav support: Hotspots are focusable via `Tab` key and activated with `Enter` / `Space`.

---
