---
name: brand
description: Apply Logan Thorneloe's AI for Software Engineers brand to presentations, videos, diagrams, thumbnails, and illustrations. Must use for visual content created for Logan or AI for Software Engineers unless the user explicitly requests another brand or an unbranded output.
metadata:
  opencode/slash: "true"
---

# Brand

Create in the AI for Software Engineers visual identity. Read [`references/brand.md`](references/brand.md) before authoring.

## Invocation policy

Use this skill by default for **visual deliverables** for Logan or AI for Software Engineers: slides, videos, diagrams, charts, thumbnails, illustrations, and motion graphics. Do not apply it to plain prose, research, code, or operational work unless visual output is part of the request. Another named brand or an explicit unbranded request overrides this default.

`/brand` is the entry point for branded visual work. Do not invoke `/bento-slides` alone when the output should carry this brand.

## Compose with upstream skills

- **Slides/presentations:** load and follow `/bento-slides` for its document contract, then apply this brand.
- **Video/motion:** use the user's requested tool or framework, then apply this brand.
- **Standalone diagrams, thumbnails, or illustrations:** use the mode router in the brand reference.

This skill overrides upstream **creative defaults**, not technical schemas, validation, rendering, or safety requirements. Priority: explicit user direction → this brand → upstream creative guidance → generic defaults.

## Workflow

1. Identify output, audience, aspect ratio, and source material.
2. Load the relevant upstream skill when creating slides or video.
3. Choose Technical Graphic or Realistic Cel-Shaded Illustration mode.
4. Use bundled logos/fonts only where the reference permits. Resolve paths relative to this skill.
5. Build one clear visual argument per frame or slide.
6. Audit against the reference before delivery.

Do not edit or fork vendor skills to apply branding. Keep brand customizations here so upstream skills remain safely updateable.
