Graph-only task complete. Final: `dag.json`. Initial: `history/initial-dag.json`. Research revision: `history/round-1-dag.json`. Embedded revisions preserve the actual initial graph and one supplemental research round.

Sources actually used:

- [Pishro-Nik, Conditional Probability](https://probabilitycourse.com/chapter1/1_4_0_conditional_probability.php): definition, initial prior discussion, chain rule equations 1.5 and 1.7. Directly opened relevant sections after saving the initial graph.
- [Pishro-Nik, Law of Total Probability](https://probabilitycourse.com/chapter1/1_4_2_total_probability.php): two-class partition and weighted contributions. Directly opened.
- [scikit-learn, Naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html): 1.9 Bayes rule, conditional independence and probability warning; 1.9.2 estimation and smoothing; 1.9.4 presence/absence features. Directly opened relevant sections.
- [Google, Classification metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall): recall, false-positive rate and precision definitions. Directly opened relevant sections.
- Supplied source packet and user request furnished the starting model and numerical assumptions.

Further searches: none. Supplemental research consisted of opening all four supplied primary-source URLs and their relevant sections. All opened successfully. Packet-listed access failures were not repeated and those excluded sources were not used.

Research changed the graph: added the general two-clue chain-rule prerequisite before conditional independence; connected posterior normalization to classification scores. Resolved numerical gaps using exact fractions. At 1% prevalence, 90 of 1,080 modeled flags are spam (8.33%); holding detection/false-positive rates fixed, 10% prevalence gives 50% and 50% gives 90%.

Verification: `python3 check_graph.py` PASS; see `checks.json`. Verified IDs, endpoints, duplicate edges, acyclicity, target reachability, node evidence fields, actual initial preservation, count/formula agreement, numerical boundaries, and hypothetical two-clue arithmetic. Manually reviewed answers and edge reasons for denominator confusion, unexplained terms, required assumptions, and empirical-versus-constructed claims. This is a semantic review, not proof that a unique optimal prerequisite graph exists.

Material limits: no actual inbox data, word frequencies, or calibration measurements. Numbers for two word clues are explicitly hypothetical. Base-rate comparisons assume both conditional flagging rates stay fixed. No required research gaps remain. Figures and full explanatory prose are outside the requested graph-only output; the shared renderer handles the graph view. No visual rendering or browser-layout checks were performed.
