---
name: design-styles
description: Master router for visual design styles and UI aesthetics. Use when selecting, comparing, specifying, implementing, or reviewing brutalism, neo-brutalism, glassmorphism, neumorphism, skeuomorphism, minimalism, retro design, retro-futurism, Frutiger Aero, illustration systems, or design theming.
---

# Design Styles: Master Router

This is the **only installable skill** in the archive. The material in `guides/` is internal reference content, not separate skills.

## Routing procedure

1. Identify the user's requested style or visual objective. Prefer an explicitly named style over inferred aesthetic preferences.
2. Consult the matching guide from the table below; for mixed requests, consult only the applicable guides and synthesize their guidance.
3. For ambiguous styles, compare relevant alternatives briefly and recommend based on product goals, legibility, accessibility, brand, and technical constraints.
4. Use the source guide's design principles, hierarchy, layout, typography, color, texture, motion, and implementation techniques. Adapt specifics to the user's design system and framework rather than blindly copying any example.
5. For requests involving theme variables or light/dark themes, also consult the theming architecture guide.
6. For critiques, separate objective usability/accessibility issues from subjective aesthetic choices. For deliverables, produce the requested artifact; do not create unrelated images or code.

## Specialist guide routing

| Trigger / scope | Internal guide |
| --- | --- |
| Brutalism: raw, unfinished, nonconventional interfaces | [`guides/brutalism-suite/brutalism/guide.md`](guides/brutalism-suite/brutalism/guide.md) |
| Industrial brutalism: mechanical/terminal visual systems | [`guides/brutalism-suite/brutalist-skill/guide.md`](guides/brutalism-suite/brutalist-skill/guide.md) |
| Brutalist typography: oversized type and raw layouts | [`guides/brutalism-suite/brutalist-typography/guide.md`](guides/brutalism-suite/brutalist-typography/guide.md) |
| Neo-brutalism: bold colors, borders, and hard shadows | [`guides/brutalism-suite/neo-brutalism/guide.md`](guides/brutalism-suite/neo-brutalism/guide.md) |
| Frutiger Aero: glossy, nature-forward early-2000s visuals | [`guides/frutiger-aero/guide.md`](guides/frutiger-aero/guide.md) |
| Glassmorphism: translucent layered surfaces and blur | [`guides/glassmorphism/guide.md`](guides/glassmorphism/guide.md) |
| Theming architecture: CSS token systems and multi-theme implementation | [`guides/glassmorphism/theming-architecture/guide.md`](guides/glassmorphism/theming-architecture/guide.md) |
| Illustration style: visual language and illustration system rules | [`guides/illustration-style/guide.md`](guides/illustration-style/guide.md) |
| Premium utilitarian minimalism: editorial, monochrome bento layouts | [`guides/minimalist-skill/guide.md`](guides/minimalist-skill/guide.md) |
| Minimalist UI: restrained editorial interfaces and clean interaction | [`guides/minimalist-ui/guide.md`](guides/minimalist-ui/guide.md) |
| Neumorphism: soft UI, embossed surfaces, controlled lighting | [`guides/neumorphism/guide.md`](guides/neumorphism/guide.md) |
| Retro design: vintage 1960s–1980s graphic language | [`guides/retro-design/guide.md`](guides/retro-design/guide.md) |
| Retro-futurism: space-age, atomic-era, speculative future aesthetics | [`guides/retro-futurism/guide.md`](guides/retro-futurism/guide.md) |
| Skeuomorphism: tactile physical metaphors and realistic materials | [`guides/skeuomorphism/guide.md`](guides/skeuomorphism/guide.md) |

## Important distinctions

- `minimalist-skill` and `minimalist-ui` are complementary source approaches, not duplicate installable skills. Read both when the user requests a broad minimalist treatment.
- The brutalism suite contains separate variants. Select `brutalism` for raw unconventional form, `neo-brutalism` for colorful hard-shadow UI, `brutalist-typography` for typography-led treatment, and `brutalist-skill` for industrial/mechanical UI.
- Glassmorphism's theming-architecture guide is a technical companion, not another visual style.
- Never refer to internal `guides/**/guide.md` files as separately installed skills.

## Skill package architecture

Maintain exactly one `SKILL.md`: this file. When extending the collection, add resources under `guides/` as `guide.md` or other reference files and register them in the routing table. If a future task specifically requests multiple installable skills, build a separate multi-skill archive instead.
