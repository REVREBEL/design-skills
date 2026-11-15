# State and async UI

## Choose ownership

| State | Typical owner |
| --- | --- |
| Temporary UI or editable draft | Local component or nearest shared owner |
| Related transitions within a feature | Reducer when named actions clarify the changes |
| Shareable page controls | Router or URL search params with parsing and defaults |
| Cross-tree configuration or scoped dependencies | Context with a provider at the feature boundary |
| Shared client state with richer subscriptions | Existing store and selectors |
| Remote data with freshness and mutations | Framework data APIs or an existing query cache |

Reuse the installed solution. Redux Toolkit fits explicit domain actions, middleware, and existing Redux workflows. Zustand fits shared stores with targeted selectors. Jotai fits atom-based dependency graphs. TanStack Query or the existing query library fits asynchronous server state. Avoid mirroring query data into a separate store unless the feature owns an independent draft with an explicit reset or merge policy.

## Model the displayed states

- **Initial load:** Use a skeleton when layout is known, or a concise loading indicator for a small operation. Preserve layout and announce meaningful status accessibly.
- **Background refresh:** Keep usable data visible and surface update status or recoverable failures without replacing the entire screen.
- **Empty:** Distinguish an empty collection from a filter with no matches. Provide the applicable next action or clear-filter control.
- **Failure:** Give scoped feedback and a retry or recovery path when viable. Keep prior data or unsaved input if safe. Use a boundary for unexpected render errors and explicit state for expected request errors.
- **Submission:** Keep the request state associated with the originating action. Prevent accidental duplicate submissions and handle server validation. Coordinate client and server behavior for operations that may be retried.

## Coordinate data

Include all inputs and tenant or account scope in query keys where relevant. Decide when to invalidate, refetch, or update the cache based on mutation outcomes. When optimistic behavior is warranted, preserve a rollback strategy and handle concurrent mutations or refetches. Keep server and client validation aligned and test slow responses, failed requests, and out-of-order completion. Reuse cancellation or stale-result handling provided by the project. Start independent reads together only when they can execute safely in parallel.

See the [TanStack Query documentation](https://tanstack.com/query/latest/docs/framework/react/overview) for the installed version's cache and mutation behavior.
