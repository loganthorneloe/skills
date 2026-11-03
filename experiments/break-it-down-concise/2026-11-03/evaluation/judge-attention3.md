# Judge: attention3 (blind A vs B)

Both reports were rendered with Playwright at 1280px and 390px. Neither logged console errors and neither scrolls horizontally at page level. All images loaded. Every control was operated: in A, the query buttons, the multiplier slider (0 to 4), the mask checkbox and Reset; in B, the d_k slider (up to 512), the scale checkbox, New random vectors and Reset. Screenshots and scripts are in `evaluation/scratch-judge-attention3/`. Word counts are the rendered body text, including the source cards.

## Scores

Dimensions 1 to 9 are the rubric. 10 is signal density, 11 time to answer, 12 research quality, 13 visual explanation.

| Report | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | Total /65 | Probes /16 | Words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 4 | 3 | 4 | 5 | 5 | 59 | 16 | 3,413 |
| B | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | 5 | 4 | 59 | 16 | 1,905 |

### Notes on scores

- **Prerequisites and order (1, 2).** A gives the novice more groundwork before attention appears. It explains what a language model is, what a vocabulary of tokens is, and what "learned" means as nudging parameters. It then explains the recurrent problem that attention replaced, and only then the attention formula. B covers the same ground in a few sentences. It mentions gradients without teaching them, and it explains recurrence only in the "why ChatGPT" section, after the mechanism. That order works, but the contrast comes late.
- **Mechanism (3).** Both explain the computation fully. B's worked example starts from the embedding matrix X and real weight matrices, computes X·W to get Q, K and V, then fills in the whole masked 3×3 weight matrix. That makes the "learned projection" step concrete. A's example writes the query, key and value vectors by hand and computes one query row. In exchange, A lets the reader explore by changing the query, the score sharpness and the mask.
- **Presentation (9).** At 390px, B's Figure 3, Table 1 and Table 2 are cropped at the right edge and have to be scrolled sideways. B's Figure 3 image also includes the paper's own printed caption, which repeats B's caption. At 390px, A's interactive table is clipped on its right side, so the weight and share columns have to be scrolled to. A's figures all fit the screen.
- **Density and time to answer (10, 11).** Both put the short answer first. B reaches the full mechanism, a worked example and the scaling argument in about 56% of A's words, with little filler. A's extra length goes mostly to useful teaching, but some of it is repetition, such as the closing "division of labor" paragraph and the "broader implication" paragraph.
- **Research (12).** Both sets of records audit the same core papers with section-level locators and stated limits. Both records caught the inconsistent English–French BLEU figure in Table 2 (41.8 in the table, 41.0 in the text). B's records also map claims to sources. The research quality is equivalent.

## Visuals

### A

1. **Vaswani Fig. 2, first panel (scaled dot-product attention).** Shows the formula as a pipeline of matrix operations with no loop over positions.
2. **Vaswani Fig. 2, second panel (multi-head attention).** Shows h parallel heads, concatenated and projected.
3. **Interactive attention table.** Five tokens. The reader picks the query, sets a score multiplier and toggles the causal mask. It teaches that softmax turns scores into weights, that sharper scores make one key win, and that masking removes later positions. All of these behaviors were verified to work.
4. **Table 1, rebuilt as an HTML table.** Compares work per layer, steps that must run in sequence, and path length for attention versus recurrence. It teaches the parallelism argument and the n² cost.
5. **Vaswani Fig. 4 crop (the word "its" attending to "Law" and "application").** Shows a trained head resolving a reference, which ties back to the toy example.
6. **Kaplan Fig. 7 (LSTM vs transformer).** Shows transformers keep using context out to 1,000 tokens.
7. **Kaplan Fig. 1 (power laws).** Shows prediction error falling predictably as models grow.
8. **Ouyang Fig. 2 (the three RLHF steps).** Shows the human-feedback training that turned a text predictor into ChatGPT.

A should have had B's Figure 1 (the full transformer architecture), so the reader can see how one layer is built and stacked. It should also have shown how Q, K and V are computed from X·W with real numbers, as B does.

