---
name: brand
description: 'Load when the user says "make this on-brand", "use the AI for Software Engineers brand", "create branded slides", or requests visual content for Logan Thorneloe or AI for Software Engineers.'
metadata:
  internal: true
  opencode/slash: "true"
---

# Brand

Create visual deliverables in the AI for Software Engineers identity. Another named brand or an explicit unbranded request overrides this skill.

## Workflow

1. Identify output, audience, source material, channel, and aspect ratio.
2. Before authoring, read [`references/brand.md`](references/brand.md) completely. It is the source of truth for mode routing, palette, typography, assets, and audit criteria.
3. Load the technical upstream skill:
   - slides/presentations → `/bento-slides`
   - video/motion → the requested video framework
   - standalone visual → current harness's strongest deterministic visual tool
4. Route the concept using the reference's default:
   - systems, flows, comparisons, architecture → Technical Graphic
   - one physical object or metaphor → Realistic Cel-Shaded Illustration
5. Build one visual argument per output/frame/slide. Resolve bundled asset paths relative to this skill.
6. Run the reference's Final audit plus every upstream renderer/validator.

Hard exit: deliverable passes the brand audit and upstream technical validation. Report **blocked** if the required upstream capability or validation cannot run.

## Gotchas

- `/brand` owns creative direction; upstream skills retain schemas, rendering, validation, and safety rules.
- Keep customization here. Never edit or fork installed vendor skills merely to apply branding.
- Multiple concepts become separate outputs, not a grid/collage default.
- Logos belong at identity moments, not explanatory graphics, unless requested.
- “It uses the colors” is not proof of brand compliance; run the complete audit.
