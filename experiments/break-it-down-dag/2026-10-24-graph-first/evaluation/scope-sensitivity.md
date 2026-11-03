# Separate scope sensitivity — original results unchanged

Applied only the graph-blind scope audit's P8/PA4 and I6/IA1 corrections, after original results were finalized and hashed. This is not replacement scoring.

| Graphs | Original → sensitivity change | Overall |
|---|---|---|
| bayesian_spam-A, bayesian_spam-B | P8 core interpretation adequate; decision-policy portion and PA4 scoped extensions. Coverage 3→5; application utility 3→5. | Both still need repair |
| isolation-A, isolation-B | None: both voluntarily include snapshot/disjoint-write explanations, and already pass I6/IA1. | Both still need repair |
| Both evals; both backpropagation | None | Unchanged |

Removed only **bayesian_spam-A finding PA1** and **bayesian_spam-B finding PB1**, which concerned omitted mistake-cost/action thresholds. Neither graph recommends deleting a message; both state modeled probabilities' limits. Their estimation-to-score prerequisite defects remain: given/stipulated probabilities can be combined without first learning training/smoothing procedures. All edge, granularity, evidence, history and other scores remain unchanged.

Acceptance remains **1/8**: backpropagation-B accepted; seven need repair. This scope correction removes two artificial core-omission findings but changes no overall verdict. I7's guarded-update obligation is unchanged; its separate scope concern was not authorized for this sensitivity analysis.

Original results SHA-256: `493bd5c373221ced1764128074c109a38d82f5cb19cbc12c66dac23b167fdbdb`. Exact original/revised dimensions, finding IDs and probe changes are in `scope-sensitivity.json`.
