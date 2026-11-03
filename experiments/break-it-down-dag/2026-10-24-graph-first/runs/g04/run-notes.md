# g04 — completed

Produced prerequisite graph only. Final: `dag.json` (16 nodes, 26 edges). Initial state: `history/00-initial.json`. Actual research rounds: `history/01-research.md`, `02-research.md`, `03-research.md`. Final snapshot: `history/03-supported.json`. Reconstructable initial/final scripts: `build-initial.py`, `finalize.py`.

## Sources actually used

- [Conditional Probability](https://probabilitycourse.com/chapter1/1_4_0_conditional_probability.php): prior, conditional denominator, Equation 1.5 chain rule; relevant full passages opened.
- [Law of Total Probability](https://probabilitycourse.com/chapter1/1_4_2_total_probability.php): disjoint classes and weighted evidence totals; relevant full section opened.
- [Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html): Bayes formula, conditional independence, estimated priors, binary word presence/absence, probability warning. Smoothing inspected and retained only as optional scope.
- [Classification metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall): recall, false-positive rate, and precision denominators; all relevant sections opened.
- [Probability calibration](https://scikit-learn.org/stable/modules/calibration.html): supplemental source beyond packet; opened to resolve empirical-confidence interpretation (lines 74–83).

No search-engine queries. Direct URL openings followed supplied URLs and the linked official calibration topic. No access failures. Packet-listed failed sites were not retried or relied on.

## Changes and checks

Initial graph saved before browsing. First two reading rounds made no graph changes and were logged immediately. Third round consolidated verified evidence and original numerical derivations, added a general update-rule node, removed the false prerequisite from base-rate examples to word evidence, and separated optional smoothing.

`python3 .../runs/g04/finalize.py` returned PASS. `checks.json` records unique IDs, valid endpoints, acyclicity, every node reaching target, evidence presence for supported nodes, exact fractional calculations, and illustrative word-update direction checks. Manual review examined evidence coverage, assumed knowledge, and dependency necessity. These checks cannot mechanically establish pedagogical completeness.

At 1% spam, expected flags per 10,000 messages: 90 spam + 990 legitimate; spam among flags = 1/12 ≈ 8.33%. Changing the base rate while fixing the flag rates gives 0.89%, 8.33%, 50%, and 90% precision at respective base rates 0.1%, 1%, 10%, and 50%.

## Limits

No unresolved prerequisite evidence gaps. Rates and counts are a mathematical example, not measured inbox performance. No classifier trained or empirically calibrated. Scope uses binary word presence/absence; word-count variants, thresholds, costs, and smoothing are optional. No report or visualization produced or rendered, per graph-only instruction and assigned shared renderer. No skill files changed.
