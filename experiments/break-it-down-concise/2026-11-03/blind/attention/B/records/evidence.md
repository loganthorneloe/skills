# Evidence records

### E1: Scaled dot-product attention diagram and multi-head diagram
- claim: C3, C4, C5 (support)
- type: figure
- source: Attention Is All You Need — https://arxiv.org/abs/1706.03762 (v7)
- locator: Figure 2 (left and right); files Figures/ModalNet-19.png, ModalNet-20.png in e-print
- asset: assets/vaswani-fig2-scaled-dot-product.png (445x884), assets/vaswani-fig2-multi-head.png (835x1282)
- inspected: opened left panel at full size; all boxes and Q/K/V labels visible; right panel original author PNG
- notice: The operation is two matrix multiplications with a scale, optional mask and softmax between them; multi-head wraps h copies with their own linear projections.
- limits: Diagram omits the learned projections in the left panel (they appear on the right).
- rights: Paper states Google grants permission to reproduce tables and figures with attribution for journalistic or scholarly works.

### E2: Equation 1 and the scaling footnote
- claim: C3 (support)
- type: quote
- source: Attention Is All You Need (v7)
- locator: Sec 3.2.1, Eq. (1) and footnote 4
- asset: "Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V"; footnote: if components of q and k are independent with mean 0 and variance 1, q·k "has mean 0 and variance d_k".
- inspected: not applicable
- notice: The formula the whole report unpacks; footnote explains the sqrt(d_k).
- limits: none
- rights: as E1

### E3: Masking quote
- claim: C5 (support)
- type: quote
- source: Attention Is All You Need (v7)
- locator: Sec 3.2.3, third bullet
- asset: "masking out (setting to −∞) all values in the input of the softmax which correspond to illegal connections"
- inspected: not applicable
- notice: Causal mask is done inside attention, before softmax.
- limits: Paper's decoder is part of an encoder-decoder; GPT models use only this masked decoder-style stack (Kaplan Sec 2: "decoder-only").
- rights: as E1

### E4: Table 1 complexity, sequential operations, path length
- claim: C7, C11 (support)
- type: table (rebuilt as HTML from LaTeX source, values exact)
- source: Attention Is All You Need (v7)
- locator: Table 1, Sec 4
- asset: Self-Attention O(n^2·d), O(1), O(1); Recurrent O(n·d^2), O(n), O(n); Convolutional O(k·n·d^2), O(1), O(log_k(n)); Self-Attention (restricted) O(r·n·d), O(1), O(n/r)
- inspected: transcribed from LaTeX source and compared row by row
- notice: Recurrence needs n sequential steps; attention needs a constant number, at the cost of n^2 work.
- limits: Asymptotic analysis, per layer.
- rights: as E1

### E5: Training cost and quality metric
- claim: C7 (support)
- type: metric
- source: Attention Is All You Need (v7)
- locator: Sec 6.1 and Table 2
- asset: Transformer (big) 28.4 BLEU EN-DE newstest2014, +>2.0 BLEU over best previous incl. ensembles; trained 3.5 days on 8 P100 GPUs; estimated 2.3·10^19 FLOPs vs e.g. GNMT+RL 2.3·10^19 (single) and ConvS2S ensemble 7.7·10^19; base model 3.3·10^18 FLOPs at 27.3 BLEU.
- inspected: not applicable
- notice: Better quality for equal or less compute than recurrent and convolutional competitors.
- limits: FLOPs are author estimates; EN-FR number inconsistent across text (41.0 vs 41.8) so omitted.
- rights: as E1

### E6: Attention head resolving "its"
- claim: C3, C11 (support / qualify)
- type: figure
- source: Attention Is All You Need (v7)
- locator: Appendix, Figure 4 bottom (vis/anaphora_resolution2_new.pdf)
- asset: assets/vaswani-fig4-its-heads.png (877x643, rendered at 200 dpi from author PDF; paper trims ~37pt of top title, kept here)
- inspected: opened full size; all tokens readable, both head colors visible
- notice: From the word "its", two heads in layer 5 put nearly all weight on "Law" and "application" — the words "its" refers to and modifies.
- limits: Authors say heads are "apparently" involved in anaphora resolution; a hand-picked example.
- rights: as E1

