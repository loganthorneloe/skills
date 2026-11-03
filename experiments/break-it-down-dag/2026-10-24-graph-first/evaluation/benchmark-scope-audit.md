# Post-freeze benchmark scope audit

Audit date: 2026-10-24. Audited version: `1.0-frozen`.

Inputs read: **only** `design/benchmark/benchmark.json` and `design/benchmark/rubric.md`. No generated graphs, scores, candidate instructions, assignments, or prior experiment artifacts were inspected. This note evaluates task alignment, not any submission. The frozen inputs are unchanged.

## Finding

The benchmark mostly tests mechanisms needed by its actual requests and novice baselines. **Bayesian P8 bundles a legitimate interpretation limit with an optional decision-policy extension. PA4 makes the extension mandatory.** Explaining why a flag is not almost certainly spam requires conditional/base-rate reasoning; it does not require explaining how deletion thresholds depend on mistake costs. The word “classification” does not override the prompt’s specific questions about conditional probabilities and word clues.

A second, narrower issue is the snapshot/write-skew requirement: I6 contains conditional language, but IA1 is unconditional and the rubric permits exemptions only for expressly marked extensions. A small accurate isolation-level explanation need not choose snapshot isolation or a disjoint-write example. The benchmark should resolve that inconsistency prospectively.

These findings do **not** excuse false claims in included optional material, invalid prerequisite edges, missing novice bridges, or omission of a core mechanism. They do not prescribe a graph, node count, vocabulary, source list, or teaching order.

## Decision rule

A must-have answers the stated question, supplies a bridge the declared reader needs to understand that answer, or bounds a claim the answer actually makes. An optional extension addresses a further question whose absence leaves the requested explanation intact. A correct caveat can be useful without becoming a prerequisite. Material introduced by a chosen example must be explained even when another example could avoid it.

The rubric correctly applies this distinction to edges and says to judge depth against the question rather than a textbook syllabus. Its coverage rule, however, allows “Scoped extension” only where the benchmark explicitly permits it. Consequently, a scope error in an essential-question entry becomes an acceptance error: missing core coverage or a material lesson needed for a core application probe is a hard failure.

## Obligation-by-obligation review

### AI application evals

Request: why evals are needed, how they work, and how to start evaluating a customer-support assistant. Reader: small Python programs and model API calls; no ML, AI engineering, or statistics.

| ID | Scope judgment | Reason |
|---|---|---|
| E1 | Core | Intended tasks, success criteria, and plausible-versus-correct output are what make an evaluation meaningful. |
| E2 | Core | The reader needs to know what constitutes a case and which application configuration is being tested. Tools/retrieval/state apply only if present, as written. |
| E3 | Core | Comparing observable output against criteria is the judging mechanism. A basic check on grader mistakes is needed to interpret its results; a grader taxonomy is correctly optional. |
| E4 | Core | Recorded cases, outputs, conditions, and failure inspection make the requested first evaluation interpretable. The nondeterminism qualification prevents a false promise. |
| E5 | Core at the stated intuitive depth | Repeating one case and covering different support situations answer different questions. This distinction is a small necessary bridge to meaningful coverage, not a statistics course. |
| E6 | Core | A score’s scope and limitations explain what an eval actually tells the user. The benchmark appropriately does not require interval formulas. |
| E7 | Core as a basic workflow | Inspecting failures and comparing changes fairly explains how evals help improve the assistant. Detailed maintenance systems are optional; a short account of consistent comparisons and overfitting to familiar cases is justified. |
| E8 | Conditional, correctly marked | A support assistant need not perform actions. If actions are included, starting state, authorized outcomes, and relevant history are necessary to establish that the claimed action happened. |

Applications: **EA1, EA3, EA4 are aligned core probes** of coverage, fair comparison, and starting from scratch. **EA2 is a valid conditional probe**, and its explicit exemption for answer-only scope is appropriate. Nothing here requires turning action-specific knowledge into a prerequisite for ordinary answer judging.

### Transaction isolation

Request: why individually correct operations can give a wrong concurrent result and how isolation levels help. Reader: basic SQL SELECT/UPDATE; no database internals.

