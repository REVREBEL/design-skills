# React with Vite

## Establish the entry points

- Check the pinned Vite, React plugin, Node, package manager, TypeScript and test runner. Follow the installed Vite major's docs. For a new app, start from a compatible React and TypeScript template and add optional integrations only when needed.
- Trace `index.html`, the React entry module, router and provider mounting, imported CSS, and the deployment output. Colocate feature code and tests. Introduce feature boundaries as the application grows and use workspace package exports for cross-package contracts.
- Use the repository's existing React plugin and inspect plugin effects separately for dev, build, and tests. Align import aliases across Vite, TypeScript, the test runner, and Storybook when applicable. Confirm how each workspace resolves React before applying deduplication. Prefer compatible peer dependencies for shared UI packages.

## Diagnose dev and production separately

| Symptom | Inspect |
| --- | --- |
| Alias typechecks but browser import fails | Vite resolution, alias target and file case, workspace exports, and test or preview config |
| Fast Refresh remounts a component | Refresh boundary, mixed exports, module graph, and React plugin version |
| Development API requests work but deployment fails | Dev proxy versus the production host's API routing, base URL, credentials, and browser network response |
| Built assets 404 under a subpath | Vite base, router base, host mount path, and emitted asset URLs |
| Direct navigation to an SPA route returns 404 | Host fallback to the app entry HTML, preserving asset and API routing |
| Variables differ in preview or deployment | Build mode and injected build-time values, then inspect the deployed artifact |
| Shared UI renders unstyled | CSS entry imports, consumer CSS pipeline, library CSS exports, and utility source scanning if applicable |

Treat client env as public. Vite's default client prefix is `VITE_`. Values exposed to the client are bundled for that build. Check mode and environment precedence, parse strings as needed, and keep credentials on the server. Use imported asset URLs when the build should process the asset and follow the host's base-path behavior for public files.

## Test and optimize

- Run the project's explicit typecheck, lint, and tests alongside the production build. Vite's TypeScript transform does not substitute for typechecking. Use the repository's Vitest or existing runner and configured browser/DOM environment for interaction tests. Use the normal router and provider test wrapper.
- Measure initial and navigational chunks, compressed transfer size, parse cost, and user-visible latency. Use the project's existing analyzer or a compatible plugin with the installed bundler. Split routes or expensive optional features when the evidence warrants it. Inspect duplication and shared chunks before adding manual chunk rules.
- Run production preview as a local smoke test, then verify the actual host when routing, headers, env injection, subpaths, caching, or deployment fallback is involved. Verify direct navigation and a representative lazy route.

Official references [Vite guide](https://vite.dev/guide/), [Environment and modes](https://vite.dev/guide/env-and-mode.html), and [Production build](https://vite.dev/guide/build.html).
