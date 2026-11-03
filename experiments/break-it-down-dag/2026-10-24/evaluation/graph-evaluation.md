# Independent prerequisite-graph audit

Completed 24 October 2026. This is phase 2 of the exploratory pilot. The four blind report comparisons were saved before the graph associations were disclosed. Their score JSONs and `report-evaluation.md` remain frozen. This assessment evaluates the actual graphs, their recorded research, and correspondence to the reports; it does not rescore the reports or infer a production effect from the labels.

## Method and result

Read the graph rubric, DAG-specific requirements, initial/final graph records, rendered graphs, run notes, and associated reports for e02, e04, e05, and e07. Checked node IDs, endpoints, acyclicity, reachability, revision differences, explanatory source passages, report sequence, and desktop/narrow presentation. Source checking used the cited primary documents; render checks used Chromium at 1440 and 390 pixels. No evaluated files were edited. Scores use 1 = major failure, 3 = mixed/usable with substantive repair, and 5 = strong with no material issue found.

All four graphs pass structural validation. None earns a high score for prerequisite correctness. Their strongest contribution is making important questions and research gaps inspectable. Their weakest is treating a useful reading sequence as a set of necessary dependencies. Several reports explain missing prerequisites better than their graphs do.

| Graph dimension | Encryption B / e02 | Isolation A / e04 | Evals A / e05 | Causal B / e07 |
|---|---:|---:|---:|---:|
| Reader fit | 4 | 4 | 4 | 4 |
| Prerequisite completeness | 3 | 4 | 4 | 3 |
| Edge necessity/direction | 2 | 2 | 3 | 3 |
| Granularity/parsimony | 3 | 3 | 3 | 3 |
| Evidence alignment | 3 | 3 | 3 | 3 |
| Research-loop traceability | 3 | 4 | 4 | 2 |
| Synthesis realization | 4 | 4 | 4 | 4 |

These are ordinal judgments, not calibrated measurements; one-point differences should not be treated as precise effects. Graph presentation is discussed separately rather than adding an eighth dimension.

| Structural check | Encryption | Isolation | Evals | Causal |
|---|---:|---:|---:|---:|
| Nodes / edges | 11 / 13 | 13 / 19 | 10 / 11 | 9 / 12 |
| Unique IDs, valid endpoints, acyclic | Pass | Pass | Pass | Pass |
| Every node has a path to target | Pass | Pass | Pass | Pass |
| Rendered node/edge correspondence | Pass | Pass | Pass | Pass |

Every-node reachability is a graph property, not evidence that each node is conceptually necessary. Optional scope checks can reach the target because an author drew an edge. Similarly, a topological ordering can be valid while omitting an actual prerequisite.

## Encryption — e02, report B

Artifacts: [graph](../runs/e02/dag.html), [JSON](../runs/e02/dag.json), [report](../runs/e02/report.html).

**Reader fit 4; completeness 3.** The graph starts at message representation and includes the arithmetic, computational asymmetry, randomized protection, practical file encryption, and key identity that a novice needs. However, `pair` already uses “public exponent,” “product,” and “matching private exponent” without explicit prime/exponent foundations or a `mod` dependency. `hybrid` needs the symmetric-key baseline. The report supplies that missing bridge in “First, a message is already numbers”: “A shared-key, or symmetric, scheme uses the same secret key to encrypt and decrypt.” It defines primes in “Why the direction of a calculation matters.” These are successful prose repairs, not demonstrated graph completeness.

**Edge validity 2.** `bits→mod` is not necessary: a reader can understand a remainder without knowing how files become integers. `bits→secrecy` similarly overstates the representation prerequisite. The representation does matter for the RSA construction, so `bits→construction` is the smaller, defensible link. `construction→randomness` makes a particular RSA worked example necessary to understand deterministic public guessing, although the guessing argument requires only a reproducible public procedure and a small candidate-message set. `randomness→hybrid` carries an answer specifically about OAEP into a generic HPKE construction. Randomness matters to real schemes, but RSA padding is not a prerequisite for understanding hybrid encryption. These are necessity errors, not cycles.

