# Research Brief Template and Verification Guide

Use this reference to structure topic research briefs and verify them before finalization.

## Document Template

```markdown
# Topic Title

## Premise
* Direct statement of fundamental technical reality with inline citation [Source](https://example.com/source-one)
  * Immediate engineering problem with concrete metrics or operational pain
  * Why the obvious or naive workaround fails with inline citation [Source](https://example.com/source-two)
  * The concrete engineering takeaway that solves the problem

## Sources

* [Source Title](https://example.com/source-one)
  * Key architecture finding or core discovery
  * Direct metric or benchmark proven by the source
  * Verifiable quote capturing technical insight

* [Source Title](https://example.com/source-two)
  * Key architecture finding or core discovery
  * Direct metric or benchmark proven by the source
  * Verifiable quote capturing technical insight

## Topic-Named Concept 1 Ground-Up Foundation
* Base mechanism explained simply
  * Why this mechanism exists with deep-linked citation [Source](https://example.com/source-one)
  * What it actually does step by step with deep-linked citation [Source](https://example.com/source-one)
  * Direct metric or quote proving the behavior with deep-linked citation [Source](https://example.com/source-one)
  * Key engineering takeaway with deep-linked citation [Source](https://example.com/source-one)

## Topic-Named Concept 2 Inner Mechanics
* Detailed system or algorithm behavior
  * How the underlying data structure, kernel interface, or math functions with deep-linked citation [Source](https://example.com/source-two)
  * Direct metric or quote demonstrating throughput or memory scaling with deep-linked citation [Source](https://example.com/source-two)
  * Key engineering takeaway with deep-linked citation [Source](https://example.com/source-two)

## Topic-Named Concept 3 Real-World Invalidation and Traps
* Trigger or failure scenario
  * Why this happens under the hood with deep-linked citation [Source](https://example.com/source-two)
  * Exact quote or metric showing the consequence with deep-linked citation [Source](https://example.com/source-two)
  * How to architecturally fix or prevent it with deep-linked citation [Source](https://example.com/source-two)
  * Key engineering takeaway with deep-linked citation [Source](https://example.com/source-two)

## Summary
* Core engineering invariant or mental model takeaway
* Primary architectural trade-off or mitigation takeaway
```

## Pre-Flight Verification Checklist
Before saving and presenting the research brief, verify every item.

1. Premise establishes concrete operational pain with quantified metrics and failure modes.
2. Foundational primitives are explained from the ground up so any software engineer understands the premise.
3. Every single bullet delivers an actionable engineering takeaway without fluff.
4. Sources are recent from the past 1 to 2 years, or seminal foundational architectures actively deployed in modern stacks.
5. Sources section appears immediately after the premise at the top of the file without meta-schemas.
6. Deep links to specific anchors or sub-pages are used whenever available.
7. Zero shrug sections. All body sections contain dense technical specifics like named syscalls, algorithms, or benchmarks backed by inline links.
8. Supporting quotes and numerical metrics are woven directly into the body sections as linked evidence.
9. Every technical bullet has an inline citation to a verified primary source.
10. A concise Summary section concludes the brief.
11. Zero colons anywhere in headings, bullet labels, or prose notes.
12. Zero parentheses anywhere in prose notes.
13. Zero em dashes.
14. Zero AI buzzwords.
15. Zero metaphors or analogies.
16. All company names capitalized properly such that xAI uses lowercase x and uppercase AI.
17. Written directly to topic-named file in the workspace root.
