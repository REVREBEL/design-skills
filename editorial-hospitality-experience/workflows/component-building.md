# Accessible Component Library Construction (`workflows/component-building`)
## Objective
Build modular, tokenized UI components with accessible keyboard focus states (`:focus-visible`) and non-blocking form mechanics.

## Execution Steps
1. **Accessibility Rules**: Implement explicit outline rings (`:focus-visible`), touch targets (`≥ 44×44 pt`), and proper ARIA tags.
2. **Nuanced Button Mechanics**: Use `aria-disabled="true"` when keeping non-ready submission buttons keyboard-focusable to surface error tooltips (`aria-describedby`) to screen reader users. Use native disabled states when appropriate for simple form boundaries.
3. **Verification**: Execute `scripts/audit-accessibility.sh` to verify WCAG compliance.


## Detailed execution procedure (preserved)

## Workflow 6: Accessible Component Library Construction (`component-building`)

### Objective
Build modular, tokenized frontend UI components that strictly adhere to WCAG 2.2 Level AA accessibility standards, thumb-zone ergonomics, and state management rules.

### Step-by-Step Execution

1. **Build Persistent Booking Capsule & Overlay Drawer**
   - Single-line bar containing destination, date range display, guest counter, and search action button.
   - Keyboard accessible: Trap focus within drawer when open, allow `Escape` key close.

2. **Construct Spatial Room Card & Overview Panel**
   - Room card component with responsive image gallery (minimum 3 thumbnail crops), key spatial specs, and "Explore Space" drawer trigger.
   - Overview panel component incorporating vector floor plan SVG with hoverable hot-spots linked to room areas.

3. **Build Stacked Plain-Language Rate Cards**
   - Custom accessible radio group component.
   - Price display using `font-variant-numeric: tabular-nums` for vertical alignment.
   - Clear inclusion tags (e.g., "Breakfast Included", "Fully Refundable").

4. **Enforce Non-Blocking Accessibility Mechanics**
   - Use `aria-disabled="true"` instead of native `<button disabled>` to keep controls keyboard-focusable.
   - Provide explicit `:focus-visible` focus rings with minimum `3:1` contrast against surface colors.

### Output Artifact
`component-library-spec.md` detailing component APIs, props, ARIA state specifications, and keyboard interaction patterns.

---
