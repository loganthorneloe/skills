# Research and delivery notes

- Task: explain causal inference to a reader familiar with averages and percentages, using the learning-app/exam question.
- Output: `report.html`, approximately 986 KB, with embedded Inter 400/500, Sora 600, CSS, source figure, and lightweight arithmetic interaction. No runtime external asset dependency. Font license notices: `inter-OFL.txt`, `sora-OFL.txt`.
- Approximate elapsed time: 8 minutes, 15:22–15:30 UTC, 2026-10-24.
- No research graph: supplied instructions did not require one.

## Sources actually read

1. Hernán and Robins, *Causal Inference: What If*, author-hosted January 2, 2025 PDF, https://miguelhernan.org/s/hernanrobins_WhatIf_2jan25.pdf. Downloaded full PDF; extracted PDF pages 13–52 with PDF.js to `book-extract.txt`. Read relevant sections on individual/average effects, association, randomization, standardization, exchangeability, positivity, consistency, interference, and crossover limitations. Primary locators: §§1.1–1.2, 1.5, 2.1, 2.3, 3.1–3.5; Fine Points 1.1 and 2.1. Inspected Figure 1.1 on printed p. 12 (PDF p. 21). Book identifies logical conditions, not measured app performance.
2. Roschelle, Feng, Murphy, and Mason (2016), *Online Mathematics Homework Increases Student Achievement*, https://doi.org/10.1177/2332858416673968. Read full relevant Research Design, Intervention, Recruitment/attrition, Procedure, Measures, Data Analysis, Results, Discussion, and Conclusion sections through publisher PDF/text. Downloaded open-access copy from https://files.eric.ed.gov/fulltext/EJ1194398.pdf to `paper.pdf`. Affiliations confirmed on paper p. 1. Schools assigned, not students individually. 46 recruited, 45 randomized; one treated school departed and its paired control was excluded; 43 analyzed. Final student sample 2,850 includes 122 joiners. Adjusted effect 8.84 scale points; original unadjusted difference approximately 11. Paper models account for school clustering. Teacher practice year, training, technology access, population, and bundled intervention constrain interpretation.
3. AERA Open (2017), *Corrigendum*, https://doi.org/10.1177/2332858417707489. Read notice and corrected Table 4. Original PDF's effect-size column erroneously reads 50.10. Correct values: 0.29 and 0.12. Underlying subgroup score differences 14.35 and 5.84 are unchanged. Report avoids the erroneous standardized effects and links correction.
4. What Works Clearinghouse, August 2026 study review, https://ies.ed.gov/ncee/wwc/study/86375. Read Review Details, Findings, Sample Characteristics, Study Details, and comparison with older review on same page. Latest review: 2,850 students; adjusted means 690.79 versus 681.95; meets standards without reservations. Older review uses 2,728 nonjoiner sample and different means. Report explicitly selects the August 2026 record rather than mixing those populations.
5. IES grant record, https://ies.ed.gov/use-work/awards/efficacy-study-online-mathematics-homework-support-evaluation-assistments-formative-assessment-and. Read project activities, sample, research design/methods, intervention, control, measures, outcomes. Used to document teacher practice year and measured cohort. Grant-record summary says 43 randomized; original article supplies the more detailed recruitment/randomization/analysis distinction. Report does not repeat the imprecise randomization count.
6. ASA (March 7, 2016), *American Statistical Association Releases Statement on Statistical Significance and P-Values*, https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf. Read all three pages including six principles. Exact 24-word quote from principle 5 used; distinction between p-values, effect magnitude, and causal design explained. No inference that p-value gives probability of no effect.
7. Harvard faculty profile, https://hsph.harvard.edu/profile/miguel-hernan/. Read biography and current role; used to verify relevant expertise. Author book landing page https://miguelhernan.org/whatifbook read for edition/download details.

## Exhibit decisions

