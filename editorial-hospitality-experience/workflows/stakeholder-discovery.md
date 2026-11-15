# Stakeholder Discovery & Constraint Mapping (`workflows/stakeholder-discovery`)
## Objective
Establish property scope, brand position, target guest cohorts, inventory complexity, PMS/CRS integrations, and existing technical stack.

## Execution Steps
1. **Portfolio Mapping**: Inventory all property locations, room categories, dining venues, and spa offerings.
2. **Tech Stack Inspection**: Audit existing codebase, CMS, PMS, and front-end framework (React, Vue, Astro, WordPress, static HTML).
3. **Integration Audit**: Identify PMS/CRS endpoints, rate code structures, and tax calculation rules.
4. **Direct Value Framing**: Define property-specific direct booking perks (flexible cancellation, upgrade priority, breakfast credit).


## Detailed execution procedure (preserved)

## Workflow 1: Stakeholder Discovery & Constraint Mapping (`stakeholder-discovery`)

### Objective
Uncover property portfolio scope, commercial goals, guest cohorts, technical PMS/CRS constraints, and operational dependencies before commencing design or engineering work.

### Step-by-Step Execution

1. **Portfolio & Property Taxonomy Mapping**
   - Identify whether the client is a single independent boutique hotel, an urban luxury flagship, a multi-property resort collection, or an experiential hospitality group.
   - Map total room keys, inventory categories, and physical layout variations (suites, villas, residences, connected units).

2. **Technical & PMS Integration Mapping**
   - Identify underlying Property Management System (PMS) and Central Reservation System (CRS) engines (e.g., Oracle Opera Cloud, Mews, SynXis, Leading Hotels of the World CRS).
   - Document rate plan logic: multi-room occupancy constraints, minimum length of stay (MLOS) rules, regional tax inclusions, mandatory resort/facility fees, and currency conversion logic.
   - Establish Headless CMS architecture preferences (e.g., CrafterCMS, Contentful, Sanity) and existing API capability.

3. **Guest Cohort & Commercial Goal Definition**
   - Define primary guest personas (e.g., Ultra-High-Net-Worth leisure travelers, wellness retreat seekers, direct-booking loyalists, event/wedding bookers).
   - Establish commercial metrics: target direct-booking capture ratio (e.g., 65% direct vs. 35% OTA split), average daily rate (ADR) target, and average length of stay (ALOS).
   - Document exclusive direct-booking value propositions (e.g., complimentary full breakfast, room upgrade priority, flexible pre-arrival cancellation, $100 spa credit).

### Output Artifact
`discovery-constraint-spec.json` summarizing property structure, PMS engine parameters, rate logic, direct value perks, and technical requirements.

---
