# Run r03

Complete: graph-only deliverable, 22 nodes, 39 edges. Final `dag.json`; original `dag.initial.json`; post-repair snapshot `dag.after-repair-1.json`; chronological `history.jsonl`. No full report or visual renderer created, per task.

## Sources actually used

- [Conditional Probability](https://probabilitycourse.com/chapter1/1_4_0_conditional_probability.php), Hossein Pishro-Nik textbook. Supplied verified packet plus direct web reading: definition/intuition lines 24–42; conditional complement line 55; chain rules equations 1.5–1.7, lines 110–116. Supports denominator changes, prior, multiplication, and retained dependence.
- [Law of Total Probability](https://probabilitycourse.com/chapter1/1_4_2_total_probability.php), same textbook. Packet plus direct reading lines 25–46. Supports disjoint-class sum and weighted evidence denominator.
- [Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html), scikit-learn User Guide. Packet plus direct reading: lines 75–94 for theorem, conditional independence, learned prior, classification versus probability estimates; 116–124 for counts/smoothing boundary; 141–148 for Bernoulli occurrence, absence, and representation. Source formulas motivate assumptions; constructed examples are our calculations.
- [Classification metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall), Google Machine Learning Crash Course. Packet plus direct reading lines 92–127. Supports recall, false-positive rate, precision, and denominator limits.

Two direct-source reading rounds; no search-engine queries or additional sources needed. All four opened successfully. Other retrieval failures mentioned in the supplied packet were not retried or relied on. No benchmark, other-run, design, or prior-experiment material read.

## Research and repair chronology

Initial graph saved before supplemental web research. First reading round verified broad claims and left follow-up sections pending. Second read checked chain rule, Bernoulli absence, and precision. Both rounds logged immediately with no graph edits.

Exact arithmetic and graph-only case replay then exposed two teaching gaps: absent-word probabilities needed an explicit complement bridge; joint dependence and normalized probability needed clearer separation. Repair added `multiply`, `partition`, `feature_value`, `normalize`; clarified `joint`; completed the repeated-clue counterexample. An example-to-general-rule edge was replaced by actual mathematical prerequisites. Learning estimates was separated from using supplied inputs. Full snapshots and edge additions/removals preserve reconstructable edits.

## Verification

`python3 verify.py`: PASS. Unique IDs and edges, valid endpoints, acyclic, every node reaches target, supported-node evidence present. Exact rational arithmetic confirms 90 true flags, 990 false flags, 8.3333% spam among flags, and six base-rate cases including boundaries.

Unfamiliar case: prior 20%, A present and B absent, stipulated class-conditioned independence; complements and normalization give 5/21 = 23.8095%. Counterexample: duplicated word clues at 1% prior give 5/104 = 4.8077% actual versus 25/124 = 20.1613% under naive multiplication. Equal-rate evidence, zero false positives, and zero evidence denominator checked. See `case-tests.initial.json`, graph `worked_cases`, and `verification.json`.

Manually reviewed all edge claims, including target edges, and replayed both cases after repair. This is a substantive author check, not independent human evaluation. All graph nodes are supported through located source claims, supplied assumptions, or labeled derivations.

## Limits

Examples are constructed mathematical populations, not observations of present email. Base-rate comparisons hold within-class filter rates fixed; deployment changes may violate this assumption. No empirical classifier training, calibration measurement, image extraction, or browser/rendering validation performed. Source figures concern textbook examples; the requested deliverable is graph and evidence only, with visuals delegated to the common renderer. Smoothing implementation and threshold optimization remain outside scope; zero-denominator failure is disclosed.
