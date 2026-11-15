# UI Pattern: Stacked Plain-Language Rate Cards
Vertical selection cards translating internal rate codes into plain-language terms with policy toggles.


## Expanded pattern specification

## 5. Stacked Plain-Language Rate Cards & Policy Toggles (`rate-cards`)

### Component Architecture
* Replaces complex multi-column pricing matrices with vertical stacked selection cards.
* Each card represents a distinct human-centered rate category (e.g., *Flexible Rate*, *Stay & Breakfast*, *Curated Retreat Package*).

### Card Elements
* **Header**: Rate title in plain language (zero internal codes like `BAR-BB-NONREF`).
* **Inclusions List**: Bullet points explicitly listing perks (e.g., *Daily Artisanal Breakfast*, *Complimentary Valet*, *Flexible Cancellation until 3 PM 7 Days Prior*).
* **Price Display**: Total stay rate prominently displayed in bold tabular numbers, with base rate + tax breakdown visible on hover or toggle.
* **Selection State**: Card selected via custom radio control (`input[type="radio"]`) wrapped in accessible `<label>`.

### Interactive Policy Comparison Toggle
* Inline toggle switch allowing guests to compare *Flexible Terms* vs. *Non-Refundable Terms* with real-time price adjustment calculation displayed instantly.

---
