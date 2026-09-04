---
name: research
description: 'Load when the user says "research this AI topic", "do technical research", "investigate this engineering concept", "write a research brief", or requests an engineering investigation of an AI system, model architecture, or infrastructure pattern.'
---

# Technical Research Skill

Conduct exhaustive technical research on engineering concepts in AI grounded for software engineers.

Produce publication-ready, source-first research briefs that succeed on the first run. The brief must get the premise correct upfront, explain foundational mechanisms from the ground up, deliver high-density takeaways on every bullet, and anchor every technical claim in recent, verified primary sources.

Write the research brief directly to a topic-named file in the workspace root, using `[topic-slug].md`.

## 1. Frame the Concrete Premise

1. Identify the core technical reality and the immediate engineering bottleneck.
2. Quantify real operational pain upfront by specifying where latency spikes, where GPU clusters stall, where memory exhausts, or where security boundaries break.
3. Detail why obvious workarounds fail, demonstrating the trade-offs.
4. State the concrete architectural resolution that solves the bottleneck.
5. Use nested sub-bullets in the premise to establish empirical evidence, benchmark degradation numbers, or operational cost multipliers.
6. Answer directly why a software engineer must understand this topic right now.

Criterion. Premise establishes quantified operational pain, why naive solutions fail, and the architectural fix using sub-bullets.

## 2. Discover and Qualify Sources

Read [references/sourcing-rubric.md](references/sourcing-rubric.md) and enforce its hierarchy.

1. Locate 3 to 5 Tier 1 primary sources including lab technical reports, conference papers from NeurIPS, ICML, MLSys, and USENIX, first-party docs, CVE records, or pull requests.
2. Enforce recency. Prioritize sources from the past 1 to 2 years. Foundational papers are permitted only when their architectural mechanism remains actively deployed without change.
3. Verify live links. Confirm every URL resolves cleanly and points directly to the cited documentation or paper.
4. Deep link. Link directly to specific anchors, chapters, sub-pages, or line ranges containing the cited information.
5. Pull essential findings, proven benchmarks, and direct quotes directly into high-density bullets under each source. Do not use rigid meta-labels or schemas.

Criterion. At least 3 Tier 1 sources from the past 1 to 2 years with deep links and verified quotes.

## 3. Build Ground-Up Concept Progression

1. Target a software engineer with systems foundations but no specialized machine learning background.
2. Introduce physical hardware and memory constraints before explaining higher-level algorithms.
3. Define intermediate mathematical and software structures before describing optimizations.
4. Explain causal mechanics step by step, detailing what triggers each state transition, what executes under the hood, and why failure occurs.
5. Every bullet point must communicate an important, actionable engineering insight, trade-off, or architectural invariant. Never include generic filler.
6. Zero shrug sections. Every body section must contain dense technical specifics like named kernel calls, data structures, algorithms, benchmarks, or vulnerability records backed by inline citations.

Criterion. Reader understands foundational mechanics before advanced behaviors; every bullet delivers an actionable takeaway.

## 4. Draft the Source-First Brief

Read [references/brief-template.md](references/brief-template.md) for the required layout.

1. Name every section header after the specific technical topic. Never use generic meta-labels like Problem Statement.
2. Place the Sources section immediately after the premise under the clean header `## Sources`.
3. Weave exact quotes and numerical metrics into the body sections as linked supporting evidence.
4. Every technical claim, metric, formula, CVE, or mechanism in every section must feature an inline markdown link to a verified primary source.
5. Conclude with a concise Summary section capturing core engineering invariants and architectural trade-offs.

Criterion. Brief renders as valid Markdown at `[topic-slug].md` with sources first and inline citations across all sections.

## 5. Formatting and Proof Gates

Enforce strict formatting constraints throughout all output text.

* Zero colons rule. Never use a colon anywhere in headings, bullet labels, or prose notes. Colons are permissible only inside verified markdown link protocol prefixes like https.
* Zero parentheses rule. Never use parentheses in prose notes. Rewrite sentences smoothly with commas or periods. Parentheses are strictly reserved for markdown link syntax.
* Zero em dashes. Use commas, periods, or hyphens instead.
* Zero buzzwords. Eliminate words like game-changing, delve, tapestry, landscape, revolutionize, crucial, and foster.
* Zero metaphors. Describe systems using literal software and hardware primitives rather than figurative analogies.
* Company capitalization. Ensure company names are capitalized accurately, such as xAI using lowercase x and uppercase AI.

Verify all items in the pre-flight checklist in [references/brief-template.md](references/brief-template.md) before final output.

## Hard Exit

Verify each condition before concluding.
* The report file exists at `[topic-slug].md` in the workspace root.
* The premise contains quantified operational pain with nested sub-bullets.
* Every conceptual section contains dense technical specifics with inline citations.
* Zero colons exist outside https links.
* Zero parentheses exist outside markdown links.
* Zero em dashes or marketing buzzwords appear in the brief.
* The brief concludes with a high-signal Summary section.
