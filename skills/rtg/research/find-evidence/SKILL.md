---
name: find-evidence
description: Finds and extracts supporting evidence from sources, including original figures, tables, exact quotations, and reported metrics, with locators and the context needed to use them faithfully. Use when a claim, report, or explanation needs source exhibits, when pulling a chart or quote from a paper or page, or when another agent needs evidence returned for specific claims.
---
# Find Evidence

Pull the strongest original exhibits from sources that show, in the source's own terms, why a claim holds. Evidence is what the source itself presents; a paraphrase or regenerated chart is not a substitute when the original is available and useful. Read the Gotchas before starting.

## 1. List the claims

Number the claims that need support (C1, C2, …). When a calling agent or a `source-audit` result already numbered them, reuse those IDs. Each exhibit must support, qualify, or give needed context for one of them. If a source has not been audited, audit it with the `source-audit` skill when available and return those records in their own section before the exhibits; otherwise mark the source unaudited.

## 2. Survey each source

Read the relevant full sections, not only the abstract. Inspect figures, charts, diagrams, tables, reported metrics, and precise wording. If an audit already read the source, survey from those notes and reopen only what you need. Note each useful candidate's locator, claim, and what it shows.

When numbers disagree within a source or across versions, compare versions (for example arXiv v1 against the latest) and record the conflict in the exhibit's limits.

## 3. Choose exhibits

Select exhibits that teach different things. Include several when each adds something; one image, one metric, and one quote are not a completion target, and irrelevant exhibits should not be forced in to fill a quota. Stop when every claim has its strongest available support or a recorded gap. Look beyond the given sources only when the caller asks.

- Use a figure, chart, or diagram when it shows a relationship, trend, or mechanism better than words.
- Use a source table when readers need to compare shared attributes or precise values.
- Use a short exact quotation when wording matters, such as a consequential definition, argument, or stated limitation.
- Use a metric when a number carries the claim. Record its unit, denominator, population, time period, and comparison condition.

## 4. Extract faithfully

1. Get the original asset first: publisher figure files, supplements, or the source bundle (for arXiv, the e-print TeX source contains the authors' image files). Otherwise render the relevant PDF region. When an HTML version omits a figure, check the PDF or supplements. If no PDF tool is installed, install a portable one in a temporary environment or record the gap.
2. To crop, render the full page, locate the caption and the figure or table edges, then crop with a margin. Confirm every row, axis, legend, and label is inside the crop.
3. Preserve axes, legends, labels, proportions, colors, and caption context. Never invert, recolor, or crop away meaning.
4. Open each extracted image and check it for clipping, blur, and legibility. Keep a full-resolution version for an enlarged view.
5. For a key table, return both a rendered image and the transcribed values. A table may be rebuilt as HTML with attribution only when its values match the source exactly.
6. Copy quotations exactly and keep them short; use ellipses only where omission does not change meaning.
7. Follow the source's stated reuse terms. When copies of a source (publisher, repository, PubMed Central) carry different terms, use the most permissive copy. When none are stated, attribute the exhibit, record "rights unstated," and let the caller decide whether to embed or link.

Generated visuals, calculations, and constructed data may supplement source exhibits; return them as type `generated` and never mix them with published observations.

## 5. Return results

Return one record per exhibit to the user or calling agent:

```markdown
### E<n>: <short title>
- claim: <claim IDs> (support | qualify | context)
- type: figure | table | quote | metric | generated (combine with + when needed, e.g. metric+quote)
- source: <title> — <url> (version <id if any>)
- locator: <figure/table number, page, section, or timestamp>
- asset: <local path or URL of the extracted image or table data; exact text for quotes; value with unit and conditions for metrics>
- inspected: <what was checked, e.g. "opened at full size, all rows and legend visible"> | not applicable
- notice: <what the reader should see in it and why it supports the claim>
- limits: <conditions, conflicts, or caveats that change its interpretation>
- rights: <stated terms, or "rights unstated">
```

Then list claims still lacking evidence and useful candidates omitted or not extracted, each with its reason. Never report an extraction or inspection that did not happen.

## Gotchas

- A source link, prose summary, or regenerated chart does not substitute for an available, useful original figure.
- A caption restated is not analysis. The `notice` field must say what to look at and why it matters.
- Numbers without units, denominators, populations, or conditions mislead. Keep them attached.
- A proxy metric does not establish a hidden state or causal effect. Say what was measured.
- Guessed crop bounds clip table rows. Always reopen the crop.
