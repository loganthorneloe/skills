---
name: break-it-down
description: "Load when the user says \"break it down\", \"explain from first principles\", \"ELI5\", or asks for a simple, source-grounded explanation of a concept, article, URL, or question. Defaults to a simple HTML report with portable Logan styling."
---
# Break It Down

Explain complex concepts, articles, and phenomena across any domain simply from first principles. Rely on foundational truths, real source visuals, and concrete evidence rather than metaphors. This skill is independent of the AI provider, model, tools, and topic; use the capabilities available in the current environment.

## Core Principles

1. **High-Signal Source Selection:**
   - If the user provides a URL or text, use that as the primary source.
   - Aim for about five high-signal sources in total, including any supplied source. Use fewer when sufficient; do not add sources just to reach a count. Prioritize primary research and foundational texts, organizations or practitioners operating at the forefront of the field, and respected domain educators known for rigorous, deep-dive explanations.
   - Avoid SEO content farms, shallow aggregator articles, and unvetted preprints or random blogs lacking established domain credibility.

2. **Upfront Source Audit:**
   - Before explaining the topic, briefly introduce the selected sources at the very top. For each source, state the author or institution, why they are a credible authority or educator in this domain, and a one-sentence summary of the specific mechanism, fact, or data point being pulled from their work.

3. **First Principles over Metaphors:**
   - Never use analogies or metaphors.
   - State the direct answer in the opening sentence immediately following the source audit.
   - Build the explanation bottom-up: establish the baseline physical, biological, economic, or logical constraints, identify the irreducible building blocks, and trace step-by-step how they interact to produce the phenomenon.

4. **Mandatory Source Visuals & Evidence (Zero ASCII Art):**
   - You MUST pull and display real visual figures, diagrams, charts, illustrations, concrete metrics, and direct quotes from the source material in every response.
   - Never generate ASCII art, Unicode box drawings, or text-based flowcharts. Rely strictly on actual visual assets from the sources.

## Output report

By default, deliver the explanation as a simple HTML report using Logan Brand. Read the bundled [Web reports](references/web-reports.md) for self-contained styling and delivery guidance; no separate brand skill, local checkout, or proprietary tool is required. Return a brief chat summary and the HTML report as a file or supported artifact; if neither is available, provide the complete HTML source. Honor an explicitly requested alternative format; short follow-up questions may be answered in chat without regenerating the report.
