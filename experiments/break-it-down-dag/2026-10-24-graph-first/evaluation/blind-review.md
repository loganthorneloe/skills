# Independent graph-only review — frozen rubric v1.0

Original scores, prior to any scope amendment. Evaluated only released blind packages, their supplied evidence/history, frozen benchmark/rubric, and relevant primary pages. All eight structures pass; 224 edges individually classified in `results.json`. Semantic outcome: **one accepted, seven need repair**. No score averages determine acceptance.

Dimensions: reader fit / coverage / edges / granularity / evidence / history / application. Scores are ordinal, not interval measurements.

| Group | Graph | Dimensions | Overall |
|---|---|---|---|
| Regression | evals-A | 4 / 3 / 5 / 4 / 5 / 4 / 3 | Needs repair |
| Regression | evals-B | 5 / 3 / 3 / 3 / 5 / 4 / 3 | Needs repair |
| Regression | isolation-A | 5 / 3 / 3 / 3 / 5 / 4 / 3 | Needs repair |
| Regression | isolation-B | 5 / 3 / 3 / 3 / 5 / 4 / 3 | Needs repair |
| Held-out | backpropagation-A | 5 / 5 / 3 / 3 / 5 / 4 / 5 | Needs repair |
| Held-out | backpropagation-B | 5 / 5 / 4 / 5 / 5 / 4 / 5 | Accepted |
| Held-out | bayesian_spam-A | 5 / 3 / 3 / 4 / 5 / 4 / 3 | Needs repair |
| Held-out | bayesian_spam-B | 5 / 3 / 3 / 3 / 5 / 4 / 3 | Needs repair |

## Regression pairs

**Evals:** A has cleaner dependencies but leaves “application configuration” unexplained, omits the explicit case-versus-attempt distinction, and scopes test-set overfitting controls out of a frozen core obligation. Its answer-focused starter receives the E8 action-extension exception; this is a scope interpretation, not credit for action evaluation. B provides explicit configuration, repeated-attempt, held-out-case and subgroup lessons. However, its included action branch never teaches comparing controlled initial state with the requested authorized transition: a preexisting or wrong refund remains unaddressed. `outcome→run` also makes action-specific knowledge mandatory for ordinary answer runs. `run→grade` confuses producing/recording an output with understanding how an available output is judged. Both support first execution without a previous version; neither is penalized merely for discussing later improvement.

**Isolation:** Both reconstruct shared-rule violations, stable snapshots, serial equivalence and whole-transaction retries. A's `snapshot→levels` imports implementation knowledge into a guarantee table; `atomicity→interference` adds an all-or-nothing lesson not needed by its actual disjoint-write explanation. B separates the atomicity contrast correctly, but `read_committed→levels` claims the child uses statement-level visibility when its answer does not. `repeatable_read→levels` bundles a relevant phantom guarantee with unnecessary snapshot/update/retry mechanics. Both include practical remedies/retries, so the frozen I7 exemption for *entirely excluded* practical remedies does not apply. A lacks guarded-update reasoning; B explains PostgreSQL UPDATE rechecking but omits affected-row handling and the full stale-absolute versus guarded-relative contrast. IA3 fails/partially passes respectively; IA1, IA2 and IA4 pass for both.

## Held-out pairs

**Backpropagation:** Both teach local sensitivity, multiplication along paths, addition across paths, saved forward values, backward computation and separate optimizer updates. All four transfer probes pass. Independent numerical recalculation reproduces both gradients and updated losses; finite-difference errors remain below 1e-8. A's single material defect is `local_rules→chain`: a bundled square/ReLU/loss lesson is made prerequisite to a generic factors-a-and-b explanation that only needs sensitivity and arithmetic. B separates local rules from the generic chain concept and qualifies ReLU requirements to its worked architecture. Its missing explicit `reverse→training` link is minor: both lessons are present and joined at the target. A's `reverse→gradient` is defensible because that question specifically asks what the completed backward pass provides; it is not a generic definition-to-algorithm reversal.

**Bayesian spam:** Both correctly explain denominators, 90 true/990 false flags, 1/12 posterior, fixed-rate base changes and word evidence. B adds an especially explicit general two-clue rule and independent-versus-duplicate example; A's conditional-independence definition still permits the duplicate-clue inference. Neither teaches probability-versus-action costs/thresholds, so both receive original P8/PA4 penalties. Independently, both require learning/estimating word probabilities before combining given probabilities (`training→word_scores`, `learn→scores`). Their actual score answers work with stipulated values; B's training node additionally bundles smoothing and alternative feature models. Move estimation to an optional branch.

## Evidence and history

All package-manifest hashes and original observed-snapshot hashes match. Snapshots substantiate the listed node/answer/edge changes; duplicate initial files and declared no-change rounds receive no extra research credit. Original arithmetic is separated from published methods. Relevant packet passages support material factual claims; supplemental ReLU, autograd convention, calibration, MVCC, UPDATE rechecking, eval holdouts and environment-isolation sections were checked against primary pages. No established fabricated evidence or revision history was found.

Process validation is limited: saved-state observations establish file states, not private reasoning or exact retrieval chronology. Raw retrieval transcripts are absent. A score of 4 reflects that limit, not a finding of fabrication. All arithmetic and integrity checks are recorded in `independent-checks.json`; common rendering is unscored.

Blinding was imperfect. Schemas/narratives expose workflow differences, and isolation-A/backpropagation-A notes explicitly say “old skill snapshot.” These accidental exposures were reported immediately; packages remained unchanged, no assignments or other condition identities were inspected or inferred. One run per topic and an artifact transfer audit cannot establish causal improvement or human-learning gains.

## Benchmark-scope note, separate from original scoring

The Bayesian user asks about conditional/base-rate reasoning and words as clues, without asking whether to delete mail. A probability-versus-certainty caveat is relevant, but mistake-cost thresholds are an adjacent useful application lesson rather than necessary to answer that literal request. Frozen P8/PA4 nevertheless require them, so their penalties remain in the original results. Any correction must be separately versioned.

Similarly, frozen I7 makes a guarded-update lesson required whenever practical remedies are not entirely excluded. Including retries can therefore trigger a separate SQL remedy beyond the user's general isolation question. This concern does not change the frozen I7 results. I6/IA1 is less consequential here: both graphs voluntarily explain snapshots and disjoint-write anomalies, and both pass those obligations.
