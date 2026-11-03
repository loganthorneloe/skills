# Proposed DAG-only replacement

`candidate.txt` contains the complete candidate skill. `replacement.txt` contains only the replacement paragraphs. No installed skill or prior experiment changed.

Contract: retain source-grounded, first-principles HTML explanations; improve the audit graph's necessity, support and history. Preserve every character outside the specified section 2 block. Keep the full skill self-contained and at most 3,000 estimated tokens.

## Rationale

- Counterfactual edge test: record the precise explanatory failure when the proposed prerequisite is removed. Delete the edge if the reader can still understand the dependent answer. This targets reading-order edges directly.
- Keep scope, optional material, examples and motivation separate from prerequisite edges. Their teaching value alone cannot establish necessity.
- Atomic questions plus splitting by different prerequisites/evidence reduce broad nodes whose support and dependencies apply to only part of their answers.
- Add `partial`; research both partial and gap nodes. Require located passages to explain every answer claim before marking supported. Preserve uncovered claims.
- Save the initial state before research, append reconstructable changes immediately, retain no-change rounds and prohibit backfilling. This targets repeated final-state snapshots and invented research histories.
- Reconcile graph answers and edges with source passages and prose; repair missing foundations in both artifacts. Reports cannot silently repair defective graphs.

Relevant refiner gotchas: apparent completion, exact verification, one default path, self-contained essential rules, metadata preservation, and behavioral evidence distinct from structural validity.

## Budget and checks

Original and candidate blocks: 1,150 characters each. Full candidate: 11,997 characters; 2,999.25 estimated tokens, rounded to 3,000 by validator. All text outside the requested block is identical. Validator `PASS` on a temporary correctly named `break-it-down-dag/SKILL.md`, using `--max-tokens 3000`. There are no target-provided scripts or native discovery checks in the target folder. Detailed counts are in `checks.json`.

Design-only abstract trace: identify reader assumptions and target → persist an initial state → test each proposed requirement by removing it conceptually → separate scope-only material → split questions with different dependencies → research unresolved claims → retain partial support and actual deltas → reconcile sources, answers and prose → inspect final structure and deliver report plus graph. This checks instruction continuity, not actual execution.

## Tradeoffs and limits

The character ceiling forces compact schema prose. No formal representation for scope-only notes, evidence coverage, deltas or prose anchors is prescribed; execution must choose these consistently. No-change rounds are legitimate when actually recorded, but the instruction alone cannot prove chronology. Source coverage and edge necessity still require expert judgment. Readability is requested without detailed graph layout rules. Structural validation does not establish semantic improvement; actual graph execution and representative behavioral validation remain pending by assignment.
