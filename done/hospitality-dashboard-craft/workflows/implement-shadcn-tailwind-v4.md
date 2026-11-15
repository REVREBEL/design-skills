# Workflow: implement with shadcn/ui + Tailwind v4
1. Inspect framework, `package.json`, `components.json`, existing UI source and `globals.css`. Verify installed APIs using project docs.
2. Preserve current brand tokens/components; create only missing primitives or composition variants. Do not transplant entire app shell without authorization.
3. Implement semantic tokens, dark/light modes and status/chart separation; compile CSS and validate contrast.
4. Separate metric domain calculation, formatting, server authorization and presentation; null-aware currency/percent/date formatters.
5. Build component contract with props, state transitions, aria behavior, keyboard interactions, empty/error/stale and responsive variants.
6. Add accessible table/chart alternatives, stable row IDs, and virtualization only when justified. For writable grids, add revision/concurrency guard and authoritative success state.
7. Exercise typecheck, unit, integration, visual, keyboard and mobile checks where environment permits; report any unavailable tests as not run.
8. Document changed files, setup, dependencies, limitations, design decisions and rollback points.
