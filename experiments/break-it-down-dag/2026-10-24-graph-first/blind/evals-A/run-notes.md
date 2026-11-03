# Run evals-A

Complete: prerequisite graph only. `dag.json` contains 20 nodes, 29 edges: 3 reader assumptions, 17 supported nodes. No explanation report, rendering, or live model/application evaluation performed.

## Evidence used

The assigned verified source packet supplied conceptual evidence from four official OpenAI guides:

- [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices): use-case objectives, variable outputs, cases, human calibration, repeated evaluation. Also directly opened and read relevant sections during round 1: workflow architecture, evaluator types, context and edge cases.
- [Getting started with datasets](https://developers.openai.com/api/docs/guides/evaluation-getting-started): packet only; annotations, reference answers, reusable datasets and graders.
- [Graders](https://developers.openai.com/api/docs/guides/graders): packet plus directly read overview, templating, string checks, similarity, and model-grader sections. Used concepts, not current SDK guidance. Page explicitly notes deprecation.
- [Working with evals](https://developers.openai.com/api/docs/guides/evals): packet only; support-ticket classification and separation of reusable definitions from particular runs. Packet reports legacy-platform transition dates; no implementation recommendation relies on this API.

Supplemental primary sources:

- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents), Anthropic Engineering, January 9, 2026. Read structure, conversational evaluation, repeated trials, starter roadmap, stable environments, transcript review, and monitoring. Used repeated-attempt variability, smaller-effect limitations, and state isolation. Broader article advice was not adopted wholesale.
- [Confidence intervals](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm), NIST/SEMATECH e-Handbook. Read complete short page. Used the observed-proportion definition; the graph does not prescribe its confidence intervals for correlated AI trials.

Evidence records identify URL, section/line locator, and precise supported claim. `exact_claim` identifies the claim being supported; it is not represented as a quotation. Most starting evidence is explicitly labeled packet paraphrase. Workflow conclusions are synthesis; the constructed refund example is explicitly hypothetical.

## Actual research/history

- Before supplemental research: saved `history/initial.json`, `history/round-00.json`, and working `dag.json`.
- Round 1: direct opens of best-practices and graders pages; navigation searches for customer, Design, variable, Overview. Saved changes immediately in `history/round-01.json` and snapshot `history/after-round-01.json`.
- Round 2: searched `site.anthropic.com engineering evals trials non deterministic evaluations agents pass rate` and `site.nist.gov proportion confidence interval sample size binomial`. Opened the Anthropic and NIST sources above. Saved changes immediately in `history/round-02.json` and snapshot `history/after-round-02.json`.
- No no-change rounds occurred. No other runs, designs, rubrics, or prior experiments read. No skill modified and no delegation.

## Checks

Ran `python3 check_graph.py`: **PASS**. See `checks.json` for unique IDs, endpoint validity, duplicate-edge checks, acyclicity, all-node paths to target, assumption roots, evidence-field completeness, and replay of actual history to final nodes/edges.

Manual semantic review split arithmetic, coverage, and uncertainty because they require different explanations. Removed reference-answer dependency from generic grading: a grader can use a success rule without a particular reference answer. Checked answers against supplied passages and directly read material. Structural PASS alone does not prove conceptual necessity or evidence adequacy.

## Limits

No access failures. Two packet sources were not independently reopened. No organization-specific policies, logs, or outputs supplied; concrete criteria require those inputs. No universal passing threshold, statistically sufficient sample size, or deployment guarantee established. Formal paired comparisons and test-set overfitting controls are outside this starter graph. Source figures were not extracted because the task requests graph-only evidence/history; shared rendering remains separate.
