# Jobs-to-be-done and information architecture
Role examples: owner/asset manager monitors asset returns and budget performance; corporate commercial lead compares portfolios; revenue manager inspects stay-date pace and revises forecast; distribution lead sees channel cost/parity; GM inspects operational exceptions; front desk agent assigns rooms and settles folios; housekeeping lead manages turn priorities; analyst reconciles source postings; administrator scopes property access. Permissions and real user needs override these stereotypes.

Architect 3 principal workspace shapes:
1. **Monitoring overview:** exceptions, changes from comparator, freshness and drillthrough. KPIs selected for decisions; no fixed count.
2. **Analytical workbench:** persistent property/date/segment context, table or chart, explanation panel, drillthrough, saved view; maintain origin context.
3. **Transactional console:** high-throughput searchable queue, selected record inspector, confirmations, write authority, recovery, audit trail. Avoid treating a modal success message as confirmed integration write.

For multi-property products define account -> region/brand -> property -> department scopes, and explain how global filters intersect local views. Saved filters and deep links must not bypass authorization. Roles may require different data density and default navigation, but give accessible discoverable navigation and straightforward way back.

Specify route map, object/relationship map, role/decision matrix, prioritized top tasks, view states, and data requirements before drawing page compositions. Mobile may offer purpose-built alert triage and quick actions rather than shrinking a 40-column forecast grid.
