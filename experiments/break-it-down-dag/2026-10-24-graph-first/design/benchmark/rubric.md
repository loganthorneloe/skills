# Frozen independent graph-only rubric

Version 1.0. Designed before graph generation. Scope: the prerequisite graph, its node answers/evidence, and its actual research/revision record. No main explanatory report, report polish, source count, node count, elapsed time, or token count contributes to graph quality. Record cost separately if available. This is an artifact audit, not a human comprehension trial and not evidence of causal improvement from an instruction variant.

## Independence and freeze

The designer read only the previous graph audit and the original topic prompts as prior experiment inputs. Candidate new instructions and new graphs were not read. The two regression topics intentionally target historical failures; the other two topic requests and checks must stay hidden from the instruction designer until candidate instructions are frozen. A coordinator/evaluator may access the complete benchmark.

Before any generation, preserve `benchmark.json`, `rubric.md`, and a manifest with SHA-256 hashes and UTC freeze time. Preserve candidate instruction hashes separately. Never silently adjust this rubric after seeing a result. A justified correction creates a new version and a deviation note; report results under the original criteria as well when feasible. Existing pilot graphs are not new benchmark observations.

Give generators only their assigned request and normal candidate instructions. Do not give them the answer expectations, dependency traps or application answer keys. Give evaluators anonymized condition/run identifiers where possible. No exact source, wording, node label, graph size or topology is prescribed.

## Evidence available to the evaluator

Collect the original request, declared assumptions/scope, machine-readable graph (or equivalent explicit node/edge representation), node questions and substantive answers, edge types/orientation/reasons, sources with locators/support status, and contemporaneous research/revision artifacts. Preserve the final state and genuinely available earlier states. Tool/retrieval records are useful for auditing; a retrospective narrative alone cannot establish chronological authenticity.

A graph answer may be brief, but must be sufficient to judge the question answered and the edges it induces. A picture with labels only cannot demonstrate explanatory completeness. Rendered-graph fidelity/readability is an optional audit-access observation; no polished HTML or SVG is required for graph-only acceptance.

Do not invent unavailable artifacts. Mark absent evidence explicitly. Missing history may make process validation unverifiable without proving fabrication. A reference to a later report does not cure a gap in the graph being evaluated.

## 1. Structural checks: report separately

For each item, record pass/fail/not applicable and the actual measurement. These checks do not count as semantic success.

1. Representation parses; node identifiers are unique and references resolve.
2. Edge orientation and relation semantics are declared or unambiguous. Normalize direction for analysis without rewriting the submission.
3. The prerequisite-only subgraph is acyclic. Other explicitly labeled relations must not be silently treated as prerequisites.
4. A target question or explicit set of target questions exists. Count nodes and typed edges; identify disconnected nodes and roots.
5. Check paths to targets and transitive redundancy for diagnosis. An assumed foundation or scoped extension may be explicitly annotated; reachability is not inherently proof of relevance or necessity. Do not create artificial edges just to make every node reach the target.
6. If a rendered view is supplied, compare identifiers, endpoints and relation types with the underlying graph. Record unreadable routing/labels separately from reasoning quality.

Broken endpoints, cycles within an alleged DAG, or indeterminate edge semantics block structural acceptance. Redundant but true prerequisite edges, disconnected optional material, absent polished rendering, and node count alone are not hard failures. A redundant edge may affect parsimony only if it impairs interpretation.

## 2. Semantic review procedure

### Establish the reader and target

Extract the exact reader baseline from the request. Do not assume probability from Python, calculus from arithmetic, or database internals from SQL. Ordinary arithmetic and explicitly stated skills may be assumed without extra nodes. Judge depth against the question, not a textbook syllabus.

Map every benchmark essential question to the graph evidence that addresses it. Use these statuses:

- **Adequate:** the concept and needed bridge are explicit at the requested depth.
- **Partial:** present but missing a consequential mechanism, assumption, or qualification.
- **Missing:** no usable answer/bridge found.
- **Scoped extension:** the benchmark explicitly permits this to be conditional, and the graph honestly limits its scope.
- **Uncertain:** evidence is insufficient to distinguish adequate from a gap; state what is needed.

The benchmark names conceptual obligations, not mandatory nodes. Accept alternative decompositions, combined questions with clear internal reasoning, frequency explanations instead of Bayes notation, scalar arithmetic instead of matrix algebra, and different concrete examples. A combined answer may discharge a prerequisite internally, but cannot hide it behind unexplained vocabulary. A graph cannot exclude a core part of the user's request merely by declaring it outside scope. Only benchmark-marked extensions have the extension exception.

### Test every prerequisite edge

For each edge A -> B, read B's actual question AND answer and the stated reader baseline. Ask:

