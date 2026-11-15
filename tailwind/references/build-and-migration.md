# Build and migration

## Find the compilation path

- Use the host's established v4 integration. Vite can use `@tailwindcss/vite`, PostCSS uses `@tailwindcss/postcss`, and the standalone CLI comes from `@tailwindcss/cli`. Load the main stylesheet containing `@import "tailwindcss";` in each independent consumer that needs it.
- Tailwind detects candidate text in source files. Keep complete class names in variant maps or static markup. For truly runtime values, use a static utility with a CSS variable and set the validated value through the existing style API.
- Check the compiler working directory and source inclusion. Use `source("…")` on the Tailwind import to set the automatic scan base, or `@source "…";` to include a specific source directory relative to the stylesheet, such as an otherwise excluded workspace or dependency. Choose whether a shared library ships compiled CSS or expects the consumer to scan its source.
- On v4 minors that support it, use a narrow `@source inline("…");` declaration for candidates unavailable as source text. Prefer explicit static candidates when practical. Confirm the selector in the built stylesheet, then inspect the loaded styles and computed value.

## Upgrade to v4

1. Confirm target browser support and review the official upgrade guide. If using the upgrade tool, run it in an isolated branch with its required Node version and inspect its changes.
2. Move to the appropriate v4 integration and CSS entry point. Port theme extensions and source paths to CSS-first directives. Retain a prior JavaScript config through explicit `@config` only while needed for migration. Audit plugins individually and use `@plugin` for compatible plugins that remain necessary. Confirm settings unsupported by the compatibility bridge are translated.
3. Compare rendered defaults in the upgraded build. Check border colors, ring width and color, shadows, radii, Preflight, important modifiers, and stacked variant order against the guide. Check scoped stylesheet access to the new theme and utilities.
4. Run the project build, inspect emitted CSS and source coverage, and verify normal app, package, and Storybook entry points where applicable.

Official references [Upgrade guide](https://tailwindcss.com/docs/upgrade-guide) and [Source detection](https://tailwindcss.com/docs/detecting-classes-in-source-files).
