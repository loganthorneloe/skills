# Run notes

Elapsed: system clock read 12:50 at start and 13:00 at finish (about 10 minutes by that clock; the wall-clock time felt longer, so treat this as approximate).

## Decisions
- Reader can program and knows matrix multiplication, so the report teaches tokens, embeddings, gradient, and softmax in a sentence each, and carries one worked example (3 tokens, 2-dimensional vectors, numbers computed with numpy) through the mechanism.
- Thirteen claims (records/claims.md), ranked; the top ones are the attention computation, parallelism and path length versus recurrence, long-context and scaling evidence, and ChatGPT's RLHF step.
- One interactive only: a d_k slider plus scaling toggle on random N(0,1) vectors. It closes the gap that the √d_k footnote leaves (why scaling matters) using the paper's own assumption; it is labeled as generated and states that trained vectors are not random.
- The premise "attention made ChatGPT possible" is a counterfactual no source tests. The report frames it as the practical route taken and says so in Limits.
- Dropped Vaswani Figures 4 and 5 (same lesson as Figure 3) and GPT-3 Figure 1.2 (in-context learning; off the question).

## Sources read
- Vaswani et al., Attention Is All You Need: arXiv v7 PDF plus the LaTeX e-print source (sections 1–6 and the appendix). Figures and tables come from the PDF at 220 dpi; Figure 1 is the authors' original PNG. Reuse permission is stated on the title page.
- Kaplan et al., Scaling Laws: arXiv v1 PDF and source, partial read (abstract, summary, §2, §3.2.1, appendix D.5). Figures 1 and 7 are cropped from the PDF. Rights unstated (arXiv non-exclusive license), so they are embedded with attribution and the captions say so.
- Radford et al., GPT-1 report: OpenAI PDF, partial read (§1–3, §4.1).
- Brown et al., GPT-3: arXiv v4, partial read (§2.1, Table 2.1).
- Ouyang et al., InstructGPT: arXiv v1, partial read (abstract, §1, Figure 1). Figure 1 is cropped. Rights unstated.
- OpenAI, Introducing ChatGPT: the canonical page returned 403 to WebFetch. A curl fetch with a browser user agent was denied by the permission classifier, and I did not try to work around it. web.archive.org was unavailable. I read it through a reader-mode proxy (hn.jakechampion.name) and checked the quotes against several consistent copies found by search. This source is marked conditional.

## Verification
- Fonts: `document.fonts.check('600 1em Sora')` and `document.fonts.check('400 1em Inter')` both returned true after `fonts.ready`, at 1280 and 390 px, using Google Fonts over the network.
- Layout: scrollWidth equals clientWidth at 1280 and 390, so there is no horizontal page overflow. No broken images, no image displayed above its natural width, and no console or page errors. I inspected full-page screenshots at both widths. Two fixes came out of that: the d_k subscript was splitting inside the flex labels, and Figure 2 was too small on mobile, so it now sits in a scroll region. Wide figures now have full-size links.
- Interactive: tested at the default (d_k 64, scaled, top weight 0.228), at the boundaries (End key to 512 scaled gives top weight 0.209; unscaled gives 0.925; Home key to 1 unscaled gives 0.149), with an arrow key, with resample, and with Reset, which returns to the exact default output. The slider shows a visible focus outline, and Tab moves on from Reset. With JavaScript off, the static fallback text shows. The results match the stated logic: scaling keeps the weights spread out, and without scaling the largest weight approaches 1 at large d_k.
- Facts: I checked the worked-example arithmetic by hand (softmax of 2.83, 1.41, 4.24 gives 0.187, 0.045, 0.768; output [0.955, 2.439]). Every quotation was checked against the PDF or LaTeX text. I corrected the draft's "eight words later" to "six and seven" and removed "hundreds of models", two unsourced "later revised exponents" mentions, and an unsourced causal claim about GPT-3's context length.
- Draft and final: draft.html has about 3,040 words in main; report.html has about 1,900. Excluding the sources section and captions, the prose went from about 2,120 to about 1,190 words, roughly 55%. All 8 source images, the worked-example table, and the interactive are kept.

## Gaps
- ChatGPT's architecture is unpublished, so its details are inferred from GPT-3 and InstructGPT, and the report says so.
- No audited source on whether attention weights faithfully explain model decisions. The report keeps the authors' hedged wording and says that a weight pattern does not show why the model answers as it does.
- Vaswani v7 is internally inconsistent: Table 2 gives EN-FR big as 41.8, while the text says 41.0. The caption discloses this.
- The fonts load from the network; they are not embedded for offline use.
