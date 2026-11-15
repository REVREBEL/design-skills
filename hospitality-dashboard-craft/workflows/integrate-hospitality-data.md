# Workflow: safe hospitality integration
1. Inventory vendors, actual endpoint docs, sandbox credentials (not pasted into reports), fields, property mapping and integration ownership.
2. Build per-field authority matrix: read system; write system if any; scoped user rights; sync lag; reconciliation and errors.
3. Define DTO/schema validation and domain normalization, currency/timezone translation, mapping of room types, rate codes, property/segment identifiers.
4. Describe refresh and consistency policy, stale/partial/error states, retry on 429 per Retry-After, and whether write idempotency is supported. Do not invent vendor capabilities.
5. For mutations, validate rights on server, check version/current state, submit safely, reconcile official response, and audit. Do not auto-queue consequential offline writes.
6. Contract-test with sandbox or fixtures, simulate duplicates/staleness/concurrency, and perform cross-property authorization checks.
7. Deliver integration contract plus evidence of actual tests and unverified assumptions.