**Granularity 3.** `mod` asks what a remainder is but also answers how to compute powers efficiently. `limits` bundles sender identification, recipient-key compromise, and message length. These are useful limits, but making the entire bundle prerequisite to the central explanation via `limits→target` confuses scope qualifications with foundations. Split only the concepts needed to fix these dependencies; there is no benefit in atomizing every mathematical term.

**Evidence alignment 3.** The RSA paper explains the calculation and includes the exact numerical example; RFC 8017 specifies public/private representations and randomized encoding. Those are substantive sources. But its octet-to-integer conversion presupposes elementary representation knowledge, and the NIST glossary does not explain all the claims in `secrecy` or the composite `target`. A relevant definition is weaker than explanatory coverage. `construction` records 17 × 157 = 2668 + 1, yet leaves the “why does that restore the input?” bridge inside the cited paper. The report itself explains remainders under both primes, including divisible inputs, in “Watch a complete numerical example.” The answer in the graph should preserve that reasoning or explicitly depend on it. [RFC 8017, §§3–5 and 7.1.1](https://www.rfc-editor.org/rfc/rfc8017.html); [RSA paper, §§VI–VIII](https://people.csail.mit.edu/rivest/Rsapaper.pdf).

The practical construction and limitations are consistent with the primary specification; the issue is how much of that explanation is represented in the nodes, not evidence of a false report claim. [RFC 9180, §§4–5 and 9](https://www.rfc-editor.org/rfc/rfc9180.html).

**Research trace 3.** The preserved initial graph has eight nodes and nine edges and matches the standalone initial file. It leaves meaningful gaps. The final graph adds `mod`, separates `randomness` and `hybrid`, and adds `limits`. However, rounds 1 and 2 contain identical node/edge snapshots, both equal to the final state, despite round 2 describing further terminology and reversibility work. Thus the final work is visible, but the intermediate sequence is not reliably preserved. This could be retrospective bookkeeping; the files cannot establish when knowledge was acquired.

The remainder explanation and distinction between raw RSA and practical schemes plausibly improve the report. The initial graph already asked about asymmetric capability, hard reversal, and identity, so subsequent sourcing of those concepts mainly demonstrates verification and elaboration rather than newly discovered prerequisites.

**Synthesis realization 4.** The report teaches message representation, symmetric keys, computational direction, modulo, the complete example, guessing, practical encryption, and identity in a coherent sequence. It supplies more mathematical explanation than `construction` and more foundational vocabulary than `pair`. The opening direct answer is an intentional preview, not a harmful ordering violation. No consequential reversal of a defensible core prerequisite was found; compliance with the graph's questionable edges would not necessarily improve the prose.

**Rendered graph.** Node and edge counts correspond to JSON. On desktop, several long curves pass behind opaque intervening boxes: `hard→pair`, `mod→construction`, `pair→identity`, and `hybrid→target`. The endpoints are correct but tracing them is difficult. At 390 pixels the scaled labels are roughly 7–8 CSS pixels. HTML questions, answers, and edge reasons provide a readable fallback.

**Smallest repairs.** Remove `bits→secrecy`; retarget `bits→mod` to the construction; add the actual arithmetic/symmetric prerequisites; separate generic randomization reasoning from its RSA application; preserve the correctness bridge in `construction`; qualify partial evidence and scope-only limits. Preserve genuine intermediate snapshots. Route edges around nodes and permit readable-width scrolling or zoom.

## Isolation — e04, report A

Artifacts: [graph](../runs/e04/dag.html), [JSON](../runs/e04/dag.json), [report](../runs/e04/report.html).

**Reader fit 4; completeness 4.** The assumed `sql` node matches the reader's basic SELECT/UPDATE knowledge. Transactions, visibility, interleaving, business rules, write skew, locks, and retries cover most of the practical problem. The largest omission is the difference between writing a stale absolute value and evaluating a conditional relative update against the current row. The report teaches this in “Express a simple change directly,” using `SET stock = stock - 1 ... AND stock > 0`, including the wait/recheck behavior and no-row result. The graph hides this important mechanism inside `practice`.

**Edge validity 2.** `levels→serial` is the clearest direction problem: interpreting the serializable guarantee in the isolation-level comparison requires knowing serial equivalence. Separate that definition from enforcement if the latter should come after the table. `skew→serial` is useful motivation, not a necessary prerequisite to the definition. `snapshot→anomalies` makes one implementation model necessary to understand dirty reads and other read phenomena. `transaction→rule` is also unnecessarily strong: an application invariant can be stated before transaction grouping. Conversely, `interleave→skew` is missing even though overlapping decisions are necessary to understand the two-doctor schedule. The rendered/topological sequence can therefore place `skew` before `interleave`; the prose sensibly does not.

**Granularity 3.** `anomalies` bundles dirty reads, nonrepeatable reads, phantoms, lost updates, and write skew. `practice` combines three different remedies. That bundling causes artificial dependencies: `retry→practice` implies retry knowledge is needed for a simple conditional statement. `serial` asks both what the guarantee means and how it is enforced, while its answer mainly gives the definition. A definition/enforcement split and three remedy branches are sufficient; a much larger graph is unnecessary.

**Evidence alignment 3.** `practice` is marked supported but cites only row-locking and deadlock sections for an answer that also includes conditional updates and whole-operation retries. The missing explanatory citations already exist elsewhere in the report: Read Committed's recheck behavior and the dedicated complete-retry guidance. [PostgreSQL 18, §13.2.1](https://www.postgresql.org/docs/18/transaction-iso.html); [§13.5](https://www.postgresql.org/docs/18/mvcc-serialization-failure-handling.html).

The anomaly table supports distinctions among read and serialization anomalies but does not explain all five failures in `anomalies`; connect the write-skew source explicitly. `snapshot` says visible committed versions without the own-writes qualification that the report correctly supplies. The two-doctor explanation has strong primary support and is a good example of explanatory, rather than merely terminological, evidence. [Ports and Grittner, §2.1.1, Figure 1](https://arxiv.org/pdf/1208.4179). The locking source supports the locking branch, not the entire selection among remedies. [PostgreSQL 18, §13.3](https://www.postgresql.org/docs/18/explicit-locking.html).

**Research trace 4.** The initial nine-node graph is preserved; the first revision answers it, and the second adds `rule`, `skew`, `locks`, and `retry` with identifiable evidence and edge changes. This is the clearest full-state revision sequence of the four. A weakness remains: `practice` was marked supported before all its distinct claims had matching evidence, and the final node still retains the narrow locking citation.

Research on invariants, disjoint-write failure, and whole-operation retry plausibly improved comprehension. In particular, the report explains why retrying only the old UPDATE retains a stale decision. The original transaction, snapshot, and level questions were already present, so their later citations demonstrate corroboration and elaboration rather than proof of prerequisite discovery.

**Synthesis realization 4.** “A worked failure” precedes snapshots and write skew; the report makes the missing interleaving relationship clear. It introduces serial equivalence in the direct answer before the table, beneficially departing from `levels→serial`. In “Three practical ways,” conditional updates and locking precede the full retry explanation, violating the bundled `retry→practice` relation but improving teaching order. These discrepancies chiefly indict the graph's granularity, not report understanding. The report also states that isolation cannot fix an application that never checks its rule.

**Rendered graph.** Thirteen nodes and nineteen edges match JSON. Dense right-margin hairpin routes make individual dependencies harder to follow than their textual edge list. Narrow scaling reduces labels to approximately 7–8 pixels; the HTML answers and edge reasons remain readable.

**Smallest repairs.** Put serial equivalence before the level table; separate enforcement; remove the unnecessary rule/snapshot/skew edges; add `interleave→skew`; split remedies and make conditional-update reasoning explicit. Attach the existing recheck/retry sources to the relevant answers, qualify own writes, and improve edge routing and mobile scale.

## Evals — e05, report A

Artifacts: [graph](../runs/e05/dag.html), [JSON](../runs/e05/dag.json), [report](../runs/e05/report.html).

**Reader fit 4; completeness 4.** `program` appropriately assumes Python and model-API familiarity. `goal→case→grader→sample→compare` captures the core progression well. `outcome` and `population` address two consequential traps: accepting a claimed action as proof and generalizing a curated score to production traffic. However, knowledge of Python does not imply understanding statistical coverage. `sample` absorbs case-versus-attempt distinctions, independent binary sampling, population selection, and grader error into one answer. The complete application under test, controlled configuration, and reset conditions are clearer in the report than in the dependency map.

**Edge validity 3.** `outcome→grader` makes record mutations and permission history prerequisites for an answer-only workflow. The report correctly labels the action-taking case as a branch in “When the assistant can take actions.” A generic observable-evidence prerequisite would work for both. `compare→workflow` is appropriate for maintenance but not necessary to start one eval run. `case→workflow` is redundant given the longer path, although not conceptually false. `population` uses case/score concepts while floating as a root; it needs either a clearer elementary question or a dependency on the case distinction. The main chain is otherwise defensible.

**Granularity 3.** `variation` merges fluency-versus-correctness with repeated-run variation. `sample` bundles several distinct inference limits. `workflow` merges first execution and ongoing comparison, creating a graph/prose mismatch. Separating those bottlenecks would be more useful than adding nodes for each checklist item.

**Evidence alignment 3.** The primary sources are relevant, but many nodes reuse the same broad dictionary of reward, limitations, grader types, and Steps 0–8. For `case`, the precise task-instance description is a better match than the repeated general reward locator. For `grader`, the calibration and grader passages matter; for execution, trial isolation matters. The underlying sources do contain useful explanations, so this is imprecise support mapping rather than fabricated evidence. [τ-bench, §3](https://arxiv.org/html/2406.12045v1); [Anthropic, grader types and Steps 2, 4–5](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).

`outcome` says “A final record proves an effect.” A final record alone is insufficient: it must be compared with a controlled starting state and the expected result. The benchmark uses expected database state; the report specifies starting records and reset conditions. The graph answer is less careful than both source and prose. The report's approximately 9.5% upper bound is correctly presented as its calculation under independent sampling from a stable population; the NIST passage supplies the statistical method, not that exact application result. [NIST, exact binomial intervals](https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm).

**Research trace 4.** The initial eight-node graph and final ten-node graph are preserved. Round 1 supplies a narrative rather than a full intermediate snapshot. The addition of `outcome` and `population` is clear, and the explicit removal of `variation→goal` as unnecessary is the strongest recorded example of reviewing edge necessity. This is genuine graph revision, not merely adding citations to an unchanged checklist. The record does not establish when the author first knew each concept.

Research about action-history failures and case-mixture limits plausibly sharpened the report. The numerical uncertainty treatment adds a specific derivation and assumptions. Core goal/case/grader/comparison questions were already in the initial graph, so the sources there chiefly document and elaborate known requirements.

**Synthesis realization 4.** The report turns the graph into a practical, coherent workflow and preserves the optional action-taking branch. Section 5, “Start with one repeatable Python run,” precedes section 6, “Use failures to decide what to change,” contrary to `compare→workflow` if workflow includes the first run. This is a sensible report order and an over-bundled target. The uncertainty explanation is qualified but demanding; the graph does not expose the probability/coverage prerequisites that would make it more novice-friendly.

**Rendered graph.** Node/edge correspondence passes. The vertical diagram and edge list are usable on desktop. The embedded SVG scales to roughly 4–5-pixel labels on mobile. The HTML edge text remains readable, but node answers require opening JSON. Fresh-context rendering confirmed one page heading; an earlier full-page capture after resizing showed a capture artifact, which is not counted as a document defect.

**Smallest repairs.** Branch action-specific evidence checks; split initial execution from maintenance; qualify `outcome` with initial/expected state; expose the case-versus-attempt and statistical bridge only where needed. Replace broad repeated evidence bundles with exact explanatory passages. Preserve the successful edge-removal rationale, add intermediate deltas, and provide readable graph zoom/scroll and node answers.

## Causal inference — e07, report B

Artifacts: [graph](../runs/e07/dag.html), [JSON](../runs/e07/dag.json), [report](../runs/e07/report.html).

**Reader fit 4; completeness 3.** Observed comparisons, counterfactual outcomes, confounding, assignment, nonuse, missingness, and observational assumptions are well chosen for a reader who knows averages and percentages. The graph nevertheless omits two important foundations that the report supplies: random assignment versus sampling/generalization, and assignment unit/dependent observations in the clustered education trial. `uncertainty` requires a probability/repeated-study mental model beyond the stated reader knowledge.

**Edge validity 3.** `compare` and `counterfactual` support the confounding explanation, and `random→assignment` is a useful bridge to the assigned-versus-used distinction. No unambiguous reversed-direction edge was found. The problem is overstatement: `random→missing` makes random allocation prerequisite to understanding selective missing outcomes and interference, although both arise without it. `random→uncertainty` is defensible for allocation chance but not for the node's broader sampling-uncertainty answer. `confounding→random` is useful motivation; it is not proof that every explanation of random assignment requires a prior confounding lesson. The first two links need narrower questions or conditional/example relationships.

**Granularity 3.** `missing` combines loss of outcomes with interference between students, which have different mechanisms and repairs. `uncertainty` combines allocation variation, sampling variation, confidence intervals, and systematic bias. Splitting those two nodes around the actual explanatory bottlenecks would improve both evidence mapping and edge necessity.

**Evidence alignment 3.** `assignment` cites early textbook passages that assume adherence. They motivate the issue but do not explain the assigned-versus-received-treatment estimand. The direct explanation is in §22.1, pp.299–301, which distinguishes the two effects and explains how actual use can be selected. Fine Point 22.2 directly explains why restricting analysis after missing follow-up can introduce bias. These are small locator repairs using the same primary source, not a need to add more sources. [Hernán and Robins, *What If*, §22.1 and Fine Point 22.2](https://miguelhernan.org/s/hernanrobins_WhatIf_2jan25.pdf).

For `missing`, Fine Point 1.1 does explain interference. The actual trial's attrition analysis and a review's low-attrition judgment support claims about that study, but they do not independently teach the general missingness mechanism. For `uncertainty`, the cited Chapter 10 passages genuinely explain repeated-study coverage and why precision excludes systematic bias. Those locators are explanatory, not decorative. The trial remains evidence for its particular app-plus-training intervention and setting. [Trial paper](https://doi.org/10.1177/2332858416673968); [WWC review](https://ies.ed.gov/ncee/wwc/Study/86375).

**Research trace 2.** The initial six-node graph is preserved. The final graph replaces a broad implementation question with `assignment`, `missing`, and `uncertainty`, and adds `observational`. But rounds 1 and 2 are each serialized three times: four entries are duplicates, not four extra research iterations. Those rounds contain summaries rather than node/edge snapshots, so the final transition cannot be reconstructed with the precision of isolation's history. The notes do contain useful research activity, including correction of a mistaken source identification, checking study counts, and obtaining an original figure; the score is therefore not a total traceability failure.

The assignment/nonuse distinction, interference and missingness checks, and explicit observational assumptions plausibly strengthen the explanation. Correcting the study identity improves factual reliability rather than discovering a prerequisite. Counterfactual comparison, confounding, and randomization were already in the initial graph; later citations mostly verify and elaborate them. Repeated revision entries provide no evidence of additional learning.

**Synthesis realization 4.** Sections 1–2 teach the comparison and selection mechanism before section 3 explains random assignment. Section 3's practical trial checklist anticipates assigned-group analysis, outcome follow-up, and clustered assignment before section 5 develops their limitations. Those previews are reasonable, but they are not a literal topological realization of all final `target` dependencies. The report's sampling/generalization distinction exceeds what the graph records. The observed-vs-intervention simulator and the real trial are coherently connected to the mechanism rather than substituted for it.

**Rendered graph.** The two main branches are relatively easy to follow on desktop, and JSON correspondence passes. Labels shrink to roughly 7 pixels on mobile. Edge reasons remain readable; node answers are not reproduced in the graph HTML.

**Smallest repairs.** Separate missingness from interference and allocation variation from population sampling. Add the short assignment-unit/generalization bridges actually used in the report. Correct `assignment` and missingness locators to the explanatory textbook sections. Distinguish a planning preview from final interpretation in `target`. Deduplicate the revision history and preserve actual state changes; add readable zoom/scroll and node-answer access.

## Cross-topic findings and report tradeoffs

**Reader assumptions are usually sensible; prerequisite closure is incomplete.** Basic SQL and Python assumptions match the requests. Encryption and causal inference need additional arithmetic/statistical bridges that the prose sometimes supplies without graph nodes. No explicit assumed node was found to contradict its request. The subtler failure is treating unfamiliar compound answers as already explained once a source is attached.

**The dominant edge problem is necessity, not graph structure.** Isolation contains a clear definitional direction problem (`levels→serial`). Across all four, several other edges encode a teaching example, motivation, optional application, or reading order. Those relations can be useful, but the variant explicitly defines an arrow as “requires,” so they cannot all be treated as equivalent. An optional application branch is particularly important for evals; scope qualifications are particularly important for encryption.

**Evidence is credible more often than precisely aligned.** The source documents generally support the reports' substantive claims. The weaker artifact is the graph's “supported” label: it sometimes covers a multi-part answer with one narrow citation, an idealized assumption, or a broad source bundle. Isolation's `practice`, causal's `assignment`, and evals' `outcome` are the clearest examples. A source locator should be accompanied by an answer that actually resolves the node's question, with partial support left visible.

**Research traces show revisions, but do not demonstrate cognitive causation.** Isolation and evals preserve informative changes. Encryption has identical final-state snapshots for successive rounds; causal repeats two rounds three times. All final graphs close every required gap, which would be stronger evidence if partial support and unresolved necessity questions remained explicit. Logs establish recorded searches and changes, not that the graph caused the author to discover or teach a concept.

**Reports often repair the graphs.** Encryption supplies prime, symmetric-key, and correctness explanations; isolation supplies conditional-update mechanics and a better serial-definition order; evals preserves an optional action branch and a sensible first-run-before-comparison sequence; causal supplies assignment-unit and population limits. Their graph scores are therefore materially lower than their frozen report scores. This is a discrepancy in artifact fidelity, not a reason to retroactively lower the blind report ratings.

| Frozen report comparison | Associated graph report | Other report | Original blind result |
|---|---:|---:|---|
| Encryption | B: 44/45 | A: 43/45 | B, narrow |
| Isolation | A: 43/45 | B: 44/45 | B, narrow; presentation difference |
| Evals | A: 44/45 | B: 44/45 | Tie |
| Causal | B: 44/45 | A: 42/45 | B |

The graph-associated reports had two wins, one tie, and one loss, with differences of at most two points out of 45. Encryption's advantage was continuity/mechanism offset by readability; causal's was prerequisite clarity and presentation. These small, topic-specific differences do not establish a general explanation-quality gain. The graph audit shows substantial semantic repair needed despite strong reports. No controlled estimate of time/token cost was available, and file size, node count, or source count was not used as a quality proxy.

**Presentation is an audit limitation.** All SVGs correspond to the JSON, but narrow screens shrink rather than preserve readable labels. Dense routing also weakens the desktop advantage of encryption and isolation. The graph should be inspectable at a readable scale with answers and edge reasons available; it need not be made part of the novice's main reading flow.

**Additional verification after freezing.** During this phase, the full author-hosted *What If* PDF was successfully retrieved and its uncertainty passages inspected. This resolves the narrower source-access limitation recorded in the causal blind evaluation and strengthens confidence in that report's interval interpretation. It does not change any frozen score. It also exposed the graph's weaker `assignment` locator by comparison with the directly explanatory Chapter 22 passage.

## Recommendation and limits

Continue this as an optional research/audit experiment; do not promote the full DAG workflow to a required default on these results. Its useful parts are explicit reader assumptions, backward prerequisite questions, visible unresolved gaps, and a short research-change record. Before a broader test, require every “requires” edge to pass a necessity check, separate optional branches and scope limits, leave partial evidence visible, and preserve authentic revision states. Judge the graph by whether it reveals and repairs an explanatory gap, not by whether every node ends green.

A follow-up should use more paired topics, independent evaluators, and novice comprehension/transfer tests, with execution cost measured separately. This pilot has four pairs, one evaluator, and no human comprehension tests. The graph phase was necessarily unblinded to the four associations; its scores were produced after the blind report scores were frozen. A single run per topic and ordinary generation variation prevent causal attribution. The proposed repairs are evaluator judgments, not experimentally demonstrated improvements.

The evidence supports retaining prerequisite questions and traceable research. It does not yet support requiring a polished DAG: all four graphs are structurally sound, but their necessity claims, support labels, and histories are less reliable than the explanations they accompany.
