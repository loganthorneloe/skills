# Source audit records

Claims
- C1: An mRNA vaccine delivers lab-made mRNA, wrapped in lipid nanoparticles, that encodes the virus's spike protein (or a piece of it); the mRNA is taken into cells near the injection site and nearby lymph nodes.
- C2: The cell's ribosomes read the mRNA in the cytoplasm and make spike protein, which the immune system then sees as foreign.
- C3: Seeing spike drives an adaptive response: B cells make spike-binding antibodies, helped by T follicular helper cells in lymph-node germinal centres; CD8 and CD4 T cells also respond.
- C4: Germinal-centre activity persists for weeks to months after the mRNA is gone, building durable antibody and memory responses.
- C5: In the phase 3 trial, the vaccine prevented most symptomatic COVID-19 (about 95%), with protection appearing roughly two weeks after dose 1.
- C6: Chemically modified bases (pseudouridine / 1-methylpseudouridine) make synthetic mRNA less inflammatory and more productive; this enabled the vaccines.
- C7: Vaccine mRNA does not enter the nucleus and is not integrated into DNA; mRNA is a non-integrating platform degraded by normal cellular processes.
- C8: Vaccine mRNA is temporary, but lasts days to a couple of weeks, not hours (detectable in blood up to ~2 weeks).
- C9: A lab study in a liver cancer cell line reported reverse transcription of vaccine mRNA into DNA; it did not show integration, and its relevance to people is disputed.

### Understanding How COVID-19 Vaccines Work (CDC)
- url: https://www.cdc.gov/covid/vaccines/how-they-work.html; text read from: same (via fetch-tool summary with quotations)
- byline: U.S. Centers for Disease Control and Prevention · public-health web page · CDC · Sept. 3, 2024 (accessed 2026-11-03)
- verdicts: C1 pass; C2 pass; C3 conditional (general level only: antibodies, "other immune cells"); C7 pass; C8 fail (gives no duration)
- use: mRNA vaccine section: muscle cells, spike piece, mRNA broken down, "do not enter the nucleus"
- credibility: national public-health agency's patient-facing explanation, consistent with the primary literature below.
- contribution: plain statement of mechanism and the nucleus/DNA point.
- limits: simplified; silent on how long mRNA lasts; read through a fetch-tool summary that quoted the page (partial read).
- read: partial (fetch summary with verbatim quotes) · via WebFetch

