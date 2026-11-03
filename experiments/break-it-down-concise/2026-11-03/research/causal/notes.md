# Research notes

Elapsed: about 16 minutes (10:53 to 11:09 CST, 2026-11-03).

Skill files followed: baseline `break-it-down/SKILL.md` steps 1–2, `source-audit/SKILL.md`, `find-evidence/SKILL.md` (read directly; Skill tool not used).

## Sources read (full text downloaded and read, not search snippets)

1. Hernán & Robins, *Causal Inference: What If*, PDF version 19 Aug 2026 (miguelhernan.org). Ch. 1, Ch. 2 §2.1, Ch. 3 intro–§3.2.
2. Cunningham, *Causal Inference: The Mixtape*, 1st online edition (mixtape-1ed.netlify.app), Ch. 4 §4.0–4.1.5, Ch. 5 §5.3.4. The current site (mixtape.scunning.com, "The Remix") returned 404 for the old chapter URL.
3. Dynarski et al., *Effectiveness of Reading and Mathematics Software Products: First Student Cohort*, IES NCEE 2007-4005 (full report, Ch. II) and 2007-4006 (executive summary, full). IES evaluation page read for the 2009 two-cohort findings.
4. Muralidharan, Singh & Ganimian, "Disrupting Education?", NBER WP 22923 (revised July 2017), intro, §2.2–2.3, §4.4–4.6, figure notes; AER 2019 abstract from aeaweb.org.
5. LaLonde (1986), AER, via gwern.net scan: abstract, intro, Table 5.
6. Gertler et al., *Impact Evaluation in Practice*, 2nd ed. (World Bank OKR PDF): Ch. 3, Ch. 4 tables, HISP tables Ch. 5–8, Table 11.2.
7. Escueta, Quan, Nickow & Oreopoulos, NBER WP 23744 (Aug 2017): §2, §4.1.

Author/affiliation checks: Hernán (miguelhernan.org/about), Cunningham (scunning.com), Muralidharan/Singh/Ganimian and Escueta et al. (paper title pages), LaLonde (article footnote). Gertler affiliation marked unverified.

Targeted erratum/replication searches: Mindspark (none found; replication data on openICPSR; larger follow-up study ongoing); IES 2007 (follow-up 2009 report found, findings verified on IES page). Textbooks and LaLonde: no erratum search beyond confirming LaLonde values against the primary; Mixtape's LaLonde transcription matches the primary.

## Extraction methods

- PDFs: PyMuPDF in a temporary venv in the scratchpad. Embedded original images extracted where the figure was a raster (Hernán Fig 1.1, 3001×2251; Mindspark Fig 2, 595×433 natural size). Tables rendered from PDF pages at 300 dpi and cropped; every crop reopened, three re-cropped after clipping.
- Mixtape tables are HTML: rendered with headless Google Chrome from the page's own table HTML, linked site CSS, and MathJax, then trimmed. Values cross-checked against page text.
- Transcribed table data saved as CSV in `assets/`.

## Access gaps

- AER published PDF for Mindspark not read (used NBER WP + published abstract); published numbers differ slightly from WP (0.37/0.23 vs 0.36/0.22; IV 0.6/0.39 vs 0.59/0.36).
- Escueta et al. published JEL 2020 version not read; counts are from the 2017 WP.
- IES 2009 two-cohort report itself not read (summary from IES evaluation page).
- LaLonde read from a third-party scan (gwern.net) of the JSTOR copy; canonical JSTOR page not accessed.
- Dehejia & Wahba (1999, 2002) known only through the Mixtape's account.
- EdWeek coverage of industry objections to the IES study seen in search results only, not read; not relied on.
- No audited RCT of a consumer self-study smartphone learning app; no education within-study comparison (observational vs. experimental in the same population).

## Notes for writers

- HISP (World Bank) data are fictional by the book's own statement; present as an illustration.
- Hernán, Mixtape examples are hypothetical; LaLonde, IES and Mindspark are real data.
- Do not describe the IES products' "prior evidence of effectiveness" as an observational estimate that the RCT contradicted; the report does not quantify that prior evidence.
- Rights: IES public domain; World Bank CC BY 3.0 IGO; Hernán all rights reserved; Mixtape, Mindspark figure, LaLonde table rights unstated or publisher-held (attribute; caller decides embed vs. link).
