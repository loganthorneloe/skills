---
name: source-audit
description: Audits research sources for relevance, credibility, method, currentness, and limits, then returns a pass, conditional, or fail verdict with a structured record. Use when vetting papers, articles, reports, documentation, or URLs before relying on them, or when a research or explanation task needs to decide which sources to trust and how to describe them.
---
# Source Audit

Decide whether each source can support the claims a task needs, and record why in a form another agent or a reader can use. Audit against the specific question being answered; a source can pass for one claim and fail for another. Read the Gotchas before starting.

## 1. Fix the question

State the question or claims the source must support. Without this, relevance cannot be judged. If auditing for another agent, take the question from its request; ask only when none can be inferred.

## 2. Read the source, not its surface

Open the full source. Read the sections that bear on the question, including methods, results, figures, captions, and stated limitations. Abstracts, snippets, search summaries, and citing articles rarely establish what a source actually shows. If full text is unavailable, say so and audit only what was read.

## 3. Evaluate

Answer each of these from the source itself, verifying claims about authors and venue rather than assuming them.

1. Identify the author or team, publication type, venue or publisher, and date.
2. Establish whether the author has relevant expertise or firsthand access: primary research, direct practice, original data, or an established record teaching the subject. Institutional prestige alone is not evidence.
3. Determine what the work demonstrates, how (method, data, sample, setup), and under which conditions. Separate its findings from the author's interpretation.
4. Check that the method can support the claim. A proxy does not establish a hidden state, and correlation does not establish a causal effect.
5. Judge currentness. Explain which findings endure and which historical results no longer describe present performance, versions, or practice.
6. Note conflicts of interest, retractions, errata, or contradicting stronger evidence found while reading.
7. Identify the specific part of the source the task should use and the limits that change how it may be stated.

## 4. Decide

Mark a source `pass` when it is relevant, credible for the claim, and its method supports the intended use. Mark it `conditional` when it is usable only with a stated restriction, such as a narrower claim, historical framing, or corroboration from another source. Mark it `fail` when it is irrelevant, unverifiable, methodologically unable to support the claim, superseded, or untrustworthy.

Prefer primary research, foundational texts, established domain educators, and practitioners with firsthand evidence. When a failing source is the only one available for a claim, fail it and report the gap rather than lowering the bar.

## 5. Return results

Return one record per audited source, in this shape, to the user or calling agent:

```markdown
### <Full title>
- url: <link>
- byline: <author or team> · <publication type> · <venue or publisher> · <date>
- verdict: pass | conditional | fail
- supports: <the claims or question this source can support>
- use: <section, figure, table, or page to rely on>
- credibility: <verified expertise or firsthand access, in a sentence or two>
- contribution: <what it establishes, how, and under which conditions>
- limits: <limits and conditions that change the conclusion>
- read: full text | partial (<what was unavailable>)
```

After the records, list unresolved gaps: claims with no passing source, and sources that could not be accessed. Do not report a field as verified when it was inferred.

When presenting an audit to readers rather than an agent, turn each record into a short entry that explains why the source is useful and trustworthy to someone who recognizes none of the names, covering its credibility, contribution, and consequential limits. These are coverage requirements, not a sentence template.

## Gotchas

- "Foundational research," author-year labels, or a famous venue do not explain credibility. Say what the authors did or saw.
- A citation count or prestige signal is not a method check.
- Older work can still be correct. Explain why it applies, not merely that it is old or new.
- Never claim to have read a section, verified a credential, or checked currentness without doing it.
