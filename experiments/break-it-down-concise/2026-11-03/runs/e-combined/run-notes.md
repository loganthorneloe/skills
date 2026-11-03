# Run notes

## Decisions
- Claims C1–C8 defined up front (see records/source-audit.md); ranked C1, C2, C5, C3/C4, C7 as core; C6 and C8 kept short.
- Four sources kept: Anthropic "Demystifying evals for AI agents" (Jan 2026), τ-bench (Yao et al., arXiv v1, 2024), Zheng et al. "Judging LLM-as-a-Judge" (arXiv v4, NeurIPS 2023), Hamel Husain "Your AI Product Needs Evals" (Mar 2024). No source failed outright.
- One running example (cracked-mug refund) carried through; one Python code sample (illustrative, with user-supplied `run_assistant` and `call_model`) using the τ-bench pass^k estimator.
- Exhibits: Anthropic components diagram (E1), τ-bench pass^k figure (E2, measured; preferred over Anthropic's illustrative pass@k chart), Zheng Table 2 position bias (E3), τ-bench failure breakdown (E4). Quotes E5/E6 used inline.
- No generated visual or interaction: exhibits plus the code sample covered the comprehension gaps.
- Rights: τ-bench figures CC BY 4.0; Anthropic diagram and Zheng table rights unstated, embedded with attribution and captions say so.

## Sources read
- Anthropic post: full text (curl of canonical page); four figures downloaded from page image CDN at 1920 px.
- τ-bench: arXiv e-print LaTeX source (intro, construction, metric, results, failure analysis; appendix skimmed); figures rendered from authors' vector PDFs with PyMuPDF (installed in scratch venv). Authors' GitHub README checked: warns original tasks are outdated, fixed in τ³-bench.
- Zheng et al.: LaTeX source and PDF v4 (Sec. 3 biases, Sec. 4 agreement); Table 2 cropped from PDF page 5 at 250 dpi.
- Husain post: full text.
- Targeted searches (one per source) for corrections/critiques: none for Anthropic or Husain; position bias corroborated by Shi et al. (ACL 2025, not audited in full); τ-bench task corrections found (confirmed via authors' README).

## Verification
- Reading-word count (prose, headings, exhibit discussion; excluding captions, metadata, code, alt text): ~1,220, at the top of the 1,000–1,200 target.
- Every factual sentence checked against records; fixes made for pass^8 phrasing (averaged probability, not task count), Claude-v1 75% limited to default prompt, failure-category definitions matched to paper text, final "within minutes" claim removed.
- Code sample executed with stub `run_assistant`/`call_model`: runs, prints e.g. `refund-damaged-mug 4/5 passed pass^3 = 0.4`.
- Playwright (Python, Chromium) at 1280 and 390 px: `document.fonts.check('600 1em Sora')` and `('400 1em Inter')` true after `fonts.ready`; no console errors or failed requests; no page-level horizontal overflow (scrollWidth = clientWidth at both widths); all 4 images loaded and none shown above natural size; wide diagram and table sit in keyboard-focusable scroll regions on narrow screens; code block scrolls and is focusable. Screenshots in scratch/ inspected: no clipping or broken assets.
- No interactive controls, so control checks not applicable.

## Gaps
- No audited source measures LLM-judge accuracy on customer-support transcripts specifically.
- Measured reliability numbers are 2024 models in simulation; current production pass^k not available.
- Failure breakdown is one model, one domain, 36 failures.
- Fonts load from Google Fonts (network dependency); assets are local relative files.

## Elapsed time
- System clock read 11:20 at start and 11:30 at the end, which seems too short for the work done; treat about 10 to 40 minutes as approximate.
