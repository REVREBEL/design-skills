# Modernization

1. Inventory React, React DOM, framework, JSX transform, TypeScript declarations, lint/test tools, and peer dependencies. Capture behavior and establish a baseline build before the upgrade.
2. Read release and upgrade guidance for the installed and target versions. Upgrade related packages together as required by their peer contracts. Plan incremental changes where legacy root APIs, refs, context, test tooling, or deprecations affect multiple entry points.
3. Translate class behavior by responsibility. Map local state to state or a reducer, move interaction side effects to handlers, and pair external synchronization with cleanup. Check preservation of state identity, callback timing, error boundaries, refs, and imperative integrations. Keep an existing class error boundary or use the app's supported boundary abstraction where appropriate.
4. Use a version-matched codemod when its scope is clear. Inspect its diff and verify changes to import paths, types, and calling conventions. Run relevant checks after each stage.
5. Adopt transitions, Suspense, action APIs, ref changes, or React Compiler only where supported and appropriate. Check semantics and recovery paths. After enabling development Strict Mode, investigate non-idempotent setup and cleanup instead of using a global flag to skip repeated work.
6. Run typecheck, lint, tests, and a production build with the resulting dependency set. Verify representative interactions, async cleanup, server hydration where applicable, and integration with the actual runtime.

Official reference [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide).