### B

1. **Vaswani Fig. 2 (both panels).** Shows the equation as a pipeline, and multi-head attention.
2. **Weight matrices as cards, plus the masked 3×3 weight table.** A complete numeric pass from X to the output, including the mask. All the arithmetic checks out.
3. **Interactive: one query against eight random keys.** The reader changes d_k and switches the √d_k division on or off. It teaches why the scaling exists: unscaled at d_k = 512, one key takes about 93% of the weight.
4. **Vaswani Fig. 1 (architecture).** Shows the full layer with residual connections and positional encoding. The caption explains that GPT keeps only the decoder side.
5. **Vaswani Fig. 3 ("making" attending to "more difficult").** Shows heads following long-distance dependencies.
6. **Vaswani Table 1, original image.** Shows the sequential-steps and path-length advantage, and the n² price.
7. **Vaswani Table 2, original image.** Shows translation quality and training cost. The caption flags the 41.0 vs 41.8 discrepancy.
8. **Kaplan Fig. 7.** Shows LSTMs against transformers by model size and by token position.
9. **Kaplan Fig. 1.** Shows the scaling laws.
10. **InstructGPT Fig. 1 (labeler win rates).** Shows that a 1.3B model with human feedback beat 175B GPT-3.

B should have had an exploratory control for the causal mask and the query choice, like A's. Its static masked table covers the mask adequately. It also lacks the RLHF step diagram, but describes those steps in one sentence. At 390px its wide figures are cropped.

## Probes (0/1/2)

| Probe | A | B |
|---|---|---|
| Q1 Tokens, embeddings, position | 2 | 2 |
| Q2 Problem attention solves | 2 | 2 |
| Q3 Queries, keys and values as learned projections | 2 | 2 |
| Q4 Computation: QKᵀ, √d, softmax, weighted V | 2 | 2 |
| Q5 Multiple heads | 2 | 2 |
| Q6 Masking, stacking, next-token training | 2 | 2 |
| Q7 Why it enabled scale | 2 | 2 |
| Q8 Quadratic cost | 2 | 2 |
| **Total** | **16** | **16** |

## Errors and overclaims

Neither report has a consequential error. I recomputed both worked examples by hand. A's weights are 0.062, 0.620, 0.062, 0.062 and 0.195, with output [0.68, 0.06, 0.26]. B's weights are 0.187, 0.045 and 0.768, with output [0.96, 2.44]. Both are correct.

### A

- A says "The authors explain why in a footnote" and then states the √d_k rationale as fact. The paper presents it as a suspicion ("We suspect…"). B gets this right. This is a minor loss of qualification.
- "Two heads put almost all of their weight on 'Law' and 'application'" describes the full Figure 4. The crop A embeds is a single panel, so the reader cannot fully check this claim against the image shown. This is minor.

### B

- "Transformers beat LSTMs at every size, by a growing margin." This is a slight overstatement of Kaplan Fig. 7, where the curves are close at the smallest sizes. Minor.
- "restricted some layers to nearby tokens, a shortcut the original paper proposed for long sequences." This links GPT-3's sparse banded attention loosely to Vaswani's restricted self-attention. GPT-3 took its version from the later Sparse Transformer work. Minor.
- The Kaplan Fig. 7 caption says models "reach about a billion parameters", while B's own source card says about 1.5 billion. This is a small inconsistency.

## Verdict

B gives a reader real understanding faster. It reaches the same 16/16 probe coverage and the same overall score in about 56% of A's words. Its numeric example derives Q, K and V from X·W, its √d_k interactive shows why the division exists, and its architecture figure shows the full layer.

The shorter report lost a little. A teaches more groundwork for a reader with no machine-learning background: what training means, and recurrence explained before attention. A's interactive shows the query, the mask and softmax sharpness together, and A has the RLHF step diagram. B's wide figures are cropped on a phone, while A's figures fit the screen. None of these losses is essential, because B covers each point adequately in text or in a static exhibit. B also hedges more carefully on the √d_k rationale and on the scope of "made it possible."
