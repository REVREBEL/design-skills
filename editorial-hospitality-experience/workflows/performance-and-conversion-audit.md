# Performance & Conversion Quality Audit (`workflows/performance-and-conversion-audit`)
## Objective
Execute final verification across Core Web Vitals, WCAG accessibility, price transparency, and zero dark patterns.

## Execution Steps
1. **Sludge & Dark Pattern Scan**: Confirm total absence of countdown timers, fake scarcity badges, and interruptive pop-ups.
2. **Price Transparency Check**: Verify upfront disclosure of total-stay pricing inclusive of taxes and mandatory resort fees.
3. **Technical Quality Gates**: Validate Core Web Vitals (`LCP < 2.5s`, `INP < 200ms`, `CLS < 0.1`) and WCAG 2.2 AA contrast.


## Detailed execution procedure (preserved)

## Workflow 10: Performance Budget & Conversion Verification (`performance-optimization`)

### Objective
Conduct final technical verification, Core Web Vitals testing, and commercial conversion validation prior to deployment.

### Step-by-Step Execution

1. **Core Web Vitals Verification**
   - Measure performance at 75th percentile under throttled mobile conditions:
     - Largest Contentful Paint (LCP) `< 2.5s`
     - Interaction to Next Paint (INP) `< 200ms`
     - Cumulative Layout Shift (CLS) `< 0.1`

2. **Data Preservation & Session Continuity Verification**
   - Test "Never Clear the Table Early" principle: Verify that selected dates, guest counts, and filtered preferences persist when navigating backward from room PDP to homepage or search overlay.

3. **Direct Booking Value & Transparency Final Verification**
   - Confirm direct booking perk guarantees (e.g., rate parity, breakfast inclusion, flexible cancellation) are prominently displayed near checkout triggers.
   - Confirm final checkout total matches initial displayed total exactly (zero hidden drip fees).

### Output Artifact
`performance-verification-signoff.md` certifying that the digital product meets all 7 Completion Standards and is ready for production release.
