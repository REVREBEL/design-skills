# Period semantics and attribution
Store **stay date**, **booking creation date**, **snapshot-as-of time** and local property timezone separately. Day-of-week versus calendar date versus equivalent lead time versus adjusted event trading periods are alternative comparisons, not competing truths. Name and persist the comparison method so the analyst can reproduce figures. Change in baseline can legitimately change the result.

Example: comparing current-year first Friday of October against prior-year first Friday isolates weekday patterns; strict calendar-date comparison answers a different question. For same-time-last-year pickup use matched days-before-arrival and consistent cohort windows where feasible. Do not force first-Friday matching across arbitrary fiscal or holiday contexts.

**RevPAR decomposition** requires at least two periods. For `RevPAR=A×O` where `A=ADR` and `O=occupancy_fraction`, exact midpoint/Shapley two-factor attribution is:
`ADR_effect = (A1-A0)×(O0+O1)/2` and `Occupancy_effect = (O1-O0)×(A0+A1)/2`.
The sum equals `RevPAR1-RevPAR0` exactly, assuming consistent definitions. Percentage shares of change are dangerous when contributions have opposite signs or the total change is zero; show absolute effects and method, only compute shares with a documented meaningful denominator. This decomposition is arithmetic, not proof of causation or margin impact.

Forecast intervals must be labeled as intervals or scenario bands, not certainty. Explain data freshness, provisional records, source corrections and reconciliation differences. A revenue manager should be able to drill from topline -> period/segment -> calculation -> contributing transactions when permitted.
