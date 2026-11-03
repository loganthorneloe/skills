# Run notes

Approximate elapsed time: about 13 minutes of wall-clock (12:50 to 13:03 CST, 2026-11-03).

## Decisions
- Claims C1–C8 (records/claims.md). Ranked: C3/C4 (time-to-distance, fourth unknown) and C5/C6 (clock precision, relativity) get full mechanism and evidence, because they answer the user's two questions. C1, C2, C7, C8 are kept short.
- One worked example runs through the whole report: a satellite 20,200 km overhead (about 67 ms delay), with timing errors turned into distance (1 ns ≈ 30 cm, 1 ms ≈ 300 km, 38.6 µs/day ≈ 11.6 km).
- One interactive, a 2D clock-bias solver. The reader sets the phone's clock error and the solver's correction. The circles and their pairwise crossing points (in a zoomed close-up) meet only when the correction equals the error. It addresses the main gap the figures leave open: why a clock error counts as a solvable fourth unknown. Toy geometry is disclosed; the only real constant is c = 0.2998 km/µs.
- Distillation: body prose went from 1,938 to 1,104 words (57%). Whole page text including the source audit, captions and the interactive went from 2,971 to 1,918 words (65%). The audit entries were shortened but all six were kept. Every figure and the interactive were kept.

## Sources read
- GSA white paper "Using GNSS Raw Measurements on Android Devices" (2017), PDF. §1 and §3.1 read in full, the rest skimmed. Figures 1, 8 and 15 were cropped from 220-dpi renders. The terms allow excerpts with a stated source line, which every caption includes.
- Ashby, "Relativity in the GPS", Living Reviews in Relativity 2003 (via PMC). §1–5 read. Figures 1 and 2 were downloaded from PMC. Reuse rights are not stated, so the captions say so.
- Ashby, Physics Today 2002. Partial read, through a fetch-tool extraction with quoted sentences.
- IS-GPS-200N (Aug 2022), PDF. §3.2.2, §3.3.1.1, §20.3.1–20.3.2 and §20.3.3.4.1 read.
- GPS.gov Space Segment and GPS Accuracy pages, read from archive.gps.gov because the live URL returns 404. Constellation and two cartoon figures downloaded; these are U.S. government works.
- Targeted erratum search for Ashby found none (the 2007 revision only added sections). No per-source erratum searches for the government and GSA documents.

## Verification
- Every factual sentence in report.html was checked against records/source-audit.md and records/evidence.md. Unsourced specifics found in the draft (satellite speed of 3.9 km/s, ionosphere altitude band, Ashby's "decades" credential) were removed or reworded.
- Derived numbers: 4.4647e-10 × 86,400 = 38.58 µs/day, × c = 11.56 km/day; 20,200 km / c = 67.4 ms; 1,500 bits / 50 bps = 30 s.
- Playwright (Chromium), at 1280 and 390 px, run on both draft.html and report.html. `document.fonts.check('600 1em Sora')` and `('400 1em Inter')` returned true after `fonts.ready`. No horizontal page overflow, no broken images, no images upscaled past natural size, no console errors or failed requests. Screenshots were inspected; the error-budget figure was unreadable at 390 px, so it and both Ashby figures were put in keyboard-focusable horizontal scroll regions on narrow screens (ArrowRight scrolls 200 px after 5 presses).
- Interactive was tested at default (12.0 km per circle, 8.3 km spread), after Solve (0.0 km, circles meet), at bias −100 (42.0 km), at the extremes −100/+100 (60.0 km), after Reset (back to default), and with the keyboard (two ArrowRight presses gave 2 µs and 11.4 km). The focus outline is solid. With JavaScript disabled, the static SVG and result text show the default state.
- The report contains no skill names or experiment labels (grep).

## Gaps
- The 4.9 m smartphone figure comes from GPS.gov's citation of an ION paper that was not read directly.
- No sourced time-to-first-fix numbers; the report gives only the 30 s frame time and A-GNSS's stated aim.
- The "< 13 m relativistic clock correction" label in GSA Fig. 8 is read as the eccentricity term, and the report hedges it with "appears to be."
- The fonts load from Google Fonts, so the page needs a network connection to show them; they are not embedded.
- Ashby's equations are images in PMC; Eq. 35 values were not transcribed, and the spec value was used instead.
