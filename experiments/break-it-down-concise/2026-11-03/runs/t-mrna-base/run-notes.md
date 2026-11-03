# Run notes

Elapsed: system clock read 12:37 at start and 12:45 at final check (about 8 minutes by clock; wall time felt longer, treat as approximate).

## Decisions
- Eight claims C1–C8 (see records/source-audit.md). Scope: COVID-19 mRNA vaccines as the worked case, since they are the licensed examples and the reader's question implies them.
- Main mechanism source: Nobel Committee scientific background (2023), read in full via curl (WebFetch returned 403).
- Efficacy: Polack et al. NEJM 2020 via PMC open-access copy; embedded its Figure 3 (cumulative incidence) because the ~12-day lag visibly shows the adaptive response building.
- DNA question handled with mechanism sources (Nobel, Pardi), a persistence qualifier (Röltgen 2022, mRNA in lymph-node germinal centres to day 60), and the contrary in vitro study (Aldén 2022) plus its published critique (Merchant 2022), quoting Aldén's own statement that integration was not tested.
- Dropped CDC explainer (agency assertion without evidence; redundant).
- Not embedded: Pardi figures (publisher copyright on author manuscript), Röltgen Figure 7 (microscopy too specialised), Nobel Figure 2 (too technical).
- One generated SVG (information-flow diagram) to close the specific gap "where would the mRNA have to go to change DNA"; three required steps given as an HTML ordered list for legibility. No interactive controls; none would add insight beyond prose and exhibits.
- Four connected tiles for B cells / helper T / killer T / memory.

## Sources read
- Nobel background (full), Polack 2020 (abstract, results, Fig 3), Pardi 2018 (relevant sections), Röltgen 2022 (results section on persistence, Fig 7 legend, limitations), Aldén 2022 (abstract, methods, discussion, conclusions), Merchant 2022 (full), CDC page (fetch summary only, dropped).
- Targeted searches: no retraction/replication found for Aldén; no correction found for Röltgen.

## Verification
- Playwright (python, Chromium) at 1280 and 390 px: document.fonts.check('600 1em Sora') true and ('400 1em Inter') true at both widths after fonts.ready (fonts load from Google Fonts; network dependency).
- No horizontal page overflow (scrollWidth == clientWidth at both widths). All three images load; none upscaled (802→640/350, 2500→912/620, 751→640/350).
- At 390 px the wide Nobel Figure 4 and the SVG diagram sit in keyboard-focusable horizontal scroll regions (Figure 4 at 620 px min width); full-size link provided.
- Keyboard Tab order reaches source links, figure links and scroll regions; visible focus outline defined.
- With JavaScript disabled the page renders the same (no JS used).
- Screenshots inspected: diagram (first version had overlapping label and unreadable mobile text; redrawn and rechecked), tiles at 390, Figure 4 at 1280 and 390.
- Factual sentences checked against records; softened three overstatements (killer T cell advantage, "main advantage" of cytoplasm-only delivery, attributed the immune-clearance argument to the critique).

## Gaps
- No source sequenced vaccinated people's genomes; the "does not change DNA" conclusion rests on mechanism plus absence of contrary in vivo evidence, stated as such in the report.
- Nobel figure reuse terms unstated; embedded with attribution and disclosed in captions.
- Memory-cell duration not quantified.
- Fonts require network; offline viewing falls back to system sans-serif.
