# Run notes

Elapsed: about 10 minutes (12:37–12:47 CST, 2026-11-03).

## Decisions
- Claims C1–C7 (see records/source-audit.md). Scope kept to the core GPS solution: satellites' broadcast, time-to-distance, four unknowns including the receiver clock bias, iterative linearized/least-squares solution, satellite clock precision and relativity, and delivered accuracy (URE vs user accuracy, DOP, multipath, atmosphere).
- Phone extras (assisted GPS, multi-constellation, Wi-Fi/cell fusion) left out and named as out of scope in the closing section, rather than sourced.
- One interaction: a 2D toy with three transmitters and a slider for the assumed receiver clock error. It answers the specific gap "why does solving for the clock need one more satellite, and how can the phone find its own clock error?" Labelled as toy scale.
- One generated synthesis table (timing error × c → distance error), labelled as calculated.
- Net relativistic offset taken from Ashby 2006 Eqs. 23 and 30 (text-searchable) because the 2003 review's Eqs. 35–36 are images in the PMC copy; 38.6 µs/day and 11.6 km/day are my arithmetic, which matches 13.7 − 2.13 km.

## Sources read
- Ashby 2003, Living Reviews in Relativity (PMC copy): partial, the sections cited. Errata search: none found.
- Ashby 2006, AAPT teaching article: full PDF text extracted with PyMuPDF.
- GPS.gov Space Segment and GPS Accuracy pages: read from archive.gps.gov because the live URLs return 404; archive says content frozen since Feb 2025.
- van Diggelen and Enge 2015, ION GNSS+: abstract only (paywalled); conditional for the 4.9 m figure.
- Navipedia (ESA) Code Based Positioning (SPS) and Positioning Error: full relevant sections.
- Springer page for Ashby 2003 blocked by a JS challenge / auth redirect, so the specific Creative Commons license could not be confirmed; journal copyright page states its articles are under a Creative Commons license.

## Exhibits embedded (assets/)
- gps-constellation.jpg (GPS.gov, public domain)
- ashby-2006-fig1-navigation.png (rendered at 220 dpi from page 3 of the AAPT PDF and cropped; rights unstated, attributed)
- ashby-fig1-allan-deviation.jpg, ashby-fig2-orbit-frequency-shift.jpg (PMC originals; CC per journal policy, attributed)
All opened at full size and checked for clipping and legibility.

## Verification
- Playwright Chromium at 1280 and 390 px: no console errors, no horizontal page overflow (scrollWidth − innerWidth = 0 at both), all four images loaded.
- After document.fonts.ready: document.fonts.check('600 1em Sora') = true and document.fonts.check('400 1em Inter') = true at both widths (fonts load from Google Fonts, so a network connection is needed).
- At 390 px the two Ashby charts sit in keyboard-focusable horizontal scroll regions at natural size (scrollWidth 634/684 vs 350 client).
- Interaction: default (0 ticks, spread 58 units, "too large"), keyboard ArrowRight (1 tick, singular label), max 140 ("too small", 99 units), min −40 (96 units), Solve (finds 60, circles meet, spread 0), Reset (back to 0). Focus outline is solid red. With JavaScript disabled the pre-rendered SVG and readout show the default state.
- Screenshots reviewed: full page at both widths, demo at default/solved/max/no-JS, demo at 390 px. Fixed during checks: triangle clipped at SVG bottom and label overlap (moved true position), "1 ticks" pluralization, illegible chart labels on mobile (scroll regions), transmitter B label clipped on mobile (moved down).

## Gaps
- Smartphone 4.9 m figure rests on an abstract and 2014 phones.
- Ashby 2003 license specifics not confirmed; AAPT figure rights unstated.
- GPS.gov pages are an archived snapshot; satellite count dated July 2023.
