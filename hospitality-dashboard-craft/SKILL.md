---
name: hospitality-dashboard-craft
description: Design, build, refactor, and audit restrained, accessible, data-trustworthy hospitality dashboards and operational applications using React, shadcn/ui, and Tailwind CSS v4. Use for hotel revenue/forecast, distribution, PMS/CRS/RMS, operations, portfolio analytics, data grids, component systems, KPI correctness and integration workflows.
---
# Hospitality Dashboard Craft v3.2

## Purpose
Deliver operationally correct, aesthetically restrained software. Minimalism reduces noise, never decision-critical information. Preserve visual distinction without prescribing a universal dashboard. Adapt to the current application; do not rebuild what already works.

## First steps
1. Classify deliverable: critique, design concept, specification, React implementation, integration, audit, or production verification. Do not conflate these.
2. Inspect actual repository, packages, source data, user roles, brand tokens and authorizations when available. When inaccessible, mark assumptions, do not invent.
3. Identify decisions and workflows before choosing monitoring dashboard, analytical workbench, transactional console, or admin view.
4. Read `references/01-decision-rules.md`, then selectively consult routed references and workflows below. Load only relevant files, not the entire library.
5. Validate domain mathematics BEFORE visualizing or enabling writes. Use `workflows/validate-metric-semantics.md`.
6. Design interaction states proportional to the operation's risk, then implement and evaluate. Report tests run, evidence and gaps.

## Directive hierarchy
- **Invariants:** authorized access, no fabricated data/API capabilities, defined metric grain and bases, division-by-zero as null/unavailable, safe mutation contracts, truthful test claims, applicable accessibility requirements.
- **Context decisions:** screen density, layout, chart, theme, comparison alignment, data freshness thresholds, input modality, permissions architecture, and component variants. Decide by role/task/stack.
- **Hypotheses:** fixed KPI counts, five-second scan test, task-completion targets, default stale-data thresholds, typography and marketing conversion claims. Propose tests rather than asserting empirical validity.

## Mandatory domain gate
Before calculating any KPI, specify numerator, denominator, inventory basis (physical/sellable/benchmark), rooms-sold basis, accounting basis (recognized vs booking value), snapshot time and stay/booking date, currency, period, segmentation, and missing-value policy. Under chosen sellable-inventory assumption `sellable=physical-OOO`, never subtract OOO a second time. Other reporting standards may use different availability rules. Undefined ratios are `null`, displayed as N/A with explanatory reason. ADR × occupancy = RevPAR only when all component definitions align and percentage is scaled as a fraction. Do not claim ADR-vs-occupancy attribution from a single period.

## Integration safety gate
PMS, CRS, RMS, POS and other platform roles are examples, not immutable owners. Verify per-field read/write authority and reconciliation rules. No guest PII or credentials in client logs. Do not enable operational offline write queues or optimistic commits unless explicitly supported and conflict-safe. Use mock data only when labeled.

## Routing
| Task | Read |
|---|---|
| KPI, pickup, RevPAR, channel contribution | `references/02-metrics-and-accounting.md`; `references/03-time-baselines-and-attribution.md`; `workflows/validate-metric-semantics.md` |
| Dashboard hierarchy or personas | `references/04-roles-and-information-architecture.md`; `workflows/design-workspace-architecture.md` |
| Visual design, critique, density | `references/05-minimalism-and-visual-language.md`; `workflows/visual-design-critique.md` |
| shadcn/ui, Tailwind v4, code | `references/06-shadcn-tailwind-architecture.md`; `patterns/analytical-table.md`; `workflows/implement-shadcn-tailwind-v4.md` |
| Charts and tables | `references/07-visualization-and-data-grids.md`; `patterns/kpi-and-variance.md`; `patterns/analytical-table.md` |
| PMS/CRS/RMS data/write workflow | `references/08-data-contracts-and-write-authority.md`; `workflows/integrate-hospitality-data.md` |
| Accessibility/mobile/performance | `references/09-accessibility-performance.md`; `workflows/test-and-handoff.md` |
| Forecast editor, property switch, exceptions | `patterns/forecast-editor.md`; `patterns/property-switcher.md`; `patterns/states-and-feedback.md` |

## Output contracts
- **Audit:** verified findings, severity, impact, traceable location/evidence, proposed corrections, unverified areas.
- **Concept:** task, decision owner, information hierarchy, states, sketch/spec, rationale, open assumptions.
- **Implementation:** files/patches, dependencies and version constraints, story/usage, test results, data provenance, rollback or limitations.
- **Integration:** system mapping, read/write scope, contract, failure/retry behavior, authorization, reconciliation and test plan.
- **Production-ready claim:** only after appropriate integration, regression, accessibility and operational review actually executed; otherwise label appropriately.

## Quality gates
Check semantic metrics, permission isolation, no fabricated data, keyboard operability, WCAG 2.2 AA applicability, layout on touch and dense screens, contrast, focus, state feedback, data freshness and correct missing values. Automated scans are incomplete; document manual review required. Use `python3 scripts/check_metrics.py` and `python3 scripts/validate_package.py` for package-level checks. Do not claim they certify a deployed website.