1. Which part of B cannot be understood without A's information?
2. Could the reader understand that same part through a short explanation already inside B or another licensed foundation, without learning A? If so, is the edge merely optional reading order?
3. Is the dependency actually on only one portion of a bundled A or B? Does this accidentally make an optional branch mandatory?
4. Does the direction match conceptual dependence, or did the author connect motivation/example to a later definition?
5. Is it necessary only for a chosen construction/application? If so, is that condition clear?

Evaluate necessity relative to the represented question and explanatory route, not the impossible standard that no alternative pedagogy exists. A particular worked construction may need a foundation that a different construction would not. Require a concrete information dependency rather than a plausible sentence containing “because.”

Classify edges as defensible prerequisite, explicitly conditional prerequisite, redundant but valid, motivation/reading-order/example mislabeled as prerequisite, reversed, invalid for the stated scope, or uncertain. For material problems quote or identify the endpoints and explain the missing/incorrect information dependence. Check missing dependencies too: a valid list of existing edges can still omit a bridge essential to the answer.

The benchmark's dependency probes are diagnostic examples, not a prohibited-string list. A superficially similar edge can be valid if the submitted nodes have narrower questions that make the dependence real. Conversely, avoiding the exact labels does not remove the underlying defect.

### Judge granularity and parsimony

Identify bottlenecks, not a preferred node count. A node is too broad when its parts need different foundations, support or scope and that bundling makes an edge or support claim misleading. A node is too fine when it adds bookkeeping without revealing a dependency or unfamiliar concept. Some explicit internal explanation is appropriate; every word need not become a node. Optional cautions may attach as annotations or extensions instead of spurious foundations for the target.

### Check factual correctness and evidence entailment

For every material explanatory node, inspect the cited passage or equivalent accessible primary evidence. Record source, exact locator, claims actually supported and any limits. Prefer primary texts/specifications or authoritative educational explanations appropriate to the claim; a relevant title, broad source bundle, glossary definition, or search result is not automatically explanatory support.

Check whether the answer resolves its question, not just whether its words occur in a source. For compound answers check each material part. A source supporting locking does not thereby support conditional UPDATE semantics and complete retries. A source defining a gradient does not alone explain the chain rule for a calculus novice.

Elementary arithmetic, a worked derivation and a clearly marked author's inference need not each have an external citation. Recompute numerical examples and inspect the premises. Distinguish “source establishes the method” from “source reports this exact result.” Label inference and simplification; ensure simplified models preserve the relevant mechanism and state their assumptions.

Use support statuses supported, partly supported, inference/derivation checked, unsupported, contradicted, or inaccessible. Partial/inaccessible evidence must remain visible. Honest uncertainty is better evidence practice than falsely marking a node complete, but a material unresolved prerequisite still prevents full completion. No minimum number of sources is imposed.

### Audit the actual research record

Compare original snapshots/deltas, search/retrieval records, and final graph. A trace can show verification of an already-known concept, discovery recorded as new by the author, edge removal, corrected evidence or a changed scope. Distinguish these activities.

A simple authentic record is sufficient. Do not require a minimum number of rounds or force a revision when none is warranted. An unchanged graph after verification is allowed if honestly recorded. A purely final graph can be semantically evaluated but cannot independently demonstrate a research loop.

Duplicated entries are not extra iterations. Identical snapshots do not substantiate claimed node/edge edits; ask whether the edits were to answers/evidence instead and inspect them. Timestamp labels are not proof that knowledge was acquired then. Do not infer thought chronology, prerequisite discovery, or research causation from retrospective prose. Report inconsistency and uncertainty; call fabrication a hard failure only when the available record establishes a false or manufactured history, not merely because logs are missing.

### Probe utility using application questions

Answer each benchmark application question using only the concepts and links actually available in the graph, plus the declared reader baseline. This is an evaluator's transfer audit, not an actual novice outcome. For each question record:

- Pass: the graph makes the required reasoning reconstructable without a new material lesson.
- Partial: a correct answer is plausible, but a missing bridge must be supplied by the evaluator.
- Fail: a critical prerequisite is missing/wrong or the graph encourages the wrong answer.
- Scoped extension: explicitly allowed conditional branch is absent and not used in the graph's claims.

Cite the exact graph content that enables each step. Do not credit correctness supplied from the evaluator's own expertise. A memorized number in a node is insufficient if the graph gives no way to adapt the reasoning. Distinguish genuine reasoning utility from checklist coverage. Graphs can use different numbers/examples; the conceptual transfer must still work.

## 3. Severity and scoring

A **material** defect would plausibly prevent this reader from understanding or applying a core target concept, teach a false mechanism/scope, assert a false necessity/direction, or overstate consequential evidence. A typo, harmless redundant true edge, optional extra detail or alternate label is minor. Explain the concrete impact for every material judgment.

