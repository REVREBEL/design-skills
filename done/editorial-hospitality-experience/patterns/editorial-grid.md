# UI Pattern: Asymmetric Editorial Grid & Spreads
12-column fluid grid pairing 16:9 imagery with offset typography blocks (measure <= 80ch).


## Expanded pattern specification

## 2. Asymmetric Editorial Grid & Spreads (`editorial-grid`)

### Visual & Spatial Architecture
* **Column Grid**: 12-column fluid grid on desktop (`1440px` max-width, `48px` margins, `24px` gutters), 6-column on tablet, 4-column on mobile.
* **Spatial Cadence**: Alternating asymmetric spreads pairing full-bleed 16:9 spatial imagery with offset text blocks (e.g., 7-column image container paired with 4-column typography block with 1-column offset gap).
* **Typographic Interleaving**: Drop-cap intro paragraphs set in display serif fonts, paired with strict line-length constraints (`measure <= 80ch`).

### Responsive Adaptation
* On viewports `< 768px`, 12-column asymmetric spreads collapse into a single-column vertical stack.
* Images maintain aspect ratio (`3:2` or `4:3` on mobile) to prevent Cumulative Layout Shift (`CLS < 0.1`).

---
