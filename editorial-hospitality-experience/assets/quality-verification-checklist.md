## 5. HEURISTIC EVALUATION & QUALITY VERIFICATION CHECKLIST (quality-verification-checklist)

AI agents must execute this 12-point audit before submitting any generated luxury hospitality digital product code, design layout, or architectural specification.

### 1. Choice Overload & Sludge Check
* [ ] **Room Category Cap**: Are total room options displayed simultaneously capped at 5–7 categories per view step? *(Chernev Choice Overload Rule)*
* [ ] **De-Sludged Rate Plans**: Are raw database codes (`BAR-BB-NONREF`) translated into plain-language selection cards (*Flexible Rate* vs. *Stay & Breakfast*)?
* [ ] **Attribute Alignment**: Are room differences structured logically across standardized dimensions (square footage, bed type, view orientation) to enable easy comparison?

### 2. Ethical Conversion & Dark Pattern Ban
* [ ] **Zero Mass-Market Urgency Tactics**: Are countdown clocks, flashing inventory alerts, or artificial booking counters completely absent?
* [ ] **Zero Interruption Modals**: Is active editorial browsing uninterrupted by email pop-ups or instant discount overlays?
* [ ] **Fine-Dining Service Principles**: Are user date inputs, filter choices, and session states preserved when navigating between pages or step views?

### 3. Spatial & Product Truth Transparency
* [ ] **Transparent Total Pricing**: Is total stay cost (inclusive of mandatory taxes, resort fees, and service charges) displayed up front?
* [ ] **Spatial Specifications**: Does every accommodation detail view include architectural floor plans, exact square footage/meters, bed setup, and window view orientation?
* [ ] **30/70 Media Balance**: Does photography balance 30% detail crops (materials, textures, light) with 70% wide spatial comprehension shots and floor plan overlays?

### 4. Technical Performance & Accessibility
* [ ] **Core Web Vitals**: Is Largest Contentful Paint (`LCP < 2.5s`), Interaction to Next Paint (`INP < 200ms`), and Cumulative Layout Shift (`CLS < 0.1`) verified at the 75th percentile?
* [ ] **WCAG 2.2 AA Contrast**: Does body text meet or exceed `4.5:1` contrast, and display/borders meet `3:1` contrast?
* [ ] **Focus Management**: Are explicit `:focus-visible` rings present and `aria-disabled="true"` mechanics used for non-blocking button states?
* [ ] **System Media Overrides**: Does the interface honor user media overrides via `@media (prefers-reduced-motion)` and `@media (prefers-reduced-data)`?

---

*End of Section 6: Assets, Schemas & Operational Checklists*


## Completion-tier policy

Concept-only: validate rationale, constraints, brand fit, accessibility intent, and open questions. Prototype: additionally verify interactions, responsive states, and representative keyboard paths. Production: run real end-to-end tests, integration contracts, accessibility scans, and field/lab performance evidence. Never claim a skipped check passed.
