# Integration data and write authority
Do not assume a universal PMS/CRS/RMS/POS ownership map. Document a contract per property and field: entity and ID, authoritative read origin, permitted write target, user role/property scope, sync frequency, timestamp, units, currency, timezone, transforms, validation rules, conflict resolution, retry/idempotency policy and audit record.

Example fields: `roomStatus`, `availabilityByDate`, `rateRestriction`, `forecastValue`, `reservationState`, `folioCharge`. The vendor assigned to each field must be verified from documentation or deployment configuration. Many RMS products recommend rates rather than write them; some PMS deployments control rates. Never infer API names, schemas, write permissions or SLAs.

Risk classification: read-only report (cache permitted with disclosure); non-financial draft (may autosave with revision checks); operational reservation/room assignment (verify current state and conflict); pricing/availability changes (freshness and authorization); financial folio/payments (strict review and reconciliation); identity grants (re-auth and audit where appropriate). No default offline queue for critical writes. UI success follows authoritative acknowledgment, not optimistic visual state alone.

Security: enforcement happens server side; scoped deep links alone are not a guard. Minimize PII but allow authorized operational access when necessary. Restrict exports, redact logs and error telemetry, protect secrets and bearer tokens server side, document retention, implement audit trail without sensitive payload logging.
