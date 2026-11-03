# Run notes

Approximate elapsed time: about 25–30 minutes of wall-clock work (file timestamps 10:55 to ~11:03 local, plus earlier research turns).

## Decisions
- Seven claims (C1–C7): why evals, anatomy, criteria from error analysis, binary grading, LLM judges, support-agent evaluation, statistical noise. Records in records/source-audit.md and records/evidence.md.
- Primary research anchors: τ-bench (support-specific, CC BY 4.0, figures embedded), MT-Bench judge paper (bias and agreement numbers), Shankar et al. (criteria drift), Miller (error bars). Practitioner/vendor sources (Husain x2, Anthropic docs) used for method, marked conditional.
- Figures extracted from arXiv e-print source bundles (authors' vector PDFs rendered at 3x with PyMuPDF), not screenshots. MT-Bench figure has only arXiv's non-exclusive license; embedded with attribution and the caption says so.
- One generated diagram (eval loop SVG), one Python harness sketch (closes "how would I start" for a Python reader), one calculator (error bar vs. number of cases), using Miller's Bernoulli SE formula. Calculator shows a warning and drops the interval claim when fewer than 5 passes or failures.
- Light theme only (no dark mode requested).

## Sources read
- τ-bench arXiv 2406.12045 v1: LaTeX source, intro/construction/experiments/analysis read; appendix skimmed.
- Zheng et al. arXiv 2306.05685 v4: LaTeX source of judge-limitation section and agreement tables.
- Shankar et al. arXiv 2404.12272 v1: abstract + HTML via fetch summary (first ~100k chars).
- Miller arXiv 2411.00640 v1: LaTeX intro, Sec. 2.1, variance reduction, paired analysis, conclusion.
- Anthropic "Define success criteria and build evaluations": fetch summary, first ~100k of ~153k chars.
- Husain "Your AI Product Needs Evals" and "A Field Guide…": fetch-tool summaries only (partial reads).
- Corroboration searches: τ-bench task defects (HAL leaderboard / tau2-bench-verified, search snippets only); position-bias follow-up work (Shi et al., search snippets only). Neither is cited in the report body.

## Verification
- Playwright Chromium at 1280 and 390 px: no console/page errors; no horizontal page scroll at either width; document.fonts.check('600 1em Sora') and ('400 1em Inter') both true after fonts.ready (fonts loaded from Google Fonts over the network).
- All four images load at natural sizes (none upscaled). Wide τ-bench setup figure and the SVG diagram sit in keyboard-focusable horizontal scroll regions on narrow screens; tall MT-Bench figure links to full size.
- Calculator tested at default (50/80% → ±11.1, 68.9–91.1%), changed (400 cases → ±3.9), boundaries (100%, 0%, n=10, n=1000 via End key), reset, Tab focus order, and with JavaScript disabled (static default text matches computed default).
- Fact pass against records: removed unsourced claims ("newer models score higher", reviewer-disagreement aside, "later larger study" corroboration), attributed the policy-ablation interpretation to the authors, added the "deliberately similar answers" caveat to position-bias numbers.

## Gaps
- Husain posts and Anthropic docs read only through fetch summaries; quotes from them are as returned by the fetch tool (the Anthropic quote appears verbatim in the summary).
- C4 (binary vs Likert) rests only on practitioner advice.
- τ-bench numbers are 2024-model results; some original tasks later found defective (secondary sources, not verified).
- τ-bench figure numbering not confirmed against the compiled PDF; captions cite figures by content.
- Fonts depend on network access to Google Fonts; no offline embedding.
