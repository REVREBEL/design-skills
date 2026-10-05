---
name: form-layout-design
description: Design and implement clear, responsive form layouts with strong visual hierarchy, field grouping, spacing, and Tailwind CSS. Use when asked to "design this form", "improve the form layout", "group these fields", "make this form responsive", "clean up these inputs", "implement this form in Tailwind", or fix dense/confusing data-entry UI. For task flow and step sequencing use journey; for token-system architecture use design-system-patterns.
---

# Form Layout Design

Design the visible structure of forms so users can scan, understand, and complete them without fighting the interface.

## Scope

**IS:** visual hierarchy, field grouping, section structure, responsive columns, spacing, control sizing, label/helper/error placement, action layout, Tailwind implementation, and visual QA of form states.

**IS NOT:** deciding what data the product should collect, business validation rules, server behavior, checkout logic, or multi-step task sequencing. Route those decisions to `journey` or the owning product/domain skill.

When the request includes both structure and implementation, solve the visual structure first, then express it in Tailwind.

## Design Workflow

### 1. Read the existing system before styling

Inspect the current code and preserve established:
- typography
- color and semantic tokens
- border radii
- control heights
- spacing scale
- button variants
- breakpoints
- Tailwind version and configuration
- existing form/input components

Do not introduce a parallel mini-design-system inside one form.

If the project already has reusable `Input`, `Select`, `Field`, `FormSection`, or button components, compose them before creating new primitives.

### 2. Establish the form hierarchy

Organize content from largest relationship to smallest:

1. **Form**
2. **Section**
3. **Field group / row**
4. **Field**
5. **Label + control + helper/error**

A user should be able to understand the grouping before reading every label.

Use the weakest grouping signal that works:
- proximity first
- whitespace and headings second
- dividers or background regions when boundaries need reinforcement
- cards only when a section is genuinely an independent surface or action unit

Avoid wrapping every field group in a bordered box.

### 3. Group by meaning, not by available space

Fields that belong to one mental task should stay together.

Examples:
- First name + Last name
- City + State + Postal code
- Card number + Expiration + Security code
- Arrival time + transportation notes

Do not pair unrelated fields merely because two columns are available.

Keep:
- label closer to its control than to the next field
- helper/error text visually attached to the control it describes
- related actions adjacent
- destructive or secondary actions spatially distinct

### 4. Choose the simplest layout that preserves comprehension

Default to one column.

Use multiple columns only when:
- fields are short and strongly related
- reading order remains obvious
- the relationship survives responsive stacking

Prefer:
- 2-column rows for short paired fields
- full-width rows for addresses, notes, long selects, consent, and complex controls
- content-width constraints so forms do not stretch across wide screens

Do not compress a form just to reduce vertical scrolling. A shorter form that is harder to parse is not an improvement.

### 5. Design responsive behavior intentionally

Mobile is not a scaled-down desktop form.

At narrow widths:
- collapse paired columns when controls become cramped
- preserve DOM/tab order
- keep controls and primary actions at least 44px tall where practical
- allow long labels and error messages to wrap naturally
- avoid horizontal scrolling
- keep touch targets separated

Let content determine breakpoints. Use the project's existing Tailwind breakpoints unless the component genuinely needs a container-query solution.

### 6. Implement with Tailwind as a system

Prefer layout primitives that communicate intent:
- `grid` for aligned field rows and predictable column spanning
- `flex` for small inline groups and action rows
- `gap-*` for relationships between siblings
- `space-y-*` for simple vertical stacks where appropriate
- `max-w-*` for readable form width
- `min-w-0` on grid/flex children that may contain long content
- responsive prefixes for reflow
- semantic design tokens/classes over arbitrary raw colors

Use native Tailwind utilities unless the host project already defines higher-level stack/layout utilities.

Avoid:
- one-off pixel margins between sibling fields
- negative margins to repair field alignment
- arbitrary hex colors when project tokens exist
- inline styles for responsive layout
- deeply repeated class strings when a project component/variant should own them
- breakpoint soup that creates a different layout at every screen width

For concrete patterns, read `references/tailwind-form-layouts.md`.

### 7. Design all visible states

A form layout is incomplete if only the pristine state looks good.

Verify:
- default
- hover where appropriate
- focus-visible
- filled
- disabled
- read-only
- validation error
- helper text
- loading/submitting
- success/confirmation when shown inline

Error text belongs immediately below the affected control or field group. Do not rely on color alone.

Never use placeholder text as the only label.

### 8. Place actions according to task hierarchy

The primary action should be visually obvious without overpowering the form.

For most forms:
- primary submit last in reading order
- secondary/back action nearby but visually quieter
- destructive action separated from routine progression

On mobile, actions may stack when horizontal layout becomes cramped.

Do not make every action the same weight.

## Tailwind Layout Heuristics

Use these as defaults, then adapt to the existing design system:

| Relationship | Typical treatment |
|---|---|
| Label → control | tight |
| Control → helper/error | tight |
| Field → field | moderate |
| Related row → related row | moderate |
| Section heading → first field | moderate |
| Section → section | generous |
| Form content → primary action | generous |

The important signal is the **ratio** between internal and external spacing, not a universal pixel value.

## Visual QA

Before considering the form complete, check:

- Can the groups be understood when squinting at the page?
- Is the label-control relationship stronger than the relationship between adjacent fields?
- Are unrelated fields accidentally sharing a row?
- Are sections distinguishable without excessive borders/cards?
- Does the form maintain a sensible max width on large screens?
- Does it become a coherent single-column experience on small screens?
- Are field widths proportional to expected input?
- Do helper and error messages stay attached to their controls?
- Are focus and error states visible against the actual background?
- Is the primary action easy to find?
- Are Tailwind classes using the project's tokens and conventions?
- Are there arbitrary values that should become an existing token or reusable variant?

## Handoffs

- **`journey`**: field/step sequencing, multi-step flows, progress, back behavior, task completion.
- **`law-of-proximity`**: deeper analysis of spatial grouping.
- **`law-of-common-region`**: deciding when a visible container/boundary is justified.
- **`layout-grid`**: page-level grid architecture beyond the form.
- **`spacing-system`**: defining or changing the product-wide spacing scale.
- **`responsive-design`**: broader cross-device interaction concerns.
- **`design-system-patterns`**: token architecture, theming, component-system foundations.
- **`component-architecture`**: extracting repeated form UI into reusable component APIs.
