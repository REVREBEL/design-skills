# Workflow: validate metric semantics
**Input:** sample dataset, proposed metric, property reporting conventions and source mapping.
1. Determine user decision and whether metric describes stay, booking, posting, snapshot or booking channel.
2. Record reporting contract: numerator/denominator; units; recognized vs booked; sold-room basis; physical/sellable/benchmark inventory; OOO/OOS; exclusions; segment/date/timezone; snapshot-as-of; missing-data policy.
3. Verify definitions against reporting policy/vendor contracts before coding. If unavailable, describe candidate conventions, select one only for labeled example.
4. Compute aggregate from numerators/denominators, not unweighted means. Zero denominator -> null plus reason. Reject negative eligible inventory or inconsistent counts unless documented override.
5. Cross-check ADR × occupancy fraction vs RevPAR under aligned definitions. Investigate disagreement before rendering.
6. For pace, record explicit comparison type and align snapshot lead time/cohorts. For attribution, demand two periods and named method; show absolute effects when shares are misleading.
7. For net-after-acquisition, document cost scope, allocations and label correctly.
8. Execute fixture harness and additional scenario tests specific to report; log scope and failures. Handoff a metric dictionary row and UI copy for empty/missing states.