| ID | Scope judgment | Reason |
|---|---|---|
| I1 | Core | Grouping, commit/rollback, and the distinction between atomicity and isolation prevent a central category mistake. No implementation internals are necessary. |
| I2 | Core | A concrete interleaving supplies the mechanism behind the requested failure. |
| I3 | Core | “Wrong result” must be defined by an application rule; otherwise the example cannot establish why individually valid work conflicts. |
| I4 | Core | Serial equivalence explains the strongest guarantee and distinguishes an outcome property from literal one-at-a-time execution. Correct transactions remain a necessary premise. |
| I5 | Core at its stated modest depth | Some comparison of weaker guarantees and serializability is explicitly requested. Concrete observation/outcome differences are appropriate; exhaustive anomaly tables and universal engine claims are not. |
| I6 | Conditional route; marking needs repair | A snapshot explanation needs visibility semantics and an adequate account of any claimed anomaly. But snapshots and disjoint-write skew are not necessary foundations for every explanation of isolation levels. The minimum’s “if that behavior is discussed” conflicts with treating the entire entry as unconditional core. |
| I7 | Conditional, correctly marked | A guarded relative UPDATE is a practical remedy beyond the minimum conceptual request. If offered, its difference from a stale absolute write, result handling, and engine/rule limits must be correct. |
| I8 | Core as bounded enforcement/tradeoff explanation; details conditional | Explaining protection or rejected unsafe overlap connects guarantees to how they help. If abort/retry is used, fresh reads and recomputation are essential. A separate implementation lesson on every locking or detection scheme is not required, and the alternatives correctly permit a bounded remedy. |

Applications: **IA2 is aligned core**: serializable is neither literal isolation in time nor a repair for wrong application logic. **IA3 is properly conditional** on practical remedies. **IA4 is a defensible basic operational probe** of a serialization failure: merely replaying the stale decision undermines the mechanism the reader is learning. No exhaustive external-side-effect treatment should be added to it.

**IA1 is valid and useful for a snapshot/write-skew explanation, but too specific as an unavoidable pass gate for this request.** A reader can understand interleaving, atomicity versus isolation, weaker read guarantees, serial equivalence, and a bounded enforcement mechanism without yet learning snapshot visibility and a cross-row anomaly. I5’s requested distinction between stable repeated reads and serial equivalence does not uniquely require snapshot isolation or write skew. The audit recommends conditional applicability for IA1, not weakening the correctness expected when a submission discusses stable snapshots or makes broad claims that they prevent incompatible decisions.

### Backpropagation

Request: how a small network determines each weight’s contribution to prediction error, how that helps learning, with traceable tiny-example arithmetic. Reader: arithmetic/basic Python, no calculus; benchmark additionally names variables/functions, which are consistent with a basic Python explanation but should still receive ordinary contextual definitions.

| ID | Scope judgment | Reason |
|---|---|---|
| B1 | Core | Inputs, adjustable weights, intermediate values, and a forward calculation establish the object whose sensitivity is sought. |
| B2 | Core | A concrete loss defines what the backward calculation measures. Prediction discrepancy, scalar loss, and sensitivity cannot be silently conflated. |
| B3 | Core | The reader lacks calculus. Meaning, sign, magnitude, and locality of a rate of change must precede meaningful use of derivative notation. |
| B4 | Core | Multiplying local sensitivities through composition is the central explanatory bridge, not optional mathematical background. |
| B5 | Core | Carrying loss sensitivity backward and reusing forward values distinguishes backpropagation from independently perturbing each parameter. |
| B6 | Core in a minimal form | Multiple contributions must add for the method to handle shared values/weights. This is part of the backpropagation mechanism, not a separate advanced architecture topic. A tiny branch or internal example is enough; a single-chain illustration alone must not imply multiplication handles every route. |
| B7 | Core | The user explicitly asks how it learns. Gradient calculation, an update, and step size connect sensitivity to learning while separating backprop from the optimizer. |
| B8 | Core as a short interpretation limit | The user’s “contributed” wording could imply blame or general importance. Local sensitivity at the present loss/input/parameters is the necessary meaning; no feature-attribution or generalization curriculum is required. |

Applications: **BA1–BA4 are aligned.** BA1 tests the requested traceable calculation; BA2 tests the explicitly requested learning connection and limits of finite steps; BA3 tests the small but essential addition-across-paths mechanism; BA4 tests what a local result establishes. None requires matrix algebra, a production architecture, advanced optimization, or statistical learning theory. The supplied BA1–BA3 arithmetic is consistent.