### E7: LSTM vs Transformer
- claim: C8 (support)
- type: figure
- source: Scaling Laws for Neural Language Models — https://arxiv.org/abs/2001.08361 (v1)
- locator: Figure 7, Sec 3.2.1 (figures/LSTMvsTransformerSummary.pdf)
- asset: assets/kaplan-fig7-lstm-vs-transformer.png (2708x865, 200 dpi render)
- inspected: opened full size; axes, legends and labels intact
- notice: Right panel: LSTM per-token loss flattens after ~100 tokens of context while Transformer loss keeps falling to token 1000; left: Transformers reach lower loss at every size.
- limits: Small models (≤~1B), one dataset (WebText2).
- rights: arXiv non-exclusive distribution license; reuse terms unstated — embedded with attribution.

### E8: Power laws
- claim: C8 (support)
- type: figure
- source: Scaling Laws for Neural Language Models (v1)
- locator: Figure 1
- asset: assets/kaplan-fig1-power-laws.png (2502x760)
- inspected: opened full size; three panels with fits visible
- notice: Straight lines on log-log axes: loss falls predictably as compute, data, parameters grow.
- limits: Compute panel shows predicted compute at small batch size (author footnote); exponents later revised.
- rights: rights unstated (arXiv license)

### E9: GPT-3 architecture metric
- claim: C9 (support)
- type: metric+quote
- source: Language Models are Few-Shot Learners — https://arxiv.org/abs/2005.14165 (v4)
- locator: Sec 2.1, Table 2.1
- asset: GPT-3 175B: 96 layers, d_model 12288, 96 heads, d_head 128, context 2048 tokens; trained on 300B tokens; "alternating dense and locally banded sparse attention patterns".
- inspected: not applicable
- notice: The 2017 mechanism at scale: 96 heads x 96 layers.
- limits: GPT-3, not GPT-3.5.
- rights: rights unstated

### E10: RLHF three-step diagram
- claim: C10 (support)
- type: figure
- source: Training language models to follow instructions with human feedback — https://arxiv.org/abs/2203.02155 (v1)
- locator: Figure 2 (figs/InstructGPT_Diagram3.1.pdf)
- asset: assets/ouyang-fig2-rlhf-steps.png (2200x1328, cropped whitespace margins only)
- inspected: opened after recrop; all three steps and bottom text "using PPO." visible
- notice: After pretraining, humans demonstrate and rank answers; a reward model trained on rankings steers the model.
- limits: InstructGPT, sibling of ChatGPT; ChatGPT used conversation data.
- rights: rights unstated

### E11: ChatGPT methods quote
- claim: C10 (support)
- type: quote
- source: ChatGPT announcement — archived https://web.archive.org/web/20221130180912/https://openai.com/blog/chatgpt/
- locator: Methods section
- asset: "ChatGPT is fine-tuned from a model in the GPT-3.5 series, which finished training in early 2022." and "using the same methods as InstructGPT"
- inspected: not applicable
- notice: Product = pretrained model + RLHF.
- limits: no architecture details.
- rights: short quotation with attribution

### E12: InstructGPT preference metric
- claim: C10 (support)
- type: metric
- source: Ouyang et al. (v1), Sec 1 results
- asset: 1.3B InstructGPT outputs preferred to 175B GPT-3 outputs by labelers; 175B InstructGPT preferred to 175B GPT-3 85 ± 3% of the time (95% CI), same architecture.
- inspected: not applicable
- notice: Same architecture, different training -> very different usefulness.
- limits: labeler preference on API prompt distribution.
- rights: n/a (metric)

## Gaps / omitted
- Fig. 1 of Vaswani (full encoder-decoder architecture) omitted: the report covers decoder-only models, and the full diagram adds encoder parts the reader does not need.
- No exhibit for GPT-3.5 architecture (unpublished).
