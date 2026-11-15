# UI Pattern: Chunked Mobile Accordion & Express Checkout
Single-page accordion checkout with 1-tap digital wallet integration (Apple Pay / Google Pay).


## Expanded pattern specification

## 6. Chunked Mobile Accordion & Express Checkout (`mobile-booking-flow`)

### Mobile Architecture
* Replaces multi-page checkout flows with a single-page, progressive accordion interface.
* **Chunked Accordion Steps**:
  1. *Stay Summary & Guest Details*
  2. *Add-On Customization & Concierge Requests*
  3. *Payment & Guarantee*

### Express Payment Integration
* Prominent top-placed Digital Wallet buttons (`Apple Pay`, `Google Pay`) for 1-tap booking completion.
* Auto-fills guest name, email, and phone number directly from digital wallet tokens.

### Accessibility Mechanics
* Accordion panels use `<button aria-expanded="true/false" aria-controls="section-id">`.
* Closed sections display summary chips (e.g., "Oct 14-18, 2 Guests • Flexible Rate Selected") so progress is always visible.

---
