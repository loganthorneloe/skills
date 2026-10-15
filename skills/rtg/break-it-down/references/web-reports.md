# Web reports

Read before composing an HTML report. Use the core skill's source audit, depth, and evidence requirements. HTML is an explanatory medium: use its visual and interactive capabilities to help the reader understand relationships, not merely to format a document.

## Logan typography and styling

The bundled assets and rules are sufficient without a separate brand skill, personal checkout, account, or font download. An available current brand kit can refine them. Honor explicit user design direction.

### Load the actual fonts

- Use **Sora SemiBold, weight 600**, for headings and prominent numbers, with tight letter spacing. Use **Inter 400** for body text and **Inter 500** for labels and controls. Use a readable monospace face for code.
- Copy [the bundled fonts stylesheet](../assets/fonts.css) and its sibling `fonts/` directory into the report assets, or embed the font files with equivalent `@font-face` rules for a single-file report. Keep the Sora and Inter OFL licenses with distributed font files; include their notices in the HTML when embedding fonts.
- The stylesheet declares font faces; the report must also apply Sora to headings/numbers and Inter to body/controls. Font-family names without loaded assets are insufficient. Do not substitute system fonts to avoid bundling available fonts.
- Keep system fallbacks for loading failures. Verify that the declared font faces actually load and that rendered headings use Sora 600. A computed CSS font-family string alone does not prove this. If the delivery environment prevents font loading, disclose degraded typography.

### Palette

Default to light. Define semantic CSS variables using the following values. Use the dark column only when requested or useful to the destination. Never invert source figures.

| Role | Light | Dark |
| --- | --- | --- |
| Canvas | `#f5f4f0` | `#101527` |
| Surface | `#ffffff` | `#1e2537` |
| Main text | `#101527` | `#f3f5f8` |
| Secondary text | `#646c77` | `#adb4c0` |
| Hairline border | `#cbd0d3` | `#3e4659` |
| Blue accent | `#2f6c9e` | `#8db7de` |
| Green accent | `#46734d` | `#9ac9a2` |
| Red accent | `#bf3030` | `#ed7777` |

### Composition

- Keep prose around 720px wide with responsive 20–24px side padding, 16–17px body text, and line height around 1.75. Let figures and interactive explanations use a wider bounded area when their labels or relationships need it. Do not squeeze every visual into the prose column.
- Use warm paper, ink text, thin structural lines, near-square surfaces, deliberate whitespace, and consistent spacing. Avoid gradients, decorative backgrounds, shadows, and dashboard cards around ordinary paragraphs.
- Place short headings above their content. Omit obligatory logos, eyebrow labels, slogans, generic subtitles, and footer strips. A red terminal period is optional on the main title, not required on subheadings. Keep substantive text in the main text color.
- Make body links visibly heavier and underlined, with red hover/focus treatment and visible keyboard-focus outlines. Use a small red external-link arrow only for external text destinations, hidden from assistive technology. Internal actions and downloads need no decorative arrow.
- Give important metrics Sora numerals plus the units, conditions, and comparison needed to interpret them. Color must not be the only carrier of meaning. Retain category distinctions even when additional chart colors are needed.
- Preserve source images, labels, colors, proportions, and attribution. Add the report's styling around them. Provide an enlarged view or full-resolution link when fine details cannot be read at report width, and explain the important details in the visible text.

## Design the explanation in HTML

### Use interaction to teach

For a full report, actively design a substantive interactive explanation around a relationship the reader needs to understand. Prefer a manipulable model, a process that can be inspected step by step, or a comparison whose relevant differences are made visible. Use appropriate native controls and lightweight JavaScript with HTML, SVG, or canvas. The topic determines the form; do not reuse one widget for every report.

Before implementing it, identify the question the interaction answers, what the reader controls, what visibly changes, and what they should learn. If changing the control teaches nothing beyond the prose, redesign or omit it. When the subject genuinely offers no useful interaction, use a clear static explanatory visual rather than adding decorative controls. A short fact or follow-up need not become an interactive report.

Keep controls next to their consequences. Show current values, meaningful units, a clear default state, and a reset when useful. Explain assumptions and provenance alongside the visual. Do not invent empirical relationships to make a simulation work. Label constructed data and calculations clearly, and link the source of empirical inputs. Source findings and interactive illustrations must remain distinguishable.

### Keep the reading path open

Keep definitions, explanation, quotations, evidence interpretation, caveats, and technical detail visible in the normal reading flow. Do not use `<details>`, accordions, or disclosure dropdowns to hide report content unless the user explicitly requests that treatment. A select control may choose an actual model parameter when appropriate; it must not become a container for prose. No hover-only explanations of essential information.

The page should explain the subject before the reader touches a control. Interaction deepens that understanding. Provide a static initial view and readable explanation if JavaScript is unavailable. Respect reduced motion, label controls, support keyboard use, and expose changing results accessibly.

### Choose tables deliberately

Use tables when readers need to compare the same attributes across multiple items or inspect precise values. Use connected prose for reasoning and visual models for mechanisms. Do not turn every list, conceptual distinction, or sequence into a table. Review repeated tables together: each must offer a comparison that would be harder to understand in another form. A sortable table is useful only when sorting helps answer a real question.

## Evidence placement and depth

Plan the explanation and evidence together before coding. Each major section should advance understanding and resolve its subquestion, not simply name a category. Allow enough space for definitions, intermediate causal steps, conditions, and implications. Short sentences can support a long, comprehensive explanation.

For every retained source exhibit, make its purpose explicit in the surrounding prose: what question it answers, what the reader should notice, how that supports the explanation, and which limits matter. Read the complete caption and relevant methods. Preserve original figures as evidence; original diagrams and interactions can explain or extend them, with separate attribution. Do not replace a revealing source figure with a generic generated graphic or insert irrelevant evidence to meet a quota.

Quotes should preserve a precise definition, consequential argument, or useful limitation in the author's own words. Metrics should quantify something the reader needs to understand. A large number without its denominator, comparison, or measurement conditions is incomplete. Be selective without stripping away the evidence needed for depth.

## Packaging and verification

Prefer portable HTML with embedded CSS and only the JavaScript needed for the explanation. No framework, server, or build pipeline is required. Bundle fonts, licenses, and source assets with relative paths, or embed them for single-file delivery. Avoid personal filesystem dependencies. If an asset requires the network, disclose that rather than claiming offline availability.

Before delivery, check:

1. **Understanding.** The direct answer, prerequisites, mechanism, important conditions, and implications are explained. Major questions are answered, not deferred to links or hidden content.
2. **Evidence.** Source claims and interpretations match the full material. Every quote, number, and figure has a clear role and nearby attribution. Constructed visuals are labeled. Important source findings were not skipped for brevity.
3. **Typography.** Font files load successfully, the Sora 600 and Inter faces are loaded, and heading/body styles use the intended faces and weights. Inspect the rendered result, not only the CSS.
4. **Visual layout.** Inspect desktop and narrow layouts. Text, controls, images, legends, and labels remain readable without clipping. All packaged assets resolve. Test each delivered theme.
5. **Interaction.** Operate each control. Check its default, changed, and boundary states against the stated calculation or logic. Verify keyboard access, visible focus, meaningful result updates, and a readable noninteractive view.

Fix failed checks and repeat affected checks. Report checks that the environment cannot support. Deliver the actual file or artifact with a brief summary and working link. Keep validation fixtures and maintenance notes outside the installable skill.
