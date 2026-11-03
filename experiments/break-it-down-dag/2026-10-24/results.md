# Break It Down DAG pilot

The DAG approach produced small, mixed report gains and an inspectable research record. It is not ready to replace the current skill: graph validity did not guarantee true prerequisites or complete evidence support. Keep the new skill experimental.

## Report results

Four topics, eight distinct generation agents, one independent evaluator. Report labels were concealed until all report scores were saved; graph inspection happened afterward. One generation per condition/topic.

| Topic | Baseline /45 | DAG /45 | Preference |
| --- | ---: | ---: | --- |
| AI evals | 44 | 44 | Tie |
| Causal inference | 42 | 44 | DAG |
| Public-key encryption | 43 | 44 | DAG |
| Database isolation | 44 | 43 | Baseline |

**Aggregate: 175/180 DAG, 173/180 baseline.** This is a descriptive sum of ordinal ratings, not a statistically established advantage. Encryption improved the explanation of the inverse operation, with denser reading. Causal inference more explicitly separated random assignment from representative sampling; some gain also came from preserving a source figure. Isolation was a conceptual tie, with the baseline winning on mobile scrolling cues. Evals had complementary strengths and tied.

## Slices across reports

Means across four topics, 1–5. Delta is DAG minus baseline.

| Dimension | Baseline | DAG | Delta |
| --- | ---: | ---: | ---: |
| Prerequisite coverage | 4.75 | 5.00 | +0.25 |
| Conceptual continuity | 4.75 | 5.00 | +0.25 |
| Mechanistic depth | 4.75 | 5.00 | +0.25 |
| Evidence for foundations | 5.00 | 5.00 | +0.00 |
| Accuracy | 5.00 | 5.00 | +0.00 |
| Transfer to a new case | 5.00 | 5.00 | +0.00 |
| Source/exhibit quality | 5.00 | 5.00 | +0.00 |
| Readability | 4.25 | 4.00 | -0.25 |
| Presentation | 4.75 | 4.75 | +0.00 |

Foundation-evidence scores tied at the ceiling. This pilot therefore did not demonstrate the hoped-for improvement in source support for foundational concepts. The slight conceptual gains are useful examples, but coarse scores and a strong baseline limit what can be inferred.

The reports averaged 2,216 baseline versus 2,079 DAG reading words (approximately 6% fewer for DAG). Length is descriptive, not a quality proxy. Source choices, effort, and latency were not controlled; no reliable cost or speed comparison is available. See [output metrics](output-metrics.json).

## Graph findings

All four graphs pass structural checks: encryption 11 nodes/13 edges, isolation 13/19, evals 10/11, causal inference 9/12. They preserve initial graphs and research revisions. The independent audit found edges that encode reading order rather than necessity, and nodes marked supported whose evidence is partial. Structural PASS is not a conceptual PASS.

| Graph dimension (1–5) | Evals | Causal | Encryption | Isolation |
| --- | ---: | ---: | ---: | ---: |
| Reader fit | 4 | 4 | 4 | 4 |
| Prerequisite completeness | 4 | 3 | 3 | 4 |
| Edge necessity/direction | 3 | 3 | 2 | 2 |
| Granularity | 3 | 3 | 3 | 3 |
| Evidence alignment | 3 | 3 | 3 | 3 |
| Research trace | 4 | 2 | 3 | 4 |
| Realization in the report | 4 | 4 | 4 | 4 |

The important failures are concrete:

- **False or reversed prerequisites:** isolation's `levels → serial` reverses the definition needed to understand the guarantee. Encryption's `bits → mod` makes file representation necessary for understanding remainders.
- **Overstated support:** isolation's `practice` cites locking for an answer also asserting conditional updates and whole retries; causal's `assignment` points to passages assuming adherence instead of the chapter that explains assignment versus actual use.
- **Graph/prose mismatch:** the reports often supply omitted foundations or a better teaching order. The causal report's improved sampling distinction is missing as an explicit graph prerequisite. The graph cannot be credited with causing every report improvement.
- **Unreliable history:** encryption's successive snapshots are indistinguishable despite claimed changes; causal duplicates two rounds three times. All graphs have recorded revisions, but the fidelity varies.
- **Audit usability:** rendered nodes/edges match JSON, but labels shrink to roughly 4–8 CSS pixels on mobile. These evaluated renderings are preserved, not silently repaired.

The independent evaluator recommends optional experimentation, not mandatory adoption. The next candidate should test strict edge necessity, separate optional/scope relationships from prerequisites, retain partial/gap status until evidence explains the complete answer, and save actual intermediate states or exact deltas. These are proposed repairs, not validated improvements. Full node-specific findings and minimal repairs: [graph audit](evaluation/graph-evaluation.md).

## Experimental boundary and limitations

- Current skill and its pre-existing uncommitted edits preserved byte-for-byte. New source: `skills/wip/break-it-down-dag/SKILL.md`; registered in WIP listings and linked into the personal Codex skill directory with no duplicate frontmatter names in the checked roots.
- The only instructional edits are the research workflow and removal of one illustrative source-audit example to fit the required 3,000-token self-contained budget. Name/WIP metadata differ. All remaining text is identical. The example removal is a small non-DAG confound; [exact diff](skill-change.diff).
- Four paired outputs, one inherited model configuration, one evaluator, no repeated seeds, no human comprehension tests. Scores cluster near the ceiling. Different search results, research effort, examples and presentation can change the outcome. This cannot isolate graph structure from added research effort.
- The evaluator derived correct transfer answers from every report; that does not show that a novice would do so unaided. No consequential factual error was found in checked claims, which is not exhaustive factual certification.
- SQL was not run against a live database, and the eval starters did not test a live model. The initial textbook access limitation was resolved during the graph phase by retrieving the full author-hosted PDF; frozen report scores were unchanged. Verification limits are recorded in run/evaluation notes.
- Evaluated artifacts and blind scores are frozen. Proposed repairs have not been silently applied to the scored version.

## Validation and review

Repository validator **PASS** at 3,000 estimated tokens; creator validator **valid**; eight actual researched executions; all four graph structural checks **PASS**. Desktop/mobile and applicable control checks are recorded for all reports. Hash checks confirm canonical skill, variant, reports and blind scores are unchanged. Full commands and limits: [validation](validation.md).

Comparison page **PASS** at 1440px and 390px: all local links resolve, all four topic choices select the expected report pair, keyboard type-ahead works, eight report links remain available without JavaScript, and no page overflow or script errors were found. Desktop and fresh-context mobile screenshots inspected. Final `git diff --check` is clean.

[Open side-by-side review](index.html) · [Blind report evaluation](evaluation/report-evaluation.md) · [Graph evaluation](evaluation/graph-evaluation.md) · [Frozen protocol](protocol.md) · [Unblinded scores](scores-unblinded.json)
