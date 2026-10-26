---
name: source-audit
description: Audits research sources for relevance, credibility, method, currentness, and limits, then returns per-claim pass, conditional, or fail verdicts in a structured record. Use when vetting papers, articles, reports, documentation, or URLs before relying on them, or when a research or explanation task needs to decide which sources to trust and how to describe them.
---
# Source Audit

Decide whether each source can support the claims a task needs, and record why in a form another agent or a reader can use. A source can pass for one claim and fail for another, so verdicts are per claim. Read the Gotchas before starting.

## 1. Number the claims

Break the question into numbered claims (C1, C2, …), each specific enough to check. Cover every part of the question with as many claims as it needs. "How much?" becomes a claim about a named measure, such as an effect size or percentage-point difference. If the question assumes something the sources reject (for example, that lab "massed" study equals real cramming), say so in the gaps list. Take claims from the calling agent when it supplies them, and keep its numbering so other skills can refer to the same IDs. Ask only when no claim can be inferred.

## 2. Read the source, not its surface

Open the full source and read the sections that bear on the claims, including methods, results, figures, captions, and stated limitations. Abstracts, snippets, search summaries, and citing articles rarely establish what a source shows. For a preprint or living document, check the version history and note the version read.

If the canonical page is blocked, use an authoritative mirror (publisher PDF, PubMed Central, Europe PMC, author copy) and record it. A fetch tool's summary is not the source; count it as a partial read. If no PDF tool is installed, use any available renderer or text extractor, or install a portable one in a temporary environment; if that fails, record the gap. For long documents, reading only the sections that cover the claims is acceptable and recorded as partial.

## 3. Evaluate

Answer each from the source, verifying author and venue claims against the document or an independent record rather than assuming them.

1. Identify the author or team, publication type, venue or publisher, and date. For undated living pages, record the access date.
2. Establish relevant expertise or firsthand access: primary research, direct practice, original data, or an established teaching record. Institutional prestige alone is not evidence. When the author is anonymous or pseudonymous, judge the work by whether its claims check out against the primary sources it cites.
3. Determine what the work demonstrates, how (method, data, sample, setup), and under which conditions. Separate findings from the author's interpretation.
4. Check that the method can support each claim. A proxy does not establish a hidden state; correlation does not establish a causal effect.
5. Judge currentness: which findings endure and which historical results no longer describe present performance, versions, or practice.
6. Note conflicts of interest, internal inconsistencies, and contradicting evidence found while reading. Run one targeted search per source for retractions, errata, or failed replications of its claims. Spot-check only the cited numbers a verdict rests on against their primary sources, and record what was checked in `limits`. Do not audit a source's whole citation list.
7. Identify the specific sections to rely on and the limits that change how each claim may be stated.

## 4. Decide per claim

Mark a claim `pass` when the source is relevant, credible for it, and its method supports the intended use. Mark it `conditional` when usable only with a stated restriction, such as a narrower claim, historical framing, an unverifiable author, or corroboration from another source. Mark it `fail` when the source is irrelevant to it, its substance cannot be checked, its method cannot support it, or it is superseded or untrustworthy. A partial read can still pass if the sections read fully cover the claim.

Prefer primary research, foundational texts, established domain educators, and practitioners with firsthand evidence. When a failing source is the only one for a claim, fail it and report the gap rather than lowering the bar.

## 5. Return results

Return agent records unless the caller asks for reader-facing entries. Mark any inferred, unverified value inline with `(unverified)`.

```markdown
### <Full title>
- url: <canonical link>; text read from: <mirror or same>
- byline: <author or team> · <publication type> · <venue or publisher> · <date or "undated, accessed <date>">
- verdicts: C1 pass; C2 conditional (<restriction>); C3 fail (<reason>)
- use: <sections, figures, tables, or pages to rely on>
- credibility: <verified expertise or firsthand access, in a sentence or two>
- contribution: <what it establishes, how, and under which conditions>
- limits: <limits, inconsistencies, and conditions that change the conclusion>
- read: full | partial (<what was read, skimmed, or not read>) · version <id if any> · via <access route if not the canonical page>
```

Then a gaps list, one line each: `- C<n>: <no passing source | only conditional sources | inaccessible source | unresolved conflict | disputed premise> — <detail>`.

For reader-facing entries, omit failed sources. For each remaining source, explain why it is useful and trustworthy to someone who recognizes none of the names, covering credibility, contribution, and consequential limits, and state any conditional restriction where it applies. These are coverage requirements, not a sentence template.

## Gotchas

- "Foundational research," author-year labels, or a famous venue do not explain credibility. Say what the authors did or saw.
- A citation count or prestige signal is not a method check.
- Older work can still be correct. Explain why it applies, not merely that it is old or new.
- A secondary source that misquotes its primary source (for example, a confidence bound reported as the effect) fails for that claim even if the rest is sound.
- Never claim to have read a section, verified a credential, or checked currentness without doing it.