### Bayesian spam classification

Request: explain the 90%/10% flag rates with a 1% spam base rate, why flags are not almost certainly spam, how changing the base rate changes the answer, and how words serve as clues. Reader: percentages/arithmetic, no probability.

| ID | Scope judgment | Reason |
|---|---|---|
| P1 | Core | Identifying the group each percentage describes is the missing novice bridge and the source of the conditional reversal error. |
| P2 | Core | Starting class sizes make the base-rate effect intelligible. |
| P3 | Core | Applying rates to their own groups explains true and false flagged counts. |
| P4 | Core | Dividing flagged spam by all flags directly answers the user’s question; denominator meaning is indispensable. |
| P5 | Core | Changing the base rate with stated rates held fixed is explicitly requested. The fixed-rate assumption must be clear. A brief real-world applicability caveat is useful; a deployment-shift lesson is not required. |
| P6 | Core | Comparing word frequency across classes and combining it with the base rate is explicitly requested. A single-word example suffices. |
| P7 | Conditional, correctly marked | Multiple-clue likelihood multiplication adds an independence assumption. That assumption and correlation risk must be explained if the method is used, but neither is required for the original flag calculation or a one-word example. |
| P8 | Mixed: split warranted | “Posterior is not certainty” is directly relevant. Applicable premises bound the calculation. Choosing review/deletion thresholds from mistake costs answers a different question and is an optional downstream decision-policy extension. |

Applications:

- **PA1: core and aligned.** The frequency calculation gives 90 flagged spam and 990 flagged legitimate messages, hence 90/1,080 = 1/12 ≈ 8.33%. It tests the exact requested reversal.
- **PA2: core and aligned.** With equal starting groups and the same flagging rates, 90% of flags are spam. Naming the held-fixed rates tests the requested base-rate comparison.
- **PA3 first part: core and aligned.** Equal word frequencies in both classes leave the prior unchanged. This is a direct test of what makes a word informative. The correlated-clues part is correctly conditional on multi-clue modeling.
- **PA4: optional extension as written.** A 60% estimate does not, by itself, specify deletion. However, explaining an appropriate threshold through asymmetric mistake costs requires decision content beyond P1–P6. A fully correct conditional/base-rate and word-clue explanation can leave that content absent. Failure to teach it should not become a material core omission for this prompt.

The distinction matters even though P8 says “a brief practical caveat suffices.” Brevity reduces the cost of the extra requirement; it does not establish that the extra lesson is necessary. Conversely, if a submission claims that a particular posterior obliges deletion, or includes a cost-based policy, that claim must be assessed for correctness and support. Conditional status cannot protect a false included claim.

## Recommended versioned treatment

1. **Keep v1.0 and its original results unchanged and identifiable.** Any alternative applicability judgment belongs in a new benchmark version or clearly labeled sensitivity analysis. Do not silently turn a frozen failure into a pass.
2. **Prospective v1.1: split P8’s interpretation limit from its decision-policy extension.** Retain core probability interpretation and relevant premises; explicitly permit omission of mistake-cost thresholds and deletion policy. Make PA4 a conditional extension when the explanation includes action recommendations, or retain it as an unscored extension probe. If decision policy is intended to be core, instead expand a future user prompt to ask how the filter should choose flag/review/delete actions, then generate fresh observations against that prompt.
3. **Prospective v1.1: align I6 and IA1 applicability.** Explicitly mark snapshot/write-skew treatment conditional on that explanatory route or on claims that require it. Keep I2–I5’s core concurrency and guarantee requirements. An alternative future prompt could explicitly request why stable snapshots and disjoint writes still allow bad outcomes.
4. **Preserve the other substantive requirements.** Do not use this audit to remove local-rate meaning, additive gradient paths, denominator normalization, grader limits, fair comparisons, or transaction recomputation merely because their vocabulary is absent from the prompt. They supply mechanisms or necessary claim boundaries for the requested explanation.
5. **Report the effect, not a revised winner.** If existing results are reanalyzed, show original-v1.0 and revised-applicability verdicts together, identify exactly which omission/probe decisions changed, and retain every independent factual, edge, evidence, or process finding. This audit has not inspected results and makes no prediction about whether any overall verdict changes.
