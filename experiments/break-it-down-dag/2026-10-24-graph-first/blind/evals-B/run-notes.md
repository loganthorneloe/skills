# evals-B run notes

Status: complete for the requested graph-only scope. 18 nodes, 29 edges. No full explanation report or renderer produced.

## Sources used

Read only the assigned local worker instructions, assigned-skill snapshot, request and ai-evals source packet before creating output. Used all four supplied primary-source paraphrases:

- [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): application scope, objectives, cases, calibration and recurring evaluation. Also opened relevant original HTML passages during supplemental research.
- [Getting started with datasets](https://developers.openai.com/api/docs/guides/evaluation-getting-started): references, expert annotation and repeatability; packet only.
- [Graders](https://developers.openai.com/api/docs/guides/graders): meaning and selection of grading rules; packet only.
- [Working with evals](https://developers.openai.com/api/docs/guides/evals): reusable data, configuration and outputs; packet only. Legacy tutorial used conceptually, not as a recommended current implementation.

Supplemental research read relevant HTML sections of:

- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), Anthropic Engineering, January 9, 2026: evaluation structure, conversational agents and nondeterminism.
- [Realtime Eval Guide](https://developers.openai.com/cookbook/examples/realtime_eval_guide), OpenAI Cookbook: sections 4.1–4.3 and 6. General data/comparison lessons transferred to text support; voice-specific implementation excluded.

Exact queries appear in `dag.json` revision 1. Both searches occurred after `dag.initial.json` and revision-zero `dag.json` were saved. Search hits other than the three opened primary pages were not used as evidence. No retrieval failures occurred. Sources are practitioner documentation, not independent proof that a particular assistant meets its requirements.

## Revision history

Initial graph preserved verbatim in `dag.initial.json` and `dag.json` revisions[0]. Supplemental research added repeated trials, held-out cases and subgroup score interpretation. It also moved outcome observation before the run that records evidence. Final nodes contain answers; edge explanations express prerequisites. No unrelated branch remains.

## Verification

Ran `python3 check_graph.py`: PASS. Results in `checks.json`. Checked unique IDs/edges, valid endpoints/target, acyclicity, every node's path to target, required fields, evidence presence and initial-snapshot preservation. Manually reviewed answers in dependency order and edge necessity, grounding in the reader's Python/API knowledge. Numerical examples checked by elementary arithmetic; illustrative, not measurements.

No model API call, support-system trial, grader calibration experiment or rendering check performed. The shared renderer is responsible for the visual view. These checks establish graph integrity, not empirical application quality.

## Remaining limits

Actual support policies, customer inputs, action permissions and expert expectations are unavailable. The starter plan is explicitly constructed and needs those inputs before use. Small-score statistical significance, confidence intervals and sample-size selection remain outside the starter scope; the graph discloses that limitation rather than claiming reliable superiority. No universal deployment threshold is proposed. Current vendor API wiring was not researched because only the prerequisite graph was requested.
