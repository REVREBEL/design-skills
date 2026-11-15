# Headless API & PMS Orchestration (`workflows/api-orchestration`)
## Objective
Connect presentation layers to Headless CMS and PMS/CRS middleware via GraphQL or REST endpoints.

## Execution Steps
1. **Data Bifurcation**: Fetch static editorial content via CMS endpoints and hydrate live availability/rates asynchronously.
2. **Rate Code Mapping**: Intercept legacy PMS codes (`BAR-BB-NONREF`) in middleware and map them to human selection cards.
3. **Fallback Handling**: Implement graceful fallback states if live PMS queries experience edge latency.


## Detailed execution procedure (preserved)

## Workflow 8: Headless API & PMS Orchestration (`api-orchestration`)

### Objective
Build an API middleware orchestration layer that bridges Headless CMS content schemas (CrafterCMS) with Property Management Systems (Opera/Mews) while translating database codes into human copy.

### Step-by-Step Execution

1. **CMS Content Schema Querying**
   - Construct GraphQL queries to fetch structured CMS content across the 15 core schemas (Property, Room Category, Rate Inclusion, Policy, FAQ, etc.).

2. **PMS Live Availability & Rate Mapping**
   - Build edge API middleware to execute REST/GraphQL queries against PMS endpoints for real-time date availability, inventory count, and total stay rates.
   - Implement short-lived edge caching (e.g., 60-second SWR) for rate lookups to prevent rate-limiting while preserving inventory accuracy.

3. **Plain-Language Rate Code Translation**
   - Intercept raw PMS rate codes (e.g., `BAR-BB-NONREF-3N`) and translate them into structured plain-language cards (*Flexible Rate*, *Stay & Breakfast*, *Advanced Purchase*).
   - Calculate total stay price up front inclusive of mandatory regional taxes and resort fees.

4. **Guest Session & Inventory Lock Management**
   - Preserve selected dates, guest counts, and room choices across step navigations using encrypted session cookies or local state.
   - Dispatch clean booking payload to PMS CRS upon guest checkout completion.

### Output Artifact
`api-orchestration-spec.md` with GraphQL queries, PMS translation mapping functions, caching strategies, and booking payload schemas.

---
