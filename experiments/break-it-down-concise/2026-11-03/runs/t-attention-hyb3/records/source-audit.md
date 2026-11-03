# Source audit records (accessed 2026-11-03)

### Attention Is All You Need
- url: https://arxiv.org/abs/1706.03762; text read from: arXiv PDF v7 and arXiv e-print LaTeX source v7
- byline: Ashish Vaswani, Noam Shazeer, and colleagues (Google Brain, Google Research, University of Toronto) · conference paper · NeurIPS 2017 (Advances in Neural Information Processing Systems 30) · first posted June 2017 (v1), v7 August 2023
- verdicts: C1 pass; C2 pass (authors' stated hypothesis plus variance argument; "We suspect"); C3 pass; C4 pass; C5 pass; C6 pass; C7 pass (asymptotic, per-layer analysis); C8 pass (2014 WMT benchmarks, historical); C12 conditional (authors say heads "appear"/"seem"; qualitative examples only); C13 pass (Table 1 complexity)
- use: §3.1–3.5 (architecture, Eq. 1, footnote 4, multi-head, masking, positional encoding), §4 Table 1, §6.1 Table 2, Figure 1, Figure 2, appendix Figures 3–5
- credibility: The authors designed, trained, and measured the model; this is the primary description of the architecture every later transformer cites.
- contribution: Defines scaled dot-product and multi-head attention, the causal mask, positional encoding; argues parallelism and path length; reports translation results and training-cost estimates.
- limits: Encoder-decoder translation model, not a chat model. Training FLOPs are estimates (time × GPUs × assumed TFLOPS). In v7, Table 2 lists EN-FR big at 41.8 BLEU while §6.1 text says 41.0 (internal inconsistency; avoid quoting EN-FR big). sqrt(d_k) rationale is a stated suspicion. Attention visualizations are hand-picked examples. Retraction/errata search: none found beyond version revisions.
- read: full for §1–6 and appendix visualizations; skimmed §5 training details · version v7 · via arXiv PDF + LaTeX source

### Scaling Laws for Neural Language Models
- url: https://arxiv.org/abs/2001.08361; text read from: arXiv PDF v1 and e-print source
- byline: Jared Kaplan, Sam McCandlish, and colleagues (OpenAI, Johns Hopkins University) · preprint · arXiv · January 2020
- verdicts: C9 pass (decoder-only Transformers vs LSTMs on WebText2, 1024-token context, up to ~1.5B params)
- use: Figure 1 (power laws), Figure 7 and §3.2.1 (LSTM vs Transformer), §2 setup
- credibility: The team trained the models themselves across many sizes; the LSTM comparison uses the same dataset and context length.
- contribution: Shows smooth power-law loss improvements with N, D, C, and that Transformers keep improving on later tokens while LSTMs plateau after under 100 tokens.
- limits: Measures test loss (cross-entropy), not usefulness. Models up to ~1.5B parameters; exponents later revised by other work (e.g., Hoffmann et al. 2022 compute-optimal training) — do not state the exact exponents as current. Preprint by the lab that built GPT-3 (interest in scaling). Right panel of Fig. 7 has unusual y-axis tick ordering in the source.
- read: partial (abstract, §1 summary, §2 setup, §3.2.1, appendix D.5 captions) · version v1

### Language Models are Few-Shot Learners
- url: https://arxiv.org/abs/2005.14165; text read from: arXiv PDF v4
- byline: Tom B. Brown, Benjamin Mann, and colleagues (OpenAI) · conference paper · NeurIPS 2020 · first posted May 2020
- verdicts: C10 pass (architecture facts for GPT-3)
- use: §2.1 and Table 2.1
- credibility: OpenAI's own technical report on the model it trained.
- contribution: GPT-3 uses the GPT-2 transformer with alternating dense and locally banded sparse attention; 8 sizes up to 175B (96 layers, d_model 12288, 96 heads, d_head 128); 2048-token context; trained on 300B tokens.
- limits: GPT-3 is not ChatGPT; ChatGPT's exact model is undisclosed.
- read: partial (abstract, §1 framing, §2.1, Table 2.1) · version v4

### Improving Language Understanding by Generative Pre-Training
- url: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf; text read from: same
- byline: Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever (OpenAI) · technical report · OpenAI · June 2018
- verdicts: C10 pass (decoder-only transformer with masked self-attention); C9 conditional (authors' claim that transformers capture longer-range structure than LSTMs; corroborate with Kaplan Fig. 7)
- use: §3.1 Eq. 1–2, §2 related work, §4.1 model specifications
- credibility: The first GPT; authors built and trained it.
- contribution: Next-token objective over a context window; 12-layer decoder-only transformer with masked self-attention; chose transformer for "more structured memory" for long-term dependencies.
- limits: Not peer reviewed; small model (12 layers) by later standards.
- read: partial (abstract, §1–3, §4.1) · version: only one

### Training language models to follow instructions with human feedback
- url: https://arxiv.org/abs/2203.02155; text read from: arXiv PDF v1
- byline: Long Ouyang, Jeff Wu, and colleagues (OpenAI) · conference paper · NeurIPS 2022 · first posted March 2022
- verdicts: C11 pass (RLHF method and effect for InstructGPT)
- use: abstract, Figure 1, §1 method description
- credibility: OpenAI team that built InstructGPT; human evaluations with stated confidence intervals.
- contribution: Supervised fine-tuning on labeler demonstrations, reward model on rankings, PPO; 1.3B InstructGPT preferred over 175B GPT-3 by labelers on API prompts.
- limits: Preference judged by ~40 contractors on OpenAI API prompt distribution; win rate is a preference measure, not correctness. InstructGPT is ChatGPT's sibling, not ChatGPT.
- read: partial (abstract, §1, Figure 1 and caption) · version v1

### Introducing ChatGPT
- url: https://openai.com/index/chatgpt/; text read from: reader-mode copy https://hn.jakechampion.name/reader/https://openai.com/index/chatgpt (canonical returned HTTP 403 to the fetch tool)
- byline: OpenAI · company blog post · OpenAI · November 2022 (page shows only "2022"; November 30, 2022 launch date from multiple consistent secondary copies, (unverified) against canonical page)
- verdicts: C11 conditional (via mirror; quotes checked against several independent copies from search, wording consistent)
- use: Methods section quotes; Limitations first item
- credibility: The company's own announcement of how it trained the product.
- contribution: ChatGPT trained with RLHF using InstructGPT methods with different data collection; fine-tuned from a GPT-3.5 series model.
- limits: No architecture details; marketing venue; read through a third-party reader proxy, not canonical page.
- read: partial (methods and limitations quotes via fetch-tool summary of mirror) · via reader proxy

## Gaps
- C11: only conditional source for ChatGPT's specific training (canonical page blocked) — corroborated by InstructGPT paper for method.
- Disputed premise: "attention made ChatGPT possible" is a counterfactual no source tests. Sources show attention was the architecture used and that it trained in parallel, used long context better than LSTMs, and scaled smoothly; they do not show no other architecture could have worked.
- C12: no source checked on whether attention weights faithfully explain predictions; report keeps the authors' hedged wording.
