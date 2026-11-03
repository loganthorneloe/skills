# Post-freeze scope addendum: I7 / IA3

Date: 2026-10-24. Benchmark: `1.0-frozen`.

Inputs: only the frozen `design/benchmark/benchmark.json` and `design/benchmark/rubric.md`. No candidate instructions, generated outputs, scores, repair files, or protocol files were read. This addendum changes no benchmark or result.

## Clarification of the earlier audit

The earlier audit’s description of I7/IA3 as correctly conditional was too generous to the frozen wording. It expressed a defensible applicability rule, but did not clearly distinguish that rule from the broader exemption actually written into v1.0.

I7’s alternatives say: “If practical remedies are entirely outside the graph's declared explanatory scope, mark this as an application extension, not a core omission; if offered as a remedy it must be explained correctly.” IA3 says: “extension if practical remedies explicitly excluded.” The rubric allows scoped-extension status only when the benchmark explicitly permits it.

Consequently, **v1.0 does not clearly permit exempting guarded UPDATE solely because that particular remedy is absent.** A graph explaining serialization retries has not entirely excluded practical remedies. Under the frozen benchmark’s strict applicability rule, its omission of guarded UPDATE/result handling can therefore be treated as an I7/IA3 gap. The narrower exemption recommended below must not be silently substituted into original-v1.0 scoring.

## Task alignment

**Explaining serialization retries does not, by itself, justify requiring a separate guarded UPDATE/result-count lesson for the actual user request.**

The request asks why concurrent, individually correct operations can produce a wrong result and how isolation levels help. Retrying a rejected transaction explains how an application can recover while respecting an isolation guarantee: fresh reads and recomputation are necessary to that explanation. Guarded relative UPDATE offers a different, bounded remedy for a particular stale read/write pattern. Understanding the former does not require learning the latter’s conditional mutation semantics or affected-row handling.

This distinction is reinforced by I8’s alternatives: “Definitions, one bounded remedy and tradeoffs suffice; all remedies must not inherit every other remedy's prerequisites.” Making *any* practical remedy trigger I7 imports a second remedy’s lesson into an otherwise sufficient explanatory route. Basic SQL familiarity does not resolve the scope issue: it neither supplies engine-specific concurrent UPDATE behavior nor turns every SQL remedy into requested content.

The appropriate conclusion is a **benchmark applicability defect**, not a claim that I7/IA3 are bad questions. They are valid tests when a guarded-update remedy is actually taught or relied upon.

## Recommended prospective rule

In a versioned amendment:

- Apply I7 and IA3 when the explanation offers, recommends, demonstrates, or relies on a guarded relative UPDATE (or an equivalent conditional single-statement mutation) as its remedy. Require the absolute-versus-relative distinction, failure/no-row handling, rule limits, and support for any engine/level-specific semantics claimed.
- Permit scoped-extension status when that remedy is absent and not needed to support the explanation’s claims. Merely discussing locking, serialization failures, or whole-transaction retries does not activate I7/IA3.
- Keep I8/IA4’s appropriate recomputation requirement when retrying a serialization failure is discussed. Do not confuse omission of guarded UPDATE with an incorrect retry explanation.
- Continue evaluating broad or false claims on their merits. If a submission claims that a remedy works universally, it must justify or narrow that claim; extension status cannot shield included misinformation.

Keep original-v1.0 results identifiable. Any reanalysis should report the changed applicability decisions explicitly and retain independent factual, dependency, support, and process findings. A future prompt could instead expressly request both serialization retry and a single-statement SQL remedy if both are intended as mandatory coverage.