- Original article Figure 2, p. 9: included, cropped from original PDF. Inspected full page and crop. Axes, labels, bar proportions, grays, and legend unchanged. Caption explains median grouping, original 487 lower bound, scale points, attribution, and CC BY 3.0 reuse. Text distinguishes within-subgroup comparison from adjusted overall effect and does not imply each student benefited. Figure links to original PDF page for enlargement. Crop `figure2.png`; source page `source-page9.png`.
- WWC latest findings/primary paper Table 2: selected model-adjusted means reproduced as accessible HTML table with explicit date, denominator, units, comparison, and interpretation. Not a generated empirical replacement chart.
- ASA principle 5: short quotation explains why significance does not answer magnitude/usefulness.
- Original paper Figure 1, p. 4: inspected (`source-page4.png`); omitted because teacher-report UI describes product mechanics but adds little to the causal comparison question. Bundle caveat is explained in prose.
- Book Figure 1.1: inspected (`book-page21.png`); omitted because unfamiliar mathematical notation would require additional instruction and its distinction is already directly established by the concrete counterfactual example. No replacement presented as source evidence.
- Paper Tables 1/3/4: read, not reproduced wholesale. Demographic table and regression coefficients would distract from first-principles question. Table 3 used to check joiner sensitivity; corrected Table 4 supplies subgroup differences. Avoided original erroneous effect-size column.
- Original constructed 200-student example and slider: specifically closes the gap between observed group averages and the known effect. Two inputs: group preparation mix and uniform benefit. Visible consequences: observed gap, true effect, raw means/counts, standardized means. Synthetic fixed-score assumptions explicit. Not an empirical model of app response.

## Verification

`verification.json` records final isolated headless Chrome run. Used fresh temporary browser context/profile; did not touch other sessions.

- Desktop 1280×900: document width 1280, no horizontal overflow.
- Mobile 390×844: document width 390, no overflowing elements.
- Embedded image decoded at 426×308; full crop visually checked against source.
- FontFaceSet: Inter weight 400 loaded; Inter 500 loaded; Sora 600 loaded. Actual font loading checked, not just CSS family names. CSS retrieved via public stylesheet and font binaries embedded as TTF (the intermediate downloaded filenames end in `.woff2`, but actual source and embedded MIME/format correctly use TTF).
- No page JavaScript errors.
- Interaction assertions: (mix, benefit) = (80,0): gap +12; (50,0): 0; (20,0): −12; (20,10): −2; (80,10): +22; (50,5): +5. True effect and standardized result equal selected benefit. All calculations pass.
- Reset returns mix 80%, effect 0, gap +12.
- Keyboard ArrowLeft moves mix from 80 to 70, updates gap to +8; focus outline is solid.
- JavaScript disabled: default gap 12 and full reading flow remain present; no essential hidden content.
- Inspected desktop/mobile top screenshots and mobile interaction/source figure screenshots. No clipped heading, table, control, or chart label observed. Figure is compact at mobile size; linked original provides enlarged view.
- Saved `desktop.png`, `mobile.png`, `static-mobile.png`, `mobile-demo.png`, `mobile-figure.png`; `verify.cjs` is the exact reproducible checker. Top crops capture the preceding version before the additional IES source audit entry; final full screenshots supersede them.
- Explanation review: terms introduced before use; no analogies; connected numerical confounding example; random assignment mechanism; assignment-versus-use distinction; spillovers/group analysis; observational assumptions; chance versus confounding; evidence limited to tested intervention/population.

## Access gaps and recovered issues

- Ordinary shell network access unavailable; permitted escalated public downloads succeeded.
- Direct Sage download returned HTTP 403; equivalent ERIC open-access PDF succeeded. Publisher full text and original PDF sections were also available through research browser.
- Old Harvard PDF links redirected/failed; author's current landing page identified downloadable January 2025 PDF. Browser extractor rejected full PDF length; local PDF.js extraction succeeded.
- PyMuPDF and pdftotext unavailable. Used existing PDF.js and pdftoppm; no package installation required.
- Default Playwright browser version missing. Existing Google Chrome used in isolated headless context; initial sandbox launch failed, permitted escalated verification succeeded.
- No remaining material access or rendering gap. External source links require internet; report content/assets work offline. No screen-reader testing performed; semantic labels, output announcements, focus, and keyboard interaction were checked structurally/functionally.
