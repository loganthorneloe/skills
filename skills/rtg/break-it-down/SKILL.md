---
name: break-it-down
description: 'Load when the user says "break it down", "explain from first principles", "ELI5", or asks for a simple, source-grounded explanation of a concept, article, URL, or question.'
---
# Break It Down

Explain complex subjects from first principles in plain language, with enough depth to understand how they work. Default to a Logan-branded HTML report combining connected explanation, purposeful source evidence, and custom visual interactions. Remain independent of provider, model, tools, and topic.

## 1. Establish what needs explaining

- Identify the central question, prerequisite concepts, mechanism, consequences, and important limits. Use the user's supplied source as the starting point when present.
- Simple means understandable, not short or shallow. Reduce assumed knowledge and explain unfamiliar terms. Do not remove causal steps, qualifications, or useful evidence to make the report brief. Scale length to the subject, without padding or a fixed word limit.
- Before composing HTML, read [Web reports](references/web-reports.md), including its typography, interaction, and verification requirements. Read the Gotchas below before research and design.

## 2. Read for understanding and evidence

- Start with about five high-signal sources. Use fewer when sufficient and more when important questions remain unsupported. Prefer primary research, foundational texts, established domain educators, and practitioners with direct evidence. Reject shallow aggregators and unvetted claims.
- Read the relevant full sections, methods, results, figures, and captions. Search snippets and abstracts alone rarely support a comprehensive breakdown. Follow a source's important evidence rather than stopping after finding a quotable sentence.
- For each major explanatory point, identify what the source establishes, how it establishes it, and what remains uncertain. Distinguish findings, author interpretation, and your synthesis.
- Collect original figures, useful metrics, and short direct quotations as you read. Choose each because it answers a reader's question, exposes a mechanism, quantifies an effect, or clarifies a limitation. Do not satisfy an evidence quota with decorative images, incidental numbers, or generic advice quotes.
- Preserve attribution, source links, locators, units, populations, time periods, and comparison conditions. Respect quotation and reuse limits. If valuable evidence is inaccessible, disclose the specific gap instead of inventing it.

## 3. Build the explanation

- Put a compact source audit at the top. Identify each author or institution, why it is credible for this question, and the specific contribution being used. Keep it visible and proportional to the report.
- State the direct answer immediately after the audit. Establish the basic constraints and components, then explain step by step how their interactions produce the result. Never use analogies or metaphors.
- Develop a connected argument, not a catalog of labels or recommendations. Explain what each concept is, how it works, why it matters, and when the conclusion changes. Address the important subquestions before ending.
- Integrate source visuals, metrics, and quotations beside the explanations they support. Introduce the question, show the evidence, and explain what to notice and what it does not establish. A caption or source link alone is not analysis. Display original source visuals rather than merely linking to them.
- Use worked examples where they resolve a comprehension gap. Clearly distinguish constructed examples, simulations, calculations, and original explanatory graphics from published observations. Original visuals supplement source evidence rather than replacing it.

## 4. Compose and verify the report

- Use the bundled fonts and presentation guidance. Build custom HTML/SVG/canvas explanations and meaningful interaction where readers can inspect a process, comparison, or change. Choose the form for the concept rather than defaulting to tables.
- Keep the complete explanation visible. Do not hide definitions, evidence, technical depth, or concluding material in dropdowns or accordions. An interaction should reveal a relationship through changed state, not merely reveal a paragraph.
- Verify completeness, evidence relevance, actual font loading, rendering, and interaction behavior using the Web reports checks. Fix observed defects before delivery. If a check is unavailable, state the precise verification gap without claiming it passed.
- Deliver the HTML file or supported artifact with a brief summary and usable link. If neither is available, provide complete HTML source. Honor an explicitly requested format. Short follow-ups can stay in chat without a new report or repeated evidence quota.

## Gotchas

- A font-family declaration does not load a font. System fallback is a degraded state, not completed Logan branding.
- ELI5 does not mean a compressed overview. Explain the full mechanism in accessible steps.
- Source-only evidence does not forbid original explanatory graphics or interactive models. Label their provenance and assumptions.
- A theme toggle, accordion, or sortable table alone does not make an interactive explanation. Preserve useful tables for genuine comparisons, not ordinary prose.
- Do not infer a hidden state or causal effect from a proxy without the necessary evidence. Explain the measurement and its limits.
- Never generate ASCII art, Unicode box drawings, or text-based flowcharts. Use real source images and rendered graphics.
