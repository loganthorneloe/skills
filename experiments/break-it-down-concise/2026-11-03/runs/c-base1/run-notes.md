# Run notes

Elapsed: about 7 minutes by the system clock (11:10 to 11:17 CST, 2026-11-03), steps 3 to 6 only. Research came from the frozen packet.

## Decisions

- I wrote the report in the packet's prerequisite order: observation, association, counterfactual, average effect, self-selection, other non-causal routes, adjustment limits, randomization, reading results, practical wrinkles, quasi-experiments, then implications and limits.
- All seven audited sources appear in the source audit, because each passes or is conditional for at least one claim. Escueta et al. lists four authors, and Gertler et al. is shortened to "Paul J. Gertler, Sebastian Martinez, and colleagues" because it has five.
- Embedded exhibits: E1 (Hernán Fig 1.1), E2/E3 (Mixtape Tables 4.2/4.3, as two tiles), E9 (LaLonde Table 5), E5 and E6 (IES Tables II.5 and II.6), and E8 (Mindspark Fig 2 with its note). These were copied into `assets/`. E12 is rebuilt as an HTML synthesis table labeled as the book's fictional case, with values matching the transcription CSV. E4, E7, E13, E14, and E15 are used as short quotes and metrics in the prose. E10 and E11 contribute only their numbers (−14.46, t = −49, −10.14); their images were not embedded, to keep the exhibits focused.
- Rights: IES (public domain) and World Bank (CC BY) are embedded with attribution. Hernán is "all rights reserved" and is embedded with attribution for commentary. Mixtape, LaLonde, and the Mindspark figure have unstated reuse terms and are embedded with attribution, and their captions say so.
- The interaction is a constructed six-student example (E16), labeled as invented. Readers can toggle who uses the app, draw names at random, and run 1,000 random half-splits at class sizes 6, 60, or 600 built from copies of the six types. It addresses two gaps: that gap = effect + selection bias, and that chance assignment is right on average with an error that shrinks as samples grow (C7, C8). For size 6 it enumerates all 20 splits exactly.
- Reverse causation (C5) is presented as settled reasoning without a source exhibit, per the audit gaps list. Spillovers (C10) are stated definitionally.
- Voice pass: I removed bold lead-in labels from every bullet list, cut a long Mixtape quote down to a paraphrase, shortened the IES quote, fixed a wrong word count ("five words"), and checked for filler and analogies.

## Verification (Playwright, Python, Chromium headless)

- At 1280 px and 390 px, `document.fonts.check('600 1em Sora')` and `('400 1em Inter')` both returned true after `document.fonts.ready`. There was no horizontal page overflow, no console or page errors, and all 7 images loaded. No image displays above its natural width.
- Full-page screenshots at both widths were inspected. Defects found and fixed:
  - The Mixtape tile images were vertically distorted because the height attribute had no `height:auto`. Aspect ratios now match the natural ratios (1.022, 0.984).
  - At 390 px, the wide source tables were scaled to 350 px and unreadable, because inline max-width overrode the scroll rule. They now render at 760 px inside keyboard-focusable horizontal scroll regions, with full-size links.
  - The six-student table was clipped at 390 px. It now fits at 312 px.
- Controls, with values confirmed by hand arithmetic:
  - The default state reads 80.0 / 62.0 / 18.0 / 16.0.
  - Unticking A gives 79.0 / 66.5 / 12.5 / 10.5.
  - Leaving no users shows the empty-group message.
  - Ticking D by keyboard (Space) gives −5.2 / −7.2.
  - The hat draws vary, and gap minus bias equals 2 every time.
  - Reset restores 18.0.
- Simulation:
  - Size 6 shows an average of 2.0 and a middle 95% of −10.2 to 14.2 (exact, from 20 splits), with a range of −14 to 18.
  - Size 60 shows about 2.0, from about −2.0 to 6.0.
  - Size 600 shows 2.0, from 0.7 to 3.4.
  - Pressing Enter on the run button works.
  - Focus outline is solid red.
- With JavaScript disabled, the page shows the self-selected state (gap 18.0) and the precomputed 6-student range in static text. The histogram is empty without JavaScript.

## Gaps

- Fonts load from Google Fonts over the network. They are not embedded, so offline viewing falls back to system sans-serif.
- Dark mode was not requested and is not implemented.
- On narrow screens the scanned LaLonde table is soft but legible.
- Packet gaps carried into the report's closing limits: no randomized trial of a consumer self-study smartphone app, LaLonde's evidence comes from job training, and the textbook examples are hypothetical.
- The "Run 1,000 random draws" button enumerates all 20 splits at size 6 instead of drawing randomly. The status line and the "20 possible" readout state this.
