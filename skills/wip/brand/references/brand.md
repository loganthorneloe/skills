# AI for Software Engineers brand

## Identity

- Brand: **AI for Software Engineers** / **AI for SWEs**
- Audience: working software engineers learning AI systems, infrastructure, tooling, and tradeoffs
- Character: technical, direct, pragmatic, premium, calm, modern
- Voice: engineer-to-engineer; concrete and conversational; never corporate, hype-heavy, or generic

## Core system

### Palette

| Token | Value | Use |
| --- | --- | --- |
| Deep blue | `#101527` | Primary dark background, linework on white |
| White | `#FFFFFF` | Primary text on dark, technical-graphic background |
| Red | `#CC3333` | Sparse emphasis, key state, brand mark |
| Red hover/dark | `#B82E2E` | Secondary red state |
| Elevated dark | `#1E2334` | Cards/panels on deep blue |
| Border dark | `#303544` | Dividers, borders, inactive edges |
| Muted gray | `#535764` | Secondary structures |
| Secondary text | `#9FA1A9` | Captions and supporting text |

Red is an accent, not a fill for large areas. Technical Graphic Mode is stricter: white and deep blue only unless the user requests color.

### Typography

- Headings: **Sora**, weights 600–800
- Body/labels: **Roboto**, weights 400–700
- Keep labels short and hierarchy obvious.
- Avoid more than two type families.

Bundled files:

```text
assets/fonts/Sora-SemiBold.ttf
assets/fonts/Sora-Bold.ttf
assets/fonts/Sora-ExtraBold.ttf
assets/fonts/Roboto-Regular.ttf
assets/fonts/Roboto-Medium.ttf
assets/fonts/Roboto-Bold.ttf
```

Embed the fonts for portable/self-contained outputs. Do not rely on network font loading in final deliverables.

### Marks

Prefer the authoritative Drive-sourced SVG marks:

```text
assets/logos/duck-dark.svg
assets/logos/duck-dark-filled.svg
assets/logos/duck-light.svg
assets/logos/duck-small-dark.svg
assets/logos/duck-small-light.svg
```

Raster fallbacks and the wordmark:

```text
assets/logos/ai-for-swes-square.png
assets/logos/ai-for-swes-wordmark.png
```

- Use the wordmark on branded covers, end cards, and publication identity moments.
- Use an SVG duck mark when space is constrained; choose the dark/light variant for its intended background.
- Preserve aspect ratio and original colors; never recolor, distort, outline, or add effects.
- Keep clear space around marks.
- Do **not** place logos in explanatory technical graphics or editorial thumbnails unless explicitly requested.

## Mode router

- System, flow, comparison, dependency, architecture, process, bottleneck, or tradeoff → **Technical Graphic Mode**.
- One strong object, machine, physical metaphor, symbolic scene, hardware, or infrastructure subject → **Realistic Cel-Shaded Illustration Mode**.
- Multiple options → separate outputs, never a grid or collage.

## Technical Graphic Mode

Use for diagrams, charts, explainers, architecture sketches, process flows, system maps, comparisons, bottleneck visuals, headers, and clean editorial thumbnails.

### Style

- White `#FFFFFF` background.
- Deep blue `#101527` only unless asked otherwise.
- Clean technical linework.
- Functional node-link systems language.
- Nodes, edges, arrows, clusters, routes, loops, containers, and grouped components only when they explain relationships.
- Simple outline software icons.
- Generous whitespace.
- Minimal, modern, premium, calm, software-engineering focused.

### Rules

- Base visuals on source content when provided.
- Explain one core idea clearly.
- Use short labels only: 1–3 words.
- Do not include the newsletter title.
- For thumbnails, default to 16:9, use 3–5 main components, and avoid phrase text unless asked.
- Prefer code-authored SVG/HTML shapes and diagrams so geometry stays editable and deterministic.

### Avoid

Logos, watermarks, screenshots, fake dashboards, stock-photo people, cartoons, mascots, robots, brains, galaxies, nebula effects, 3D objects, decorative clutter, sparkles, stars, random dots, background speckles, and long text.

## Realistic Cel-Shaded Illustration Mode

Use for pictures, realistic conceptual thumbnails, visual metaphors, technical objects, machines, compute hardware, infrastructure, chips, servers, instruments, and physical systems.

### Style

- Realistic cel-shaded illustration.
- High-detail rendering.
- Crisp dark linework.
- Hard-edged cel shading.
- Flat, controlled color planes.
- Realistic proportions and believable forms.
- Clean, readable composition.
- Solid deep-blue `#101527` background.

### Subject direction

- Prefer metal, machinery, compute, infrastructure, servers, GPUs, chips, cooling, cables, control panels, industrial systems, robotics, aerospace hardware, and scientific instruments when relevant.
- Choose the subject from the core argument, not title keywords.
- Prefer one dominant object or tightly unified concept.
- Keep it centered, readable, fully contained, and free of text unless asked.
- Default to square unless asked otherwise.

Reference composition:

```text
assets/examples/foundations-cel-shaded.png
```

Use it as style evidence, not as a template to repeat.

### Avoid

Cartoon, cute, toy-like, mascot, simplified vector icon, clipart, chibi, exaggerated proportions, low detail, generic AI imagery, generic robots/computers, random machines, photorealism, 3D-render appearance, gradient backgrounds, soft airbrush shading, texture noise, blur, depth of field, sketchiness, messy lines, stars, scenery, background objects, and text.

## Slides

- Default to 16:9.
- Use deep-blue covers with white type and sparse red emphasis.
- One argument per slide; favor diagrams, charts, and progressive reveals over bullet walls.
- Use Sora for titles and Roboto for body/labels.
- Keep a clear grid, generous margins, and strong whitespace.
- Dark cards may use `#1E2334` with `#303544` borders.
- Technical diagrams should retain their white/deep-blue mode when placed as a deliberate light canvas within the deck.
- Use morphs only to explain continuity or state change, not decoration.
- Embed fonts and used assets in `.bento.html` outputs.

## Video and motion

- Default to 16:9 unless the delivery channel says otherwise.
- Use motion to explain causality, flow, state, hierarchy, or transformation.
- Keep pacing calm and deliberate; allow stillness around key claims.
- Favor clean reveals, route tracing, grouped movement, and purposeful camera motion.
- Avoid idle wobble, decorative particle fields, gratuitous zooms, and unrelated transitions.
- Build technical graphics as seek-safe SVG/HTML animation where practical.
- Use cel-shaded imagery for strong physical metaphors; do not force it into abstract systems explanations.
- End cards may use the wordmark; explanatory scenes should not be logo-stamped.

## Final audit

- Correct mode for the idea?
- One clear argument per output/frame/slide?
- Palette and typography exact?
- Red sparse and meaningful?
- Technical labels 1–3 words?
- No forbidden decorative AI clichés?
- Logo omitted unless it serves an identity moment?
- Fonts/assets embedded or local?
- Upstream Bento or video-framework validation still passes?
