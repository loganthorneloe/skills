# Source audit records (accessed 2026-11-03)

### Attention Is All You Need
- url: https://arxiv.org/abs/1706.03762; text read from: arXiv e-print LaTeX source (v7 bundle) and v7 PDF
- byline: Ashish Vaswani, Noam Shazeer, and colleagues (8 authors, Google Brain / Google Research / University of Toronto) · conference paper · NeurIPS 2017 (arXiv preprint) · June 2017 (v1 12 Jun 2017; v7 Aug 2023)
- verdicts: C1 pass (embeddings, softmax over next-token probabilities; context only); C2 pass; C3 pass (stated as authors' suspicion with variance argument); C4 pass; C5 pass; C6 pass; C7 conditional (qualitative examples chosen by authors from a translation encoder, not a GPT model); C9 pass; C12 pass
- use: §3.2.1 Eq. 1 and footnote 4; §3.2.2; §3.2.3 masking; §3.4–3.5; §4 and Table 1; §5.4 training time; appendix Figure 3; Figure 2; Table 3 row (A) single-head −0.9 BLEU
- credibility: The authors designed, trained, and measured the model the paper defines; it is the primary specification of the Transformer.
- contribution: Defines scaled dot-product and multi-head attention, the causal mask, positional encodings, and gives asymptotic cost, sequential-operation, and path-length comparisons with recurrent and convolutional layers; reports translation results (28.4 BLEU EN-DE, base model 12 h on 8 P100 GPUs).
- limits: Built for translation (encoder-decoder), not a chat model; Table 1 is asymptotic analysis, not measured speed; visualisation figures are hand-picked examples. Errata search: none found affecting the cited sections. Spot-checked: Eq. 1, h=8, d_k=64, 12 h / 8 P100 against source TeX.
- read: full for §1–4, §5.4, appendix; skimmed results · version v7 · via arXiv e-print

### Scaling Laws for Neural Language Models
- url: https://arxiv.org/abs/2001.08361; text read from: arXiv e-print source and v1 PDF
- byline: Jared Kaplan, Sam McCandlish, and colleagues (OpenAI / Johns Hopkins) · preprint · arXiv · January 2020
- verdicts: C1 pass (autoregressive cross-entropy over 1024-token context, BPE 50,257 vocab); C10 pass for WebText2-trained models up to ~1.5B non-embedding parameters; conditional for "why ChatGPT" (correlates scale with loss; does not test chat ability)
- use: abstract, §1.1 summary, §3.2.1 and Figure 7 (LSTM vs Transformer)
- credibility: OpenAI researchers who trained hundreds of models and report the measured curves directly; LSTM comparison run by an author (T. Henighan) on the same data and context.
- contribution: Test loss follows power laws in parameters, data, and compute over many orders of magnitude; LSTMs match transformers on early tokens of a context but plateau after <100 tokens while transformers keep improving.
- limits: Loss is a proxy for capability, not task performance. The compute-optimal split between model size and data was later revised by Hoffmann et al. 2022 ("the model size and the number of training tokens should be scaled equally"; read abstract only), which does not affect Figure 7. Figure 7 right panel's y-axis tick labels read 6,4,5,3,2 top to bottom in both the figure file and the published PDF (an apparent labeling error in the source); the trend comparison is unaffected. LSTM range smaller (to ~2×10^8).
- read: partial (abstract, §1, §2 setup, §3.1–3.2.1 read; rest skimmed) · version v1

### Language Models are Few-Shot Learners
- url: https://arxiv.org/abs/2005.14165; text read from: arXiv v4 PDF
- byline: Tom B. Brown, Benjamin Mann, and colleagues (OpenAI) · conference paper · NeurIPS 2020 (arXiv) · May 2020
- verdicts: C1 pass ("autoregressive language model"); C5 pass (96 layers, d_model 12288, 96 heads, d_head 128); C11 pass for GPT-3's architecture; C11 conditional for GPT-3.5 (paper predates it)
- use: abstract; §2.1 Model and Architectures; Table 2.1
- credibility: The team that trained GPT-3 describing its own model.
- contribution: GPT-3 uses the GPT-2 transformer architecture with alternating dense and locally banded sparse attention; 175B parameters; few-shot behaviour from text prompts alone.
- limits: Says nothing about GPT-3.5 or ChatGPT's exact architecture. Errata search: none affecting §2.1.
- read: partial (abstract, §1 intro, §2.1, Table 2.1) · version v4

### ChatGPT: Optimizing Language Models for Dialogue
- url: https://openai.com/index/chatgpt/; text read from: Internet Archive copy of https://openai.com/blog/chatgpt/ (canonical page returned 403)
- byline: OpenAI · company announcement · OpenAI blog · November 30, 2022
- verdicts: C11 pass (fine-tuned from GPT-3.5 series with supervised fine-tuning + RLHF, same methods as InstructGPT); C11 conditional for architecture (announcement does not say "transformer")
- use: Methods and Limitations sections
- credibility: First-party description by the company that built and released ChatGPT.
- contribution: States the training recipe and lineage: "ChatGPT is fine-tuned from a model in the GPT-3.5 series, which finished training in early 2022."
- limits: Marketing-adjacent first-party post with no architecture details; the transformer link rests on the GPT-3 paper and OpenAI's series naming, not on this page.
- read: full (archived copy) · via web.archive.org

### In-context Learning and Induction Heads
- url: https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html
- byline: Catherine Olsson, Nelson Elhage, and colleagues (Anthropic) · research article · Transformer Circuits Thread · March 2022
- verdicts: C7 conditional (causal evidence for small attention-only models; indirect for large models)
- use: definition of induction heads; summary of six arguments; repeated-sequence example "The cat sat on the mat. The cat …"
- credibility: Authors trained many model snapshots and ran ablations directly; they state the strength of each argument themselves.
- contribution: Defines induction heads (prefix matching + copying, completing [A][B]…[A] with [B]) and links their formation to a sharp gain in in-context learning.
- limits: Authors call large-model evidence "preliminary and indirect". Not peer reviewed in a conventional venue.
- read: partial (first ~100k of ~395k characters plus targeted passages) · via canonical page

### Attention is not Explanation
- url: https://aclanthology.org/N19-1357/
- byline: Sarthak Jain and Byron C. Wallace · conference long paper · NAACL 2019, Association for Computational Linguistics · June 2019
- verdicts: C8 conditional (tested BiLSTM/CNN-style encoders with attention on classification tasks, not GPT-style transformers)
- use: abstract; §1 Figure 1 discussion; §3 setup
- credibility: Peer-reviewed empirical study that measured agreement of attention weights with gradient-based importance and built counterfactual attention distributions.
- contribution: Attention weights frequently disagree with other importance measures, and very different attention distributions can yield the same prediction.
- limits: Not transformer language models; later work (e.g. Wiegreffe & Pinter 2019, not read) disputes how strongly to read it. Use only to say an attention picture is not proof of why a model answered.
- read: partial (abstract, §1–3) · via ACL Anthology PDF

## Gaps
- C11: only conditional sources for GPT-3.5's exact architecture — OpenAI has not published it; stated as lineage from GPT-3.
- C7: only conditional sources — interpretable head behaviour shown by examples and small-model ablations.
- C8: only conditional sources — evidence is from non-transformer models.

Addendum (Kaplan): also pass for C13 (new claim) "feed-forward layers hold two thirds of each layer's parameters in standard sizing" — §2.1 Table 1: attention 4·n_layer·d_model², feed-forward 8·n_layer·d_model² with d_attn = d_ff/4 = d_model (N ≈ 12 n_layer d_model²).
