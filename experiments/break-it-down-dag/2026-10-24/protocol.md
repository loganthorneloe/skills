# Break It Down DAG pilot — frozen before generation

Question: does explicit prerequisite-DAG research improve an explanation for a novice, compared with the current working-copy skill?

Eight independent generation agents, one per skill × topic; four matched prompts. One independent evaluator scores anonymized HTML pairs before graph inspection. Same inherited model, available tools, output contract, prompts, and no imposed length/source quota. Run sequential waves of up to three workers due to concurrency limits. No cross-run reading, nested delegation, or draft repair based on comparative results. Single sample per cell; exploratory, not a statistical or causal result. Search results, execution order, output length, and research effort may differ. More research is part of the treatment; this pilot cannot separate graph structure from extra effort.

Baseline is the exact pre-existing uncommitted working copy, saved as inputs/baseline.txt. Original remains untouched. Variant is inputs/variant.txt, identical to the WIP source. Hashes in inputs/hashes.json. Only research workflow changes plus unique name/WIP metadata. To retain the 3,000-token single-file limit, the variant removes the illustrative source-audit example and compresses the two original research paragraphs; explicit source-audit, evidence, presentation, styling, verification, and delivery requirements remain. This small non-DAG instructional difference is a possible confound.

## Contract and applicable skill-refiner gotchas

Representative requests: explain evals, causal inference, encryption, isolation to explicitly described novices. Deliver complete research-backed HTML plus an actual prerequisite DAG for the variant. Preserve canonical skill bytes. Keep experiment artifacts outside the installable skill. Relevant gotchas: discovery name collisions; single-file portability; source support vs structural validity; honest blocked checks; actual behavioral runs rather than trace-only proof.

## Frozen report scoring (1–5, equal weight)

1. Prerequisite coverage relative to the stated reader: 1 essential foundations missing; 3 mixed; 5 necessary foundations explicitly taught.
2. Dependency order and conceptual continuity: 1 circular/unexplained leaps; 3 some gaps; 5 concepts built before use with explicit connections.
3. Mechanistic depth: 1 definitions only; 3 partial how/why; 5 clear causal/computational mechanism and consequences.
4. Evidence support for foundations: 1 citations only support the headline topic; 3 uneven foundation support; 5 relevant explanatory passages support key prerequisites.
5. Accuracy and qualification: 1 consequential error; 3 oversimplified; 5 accurate, bounded conclusions.
6. Transfer to the user's concrete question: 1 cannot apply; 3 partial recipe; 5 can reason through a fresh case.
7. Source/exhibit quality: 1 unsupported or decorative; 3 uneven; 5 relevant original evidence analyzed with provenance and limits.
8. Readability and cognitive load: 1 overwhelming/fragmented; 3 workable; 5 clear prose and proportionate prerequisites.
9. Presentation/usability: 1 broken/unreadable; 3 minor defects; 5 readable desktop/mobile, accessible controls and evidence.

Report per-topic winners/ties and per-dimension deltas; do not use length, source count, or DAG existence as a quality proxy. Score readable report first, then inspect DAGs separately. Quote short exact passages or section locators as evidence. Flag unsupported claims and hard errors; high style scores cannot erase them. Do not manufacture human comprehension results.

## Graph audit (separate 1–5 dimensions)

Reader fit; prerequisite completeness; edge necessity/direction; granularity/parsimony; evidence alignment; research-loop traceability; synthesis realization. Check actual initial→final revisions, not just polished final DAGs. Distinguish acyclicity from conceptual correctness. Identify missing nodes, false dependencies, assumed knowledge, irrelevant nodes, unsupported answers, and report order violations with exact IDs. Suggest the smallest repairs; do not silently modify evaluated outputs.

## Expected topic probes (evaluator only)

- Evals: task behavior vs plausible text; variable inputs/outputs; correctness criteria; representative cases; evaluators/labels and their limitations; failure analysis, change comparison, and deployment shift. Probe a test set that misses a new failure type.
- Causal inference: comparison, counterfactual outcome, selection/confounding, assignment/randomization, sampling variation and generalization. Probe baseline differences and randomization versus sample representativeness.
- Encryption: plaintext/ciphertext/algorithms/keys; asymmetric relationship; feasible forward/infeasible reverse; key distribution/authenticity; confidentiality versus signatures; real limits. Probe an attacker substituting their own public key.
- Isolation: transaction and invariant; interleaving/snapshots; conflicts/anomalies; isolation guarantees; coordination/abort/retry; implementation-specific behavior. Probe write skew or a lost update and explain why an isolation label alone is insufficient.

## Completion evidence

Repository validator PASS within 3,000 estimated tokens, creator validator, diff whitespace check, installed personal-harness link and collision audit, eight actual runs, independent report/graph assessment, graph structural checks, reviewable index linking all reports and DAGs. Record unavailable checks honestly. Do not replace baseline or promote variant based on a single pilot.