Score these seven dimensions on 1–5 ordinal scales. Use **NE** when evidence is unavailable rather than inventing a score.

| Dimension | 1: major failure | 3: mixed, substantive repair needed | 5: strong |
|---|---|---|---|
| Reader fit | Assumes major unstated knowledge; target inaccessible | Some bridges fit, others exceed baseline | All material bridges fit reader; terms/mechanisms introduced economically |
| Prerequisite coverage | Central mechanism or several foundations absent | Core present, at least one material gap | Required concepts and scoped conditions adequately represented |
| Edge validity/direction | Recurrent invalid/reversed necessity claims | Some material dependency errors | All material prerequisite claims defensible; other relations distinguished |
| Granularity/parsimony | Bundling or fragmentation obscures reasoning | Some splits/merges materially needed | Units expose real bottlenecks without unnecessary atomization |
| Evidence alignment | Material false support, contradiction or pervasive lack of evidence | Relevant evidence with material mapping/support gaps | Material claims entailed or transparently derived; limits accurate |
| Research-record authenticity | Demonstrably false chronology/state claims | Real record with material inconsistencies or reconstruction limits | Available record is internally consistent, actual states/deltas traceable, claims modest |
| Application utility | Most core probes fail | At least one material transfer gap | All applicable core probes reconstructable from graph |

Scores 2 and 4 indicate intermediate quality: 2 is substantially flawed but not wholesale failure; 4 has minor limitations without a material defect in that dimension. Do not average scores into an acceptance decision; a high total cannot compensate for a false dependency or missing core mechanism. Report dimensional scores plus findings, coverage and probe outcomes. These are judgments, not interval measurements.

## 4. Hard failures and transparent acceptance

Report three separate verdicts: **structural**, **semantic**, and **process/evidence validation**. Then derive overall status.

Hard failures requiring repair:

- Structurally invalid prerequisite DAG or unusable/ambiguous representation.
- Any material false explanatory claim, invalid/reversed prerequisite edge, or unacknowledged core coverage omission.
- Any core application probe that fails or requires the evaluator to add a material missing lesson.
- Material claim labeled fully supported when inspected evidence does not entail it; inaccessible evidence alone is uncertainty, not proof of contradiction.
- Demonstrably fabricated source, quote, retrieval or revision history.

**Accepted:** structure passes; all applicable core concepts are adequate; no material dependency/factual/support defect; every applicable core application probe passes; evidence and process record are sufficiently available to validate material claims; all seven dimensions score at least 4; no hard failure. Minor issues may be listed. An authentic unchanged research graph can pass: gratuitous revisions are not required.

**Needs repair:** a concrete material defect is established. List the smallest repair and affected obligation/edge/probe. Do not hide known defects behind an “inconclusive” label.

**Incomplete/unverifiable:** no established material defect, but missing/inaccessible evidence, genuinely partial core support or unavailable history prevents the full acceptance claim. Provide semantic results that are still supportable. A graph may pass semantic review while process validation remains unverifiable; do not conflate those conclusions.

**Accepted with scoped extensions:** same criteria as Accepted, with only benchmark-permitted conditional extensions omitted. Record which applications were exempt. This is equivalent to acceptance for the declared request, not a discounted score. The central request cannot be downgraded to an extension.

No pass can be earned merely by making all support fields green or by passing structural checks. Conversely, an honestly partial record earns credit for accurate status reporting even when work remains incomplete.

## 5. Comparison and reporting template

For each graph save a structured result and a short narrative with:

1. Anonymized run ID, request ID, candidate/benchmark hashes and evidence availability.
2. Structural check results and graph counts.
3. Coverage map from benchmark question IDs to graph nodes/answers, status and explanation.
4. Edge findings: endpoints, actual question/answer meaning, category, materiality, reason and proposed minimal repair. Include all material missing edges/bridges.
5. Evidence checks: claims, locators, entailment and access limits; independently verified arithmetic/inferences.
6. Research-record findings grounded in actual artifacts; available history versus claimed history.
7. Application results with graph-supported reasoning and explicit evaluator-supplied gaps.
8. Seven dimensional scores, separate verdicts and overall acceptance.
9. Minor issues and unresolved evaluator disagreements. A second evaluator, if available, first records independent judgments; adjudication preserves disagreements and original results.

Report regression and held-out topic results separately. With one run per topic, describe observed strengths/defects; do not infer general performance or statistical significance. If comparing variants, report paired counts and concrete defect changes, not just total scores. A larger graph or more citations is not evidence of improvement. No claim about improved human learning is warranted without actual reader testing.
