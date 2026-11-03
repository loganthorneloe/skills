# Evidence records

### E1: Scaled dot-product and multi-head attention diagram
- claim: C1, C3, C4 (support)
- type: figure
- source: Attention Is All You Need — https://arxiv.org/abs/1706.03762 (v7)
- locator: Figure 2, p. 4
- asset: assets/vaswani-fig2-attention.png (cropped from PDF at 220 dpi, caption excluded and rewritten)
- inspected: opened at full size; both panels, all boxes and Q/K/V labels visible
- notice: left panel is Eq. 1 as a pipeline — MatMul (QK^T), Scale, optional Mask, SoftMax, MatMul with V; right shows h copies run in parallel then concatenated
- limits: diagram, not data
- rights: "Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works" with attribution (title page, v7)

### E2: The attention equation
- claim: C1 (support)
- type: quote
- source: same, §3.2.1 Eq. 1
- asset: "Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V"; "The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key." (§3.2)
- inspected: not applicable
- notice: definition
- limits: none
- rights: quotation, short

### E3: Why scale by sqrt(d_k)
- claim: C2 (support)
- type: quote
- source: same, §3.2.1 and footnote 4
- asset: "We suspect that for large values of d_k, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients"; footnote: dot product of independent mean-0 variance-1 components "has mean 0 and variance d_k".
- notice: motivates the interactive
- limits: "We suspect" — hypothesis
- rights: short quote

### E4: Table 1 complexity, sequential ops, path length
- claim: C7, C13 (support)
- type: table
- source: same, Table 1, p. 6
- asset: assets/vaswani-table1-complexity.png; values Self-Attention O(n^2·d), O(1), O(1); Recurrent O(n·d^2), O(n), O(n); Convolutional O(k·n·d^2), O(1), O(log_k n); restricted O(r·n·d), O(1), O(n/r)
- inspected: opened full size; caption, header, 4 rows visible
- notice: attention's O(1) sequential ops and path length vs O(n) for recurrence; cost is the n^2 term
- limits: asymptotic per layer; constants and hardware ignored
- rights: Google permission as E1

### E5: Table 2 BLEU and training cost
- claim: C8 (support)
- type: table
- source: same, Table 2, p. 8
- asset: assets/vaswani-table2-bleu.png; EN-DE: Transformer big 28.4, base 27.3 vs best prior ensemble 26.36; base training 3.3e18 FLOPs vs e.g. GNMT+RL 2.3e19
- inspected: full size, all rows visible
- notice: base model beats prior ensembles on EN-DE at ~1/7 to 1/50 of their estimated FLOPs
- limits: FLOPs estimated; EN-FR big value inconsistent with text (41.8 vs 41.0); 2014 benchmark
- rights: Google permission

### E6: Attention head following 'making ... more difficult'
- claim: C12 (support, qualified)
- type: figure
- source: same, Figure 3, p. 13
- asset: assets/vaswani-fig3-making.png
- inspected: full size; tokens and caption readable
- notice: from 'making', several heads (colors) put weight on distant 'more' and 'difficult'
- limits: hand-picked example, encoder layer 5 of a translation model
- rights: Google permission

### E7: Transformer architecture
- claim: C5, C6 (context)
- type: figure
- source: same, Figure 1, p. 3; original file Figures/ModalNet-21.png from arXiv source
- asset: assets/vaswani-fig1-architecture.png (author's original 1520x2239 image)
- inspected: opened; all labels visible
- notice: attention is one sublayer beside Feed Forward, Add & Norm, stacked N times; positional encoding added to embeddings; GPT uses only a decoder-like stack without the cross-attention block
- limits: encoder-decoder, not GPT's decoder-only layout
- rights: Google permission

### E8: LSTM vs Transformer
- claim: C9 (support)
- type: figure
- source: Scaling Laws for Neural Language Models — https://arxiv.org/abs/2001.08361 (v1)
- locator: Figure 7, p. 9; §3.2.1
- asset: assets/kaplan-fig7-lstm-vs-transformer.png
- inspected: full size; both panels, legends, axes visible
- notice: left: at equal parameters Transformers reach lower loss and the gap widens; right: per-token loss of LSTMs flattens after <100 tokens, Transformer keeps falling to token 1000
- limits: loss on WebText2, models up to ~1e9 non-embedding params; right panel y-axis labels odd in source
- rights: arXiv non-exclusive distribution license; reuse rights unstated — embedded with attribution

### E9: Smooth power laws
- claim: C9 (support)
- type: figure
- source: same, Figure 1, p. 3
- asset: assets/kaplan-fig1-scaling.png
- inspected: full size; three panels and fit equations visible
- notice: loss falls along straight lines on log-log axes as compute, data, parameters grow
- limits: test loss, not capability; exponents later revised
- rights: rights unstated

### E10: GPT-3 dimensions
- claim: C10 (support)
- type: metric
- source: Language Models are Few-Shot Learners — https://arxiv.org/abs/2005.14165 (v4) §2.1, Table 2.1
- asset: 175.0B params, 96 layers, d_model 12288, 96 heads, d_head 128, context 2048 tokens, 300B training tokens
- notice: same mechanism, scaled
- limits: GPT-3, not ChatGPT
- rights: metric

### E11: GPT-1 decoder-only
- claim: C10 (support)
- type: quote
- source: Improving Language Understanding by Generative Pre-Training — §4.1
- asset: "We trained a 12-layer decoder-only transformer with masked self-attention heads"
- rights: short quote

### E12: InstructGPT human-preference win rate
- claim: C11 (support)
- type: figure
- source: Training language models to follow instructions with human feedback — https://arxiv.org/abs/2203.02155 (v1), Figure 1 p. 2
- asset: assets/instructgpt-fig1-winrate.png
- inspected: full size; legend, axes, error bars visible
- notice: at every size, RLHF models (PPO, PPO-ptx) are preferred over plain GPT-3 (GPT); 1.3B PPO-ptx beats 175B GPT
- limits: labeler preference on API prompts; 95% CIs shown
- rights: arXiv non-exclusive license; rights unstated — embedded with attribution

### E13: ChatGPT training
- claim: C11 (support)
- type: quote
- source: Introducing ChatGPT (via reader mirror)
- asset: "ChatGPT is fine-tuned from a model in the GPT-3.5 series, which finished training in early 2022."; trained "using Reinforcement Learning from Human Feedback (RLHF), using the same methods as InstructGPT"
- limits: mirror
- rights: short quote

### G1: Worked 3-token example (generated)
- claim: C1, C3
- type: generated — numbers computed with numpy (scratch run), X, W_Q, W_K, W_V chosen by hand
### G2: Scaling interactive (generated)
- claim: C2 — random N(0,1) vectors, real softmax; illustrates footnote 4

## Omitted
- Vaswani Figures 4–5 (anaphora, structure): same lesson as E6.
- GPT-3 Figure 1.2 in-context learning: off the attention question.
