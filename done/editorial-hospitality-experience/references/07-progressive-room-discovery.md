# Progressive Room Discovery Models (`07-progressive-room-discovery`)

## 1. Progressive Disclosure Architecture
To prevent cognitive choice overload during room selection, structure room discovery into progressive disclosure tiers:
- **Level 1 (Story Card View)**: Evocative photography, room category title, square footage/meters, bed configuration, and starting nightly rate.
- **Level 2 (Spatial Overview Panel)**: Triggered via inline preview or slide-over drawer without full page reload. Exposes architectural floor plans, light orientation, terrace specs, and bathroom details.
- **Level 3 (Transactional PDP)**: Real-time availability calendar, transparent rate cards, policy toggles, and pre-arrival customization.

*Adaptability Rule: Adjust discovery depth based on property inventory. A resort with 20 suite categories benefits from all three tiers, while a boutique property with 3 room tiers can combine Level 1 and Level 2 into a single expanded card view.*


## Expanded reference material (historical research synthesis)

The following preserved material supplies detailed examples and rationale. Where it uses absolute ratios, technology defaults, or mandated flows, interpret these as proposals subject to the current SKILL.md evidence and context rules. Do not enforce outdated universal rules.

## Reference Module 7: 3-Tier Progressive Room Discovery (`progressive-room-discovery`)

### 1. Framing Rooms as Spatial Experiences
Treating luxury accommodations as standardized e-commerce SKUs induces price sensitivity and harms conversion. Direct reservations and high-tier suite upgrades increase substantially when accommodations are engineered as distinct physical, art-directed spatial experiences. Operator research confirms that presenting rooms through spatial attributes and architectural transparency drives up to a **43% increase in high-tier suite selection**.

### 2. Three-Tier Progressive Disclosure Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│ THREE-TIER PROGRESSIVE DISCLOSURE ARCHITECTURE                         │
├────────────────────────────────────────────────────────────────────────┤
│ Level 1: Story Card View (Initial Browse Grid)                         │
│   • Emotive Visual Crop (Editorial Framing)                            │
│   • Category Title, Square Footage/Meters, Bed Configuration           │
│   • Starting Nightly Rate Indicator & "Explore Details" Trigger        │
│                                │                                       │
│                                ▼ (User Tap / Selection)                │
│ Level 2: Spatial Overview Panel (Slide-Over Drawer / Modal)            │
│   • Architectural Floor Plan Overlay & Precise Room Dimensions         │
│   • Window View & Light Orientation (e.g., South-Facing Ocean Sunset)  │
│   • Bathroom Specifications (Soaking Tub, Dual Rain Showers)           │
│   • Material Close-ups & Acoustic/Elevator Proximity Details           │
│                                │                                       │
│                                ▼ (User Action: Reserve Dates)          │
│ Level 3: Transaction Product Detail Page (PDP)                         │
│   • Real-Time Interactive Dual-Month Availability Calendar             │
│   • Localized Currency Conversion & Itemized Tax/Fee Transparency      │
│   • Stacked Plain-Language Rate Cards (Flexible vs. Stay & Breakfast)  │
│   • Integrated Pre-Arrival Service Customization                       │
└────────────────────────────────────────────────────────────────────────┘
```

---
