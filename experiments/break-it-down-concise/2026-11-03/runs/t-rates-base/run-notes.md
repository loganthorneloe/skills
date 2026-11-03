# Run notes

Started 12:37 CST; finished about 12:46 CST by the system clock (roughly 10 minutes).

## Decisions
- Seven claims (C1–C7) covering policy rate control, spending channels, demand-to-inflation, expectations/real rates, lag size, lag causes, limits. Records in records/source-audit.md and records/evidence.md.
- Backbone source is the Bank of England's 1999 MPC transmission paper (full read), since it gives the full causal chain plus the canonical lag charts. Its dated parts (floating-rate UK mortgages) are corrected with a 2019 Bank Underground post; its model lags are qualified with the Havranek & Rusnak 2013 meta-analysis and a September 2026 Dallas Fed working paper with daily Spanish data.
- Nakamura & Steinsson 2008 used only for price-change frequency.
- No generated visual or interaction: source exhibits (diagram, two simulation charts, lag density + table, mortgage chart, two daily/monthly response figures) cover each comprehension step. One transcribed synthesis table (exact values from Havranek & Rusnak Table 2, simplified row labels).
- Worked example (£200,000 variable mortgage, +1 point ≈ £167/month) is simple arithmetic, not a sourced figure.
- Dropped/softened during fact check: unsupported claims that most US homeowners' payments never change, that credibility reduces output costs, that faster communication speeds transmission, and that wages are reviewed yearly.

## Sources read
- Bank of England 1999, The transmission mechanism of monetary policy (full, PDF).
- Havranek & Rusnak 2013, IJCB (partial: abstract, sections 1–2, tables 2–3, conclusion).
- Nakamura & Steinsson 2008, QJE, author-hosted copy (partial: abstract, intro, frequency section).
- Cumming 2019, Bank Underground (full).
- Buda, Carvalho et al. 2026, Dallas Fed WP 2631 (partial: abstract, intro, sections 4, 7.2–7.3, figures 2 and 13).
- Bank of England legal page (copyright/reuse terms).
- Retraction/erratum searches: one each for Havranek & Rusnak and Nakamura & Steinsson; none found. Not run separately for the BoE report/blog (institutional) or the 2026 WP (beyond noting it revises a 2023 version).
- A Bank of England "how monetary policy works" URL returned 404 and was not used.

## Verification
- Exhibits extracted with PyMuPDF (temporary venv in scratch/) from original PDFs at 220 dpi; Bank Underground chart downloaded as the original JPEG. Every crop opened and inspected; chart 1 re-cropped once to include its note. Buda Figure 2 crop omits the figure notes on purpose (conveyed in caption).
- Playwright (Python, Chromium) at 1280px and 390px: document.fonts.check('600 1em Sora') true and ('400 1em Inter') true at both widths after fonts.ready; all 7 images loaded; no horizontal page overflow at either width (initially 432px at 390 due to the table; fixed with narrower mobile table padding and font). Desktop chart pair initially rendered at 184px each (flex sizing bug); fixed to natural-half widths (391/373px). No image upscaled beyond natural size. Wide figures sit in focusable horizontal scroll regions on narrow screens.
- Screenshots inspected at both widths: no clipping or broken assets.
- No controls exist, so control-state checks do not apply.

## Gaps
- Fonts load from Google Fonts; offline viewing falls back to system sans-serif.
- Reuse rights for the IJCB and Dallas Fed figures are unstated; Bank of England material is reproduced under its non-commercial terms. All embedded with attribution.
- Precise current lag length rests on conditional sources (1999 model, pre-2013 studies, one-country 2026 working paper); presented as a range.
- No audited source on supply-shock inflation episodes; the limits section relies on the 1999 statement that monetary policy has little effect on supply capacity.
- QJE canonical URL for Nakamura & Steinsson not verified; report links the author-hosted copy.
