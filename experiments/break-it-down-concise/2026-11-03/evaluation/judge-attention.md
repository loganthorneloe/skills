# Blind judge: attention reports A vs B

Both reports were rendered with Playwright at 1280px and 390px, with no console errors and no page-level horizontal overflow. Every control was operated: A's five query buttons, mask, scale and reset; B's five radios, the multiplier at 0 and 4, the mask and reset. All outputs recompute correctly. Screenshots and the script are in `evaluation/scratch-judge-attention/`. Word counts are the visible `main` text, including sources and captions.

## Scores

| | 1 Prereq | 2 Order | 3 Depth | 4 Evidence | 5 Accuracy | 6 Transfer | 7 Exhibits | 8 Readability | 9 Presentation | 10 Density | 11 Time to answer | 12 Research | 13 Visual | Total /65 | Probes /16 | Words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 58 | 16 | ~1,780 |
| B | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 3 | 4 | 5 | 58 | 16 | ~3,410 |

## Dimension notes

1. A covers tokens, embeddings, softmax and parameters in a few sentences. It never explains why a dot product measures match beyond "whose key points the same way." B teaches dot-product similarity, how training nudges parameters, and how recurrence works before it contrasts attention with it.
2. B introduces recurrence before attention and builds the mask, then the layer, then GPT-3. A introduces position vectors only after the mechanism, as one sentence in the heads section. That works, but it is a late add-on.
3. B adds residual connections, the variance argument behind √d_k, and a score-multiplier slider that makes softmax sharpening concrete. It also explains training as n parallel predictions. A covers the mechanism soundly but is thinner on why each step exists.
4. Both cite Vaswani for the mechanism and Kaplan for the LSTM comparison. B also supports the post-training step with InstructGPT.
5. A hedges carefully: the authors "argue this rather than test it," and the induction-head evidence for large models is "indirect." B states the √d_k rationale as fact and has two small overclaims, listed below.
6. B's multiplier and mask exercises plus the three-property synthesis let a reader reason about a new case. A's hand-computed row does the same job in less space.
7. Both use authentic figures with provenance, rights notes and limits. A noted a tick-label error in the Kaplan figure. B rebuilt Table 1 as accessible HTML.
8. A is tight and easy to follow. B is clear but long; its InstructGPT and BLEU/FLOP passages add load.
9. On mobile, A wraps wide images in scroll regions with a "Scroll sideways" hint. B shrinks or crops figures with no hint. At 390px only the left panel of B's Kaplan Fig 7 shows, while its caption says "The right panel is the one to read." The demo table is also clipped inside its scroll region.
10–11. A answers the question in its first two paragraphs and reaches the cost limit within about 1,800 words. B's short answer is also first, but it takes about twice as long to reach the same understanding.
12. A has six audited sources, a claims file, errata checks, spot-checks against the TeX source, and Hoffmann's later revision noted. B has five audited sources and evidence records with locators and inconsistency checks (it dropped an EN-FR score printed two ways). It has no claims file and no source for its "weights are hints" caution beyond Vaswani's own hedge.
13. B has six images, one rebuilt table, one interactive and limit tiles, all integrated. A has four images and one interactive, also integrated, but no visual for scaling or post-training.

## Visuals

### A
- Vaswani Fig 2 (both panels together) shows the formula as a pipeline, plus multi-head concatenation.
- An interactive row calculator with hand-picked Q/K/V lets the reader select a query, toggle the causal mask and the √2 scaling, and read q·k, score, weight and output. It teaches the full computation numerically.
- Vaswani Fig 3 ("making … more difficult") shows several heads linking distant tokens in one step.
- Vaswani Table 1 (as an image) compares sequential operations, path length and n² cost across layer types.
- Kaplan Fig 7 shows transformers beating LSTMs at every size and continuing to use context past 100 tokens.
- A should have had B's Kaplan Fig 1 power laws, which support "improve reliably with scale." It names that claim but shows no figure for it. B's Ouyang RLHF diagram would also help with the "last step" to ChatGPT. Neither omission is essential.

### B
- Vaswani Fig 2 (split panels) shows the same pipeline and multi-head structure, with a caption noting that nothing in it loops over positions.
- An interactive with five tokens (noun/verb/function-word dimensions), query radios, a score-multiplier slider, mask and reset teaches the computation, softmax sharpening, and the masking effect.
- Vaswani Fig 4 ("its" → Law/application) shows a trained head resolving a reference and is linked back to the demo.
- Table 1, rebuilt as HTML, makes the same comparison accessibly.
- Kaplan Fig 7 shows the LSTM context plateau.
- Kaplan Fig 1 shows predictable power-law improvement with compute, data and parameters.
- Ouyang Fig 2 shows the three-step RLHF process that turned GPT into ChatGPT.
- Limit tiles cover n² cost, attention weights as hints, and the need to add order.
- B has nothing it should have taken from A. A's induction-heads text has no figure in either report.

## Probes (0/1/2)

| | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Total |
|---|---|---|---|---|---|---|---|---|---|
| A | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 16 |
| B | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 16 |

A's Q3 is the weakest of these 2s. The roles of the three vectors come through matching and blending rather than B's explicit "what I'm looking for / what I offer / what I hand over."

## Factual errors and overclaims

### A
- "These models top out near a billion parameters." The source records say about 1.5B non-embedding parameters. This is loose rounding, not wrong in kind.
- Induction heads are described as "pairs of heads." An induction head is one head that works with a previous-token head, so this is a slight simplification.
- No consequential errors.

### B
- "Very large scores push the next step into a regime where training barely changes anything." The paper says "We suspect" this. B drops that hedge, which A keeps.
- "Raters preferred answers from a 1.3-billion-parameter InstructGPT model over … 175-billion-parameter GPT-3, even though … the two have the same architecture and differ only in this extra training." The two models also differ 100× in size, so "differ only" contradicts the sentence's own numbers. It echoes loose wording in the paper.
- "why GPT-3 already used local windows in some layers." This attributes a motive to the n² cost that the GPT-3 paper does not state.
- The Kaplan Fig 1 caption says "curves show no sign of flattening at the right edge." That is a mild interpretive claim, acceptable.
- No consequential errors.

## Verdict

A, the shorter report, gives a reader real understanding faster. It answers in two paragraphs, its hand-computed row carries the whole mechanism, and it reaches the same 16/16 probe coverage in about half the words, with tighter qualifications. What it lost is mostly secondary:
- B's explanation of how training adjusts parameters and its residual connections.
- The multiplier slider, which makes the √d_k and softmax-sharpening point tangible.
- The Kaplan power-law and RLHF figures that support "kept improving as they grew" and "fine-tuned for conversation."

Only the power-law figure is a real visual gap, since A names that claim without showing it. Nothing lost breaks the core answer. B is the deeper and more visually complete report at equal total score, but its extra length buys depth around the question rather than answers to it.
