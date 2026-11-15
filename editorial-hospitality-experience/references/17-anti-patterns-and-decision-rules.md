# Anti-Patterns & Corrective Decision Rules (`17-anti-patterns-and-decision-rules`)

## 1. Banned Anti-Patterns & Corrective Actions
| Anti-Pattern | Operational & Brand Failure Mode | Corrective Luxury UX Rule |
| :--- | :--- | :--- |
| **Intrusive Pop-ups** | Mid-browse discount pop-ups or survey modals obstruct visual media and cheapen brand prestige. | Use a persistent, low-profile search capsule that expands into a drawer upon interaction. |
| **Artificial Urgency** | Countdown clocks and pressure copy ("14 people viewing now!") induce anxiety and erode trust. | Provide authentic date availability calendars and transparent service guarantees. |
| **Rate Plan Sludge** | Displaying dozens of cryptic database codes (`BAR-BB-3N-NONREF`) causes choice paralysis. | Translate rate plans into 2-3 human-centered selection cards (*Flexible Rate* vs. *Stay & Breakfast*). |
| **Information Deficits** | Hiding square footage, bed setups, or cancellation terms under the guise of "minimalism" forces guests off-site. | Provide scannable spatial specs, available floor plan SVGs, and transparent policies. |
| **Inaccessible Faint Copy** | Low-contrast light-gray copy or thin font weights (`weight < 400`) violate WCAG standards. | Enforce WCAG `4.5:1` contrast ratios and visible outline rings (`:focus-visible`). |

## 2. Fine-Dining Customer Service UX Principles (NN/g)
Apply Susan Farrell's fine-dining principles to digital product interactions:
1. **The Guest Owns the Space**: Never perform unexpected layout shifts or inject pop-up modals during active browsing.
2. **Never Clear the Table Early**: Preserve user inputs, selected dates, and filter choices across step navigations and session timeouts.
3. **Match Guest Pace**: Support unhurried editorial browsing while providing express checkout pathways.


## Expanded reference material (historical research synthesis)

The following preserved material supplies detailed examples and rationale. Where it uses absolute ratios, technology defaults, or mandated flows, interpret these as proposals subject to the current SKILL.md evidence and context rules. Do not enforce outdated universal rules.

## Reference Module 17: Dark Pattern Bans & Fine-Dining UX (`dark-pattern-bans`)

### 1. Banned Mass-Market Anti-Patterns
The skill strictly forbids the following 8 deceptive e-commerce practices:
1.  ❌ **Artificial Scarcity Banners**: "Only 1 room left at this price!", "14 people viewing now!".
2.  ❌ **Countdown Timers & Pressure Tactics**: Imposing arbitrary time limits during room selection.
3.  ❌ **Intrusive Interruption Modals**: Mid-browse email capture pop-ups or exit-intent discount overlays.
4.  ❌ **Rate Plan Sludge Overload**: Surfacing unfiltered lists of cryptic database codes (`BAR-BB-NONREF`).
5.  ❌ **Drip Base-Rate Pricing**: Concealing mandatory resort fees or regional taxes until final checkout steps.
6.  ❌ **Low-Contrast Faint Copy**: Unreadable light-gray typography violating WCAG `4.5:1` contrast.
7.  ❌ **Native Disabled HTML Buttons**: Native `<button disabled>` tags that trap screen reader focus.
8.  ❌ **Forced Upfront Registration**: Forcing guest account creation before rate evaluation or checkout.

### 2. Fine-Dining Customer Service UX (Susan Farrell / NN/g)
Translating physical restaurant and luxury service principles into digital interactions:
1.  *The Guest Owns the Space*: Never interrupt active reading with unexpected modal prompts or pop-ups.
2.  *Never Clear the Table Early*: Preserve user inputs, selected dates, and filter choices across step navigations and session timeouts.
3.  *Match Guest Pace*: Support unhurried editorial browsing while providing express checkout pathways.
4.  *Contextual Cross-Selling*: Introduce ancillary services (spa, transfers, dining) after the core room reservation is confirmed, treating upsells like offering dessert after an exceptional main course.
