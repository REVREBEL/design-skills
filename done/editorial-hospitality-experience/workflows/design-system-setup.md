# Design System & Token Setup (`workflows/design-system-setup`)
## Objective
Establish design tokens for typography scale contrast, spatial grid padding, color contrast, and motion curves.

## Execution Steps
1. **Tokenization**: Define global tokens for font scales, contrast colors (`WCAG AA ≥ 4.5:1`), and spatial grid padding.
2. **Illustrative Theme Notice**: Explicitly state that token values (e.g. dark surfaces or serif display fonts) are illustrative defaults and must adapt to property brand guidelines.
3. **Verification**: Run `scripts/validate-design-tokens.py` to verify token syntax and contrast compliance.


## Detailed execution procedure (preserved)

## Workflow 4: Creative Direction & Design System Setup (`design-system-setup`)

### Objective
Establish typographic scale contrast, layout grid rhythm, 30/70 spatial media rules, and tokenized design variables that unify high-end editorial aesthetics with high-performance usability.

### Step-by-Step Execution

1. **Define Typographic Hierarchy & Pairing**
   - Select display typeface (e.g., elegant serif or refined geometric sans) for editorial headers.
   - Select highly legible body and operational typeface with `tabular-nums` support for pricing tables, availability calendars, and specs.
   - Establish modular scale ratio (e.g., 1.25 Major Third or 1.333 Perfect Fourth) ensuring dramatic scale contrast between display headers (`40px–64px`) and body text (`16px–18px`).
   - Enforce line measure caps (`≤ 80ch`) and minimum line-heights (`1.5` for body text).

2. **Tokenize Semantic Color & Spacing Systems**
   - Define background and surface neutrals providing generous semantic negative space.
   - Verify all text-to-background contrast ratios meet WCAG 2.2 AA (`≥ 4.5:1` for normal text, `≥ 3:1` for display copy and UI borders).
   - Establish spacing scale tokens (`4px`, `8px`, `16px`, `24px`, `32px`, `48px`, `64px`, `96px`, `128px`) for vertical spatial rhythm.

3. **Codify 30/70 Spatial Photography & Media Rules**
   - Enforce 30% allocation for evocative detail crops (joinery, material textures, ambient light shadows).
   - Enforce 70% allocation for spatial comprehension visuals (wide architectural room views, window view vectors, interactive vector floor plan SVG overlays).

### Output Artifact
`design-tokens.json` and `creative-direction-spec.md` containing global design variables, font definitions, contrast scores, and photography asset guidelines.

---
