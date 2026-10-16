---
name: break-it-down
description: Explains complex topics from first principles with source evidence and interactive HTML. Use for “break it down,” “explain from first principles,” ELI5, or requests for a simple, source-grounded explanation of a concept, article, URL, or question.
---
# Break It Down

Explain the subject in plain language with enough depth to understand how it works. Default to a Logan-styled HTML report combining connected reasoning, original source evidence, and purposeful interactions. Simple means understandable, not short. All instructions are here; no companion files, installed skills, local assets, or particular provider are required. Read the Gotchas before starting.

## 1. Establish the question and available capabilities

Identify the reader's central question, prerequisites, mechanism, consequences, and important limits. Start with supplied material. Ask only when missing information materially changes the explanation; otherwise proceed with stated assumptions. Honor the requested scope and format. Short follow-ups can stay in chat.

Use available research, asset-extraction, artifact, and browser tools without requiring particular APIs. If browsing is unavailable, use supplied material and clearly separate established background from unverified current claims. Request missing material only when essential. If files or previews are unavailable, deliver complete HTML source. If rendering, scripts, or external assets are blocked, retain a readable static explanation and disclose the specific limitation. Never claim access, extraction, or testing that did not happen.

## 2. Research for understanding and evidence

Start with a handful of high-signal sources; expand until important questions are supported. Prefer primary research, foundational texts, established domain educators, and practitioners with firsthand evidence. Vet relevance, methods, and currentness rather than treating institutional prestige as proof. Read relevant full sections, methods, results, figures, and captions. Snippets and abstracts alone rarely support a complete explanation.

For each source, establish what it demonstrates, how, and under which conditions. Distinguish findings, author interpretation, and your synthesis. Inspect its figures, charts, diagrams, tables, metrics, and precise quotations. Keep brief working notes of useful exhibits, locators, the question each answers, and why a valuable candidate was omitted. These notes need no separate file and stay outside the readable report.

Display useful original figures beside the claims they support. Obtain source-provided images or vectors; otherwise extract or render the relevant PDF region. When HTML omits a figure, check the original PDF or supplements. Preserve axes, legends, labels, proportions, colors, and necessary caption context. Inspect extraction for clipping and readability. Link an enlarged view when details need it. Respect reuse and quotation limits; explain specific access or rights gaps.

Include multiple exhibits when they teach different things. One image, one metric, and one quote are not a completion target. Do not stop while useful evidence remains unexamined, or force irrelevant exhibits to meet a quota. Quotes should preserve consequential definitions, arguments, or limitations. Numbers need units, denominators, populations, time periods, and comparison conditions. Keep source links and exact locators with the evidence.

## 3. Build a connected explanation

Begin with the topic title followed by the source audit. For each source, place the full linked title on the first line. Immediately below it, put the author or team first, then the publication type, venue or publisher, and date where available, together in one unlinked italic metadata line. Allow this line to wrap naturally on narrow screens.

Put the explanatory prose below the metadata. Explain the author's relevant expertise or firsthand access, what the work actually establishes, which part you use, and its important limits. Use enough sentences to make this intelligible to someone who recognizes none of the names. Verify credentials. Explain why older work still applies and which historical results say nothing about present performance. Author-year labels and “foundational research” alone are insufficient.

Source-entry layout example; adapt the content to the actual source:

[Leveraging Implicit Feedback from Deployment Data in Dialogue](https://aclanthology.org/2024.eacl-short.8/)\
*Richard Yuanzhe Pang, Stephen Roller, Kyunghyun Cho, He He, and Jason Weston · EACL short paper, Association for Computational Linguistics · March 2024*

The authors, affiliated with Meta FAIR and NYU, trained response-ranking models using deployed BlenderBot conversations. Their experiments show how the chosen feedback signal changes generated responses. This informs the discussion of feedback proxies, while leaving tool-execution accuracy untested.

State the direct answer after the audit. Define unfamiliar terms, establish the components and constraints, and explain step by step how their interactions produce the result. Address what, how, why, and when the conclusion changes. Preserve intermediate reasoning and useful qualifications without padding or a word ceiling. Never use analogies or metaphors.

Introduce the question each exhibit answers, show it, then explain what to notice and what it does not establish. Attribution or a caption alone is not analysis. Use worked examples only to close comprehension gaps. Label original diagrams, simulations, calculations, and constructed data separately from published observations. They supplement source evidence.

## 4. Make HTML teach

Design a substantive interaction around a relationship the reader needs to understand. Identify its question, reader-controlled input, visible consequence, and lesson before implementation. Use native controls with lightweight JavaScript and HTML, SVG, or canvas. Choose the form for the concept; do not recycle one widget universally. If no interaction adds understanding, use a clear static visual.

Keep controls next to results, with current values, units, sensible defaults, and reset where useful. State assumptions and source empirical inputs. Do not invent measured relationships. Provide keyboard access, labels, visible focus, accessible result updates, reduced-motion support, and a readable initial state without JavaScript.

Keep definitions, explanation, evidence, caveats, and conclusions visible in the reading flow. No accordions, disclosure dropdowns, or hover-only essential text unless requested. A select may change a genuine model parameter. Use tables for comparing common attributes or inspecting precise values; use prose for reasoning and visual models for mechanisms.

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

1. Check that the answer, prerequisites, mechanism, conditions, and implications are explained without following links or opening hidden text.
2. Confirm that unfamiliar readers can understand each source's identity, contribution, and limits. Match claims to full source material. Reconcile useful exhibit candidates with the report; repair omissions caused by stopping early or avoiding extraction.
3. Inspect desktop and narrow rendering for clipping, unreadable figures, broken assets, and brand drift. Verify loaded font faces and weights; computed font-family names alone are insufficient.
4. Operate every control at default, changed, and boundary states. Check results against its stated logic, keyboard use, focus, and static fallback. Fix observed defects and repeat affected checks.

Deliver the actual file or supported artifact with a usable link, or complete HTML source when neither is available. Briefly state material access and verification gaps. Do not describe unperformed checks as passed.

## Gotchas

- ELI5 must preserve depth. Short sentences can carry a comprehensive explanation.
- A source link, prose summary, or generated replacement does not substitute for an available, useful original figure.
- A theme toggle, accordion, or sortable table alone is not an interactive explanation.
- A proxy does not establish a hidden state or causal effect. Explain what was measured and its limits.
- Never use ASCII art, Unicode box drawings, or text-based flowcharts; use rendered graphics.
