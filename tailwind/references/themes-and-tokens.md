# Themes and tokens

- Define theme variables at the top level with `@theme` when the value should create or configure utilities or variants. Use namespaces such as `--color-*`, `--font-*`, `--text-*`, `--radius-*`, `--breakpoint-*`, and `--container-*`. Use ordinary CSS custom properties for values that need no generated utility.
- Separate palette values from semantic roles such as background, foreground, surface, border, and focus. Set runtime roles in `:root` and override them under the selected theme scope. Use `@theme inline` for aliases to runtime variables so the generated utility references the runtime variable where it is used.
- Extend the default theme by adding named variables. Reset a namespace only when the design system intentionally replaces it. Check the resulting utilities and existing consumers after a reset. Preserve consistent breakpoint units for predictable ordering.
- For shadcn/ui, match the local component token names, theme selectors, and color format. If a variable holds a full CSS color, reference it directly. If it holds legacy color channels, convert the token representation or wrap it in a compatible color function. Test opacity modifiers with real computed styles. Keep optional animation imports only when installed and used.
- Let semantic theme values handle role changes. Use `dark:` for differences that need distinct utilities. When the app controls theme via a class or data attribute, align the custom variant selector with the actual theme scope. Verify initial render, persisted theme, contrast, and focus indication.

Official references [Theme variables](https://tailwindcss.com/docs/theme) and [Dark mode](https://tailwindcss.com/docs/dark-mode).
