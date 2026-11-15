---
name: tailwind-master
description: Implement, review, and debug Tailwind CSS v4. Use for CSS-first configuration, Vite or PostCSS setup, source detection, shared design tokens and shadcn/ui themes, dark mode, responsive and container-query layouts, custom utilities and variants, scoped CSS, and upgrades to Tailwind CSS v4.
---

# Tailwind Master

1. Identify the installed v4 minor, styling entry point, build integration, and affected app or package. Trace which stylesheet actually reaches the page, Storybook preview, or library consumer. Check the pinned version before using a directive, utility, or variant introduced in a later v4 minor.
2. Classify the problem. Missing generated selectors indicate a candidate detection or compiler configuration issue. Generated CSS with no visual effect calls for inspecting stylesheet delivery, active variant conditions, the cascade, and resolved theme variables.
3. Use the existing semantic tokens and v4 utilities. Keep candidates statically discoverable. Add a theme token for a shared design role, a custom utility for reusable variant-aware behavior, or plain CSS for a local rule. For reusable layouts, choose between a viewport and container query based on what controls the available space.
4. Verify the production CSS output and the rendered component through the normal entry point. Check representative widths, themes, keyboard focus, and any package or Storybook consumers affected. State which checks ran.

| Task | Reference |
| --- | --- |
| Installation, missing classes, monorepos, and upgrade to v4 | [Build and migration](references/build-and-migration.md) |
| CSS-first tokens, semantic aliases, shadcn/ui, and dark mode | [Themes and tokens](references/themes-and-tokens.md) |
| Responsive layouts, utilities and variants, cascade, and scoped CSS | [Utilities and layout](references/utilities-and-layout.md) |
| Copyable v4 stylesheet illustrating semantic tokens and class-driven dark mode | [Theme example](assets/theme.css) |
