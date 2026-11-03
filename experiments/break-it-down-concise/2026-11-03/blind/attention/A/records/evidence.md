# Evidence records

### E1: Scaled dot-product and multi-head attention diagram
- claim: C2, C4, C5 (support)
- type: figure
- source: Attention Is All You Need — https://arxiv.org/abs/1706.03762 (v7)
- locator: Figure 2, p. 4
- asset: ../assets/vaswani-fig2-attention.png (rendered from v7 PDF at 3x, 1236×714, caption included)
- inspected: opened at full size; both panels, all box labels, Q/K/V inputs and caption visible
- notice: Left panel is the whole computation in five boxes: one matrix multiply of Q and K, scale, optional mask, softmax, a second multiply with V. Right panel repeats it h times on linearly projected inputs and concatenates.
- limits: Drawn for the translation model; GPT-style models use the masked version only.
- rights: "Provided proper attribution is provided, Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works."

### E2: Attention equation
- claim: C2 (support)
- type: quote
- source: same — §3.2.1, Eq. 1
- asset: "Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V"; "The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key."
- inspected: not applicable (copied from TeX source)
- notice: The definition in the authors' words: weights from query-key match, output a weighted sum of values.
- limits: none
- rights: quotation with attribution

### E3: Reason for 1/sqrt(d_k)
- claim: C3 (support)
- type: quote+metric
- source: same — §3.2.1, footnote 4
- asset: if components of q and k are independent with mean 0 and variance 1, q·k "has mean 0 and variance d_k"; authors "suspect" large dot products push softmax "into regions where it has extremely small gradients".
- notice: Scaling keeps the score spread independent of vector size.
- limits: Stated as a suspicion with a statistical argument, not an ablation.
- rights: quotation

### E4: Causal mask
- claim: C4 (support)
- type: quote
- source: same — §3.2.3
- asset: "We implement this inside of scaled dot-product attention by masking out (setting to −∞) all values in the input of the softmax which correspond to illegal connections."
- notice: −∞ before softmax becomes weight exactly 0.
- rights: quotation

### E5: Head dimensions
- claim: C5 (support)
- type: metric
- source: Vaswani §3.2.2; Brown et al. Table 2.1 — https://arxiv.org/abs/2005.14165 (v4)
- asset: Transformer base: h = 8 heads, d_k = d_v = 64, d_model = 512. GPT-3 175B: 96 layers, d_model = 12288, 96 heads, d_head = 128. Single-head variant 0.9 BLEU worse than best (Vaswani Table 3 row A, EN-DE dev).
- notice: Head count and size grow with the model; the mechanism is unchanged.
- limits: BLEU difference is a translation metric on one dev set.
- rights: facts with attribution

### E6: Attention following a long-distance dependency
- claim: C7 (support, qualitative)
- type: figure
- source: Vaswani appendix Figure 3, p. 13
- asset: ../assets/vaswani-fig3-making-more-difficult.png (rendered 3x, 1236×816)
- inspected: opened at full size; both token rows and colour bars visible; full caption included
- notice: From the word "making", several heads (colours) put weight on "more" and "difficult" eight tokens later, completing "making … more difficult".
- limits: One sentence chosen by the authors, encoder layer 5 of 6 of a translation model; shows where weight went, not why the output changed.
- rights: Google figure permission as E1

### E7: Complexity / sequential operations / path length table
- claim: C9, C12 (support)
- type: table
- source: Vaswani Table 1, p. 6
- asset: ../assets/vaswani-table1-complexity.png (rendered 3x, 1236×384). Values: Self-Attention O(n²·d), O(1), O(1); Recurrent O(n·d²), O(n), O(n); Convolutional O(k·n·d²), O(1), O(log_k(n)); Self-Attention (restricted) O(r·n·d), O(1), O(n/r).
- inspected: opened at full size; all four rows and three columns visible
- notice: Recurrent layers need n steps in a row; self-attention needs a constant number, and any two positions are one step apart. The price is the n² in the first column.
- limits: Asymptotic analysis; no wall-clock measurements.
- rights: Google table permission as E1

### E8: Recurrence blocks parallel training
- claim: C9 (support)
- type: quote
- source: Vaswani §1
- asset: "This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths"
- rights: quotation

### E9: LSTM vs Transformer scaling and context use
- claim: C10 (support)
- type: figure
- source: Scaling Laws for Neural Language Models — https://arxiv.org/abs/2001.08361 (v1)
- locator: Figure 7, p. 9; §3.2.1
- asset: ../assets/kaplan-fig7-lstm-vs-transformer.png (rendered from the authors' figure file in the e-print bundle at 2.5x, 2437×779)
- inspected: opened at full size; both panels, legends, axes visible; compared with published PDF page 9 — identical
- notice: Left, at every size the transformer line sits below the LSTMs and the gap widens. Right, LSTM per-token loss stops improving after <100 tokens while the transformer keeps dropping out to token 1000.
- limits: WebText2 data, ~1024 token context, models up to ~1.5B non-embedding parameters; right panel's tick labels 4 and 5 appear swapped in the source.
- rights: arXiv non-exclusive distribution licence only; reuse rights unstated — embedded with attribution

### E10: Smooth power laws
- claim: C10 (support)
- type: quote
- source: Kaplan et al. abstract
- asset: "The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude."
- limits: Loss, not task ability; the best split of compute was later revised (Hoffmann et al. 2022).
- rights: quotation

### E11: ChatGPT lineage
- claim: C11 (support)
- type: quote
- source: ChatGPT: Optimizing Language Models for Dialogue (archived)
- asset: "ChatGPT is fine-tuned from a model in the GPT-3.5 series, which finished training in early 2022." and "We trained this model using Reinforcement Learning from Human Feedback (RLHF), using the same methods as InstructGPT"
- limits: no architecture details
- rights: quotation

### E12: Induction heads
- claim: C7 (support, conditional)
- type: quote
- source: In-context Learning and Induction Heads
- asset: given "The cat sat on the mat. The cat …", induction heads "will promote the continuation “sat on the mat”"; summary pattern `[A][B]…[A]` completed with `[B]`; authors call large-model evidence "preliminary and indirect".
- limits: strongest evidence in small attention-only models
- rights: quotation

### E13: Attention is not explanation
- claim: C8 (qualify)
- type: quote
- source: Jain & Wallace, NAACL 2019
- asset: "learned attention weights are frequently uncorrelated with gradient-based measures of feature importance"
- limits: recurrent/convolutional encoders with attention on classification
- rights: quotation

### E14: Toy attention calculation
- claim: C2, C4 (context)
- type: generated
- asset: hand-chosen 2-d query/key vectors and 3-d value vectors for five tokens, computed in-page; not from any model
- notice: lets the reader see the scores, softmax weights, mask, and weighted sum with real arithmetic.

## Not extracted
- Induction-heads illustration (inline base64 image): decoding failed (truncated base64 from page); used quotations instead.
- Kaplan Figure 1 (power laws): omitted; Figure 7 carries the architecture comparison the question needs.
- GPT-3 scaling figures: omitted; not needed for the attention question.
