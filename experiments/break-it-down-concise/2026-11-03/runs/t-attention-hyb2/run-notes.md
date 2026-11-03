# Run notes

Elapsed: roughly 12 minutes by system clock (12:37 to ~12:50 CST, 2026-11-03).

## Decisions
- Framed 12 claims (later 13), records in records/claims.md, records/source-audit.md, records/evidence.md.
- Primary sources over explainers: Vaswani et al. 2017 (read from arXiv e-print TeX + v7 PDF), Kaplan et al. 2020 (e-print + PDF), Brown et al. 2020 (§2.1, Table 2.1), OpenAI ChatGPT announcement (canonical page 403; read Internet Archive copy), Olsson et al. 2022 induction heads (partial read), Jain & Wallace 2019 (abstract, §1–3). Hoffmann et al. 2022 read at abstract level only and cited only for the revised compute split.
- Exhibits: Vaswani Fig. 2, Fig. 3, Table 1 (rendered from v7 PDF at 3x, Google's stated reproduction permission for figures/tables in scholarly or journalistic works); Kaplan Fig. 7 rendered from the authors' figure PDF in the e-print bundle (arXiv non-exclusive licence; reuse rights unstated, embedded with attribution and said so in caption). Quotes for the equation, mask, sqrt(d_k), ChatGPT lineage, induction heads, attention-not-explanation.
- One interactive: a hand-computable five-token attention row (query selector, causal mask, scaling toggle, reset). Labeled as invented numbers. Chosen because a reader who knows matmul but not ML benefits from seeing scores, softmax, mask, and weighted sum numerically; no measured relationship is invented.
- Draft (draft.html, ~2,360 prose words excluding sources/figures/demo) distilled to report.html (~1,200 prose words, ~51%). All four source visuals and the interactive kept.

## Verification
- Fact-check against records led to fixes: token distance in Figure 3 example (six/seven, not seven/eight); overclaim that n² is "the main reason" for context limits softened; FFN-parameter claim replaced by Kaplan §2.1 sizing (two thirds); induction-head link to GPT-3 few-shot softened; Hoffmann claim limited to abstract wording.
- Source anomaly recorded: Kaplan Fig. 7 right-panel y tick labels read 6,4,5,3,2 in both the figure file and published PDF; noted in caption.
- Rendering (Python Playwright, Chromium) at 1280 and 390 px: no horizontal page overflow, all 4 images load at or below natural size, no console errors or failed requests; document.fonts.check('600 1em Sora') and ('400 1em Inter') both true after fonts.ready at both widths. Screenshots inspected (scratch/final-*.png). On 390 px, wide figures sit in keyboard-focusable horizontal scroll regions (min-width 720px) with full-size links and a scroll hint.
- Controls: all 20 combinations (5 queries × mask × scale) match an independent Python reference for weights (±0.0015) and output vector; aria-pressed tracks selection; boundary state (query "The" + mask) gives weight 1.0; Reset restores default; Enter/Space operate buttons/checkboxes via keyboard; with JavaScript disabled the static default table and output match the computed default.

## Gaps
- GPT-3.5 architecture unpublished; transformer design stated as inferred from lineage.
- Induction-heads page read partially (~100k of ~395k chars plus targeted passages); its inline illustration could not be decoded, so quotes were used instead of a figure.
- Jain & Wallace concerns non-transformer classifiers; used only as a caution.
- Fonts load from Google Fonts (network dependency); report is otherwise self-contained with relative assets.
