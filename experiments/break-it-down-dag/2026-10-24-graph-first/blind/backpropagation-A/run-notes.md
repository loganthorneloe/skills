# backpropagation-A run notes

Completed graph-only request using the assigned old skill snapshot. No skill files modified. No other runs, designs, rubric, or prior experiments inspected; no delegation.

Artifacts: `dag.json`, `dag.initial.json`, `verification.json`, `verify.py`. `build_graph.py` records initial construction; `finish_graph.py` records the research revision. Initial graph was saved before supplemental browsing and remains embedded verbatim in revision zero. One research round completed.

## Evidence actually used

- Supplied verified packet: Google ML Crash Course, **Nodes and hidden layers** (weighted sums and hidden values); Stanford CS231n, **Backpropagation, Intuitions** (sensitivity, chain rule, accumulation, staged computation); 3Blue1Brown, **What is backpropagation really doing?** (squared error, gradient updates, competing output/example contributions); PyTorch, **Automatic Differentiation with torch.autograd** (recorded operations and backward accumulation). The last two were used as supplied packet material, not independently reopened.
- Reopened [CS231n](https://cs231n.github.io/optimization-2/): read relevant sections through staged computation and patterns in backward flow, including square factor `2*xpy` at step (5).
- Reopened [Google nodes and hidden layers](https://developers.google.com/machine-learning/crash-course/neural-networks/nodes-hidden-layers); followed its activation link.
- Read [Google activation functions](https://developers.google.com/machine-learning/crash-course/neural-networks/activation-functions), especially the ReLU rule and Figure 6's textual description. No figure asset extracted: this task requests a graph only.
- Opened PyTorch stable autograd mechanics URL; followed its redirect to [Autograd mechanics](https://docs.pytorch.org/docs/2.14/notes/autograd.html). Read **Gradients for non-differentiable functions**, including the convention for fixed-constant max at equality.

Supplemental research used direct opens, link following, and an in-page search for `ReLU`; no search-engine queries. No source access failures. URLs, locators, claims, access provenance, and changes are retained in the graph. The elementary expansion of a square and all example numbers are original calculations, clearly separated from published evidence.

## Verification

`python verify.py` passed: 16 unique nodes, 24 edges, valid endpoints and target, no cycles, every node reaches target, evidence present on supported nodes, no remaining gap nodes, and the saved initial revision unchanged. Manually reviewed prerequisite direction and node answers: edges describe required knowledge, not chronological source order. Added `loss -> local_rules` after identifying that the `p-y` rule depends on the selected loss. No full explanation prose exists to check against.

Computed forward pass and simultaneous parameter update in Python. Independently checked all four backward sensitivities using central finite differences with epsilon 0.000001; maximum absolute difference was approximately 8.23e-11. Loss decreased from 1 to 0.3803125. The graph distinguishes this actual change from its local linear prediction.

## Limits and status

Complete within graph-only scope; no unresolved explanatory evidence gaps. One constructed example and one update establish arithmetic, not convergence, generalization, or empirical training performance. The example stays away from ReLU's corner. No framework autograd execution, rendered graph inspection, or explanation report; shared renderer handles the view. Structural validity does not certify pedagogical quality.
