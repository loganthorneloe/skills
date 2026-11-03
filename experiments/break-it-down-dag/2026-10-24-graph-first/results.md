# Graph-first refinement: experiment complete; candidate not adopted

Twelve independent graph-generation runs across five topics, two independent quality evaluators, and a separate benchmark-scope audit. The final repair passes **2/4** semantic audits. It still fails the predeclared adoption gate. Canonical Break It Down and the installed DAG version remain byte-for-byte unchanged from the start of this follow-up.

[Open comparison viewer](index.html) · [Dimensional comparison](evaluation/dimensional-comparison.md) · [Repair audit](repair/review.md)

## Results

| Phase | Scope | Accepted |
|---|---|---:|
| Current DAG instructions | Four matched topics | 0/4 |
| First candidate | Same four topics and source packets | 1/4 |
| Focused repair | Three failed topics regenerated + new held-out hash-table topic | 2/4 |

The repair is a separate single-arm test with a fresh evaluator and prospectively corrected scope criteria. These counts are not a controlled improvement estimate across phases.

| Repaired topic | Verdict | Material remaining defect |
|---|---|---|
| AI application evals | Needs repair | Checks resulting records but fails to teach the initial → authorized expected change → actual outcome comparison, including relevant action history. A preexisting refund can still appear successful. |
| Transaction isolation | Accepted with scoped extensions | No material defect found. Guarded-update recipes were honestly omitted; explaining retries does not require that separate remedy. |
| Bayesian spam | Needs repair | `dependence → calibration` makes a duplicated-word illustration mandatory for understanding model limits. Keep the example, remove/relabel the prerequisite edge. |
| Hash tables | Accepted | All lookup, collision, resizing and performance-limit probes reconstructable. |

## What changed across dimensions

The first matched comparison improved **dependency validity on two topics** and **granularity on three**. It improved coverage and application scores on **none**. Evals lost beginner bridges despite cleaner edges. Evidence alignment and research-history scores were unchanged. See the [independent dimension-by-dimension analysis](evaluation/dimensional-comparison.md) for regression versus held-out slices and exact scores.

The focused repair retained all non-DAG skill text. It audits each dependency against the child answer's actual claim, separates given inputs from their estimation and guarantees from mechanisms, and tests unfamiliar cases plus counterexamples. This corrected several earlier problems, but self-audits still missed an action-state foundation and a false example-as-prerequisite edge. **Inference:** explicit semantic review remains necessary; these results do not establish that another prompt-only refinement will reliably solve it.

## Fairness and limits

The first benchmark overrequired action-policy costs for a probability question and applied a guarded-update obligation too broadly. A separate agent audited only prompts/rubric. Original results and hashes remain frozen; a [scope sensitivity analysis](evaluation/scope-sensitivity.md) changes no original overall verdict. The repair used [versioned criteria](repair/benchmark-v1.1.json), frozen before generation. The new hash-table topic was hidden from its instruction designer.

Two notes leaked original condition labels, so the first review was only partially blinded. The repair evaluator saw no earlier outputs or scores. One run per condition/topic, shared model family, shared source packets, variable supplemental research, and different evaluators across phases limit inference. No human-comprehension study or full-report rerun occurred. Saved states support revision checks, not private thought chronology.

## Artifacts and verification

- [Current snapshot](inputs/old-skill.txt), [first candidate](inputs/new-skill.txt), [focused repair](repair/skill.txt), [repair diff](repair/instruction-change.diff).
- Actual initial/final graphs, node answers, evidence, edge reasons, research records and readable SVG/HTML are linked in the viewer.
- [Original independent audit](evaluation/blind-review.md), [structured results](evaluation/results.json), [repaired structured results](repair/results.json).
- All **12/12 structural checks pass**; structural validity is not semantic acceptance.
- Both candidate skill validators pass, all non-DAG text is identical, every version stays within 3,000 estimated tokens, and the personal harness has one resolving DAG skill link. [Validation record](validation.json).
- Desktop/mobile graph viewer checked; labels retain fixed size and graph scrolling stays contained. [Visual checks](qa/graph-view-checks.json).

No installed skill change, branch, commit, PR or publication. The original report experiment is preserved. The bounded repair round is complete; further refinement remains unproven.
