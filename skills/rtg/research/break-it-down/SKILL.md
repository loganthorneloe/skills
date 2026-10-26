---
name: break-it-down
description: Explains complex topics from first principles with source evidence and HTML reports. Use for “break it down,” “explain from first principles,” ELI5, or requests for a simple, source-grounded explanation of a concept, article, URL, or question.
---
# Break It Down

Explain the subject in plain language with enough depth to understand how it works. Default to a Logan-styled HTML report combining connected reasoning and original source evidence. Simple means understandable, not short. Read the Gotchas before starting.

## Companion research skills

This skill depends on three sibling skills. Load each by name through the harness, or read it from this skill's parent directory (`../<name>/SKILL.md`), before the step that uses it, and follow it completely:

- `source-audit` before vetting any source in step 2;
- `find-evidence` before collecting exhibits in step 2;
- `voice` before writing any report prose in step 3.

Familiarity is not a substitute for loading them. If one cannot be found, tell the user which is missing and that it installs with `npx skills add loganthorneloe/skills --skill <name>`, then stop rather than improvising it. When delegating research to subagents, instruct them to load the same skill and return its result records.

## 1. Establish the question and available capabilities

Identify the reader's central question, prerequisites, mechanism, consequences, and important limits. Start with supplied material. Ask only when missing information materially changes the explanation; otherwise proceed with stated assumptions. Honor the requested scope and format. Short follow-ups can stay in chat.

Use available research, asset-extraction, artifact, and browser tools without requiring particular APIs. If browsing is unavailable, use supplied material and clearly separate established background from unverified current claims. Request missing material only when essential. If files or previews are unavailable, deliver complete HTML source. If rendering, scripts, or external assets are blocked, retain a readable static explanation and disclose the specific limitation. Never claim access, extraction, or testing that did not happen.

## 2. Research for understanding and evidence

Start with a handful of high-signal sources; expand until every important question has a passing or conditional source. Audit each source with `source-audit` against the claims the explanation needs, and drop failures. Then run `find-evidence` on the surviving sources to collect figures, tables, quotations, and metrics for those claims. Keep both sets of result records as working notes outside the readable report; they drive the audit section, exhibit placement, and the verification in step 6.

## 3. Build a connected explanation

Write all prose in the `voice` skill. Begin with the topic title followed by the source audit, built from the audit records. For each source, place the full linked title on the first line. Immediately below it, put the author or team first, then the publication type, venue or publisher, and date where available, together in one unlinked italic metadata line. Allow this line to wrap naturally on narrow screens. Below the metadata, write the reader-facing entry `source-audit` describes.

Source-entry header example:

