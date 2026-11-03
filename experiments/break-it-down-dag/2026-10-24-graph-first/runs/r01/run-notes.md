# Run r01

Complete: graph-only artifact. Final graph has 22 nodes and 39 edges. No report or renderer produced.

## Inputs and chronology

Read only assigned worker instructions, skill snapshot, request and ai-evals source packet; later read this run's own artifacts and public source pages. No benchmarks, sibling runs, design files or earlier experiments inspected. No delegation.

- `dag.initial.json`: initial graph saved before supplemental research. Initial tool message incorrectly reported 17 nodes; the saved graph contains 16.
- Supplemental research opened OpenAI evaluation best practices and Anthropic's agent-evals article. Located relevant sections using in-page searches; no search-engine queries.
- `dag.round1.json`: added tool definition, controlled initial state, uncertainty, reserved cases and release interpretation; added located evidence and marked synthesis explicitly.
- `substantive-tests.initial.json`: tested transfer to delivery-address changes, a misleading average, and missing execution results. The missing-results case exposed a denominator gap.
- `dag.round2.json` and `dag.json`: repaired incomplete-result handling; removed a redundant edge. Full snapshots permit reconstruction; `history.jsonl` records actual rounds and final no-change verification.

## Sources actually used

All four provided primary-source excerpts were used as supplied material:

- [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): objectives, representative cases, calibration, iteration and interpretation. Also opened live relevant passages: lines 984–1052 and 1063–1123, including the held-out example at line 1029.
- [Getting started with datasets](https://developers.openai.com/api/docs/guides/evaluation-getting-started): expert annotations and repeatable case information. Packet only.
- [Graders](https://developers.openai.com/api/docs/guides/graders): exact, semantic, qualitative and programmatic checks. Packet only.
- [Working with evals](https://developers.openai.com/api/docs/guides/evals): records, separate test definition and execution, generated ticket labels and grading. Packet only; conceptual evidence, not current platform implementation advice. Packet and live best-practices page disclose the platform transition.

Supplemental primary practitioner source:

- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), Anthropic Engineering, January 9, 2026. Read structure (lines 52–68), conversational-agent evaluation (219–257), repeated attempts (271–282), and task/harness/grader design and review (286–329). Used for whole-application boundaries, observable outcomes, repeated attempts, isolated initial state and insufficient grading evidence. Its concrete examples are illustrations, not measurements of this user's assistant.

In-page queries: `hold`, `test set`, `customer`, `Compare`, `dataset`, `isolated`, `20`. The first two returned no exact matches; the comparison result exposed the hyphenated held-out passage. Both live pages were accessible. No source access gaps.

## Verification

`verification.json`: PASS for unique IDs, valid endpoints, duplicate-edge absence, acyclicity, paths from every node to the target, required fields, and evidence presence on supported nodes. `edge-audit.json` records the final dependency review and removed redundant edge. Earlier removals appear in history and snapshots.

Constructed transfer test: allowed address change with unchanged resulting record. Graph distinguishes reported success from actual failure.

Constructed counterexample: 99 correct FAQ answers plus one unauthorized refund. Graph permits 99/100 arithmetic while rejecting the average as sufficient readiness evidence.

Boundary retest: five attempts, two graded passes, three timeouts. Repaired graph requires all counts and classification of missing results, preventing an unexplained 100% score.

These were reasoning checks against the graph, not real model/app executions or independent user studies. Source-supported synthesis is labeled separately from directly documented definitions. In particular, holding out cases and reporting incomplete counts include reasoned design guidance; no formal statistical guarantee is claimed.

## Limits

Actual policy, account authorization rules, application behavior, support traffic and expert labels are unavailable. Requirements and examples are explicitly constructed; application owners must supply those inputs. No fixed deployment threshold or adequate universal sample size is inferred. Close-score statistical inference, platform setup and production monitoring implementation remain outside this beginner graph's scope. No live API evaluation, expert calibration study or visual inspection was performed; common renderer owns graph visuals.
