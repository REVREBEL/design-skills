# Typography & Layout Systems (`03-typography-and-layout`)

## 1. Typographic Hierarchy
The typographic scale enforces scannability and brand distinction without heavy visual dividers:
- **Display Serif / Bespoke Header**: Used for property titles and story spread anchors.
- **Body Copy**: Capped at line measures `≤ 80ch` with `1.5x` line-height leading. Minimum contrast ratio `4.5:1` against background.
- **Operational Data Copy**: Nightly rates, date digits, and spec tables use tabular numerals (`font-variant-numeric: tabular-nums`) for clean column alignment.

## 2. Layout Grid Systems
- **12-Column Asymmetric Grid**: Desktop viewports employ offset 12-column grids, placing text blocks and spatial media in rhythmic, off-center compositions.
- **Responsive Stacking**: On mobile viewports (< 768px), asymmetric multi-column spreads collapse into clean single-column vertical flows without losing typographic scale contrast.


## Expanded reference material (historical research synthesis)

The following preserved material supplies detailed examples and rationale. Where it uses absolute ratios, technology defaults, or mandated flows, interpret these as proposals subject to the current SKILL.md evidence and context rules. Do not enforce outdated universal rules.

## Reference Module 3: Typography & Layout Systems (`typography-and-layout`)

### 1. Typography as Navigational Skeleton
Typography establishes the architectural skeleton of an editorial digital product. By leveraging dramatic scale contrast—pairing striking editorial display serif typography with clean, highly legible sans-serif body copy—layouts establish an intuitive visual hierarchy that directs the eye down the page effortlessly.

```
┌────────────────────────────────────────────────────────────────────────┐
│ TYPOGRAPHIC CADENCE & HIERARCHY                                        │
├────────────────────────────────────────────────────────────────────────┤
│ Display Header (Serif / High-Impact Editorial Scale)                   │
│ └─► Sub-header (Categorical Context / Location Anchor)                 │
│      └─► Body Copy (Measure capped at ≤ 80 chars; WCAG AA 4.5:1)       │
│           └─► Operational Data (Tabular Alignment for Rates & Dates)   │
└────────────────────────────────────────────────────────────────────────┘
```

### 2. Ergonomics & Operational Rules
*   **Measure Constraints**: Body copy line length must be strictly capped at `≤ 80 characters` per line, paired with open leading (`1.5–1.6em`), to maintain ergonomic reading cadence across all viewports.
*   **Tabular Numerals for Operational Data**: Commercial data—such as nightly pricing tiers, availability calendars, tax breakdowns, and room square footages—must utilize sans-serif typography with tabular numeric settings (`font-variant-numeric: tabular-nums`) to enable rapid, error-free scanning during reservation flows.
*   **Rejection of Low-Contrast Typography**: Critiqued in Kevin Marks' WIRED research ("How the Web Became Unreadable"), low-contrast light gray copy and ultra-thin font weights (`font-weight < 400`) represent aesthetic negligence. Luxury interfaces reject faint typography, strictly enforcing WCAG SC 1.4.3 minimum contrast ratios (`4.5:1` for standard body copy, `3:1` for large display headers and UI component boundaries).

---