[Leveraging Implicit Feedback from Deployment Data in Dialogue](https://aclanthology.org/2024.eacl-short.8/)\
*Richard Yuanzhe Pang, Stephen Roller, Kyunghyun Cho, He He, and Jason Weston · EACL short paper, Association for Computational Linguistics · March 2024*

State the direct answer after the audit, then build the explanation in prerequisite order. Place each exhibit from the evidence records beside the claim it supports, and integrate it into the argument by explaining what to notice and any limit that changes its interpretation. Explain the evidence before considering an additional generated visual or summary. Do not repeat a question–figure–summary–disclaimer formula. Link an enlarged view when figure details need it. Use worked examples only to close comprehension gaps.

## 4. Make HTML teach

Generated visuals and interactions are optional. Add one only to resolve a specific comprehension gap left by source exhibits and prose; omit toy demonstrations that merely restate the explanation. For an interaction, identify the reader-controlled input, visible consequence, and additional insight before implementation. Use native controls with lightweight JavaScript and HTML, SVG, or canvas.

Keep controls next to results, with current values, units, sensible defaults, and reset where useful. State assumptions and source empirical inputs. Do not invent measured relationships. Provide keyboard access, labels, visible focus, accessible result updates, reduced-motion support, and a readable initial state without JavaScript.

Keep definitions, explanation, evidence, caveats, and conclusions visible in the reading flow. No accordions, disclosure dropdowns, or hover-only essential text unless requested. A select may change a genuine model parameter. Prefer relevant source tables with attribution and context; use clearly labeled synthesis tables when the comparison spans sources. Choose by purpose, not a table quota.

## 5. Apply Logan styling

Use these self-contained defaults. An accessible current Logan style reference can refine them but is never required. Honor explicit design direction.

- **Typography:** Sora SemiBold 600 for headings and prominent numbers; Inter 400 for body and 500 for labels/controls; monospace for code. Apply tight heading letter spacing. Retrieve the faces through this [public font stylesheet](https://fonts.googleapis.com/css2?family=Inter:wght@400;500&family=Sora:wght@600&display=swap). External loading requires network access. For offline delivery, embed retrieved fonts and preserve their license notices; obtain licenses from the Sora and Inter directories in the [Google Fonts repository](https://github.com/google/fonts/tree/main/ofl). If retrieval is unavailable, use system sans-serif fallbacks and disclose reduced brand fidelity. Do not invent font data or assume a family declaration loads it.
- **Palette:** default light: canvas `#f5f4f0`, surface `#ffffff`, text `#101527`, muted `#646c77`, border `#cbd0d3`, blue `#2f6c9e`, green `#46734d`, red `#bf3030`. If dark is requested, use respectively `#101527`, `#1e2537`, `#f3f5f8`, `#adb4c0`, `#3e4659`, `#8db7de`, `#9ac9a2`, `#ed7777`. Never invert source figures or rely on color alone for meaning.
- **Layout:** prose around 720px wide, responsive 20–24px side padding, 16–17px body text, line height about 1.75. Let figures and interactions expand within a bounded wider area for readable labels. Use deliberate whitespace and thin structural lines. Avoid gradients, shadows, decorative backgrounds, and boxes around ordinary prose.
- **Tiles:** where grouping helps, use connected square tiles with no gutters, shared single 1px hairline borders, about 24px padding, and content-driven heights. Stack in reading order on narrow screens. Keep headings inside the padding above their content. No colored top bars, border-straddling labels, decorative tabs, or floating headings.
- **Details:** headings above content; omit obligatory logos, eyebrows, slogans, and footer strips. A red period is optional on the title, not subheadings. Body links are heavier and underlined with red hover/focus treatment. Give external text links a small red arrow hidden from assistive technology; internal actions need none. Keep source figures' own styling intact.

## 6. Verify and deliver

Prefer one HTML file with embedded CSS and only necessary JavaScript. Embed retrieved assets when feasible; otherwise use verified public asset URLs and disclose network dependencies. No framework, server, build pipeline, or personal path is required. Self-contained instructions do not imply that every output asset is offline.

Before delivery:

1. Run the `voice` revision pass. Check that prose connects prerequisites, mechanism, evidence, and implications without requiring links.
2. Match every claim to a passing or conditional audit record. Reconcile the evidence records with the report; repair omissions caused by stopping early or avoiding extraction.
3. Inspect desktop and narrow rendering for clipping, unreadable figures, broken assets, and brand drift. Verify loaded font faces and weights; computed font-family names alone are insufficient.
4. Operate every control at default, changed, and boundary states. Check results against its stated logic, keyboard use, focus, and static fallback. Fix observed defects and repeat affected checks.

Deliver the actual file or supported artifact with a usable link, or complete HTML source when neither is available. Briefly state material access and verification gaps. Do not describe unperformed checks as passed.

## Gotchas

- A theme toggle, accordion, or sortable table alone is not an interactive explanation.
- Never use ASCII art, Unicode box drawings, or text-based flowcharts; use rendered graphics.
- Loading a companion skill is required, not optional context. Skipping `source-audit` or `find-evidence` produces unvetted sources and paraphrased exhibits.