### mRNA vaccines — a new era in vaccinology
- url: https://doi.org/10.1038/nrd.2017.243; text read from: PMC author manuscript https://pmc.ncbi.nlm.nih.gov/articles/PMC5906799/
- byline: Norbert Pardi, Michael J. Hogan, Frederick W. Porter, Drew Weissman · review article · Nature Reviews Drug Discovery · January 2018
- verdicts: C1 pass; C2 pass; C3 pass; C6 pass; C7 pass (as the field's design rationale)
- use: Introduction (safety: "non-infectious, non-integrating platform"; degraded by normal processes), Basic mRNA vaccine pharmacology, Modulation of immunogenicity (TLR7/8, pseudouridine), Box 3 (germinal centres and Tfh), section on DCs and MHC I/II
- credibility: Weissman co-discovered nucleoside modification (2023 Nobel); authors run mRNA vaccine labs at Penn. Widely used field review.
- contribution: mechanism from delivery to translation to immune activation; why modified bases matter.
- limits: written before COVID-19 vaccines existed; Weissman has commercial interests in mRNA technology (licensing); "no potential risk" of integration is a design argument, not a measured human study.
- read: partial (intro, pharmacology, immunogenicity, delivery, GC/Tfh sections; product tables skimmed) · author manuscript via PMC

### Press release: The Nobel Prize in Physiology or Medicine 2023
- url: https://www.nobelprize.org/prizes/medicine/2023/press-release/; text read from: same (curl)
- byline: The Nobel Assembly at Karolinska Institutet · prize press release · NobelPrize.org · 2 October 2023
- verdicts: C6 pass; C5 conditional (only "around 95%", secondary); C1 context
- use: "The breakthrough" section; Figure 2 (not reproduced; site terms restrict reuse); key publications list (Karikó 2005, 2008; Anderson 2010)
- credibility: the prize committee's summary of the laureates' peer-reviewed work, with primary citations.
- contribution: plain account of why unmodified lab mRNA triggered inflammation and how modified bases fixed it and increased protein production.
- limits: celebratory summary; not a method source. Images © The Nobel Committee, reproduction restricted, so linked not embedded.
- read: full

### FDA Briefing Document: Pfizer-BioNTech COVID-19 Vaccine (VRBPAC, December 10, 2020)
- url: https://www.fda.gov/media/144245/download; text read from: same PDF
- byline: U.S. Food and Drug Administration · regulatory briefing document · Vaccines and Related Biological Products Advisory Committee · December 10, 2020
- verdicts: C5 pass; C1 pass (spike antigen encoded by RNA in LNPs)
- use: Executive summary p. 6 (95.0%, 8 vs 162 cases, 36,621 participants); Figure 2 p. 30 (cumulative incidence after dose 1)
- credibility: FDA reviewers' independent analysis of the randomized, placebo-controlled phase 3 trial (~44,000 participants) for emergency authorization.
- contribution: randomized evidence that vaccination prevented symptomatic COVID-19.
- limits: data cutoff November 14, 2020, median ~2 months of follow-up, against the original virus; efficacy against later variants and after waning was lower. Figure 2 is sponsor-generated and covers all who received dose 1, not the primary endpoint population.
- read: partial (executive summary, efficacy section pp. 6, 23–31) 

### SARS-CoV-2 mRNA vaccines induce persistent human germinal centre responses
- url: https://doi.org/10.1038/s41586-021-03738-2; text read from: PMC author manuscript https://pmc.ncbi.nlm.nih.gov/articles/PMC8935394/
- byline: Jackson S. Turner, Jane A. O'Halloran, and colleagues (Ellebedy lab, Washington University) · research article · Nature · June 2021 (online)
- verdicts: C3 pass; C4 pass
- use: Abstract; Fig. 2 (germinal-centre B cells in draining lymph nodes, weeks 3–15)
- credibility: primary human data: repeated ultrasound-guided needle samples of the armpit lymph nodes that drain the injection site.
- contribution: shows spike-binding germinal-centre B cells in all 14 sampled people, sustained at least 12 weeks after the booster.
- limits: 14 lymph-node participants, BNT162b2 only, 15 weeks of follow-up; several authors have industry ties (disclosed); measures B cells, not protection directly.
- read: partial (abstract, Fig. 1–2 and captions, results on GC B cells, competing interests)

### Vaccine mRNA Can Be Detected in Blood at 15 Days Post-Vaccination
- url: https://doi.org/10.3390/biomedicines10071538; text read from: Europe PMC full text PMC9313234
- byline: Tudor Emanuel Fertig, Leona Chitoiu, and colleagues · research article · Biomedicines (MDPI) · June 2022
- verdicts: C8 pass (narrow: detectable in blood up to ~15 days in a small cohort); C1 context (intro cites LN detection to 60 days, secondary)
- use: Abstract; Results 3.1; Figure 1; limitations paragraph
- credibility: primary qPCR measurements of vaccine-specific mRNA in blood from 16 vaccinated people plus 3 unvaccinated controls (controls did not amplify).
- contribution: vaccine mRNA is not gone within hours; traces persist in plasma ~2 weeks.
- limits: small cohort, mostly single samples per person, no clinical outcomes; detects RNA fragments by PCR, not whether intact mRNA still makes protein. CC BY 4.0.
- read: partial (abstract, intro, results 3.1–3.2, Fig. 1, limitations)

### Intracellular Reverse Transcription of Pfizer BioNTech COVID-19 mRNA Vaccine BNT162b2 In Vitro in Human Liver Cell Line
- url: https://doi.org/10.3390/cimb44030073; text read from: Europe PMC full text PMC8946961
- byline: Markus Aldén, Francisko Olofsson Falla, and colleagues (Lund University) · research article · Current Issues in Molecular Biology (MDPI) · February 2022
- verdicts: C9 pass (as a report of what this in vitro study claims); C7 qualify
- use: Abstract; Methods 2.1 (0.5–2 µg/mL in culture); Discussion ("we do not know if DNA reverse transcribed from BNT162b2 is integrated")
- credibility: primary lab experiment; authors state its scope.
- contribution: the main published claim that vaccine mRNA can be copied to DNA in a cell line.
- limits: liver cancer cell line in a dish, high exposure, no integration shown, no human or animal data; contested (see Merchant comment). Targeted search found the comment; no retraction found.
- read: partial (abstract, methods, discussion)

### Comment on Aldén et al. (2022)
- url: https://doi.org/10.3390/cimb44040113; text read from: Europe PMC full text PMC9164063
- byline: Hamid A. Merchant · comment · Current Issues in Molecular Biology (MDPI) · April 2022
- verdicts: C9 conditional (one expert's critique, not new data)
- use: entire comment (in vitro model, dose, Huh7 differs from healthy liver)
- credibility: pharmacy academic with industry drug-development experience; argument checks against Aldén's own methods.
- contribution: explains why the cell-line result may not apply in people.
- limits: argument, not experiment.
- read: full

## Gaps
- C7: no human study directly sequencing genomes of vaccinated people was read; the "no integration" claim rests on mechanism, design rationale, and the absence of a demonstrated pathway in people.
- C5: efficacy against later variants and waning not covered by the sources read; stated as a limit.
