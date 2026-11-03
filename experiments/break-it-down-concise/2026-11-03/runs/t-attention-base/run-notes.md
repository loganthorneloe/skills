# Run notes

Elapsed: about 10 minutes of wall-clock by the system clock (12:37 to ~12:47 CST, 2026-11-03), plus model think time.

## Decisions
- Scope: decoder-only (GPT-style) attention; encoder-decoder parts of the original paper omitted (full architecture figure not used).
- Claims C1–C11 defined in records/source-audit.md.
- Sources read from arXiv e-print LaTeX (not abstracts): Vaswani et al. 2017 (v7), Kaplan et al. 2020 (v1), Brown et al. 2020 (v4), Ouyang et al. 2022 (v1). ChatGPT announcement read via Internet Archive snapshot (live page HTTP 403 to WebFetch).
- Considered and dropped: Jain & Wallace 2019 / Wiegreffe & Pinter 2019 (only abstracts read; mostly RNN attention). The interpretability caveat relies on Vaswani et al.'s own hedged wording instead.
- English-French BLEU omitted: v7 body text says 41.0, Table 2/abstract 41.8; targeted search found no erratum.
- Exhibits: original author figure files from e-print bundles (PNG copied; PDFs rendered at 200 dpi with PyMuPDF). Ouyang Fig. 2 cropped only to remove white margins. Table 1 rebuilt in HTML from LaTeX values.
- Rights: Vaswani paper grants reproduction of figures/tables with attribution for scholarly/journalistic use. Kaplan and Ouyang figures: arXiv non-exclusive license, rights unstated, embedded with attribution and said so in captions.
- One interactive: hand-made 5-token attention calculator (query select, score multiplier 0–4, causal mask toggle, reset). Labeled as made-up vectors. Fills the gap between the formula and the trained-model figure.

## Verification (Playwright chromium, scratch/check.py)
- 1280px and 390px: no horizontal page overflow (scrollWidth - innerWidth = 0), all 6 images loaded, no console errors.
- After document.fonts.ready: fonts.check('600 1em Sora') = true, fonts.check('400 1em Inter') = true at both widths (Google Fonts, network required).
- Screenshots inspected (scratch/shot-1280.png, shot-390.png and parts). Fixes made after inspection: enlarged Fig. 2 panels, no-wrap key vectors, "left/right" caption wording changed for stacked mobile layout, double rule removed, scroll regions given tabindex.
- Controls: default (it -> dog 62%, output [0.68, 0.06, 0.26] matches hand calculation), multiplier 0 (uniform 20%), multiplier 4 (dog 99%), query "barked" with mask (positions 4-5 shown masked, -inf), mask off, query "The" (100% self), reset restores default, keyboard arrow on radio group and slider both update the live region. No-JS render shows static default table with bars and default result text.

## Gaps
- GPT-3.5 architecture unpublished; report states ChatGPT-as-transformer rests on lineage (GPT-3/InstructGPT).
- Kaplan Fig. 7 caption in the source is empty; figure described from the paper's body text and panel titles.
- Fonts and nothing else load from the network; images are local relative assets.
