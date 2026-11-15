# Hospitality metric governance
## Required metric contract
Record `metric_id`, owner, purpose, numerator, denominator, physical/sellable/benchmark inventory policy, rooms-sold basis, revenue recognition, currency, tax/fee inclusions, stay/booking/snapshot dates and timezone, segments, granularity, treatment of complimentary/day-use/house use, missing data, aggregation and reconciliation sources. Do not declare one denominator a universal industry truth. Compare published financial, benchmarking and vendor methodologies where sources are available.

**Occupancy:** sold room nights / eligible available room nights, with denominator policy explicit. Example hotel convention: `sellable_room_nights = physical_room_nights - eligible_OOO_room_nights`; if supplied net sellable denominator, subtract nothing more. OOS treatment must follow adopted policy. A ratio with zero denominator is undefined (`null`, not zero).

**ADR:** recognized eligible room revenue / eligible sold room nights, with exclusions and revenue classification defined. Be precise about room-package allocation, taxes, complimentary and house use, and whether reporting counts day-use.

**RevPAR:** recognized eligible room revenue / eligible available room nights. `ADR × occupancy_fraction` only if all numerator and denominator semantics reconcile; avoid comparing mismatched occupancy standards.

**TRevPAR:** recognized total operating revenue under defined outlet inclusion / eligible available room nights; disclose preliminary POS/posting status and allocation.

**Pickup:** OTB at current snapshot minus OTB at historical snapshot for the SAME defined stay-date cohort and measure (rooms/revenue), preserving revisions, cancellations and booking changes. Snapshot timestamp and comparison period must be visible.

**Pace variance:** `(comparable current OTB − comparable baseline OTB) / baseline` if baseline is nonzero; display unavailable otherwise. Define lead-time alignment, seasonal/events and date alignment before computation.

**Cancellation rate:** cancellations / booked reservations or room nights, not interchangeably; use a defined observation period and cohort. Channel-specific historical cancellation rates require cited, representative local evidence, not invented industry averages.

**Channel net room revenue after acquisition costs:** recognized room revenue minus *defined* acquisition costs (commissions, GDS/transaction/merchant fees and attributable or allocated marketing, with cost attribution disclosed). Do not label this full GOP, EBITDA, or total hotel contribution. If discussing incremental operating contribution, explicitly account for variable service delivery costs and displaced demand.

Use weighted aggregates from sums, never mean of property ADR/occupancy percentages without proper weighting. Validate currency, rounding and time-zone boundaries. Distinguish unavailable from actual zero; UI should say why a value is missing.
