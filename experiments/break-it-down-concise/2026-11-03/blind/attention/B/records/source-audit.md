# Source audit records

Claims
- C1: A language model turns text into tokens, represents each token as a vector, and is trained to predict the next token.
- C2: Before the Transformer, recurrent networks processed a sequence one position at a time, which prevented parallel computation within a training example.
- C3: Scaled dot-product attention computes softmax(QK^T / sqrt(d_k)) V: a weighted sum of value vectors, with weights from query-key dot products; the sqrt(d_k) scaling keeps softmax out of tiny-gradient regions.
- C4: Queries, keys, and values come from learned linear projections; multi-head attention runs several such attentions in parallel and concatenates them.
- C5: For next-token prediction, a causal mask (set to -inf before softmax) stops a position from attending to later positions.
- C6: Attention is one sub-layer; each layer also has a position-wise feed-forward network, residual connections, and positional information must be added because attention ignores order.
- C7: Self-attention connects all positions with O(1) sequential operations and O(1) path length (vs O(n) for recurrence), is built from matrix multiplications, and reached better translation quality at a fraction of prior training cost.
- C8: Transformer language models use long contexts better than LSTMs and their loss falls as a smooth power law with parameters, data, and compute.
- C9: GPT-3 is a 175B-parameter decoder-only (autoregressive) Transformer with 96 layers, 96 heads, 2048-token context.
- C10: ChatGPT is a GPT-3.5-series model fine-tuned with RLHF using InstructGPT's methods; fine-tuning, not only architecture/scale, made it follow instructions.
- C11: Limits: per-layer attention cost grows with n^2; attention patterns are suggestive, not proof of what a model "understands".

### Attention Is All You Need
- url: https://arxiv.org/abs/1706.03762; text read from: arXiv e-print LaTeX source (v7)
- byline: Ashish Vaswani, Noam Shazeer, and colleagues (Google Brain / Google Research / U. Toronto) · conference paper · NeurIPS 2017 (arXiv preprint) · June 2017 (v7 August 2023)
- verdicts: C1 conditional (embeddings and next-token softmax described for translation decoder; language-model framing from Kaplan/GPT-3); C2 pass; C3 pass; C4 pass; C5 pass; C6 pass; C7 pass; C11 pass (n^2 complexity, Table 1; hedged "apparently" in attention-visualization captions)
- use: Sec 1; Sec 3.1–3.5 (Eq. 1, Fig. 2, footnote on dot-product variance, masking bullet); Sec 4 Table 1; Sec 6.1 Table 2 and training time; appendix attention visualizations (Figs 3–5)
- credibility: The authors designed, built and trained the architecture and report its own experiments; it is the primary definition of the Transformer.
- contribution: Defines scaled dot-product and multi-head attention, the causal mask, and the full layer; compares complexity, sequential operations and path length against recurrence; reports WMT 2014 translation quality and training cost.
- limits: Experiments are machine translation, not chat; the English-French BLEU appears as 41.0 in the body text and 41.8 in Table 2/abstract of v7 (search found no erratum), so that number is not used. Training-cost FLOPs are the authors' estimates (time x GPUs x assumed TFLOPS). Interpretability remarks are informal.
- read: partial (intro, architecture, why-self-attention, results, visualizations read in full; training details and model variations skimmed) · version v7 · via arXiv e-print source

### Scaling Laws for Neural Language Models
- url: https://arxiv.org/abs/2001.08361; text read from: arXiv e-print LaTeX source (v1)
- byline: Jared Kaplan, Sam McCandlish, and colleagues (OpenAI / Johns Hopkins) · preprint · arXiv · January 2020
- verdicts: C1 pass (autoregressive cross-entropy over 1024-token context, BPE tokens); C8 pass; C7 fail (not about parallelism)
- use: Sec 1 Fig. 1 and summary; Sec 2 setup; Sec 3.2.1 Fig. 7 (LSTM vs Transformer)
- credibility: The authors trained the hundreds of models they measure; primary empirical data.
- contribution: Shows test loss of decoder-only Transformers following power laws in N, D, C over many orders of magnitude, and that LSTMs match Transformers only on early context tokens.
- limits: Fits are empirical over their range (up to ~1.5B parameters, WebText2); later work (e.g. Chinchilla, 2022) revised the optimal data/parameter split, so the exact exponents are not presented as current; lower loss is a proxy for capability. LSTM comparison uses small models.
- read: partial (intro, summary, setup, Sec 3.2.1 read; appendices not read) · version v1 · via arXiv e-print source

### Language Models are Few-Shot Learners
- url: https://arxiv.org/abs/2005.14165; text read from: arXiv e-print LaTeX source (v4)
- byline: Tom B. Brown, Benjamin Mann, and colleagues (OpenAI) · conference paper · NeurIPS 2020 (arXiv preprint) · May 2020
- verdicts: C1 pass; C9 pass
- use: abstract; Sec 2.1 model and architectures; Table 2.1
- credibility: The OpenAI team that trained GPT-3 documents its own model.
- contribution: States GPT-3 uses the GPT-2 architecture with alternating dense and locally banded sparse attention, 175B parameters, 96 layers, 96 heads of dimension 128, 2048-token context, 300B training tokens.
- limits: Says nothing about ChatGPT or GPT-3.5 directly.
- read: partial (abstract, Sec 2.1, Table 2.1, model-training appendix line) · version v4 · via arXiv e-print source

### Training language models to follow instructions with human feedback
- url: https://arxiv.org/abs/2203.02155; text read from: arXiv e-print LaTeX source (v1)
- byline: Long Ouyang, Jeff Wu, and colleagues (OpenAI) · conference paper · NeurIPS 2022 (arXiv preprint) · March 2022
- verdicts: C10 pass
- use: abstract; Sec 1; Fig. 2 diagram; results summary (1.3B preferred to 175B GPT-3)
- credibility: The team that built InstructGPT describes its training procedure and human evaluations.
- contribution: Defines the three-step RLHF procedure; shows labelers prefer a 1.3B InstructGPT to 175B GPT-3 with the same architecture.
- limits: Preferences are from ~40 contractors on API prompts; aligns to "a specific group of people", per the authors.
- read: partial (abstract, intro, Fig. 2 caption; methods and results sections skimmed) · version v1 · via arXiv e-print source

### ChatGPT: Optimizing Language Models for Dialogue
- url: https://openai.com/index/chatgpt/; text read from: Internet Archive snapshot of https://openai.com/blog/chatgpt/ (2022-11-30) because the live page returned HTTP 403
- byline: OpenAI · company announcement · OpenAI blog · 30 November 2022
- verdicts: C10 pass; C9 conditional (post does not state GPT-3.5's architecture; link to Transformer rests on InstructGPT/GPT-3 lineage)
- use: Methods and Limitations sections
- credibility: First-party description of how the product was trained.
- contribution: States ChatGPT was trained with RLHF using InstructGPT's methods, fine-tuned from a GPT-3.5-series model that finished training in early 2022.
- limits: Marketing post, no technical detail on GPT-3.5 architecture or size; describes the 2022 launch model only.
- read: full (Methods, Limitations) · via web.archive.org

## Gaps
- C9: only conditional for GPT-3.5 itself — OpenAI has not published its architecture; the report says ChatGPT descends from the GPT-3 line, which is documented as a Transformer.
- C11: "attention maps are not explanations" literature (Jain & Wallace 2019) only skimmed at abstract level and concerns mostly RNN attention, so it is not cited; the report relies on Vaswani et al.'s own hedged wording.
