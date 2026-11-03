# g02 run notes

Complete: graph-only request. Final graph: `dag.json`; actual initial graph: `history/00-initial.json`; four subsequent research-round snapshots preserve reconstructable states, including round 3 with no changes. No report or renderer created.

Sources actually used:
- Supplied backpropagation packet: all four entries informed initial construction.
- [Google Nodes and hidden layers](https://developers.google.com/machine-learning/crash-course/neural-networks/nodes-hidden-layers): HTML lines 76–133, weighted sums and hidden values.
- [CS231n Backpropagation](https://cs231n.github.io/optimization-2/): HTML lines 25–69 and 105–170, derivative definition, local rules, chaining, cached values, accumulation.
- [3Blue1Brown Backpropagation](https://www.3blue1brown.com/lessons/backpropagation/): HTML lines 37–57 and 174–201, squared costs, sensitivity interpretation, aggregation across examples.
- [Google Activation functions](https://developers.google.com/machine-learning/crash-course/neural-networks/activation-functions): additional source, HTML lines 76–132; exact ReLU definition. Its boundary derivative was derived from the two one-sided change ratios, not attributed to an unspecified implementation.
- [PyTorch Optimizing Model Parameters](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html): additional source, HTML lines 361–424, learning rate and separation of gradient calculation from updates.
- [PyTorch Automatic Differentiation](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html): HTML lines 292–387, operation recording and backward accumulation.

No search-engine queries. Supplemental research used direct opens and targeted section reads. Initial PyTorch opens returned navigation only; preserved as a no-change research round before reading relevant sections. No source access failures.

Checks actually run: `python3 finalize.py` verified seven analytic parameter gradients by central differences (step 1e-6; absolute errors below 1e-8), forward values, simultaneous update, resulting prediction 1.45 and loss 0.00125. `python3 check_graph.py` passed unique IDs, endpoints, acyclicity, paths from every node to target, required fields, evidence presence, and initial/history preservation. Results: `numerical-checks.json`, `graph-checks.json`.

Manual dependency audit removed definition-to-algorithm confusions and motivation edges: a gradient can be defined before its algorithm; ReLU can be defined without knowing weighted sums; addition of branch effects does not require prior serial-path chaining; averaging examples uses assumed arithmetic. Nonlinearity motivation and the worked example stay separate from prerequisite edges.

Limits: original constructed example, not an empirical training result. Both ReLUs remain positive; inactive and zero cases are described but not demonstrated by this example. No autograd package or full training program executed. No convergence/generalization proof; finite differences validate this point only. No unresolved core research gap. Rendering and visual inspection belong to the shared renderer; not performed here. Source figures were not extracted because the explicit output is graph/evidence/history only.
