# Tech Stack & Headless Architecture (`13-technology-and-headless-architecture`)

## 1. Tech Stack Neutrality & Project Inspection
The AI must inspect the project's existing codebase and technical requirements before proposing implementations:
- **Presentation Layer**: Support Next.js, React, Vue, Astro, WordPress, or static HTML based on existing project context.
- **Data Integration**: Connect headless CMS repositories and PMS/CRS engines via GraphQL or REST middleware endpoints.


## Expanded reference material (historical research synthesis)

The following preserved material supplies detailed examples and rationale. Where it uses absolute ratios, technology defaults, or mandated flows, interpret these as proposals subject to the current SKILL.md evidence and context rules. Do not enforce outdated universal rules.

## Reference Module 13: Headless System Architecture & Integration (`headless-architecture`)

### 1. Decoupled Architecture Model
The platform separates the presentation layer (Next.js/React) from backend operational systems using an API-first Headless CMS (CrafterCMS) linked to Property Management Systems (Opera/Mews) and Central Reservation Systems (CRS) via GraphQL/REST API orchestration layers.

```
┌────────────────────────────────────────────────────────────────────────┐
│ HEADLESS OMNICHANNEL ARCHITECTURE                                    │
├────────────────────────────────────────────────────────────────────────┤
│ CENTRAL HEADLESS CMS (e.g., CrafterCMS)                              │
│ Core Content Repository, Localization, Media & Editorial Assets     │
└───────┬───────────────────────┬────────────────────────┬─────────────┘
        │                       │                        │
        ▼                       ▼                        ▼
┌───────────────┐       ┌───────────────┐        ┌───────────────┐
│ MARKETING WEB │       │ NATIVE MOBILE │        │ IN-ROOM TV /  │
│ (Next.js/React)│       │ APPLICATIONS  │        │ GUEST PORTAL  │
└───────┬───────┘       └───────┬───────┘        └───────┬───────┘
        │                       │                        │
        └───────────────────────┼────────────────────────┘
                                │ GraphQL / REST API Layer
                                ▼
         ┌──────────────────────────────────────────────┐
         │ ENTERPRISE SYSTEMS                           │
         │ Property Management Systems (Opera / Mews)   │
         │ Central Reservation Systems (CRS)            │
         │ Customer Relationship Management (CRM)       │
         └──────────────────────────────────────────────┘
```

### 2. Decoupled Rate Token Hydration Query
To hydrate static editorial modules with live PMS rate data without causing Cumulative Layout Shift (`CLS < 0.1`), the front-end executes asynchronous GraphQL queries against the CRS API upon date selection:

```graphql
query FetchRoomRates($propertyId: ID!, $checkIn: Date!, $checkOut: Date!, $currency: String!) {
  property(id: $propertyId) {
    roomCategories {
      id
      code
      name
      ratePlans(checkIn: $checkIn, checkOut: $checkOut, currency: $currency) {
        id
        plainLanguageName
        nightlyRate
        totalStayAmount
        cancellationPolicy
      }
    }
  }
}
```

---
