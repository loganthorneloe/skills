# Run notes

Elapsed: about 9 minutes of wall-clock time (11:20 to 11:29 CST, 2026-11-03).

## Decisions
- Claims C1–C6 (why evals, structure, how to start, LLM-judge reliability, support-specific grading and consistency, regression vs capability). Recorded in records/source-audit.md.
- Five sources kept: Anthropic "Demystifying evals for AI agents" (Jan 2026), Husain "Your AI Product Needs Evals" (2024), τ-bench (Yao et al., 2024), Zheng et al. LLM-as-a-Judge (2023), Shankar et al. "Who Validates the Validators?" (2024). None failed outright.
- Exhibits: Anthropic components diagram; Zheng Table 2 (cropped from PDF page 5); τ-bench pass^k figure and failure-breakdown figure (rendered from arXiv e-print source PDFs at 300 dpi). The τ-bench Figure 1 setup diagram was in the draft but removed during distillation and replaced by one sentence. Anthropic's pass@k/pass^k chart was rejected because it is an illustrative curve; τ-bench's measured chart was used instead.
- No generated visual or interaction: the source exhibits plus a short Python harness sketch covered the gaps. With no controls, the control-operation check did not apply.
- Distillation: draft.html has about 2,466 words in main; report.html has about 1,362 (55%, or about 53% of prose without the code block). I cut the repeated Rechat detail, the τ-bench setup figure, the verbosity-bias numbers, Husain's level cadence, and long source entries, and shortened the steps and captions. Every claim, mechanism, and limiting caveat stayed.

## Sources read
- Anthropic post: read partially, through a fetch-tool summary of the full page plus a second targeted fetch (other methods list, CORE-Bench 42%→95%). Figures were downloaded from the CDN and inspected.
- Husain post: read partially, through a fetch-tool summary.
- τ-bench: read in the arXiv v1 LaTeX source (intro, metric, experiments, failure analysis); the appendix was not read. License CC BY 4.0.
- Zheng et al.: read in PDF v4 with text extracted through PyMuPDF (§3, §4.2, Tables 2–5). The 85%/81% and Table 2 values were spot-checked. arXiv non-exclusive license, so rights are unstated and the table is embedded with attribution.
- Shankar et al.: read partially (abstract and method summary via fetch; n=9). UIST 2024 publication was not verified.
- I ran one errata search for τ-bench and found nothing specific. For Zheng, I did not run a separate errata search beyond reading.

## Verification
- Fact pass: every number in report.html was checked against the records (61.2% retail pass^1, pass^8 <25%, 36-failure breakdown, 4 of 40 task errors, Table 2 values, 85% vs 81%, 20–50 tasks, 25–50 labels, 42%→95%). I removed an unverified "Figure 4" number for τ-bench and corrected the CORE-Bench cause wording.
- Rendering was done with Python Playwright Chromium at 1280×900 and 390×900, on both draft and final. Results: document.fonts.check('600 1em Sora') was true and document.fonts.check('400 1em Inter') was true after fonts.ready, at both widths. All images loaded at or below natural size, with no horizontal page overflow and no failed requests. At 390px the wide diagram and Table 2 sit in keyboard-focusable horizontal scroll regions. I inspected screenshots, and the draft's mobile grader table was cramped, so I set a 600px minimum width inside its scroll region.
- The code sample was executed with a stub `run_assistant` and runs as written.
- Fonts load from Google Fonts, so the page needs a network connection; without one it falls back to system sans-serif.

## Gaps
- C1 and C6 rest on practitioner sources only, so they are framed as practice, not measured effects.
- All measured numbers come from 2023–2024 models and are presented historically. No current-model τ-bench results were audited.
- The Anthropic and Husain posts were read through fetch summaries, not verbatim full text.
