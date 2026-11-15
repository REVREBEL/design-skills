# Design Token Governance (`11-design-systems-and-tokens`)

## 1. Token Architecture
Maintain system-wide design tokens for typography scales, spacing grids, contrast ratios, and motion curves:
- **Immutable System Tokens**: Enforce WCAG 2.2 AA contrast ratios (`≥ 4.5:1`), touch target sizes, and layout grid margins.
- **Flexible Brand Accents**: Allow property-specific font pairings, accent colors, and imagery.

*Illustrative Note: The default values in `design-token-schema.json` (such as dark surface tokens or serif headers) represent illustrative default examples, not mandatory requirements for every hospitality brand.*


## Expanded reference material (historical research synthesis)

The following preserved material supplies detailed examples and rationale. Where it uses absolute ratios, technology defaults, or mandated flows, interpret these as proposals subject to the current SKILL.md evidence and context rules. Do not enforce outdated universal rules.

## Reference Module 11: Design System Governance & Token Schemas (`system-governance`)

### 1. Two-Tier Governance Model
To preserve brand coherence while allowing property-level creative expression across multi-property holdings, the design system enforces a strict two-tier governance model:
*   **Tier 1 (Immutable System Tokens)**: Global design tokens—including baseline typography scales, WCAG contrast rules, touch-target padding (`≥ 24×24 CSS px`), and transactional form layouts—are hardcoded into core system libraries. Property teams cannot alter these tokens.
*   **Tier 2 (Flexible Editorial Canvas)**: Local property teams are provided structured layout canvases and component slots (custom visual spreads, local cultural stories, curated amenity blocks), allowing local teams to art-direct unique property stories while ensuring every component renders within global brand standards.

---
