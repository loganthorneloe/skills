---
name: find-evidence
description: Finds and extracts supporting evidence from sources, including original figures, tables, exact quotations, and reported metrics, with locators and the context needed to use them faithfully. Use when a claim, report, or explanation needs source exhibits, when pulling a chart or quote from a paper or page, or when another agent needs evidence returned for specific claims.
---
# Find Evidence

Pull the strongest original exhibits from sources that show, in the source's own terms, why a claim holds. Evidence is what the source itself presents; a paraphrase or regenerated chart is not a substitute when the original is available and useful. Read the Gotchas before starting.

## 1. List the claims

Write the claims or questions that need support. Each exhibit must answer one of them. If a source has not been vetted, audit it first with the `source-audit` skill when available; otherwise note that the source is unaudited.

## 2. Survey each source

Read the relevant full sections, not only the abstract. Inspect its figures, charts, diagrams, tables, reported metrics, and precise wording. For each useful candidate, keep a brief working note of its locator, the claim it answers, and what it shows. Also note valuable candidates you decide to omit, with the reason. These notes stay out of any reader-facing output.

## 3. Choose exhibits

Select exhibits that teach different things. Include several when each adds something; one image, one metric, and one quote are not a completion target, and irrelevant exhibits should not be forced in to fill a quota. Do not stop while useful evidence remains unexamined.

- Use a figure, chart, or diagram when it shows a relationship, trend, or mechanism better than words.
- Use a source table when readers need to compare shared attributes or precise values.
- Use a short exact quotation when wording matters, such as a consequential definition, argument, or stated limitation.
- Use a metric when a number carries the claim. Record its unit, denominator, population, time period, and comparison condition.

## 4. Extract faithfully

1. Obtain the source-provided image or vector first. Otherwise extract or render the relevant PDF region. When an HTML version omits a figure, check the original PDF or supplements.
2. Preserve axes, legends, labels, proportions, colors, and the caption context needed to read it. Never invert, recolor, or crop away meaning.
3. Inspect each extraction for clipping, blur, and legibility. Where details are small, keep a full-resolution version for an enlarged view.
4. Copy quotations exactly, with ellipses only where omission does not change meaning.
5. Respect reuse and quotation limits. When access or rights block an exhibit, record the specific gap instead of substituting a fabricated version.

Generated visuals, calculations, and constructed data may supplement source exhibits, but label them as original work and keep them separate from published observations.

## 5. Return results

Return one record per exhibit to the user or calling agent:

```markdown
### E<n>: <short title>
- claim: <claim or question it supports>
- type: figure | table | quote | metric
- source: <title> — <url>
- locator: <figure/table number, page, section, or timestamp>
- asset: <local path or source URL of the extracted image or table; exact text for quotes; value with unit and conditions for metrics>
- notice: <what the reader should see in it and why it supports the claim>
- limits: <conditions or caveats that change its interpretation>
- rights: <reuse status or access gap, if any>
```

After the records, list claims that still lack evidence and useful candidates that could not be extracted, with reasons. Never report an extraction or inspection that did not happen.

## Gotchas

- A source link, prose summary, or regenerated chart does not substitute for an available, useful original figure.
- A caption restated is not analysis. The `notice` field must say what to look at and why it matters.
- Numbers without units, denominators, populations, or conditions mislead. Keep them attached.
- A proxy metric does not establish a hidden state or causal effect. Say what was measured.
