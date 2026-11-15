# Utilities and layout

- Use unprefixed utilities for the baseline and viewport variants for page-level changes. Use a parent `@container` and a descendant query variant such as `@md:grid-cols-2` when component layout depends on its container width. Name containers when descendants must target a specific ancestor. Check a narrow container on a wide viewport.
- Use theme-backed utilities for repeated design values and arbitrary values for isolated exceptions. For state-dependent behavior use supported variants such as `focus-visible:`, `disabled:`, `motion-reduce:`, and data or ARIA variants as appropriate. Check interactions with a keyboard and a pointer.
- Register reusable, variant-aware rules with `@utility`. Use functional utilities when the supported inputs map cleanly to CSS values and validate the installed minor's `--value()` syntax. Use `@custom-variant` for reusable selector conditions and `@variant` to apply a variant inside CSS.
- Use plain CSS or an appropriate layer for component-specific rules and generated or rich-text markup. Consider specificity, layer order, variants, and stylesheet order before adding overrides. The order of utilities in an HTML class attribute does not determine their CSS precedence.
- Use `@apply` when a CSS integration requires composed declarations. In separately compiled CSS modules or component style blocks, add `@reference` to the app stylesheet when the block needs its custom definitions without emitting them again.
- For modern utility families such as 3D transforms, subgrid, or newer variants, check the installed minor and browser requirements. Inspect computed styles when a candidate is valid but the browser or container cannot activate it.

Official references [Responsive design](https://tailwindcss.com/docs/responsive-design) and [Functions and directives](https://tailwindcss.com/docs/functions-and-directives).
