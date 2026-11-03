# Run notes

Elapsed time: about 10–15 minutes wall clock by the system clock (11:25 to 11:36 CST, 2026-11-03).

## Decisions
- Reader: can write Python and call an API, no ML background. Carried one example throughout: a refund/order support assistant. Included a minimal Python eval loop because the reader codes.
- Claims C1–C11 (see records/source-audit.md). Ranked top: C4 error analysis, C2/C3 structure and graders, C7 outcome + pass^k for support, C6 judge validation. Minor: C5, C9, C10, C11.
- One interaction (confidence-interval calculator) because a beginner's most likely misreading is trusting small score changes on a 20–50 case suite. Uses the Wilson interval rather than Miller's normal approximation, since the paper's formula targets large n; disclosed on the page.
- Exhibits: Anthropic single-turn vs agent figure (original PNG), τ-bench Figures 4 and 5 rendered from the authors' e-print PDFs (Quick Look `qlmanage` at 1800px; `sips` produced blurry output and was discarded), Zheng et al. Table 2 rebuilt as HTML (default-prompt rows in the delivered version, all six rows in the draft), short quotes. Anthropic components figure downloaded but not used (redundant).
- Distilled report body (after sources) is ~1,590 words vs ~2,940 in the draft (~54%). Cut: duplicate explanation of why benchmarks don't help, "first week" closing section, full YAML (abridged), rename rows of the bias table, extra pass^k discussion, maintenance detail.

## Sources read
- Anthropic, "Demystifying evals for AI agents" (Jan 2026): full.
- Husain & Shankar, "AI Evals FAQ" (Sept 2026): fundamentals, error analysis, design, judge-trust sections; rest skimmed by heading.
- Yao et al., τ-bench (arXiv 2406.12045v1): main text full, appendix skimmed; e-print source downloaded for figures.
- Zheng et al., MT-Bench / LLM-as-a-judge (arXiv 2306.05685v4): abstract, §1, §3.3–3.4, §4.1–4.2.
- Miller, "Adding Error Bars to Evals" (arXiv 2411.00640v1): §1, §2.1, §4, conclusion.
- Targeted searches: τ-bench errata (found maintainers' note that original tasks are outdated; successors τ²/τ³ — secondary listing only), LLM-judge bias follow-ups (Shi et al. 2025, listing only, not read), Miller critiques (none found).
- Not used: Hamel's original "Your AI Product Needs Evals" (downloaded, superseded by FAQ for this purpose).

## Verification
- Playwright Chromium at 1280px and 390px, report and draft: `document.fonts.check('600 1em Sora')` true, `'400 1em Inter'` true (after `document.fonts.ready`; fonts load from Google Fonts over the network). No horizontal page overflow (scrollWidth equals clientWidth at both widths), no broken images, no images rendered above natural size, no console errors.
- Screenshots inspected (scratch/v1280-*.png, v390-*.png): title/sources, wide figure (horizontal scroll region at 390px), tiles, donut figure, table, calculator. Fixed: table caption crowding following paragraph; tightened mobile table padding.
- Calculator: default 65–90% (n=40, 80%); n=400 → 76–84%; n=10, 0% → 0–28%; n=10, 100% → 72–100%; n=500, 50% → 46–54%; reset restores default; keyboard ArrowRight/ArrowLeft move sliders, Tab moves between them, focus outline visible; with JavaScript disabled the static default text and bar match the computed default. Values hand-checked against the Wilson formula for n=40, p=0.8.
- Facts checked against records: corrected "know in hours" to the source's "days vs weeks", added the scaffold change to the CORE-Bench 42%→95% anecdote, fixed initial static interval (63%→65%).

## Gaps
- C5 (binary over 1–5) and starting sizes rest on practitioner opinion only.
- Judge numbers are 2023 general-chat results; τ-bench numbers are 2024 models on since-corrected tasks. Both framed historically in the report.
- Anthropic figure and Zheng table: rights unstated; embedded/rebuilt with attribution and stated in captions.
- Fonts depend on network access to Google Fonts; not embedded.
- Shankar's and Miller's specific credentials were not independently verified; reader-facing entries avoid relying on them.
