# Run notes

Approximate elapsed time is about 20 minutes of wall clock (12:37 to 12:55 CST by the system clock), covering research, extraction, draft, distillation, and checks.

## Decisions
- I split the question into claims C1–C8 (see records/source-audit.md). The top-ranked claims are C3 (timing as a share of a cycle), C5 (predictable versus random noise), and C6 (passive versus active split). Those got the mechanism, the evidence, and the interactive.
- The worked example used throughout is a 100 Hz engine hum compared with a 4 kHz "s" consonant, both with a 20 µs timing error.
- I flagged a disputed premise. "Voices are high-frequency" is only partly right, because a male voice's fundamental is near 100 Hz. The report says unpredictability and high-frequency components are the real obstacles.
- Interactive (generated). The reader controls frequency and timing error. The page shows the waveform sum, the share of a cycle, the reduction in dB, and the λ/10 zone size. The formula is exact for a pure delay between equal tones, and the delay values are labelled illustrative. A static SVG for the default state is baked in for no-JS readers.
- Exhibits: Lueg patent Fig. 1 (public domain), Rivera 2018 Fig. 1 (rights unstated, attributed), Rivera 2017 Fig. 6 (rights unstated, attributed), Monson 2014 Fig. 1 (CC BY), and Gallagher & Murphy 2017 Fig. 1 (US government work). All five were kept through distillation.
- I distilled the draft to the report. The body text, excluding the source list, went from about 2,355 words to about 1,290 (roughly 55%). The whole main element went from about 2,846 words to about 1,900, because source entries were also shortened but must remain. The cuts were history detail, the car engine and road noise aside, a repeated delay-scaling sentence, figure-caption detail, and source blurbs. No visuals were cut.

## Sources read
- Lueg, US 2,043,416 (full, OCR and drawing)
- Shi et al., arXiv 2306.01425v2 (full)
- Brunnström & Moonen, KU Leuven DASP Ch. 6 slides (full)
- Rivera Benois, Nowak, Zölzer, Hybrid ANC overview (partial, sections 1–2)
- Rivera Benois, Papantoni, Zölzer, ICSV25 2018 (full)
- Rivera Benois, Nowak, Zölzer, 2017 fully digital hybrid feedback (full)
- Gallagher & Murphy, NHCA Spectrum 2017 (full)
- Monson et al., Frontiers in Psychology 2014 (partial, via fetch tool: intro, Fig. 1, licence)

These were tried and not used:
- Kuo & Morgan 1999 and Elliott & Nelson 1993 had no accessible full text.
- Wu et al. ICSV 2016 is closed access.
- MDPI Acoustics 6(4):60 returned 403 to the fetch tool. A curl retry was blocked by the permission classifier, and I did not pursue it further.
- RTINGS is JS-rendered with no body text.
- Stereophile returned 403.
- The IOA Wu PDF link was dead.
- USPTO patents 9031251 and 8718291 were image-only PDFs with no OCR, so I did not use them.

## Verification
- Playwright Chromium rendered the page at 1280 and 390 px. There was no horizontal overflow (scrollWidth equalled clientWidth at both widths), no console or page errors, and all 5 images loaded. No image is upscaled: the Monson figure shows at its natural 892 px and the others are downscaled. At 390 px, Fig. 6 sits in a focusable horizontal scroll region at 720 px.
- After document.fonts.ready, `document.fonts.check('600 1em Sora')` and `document.fonts.check('400 1em Inter')` both returned true at both widths. Fonts load from Google Fonts, so network access is needed.
- Interactive states matched hand calculations:
  - The default (100 Hz, 20 µs) gave 38 dB quieter and 34 cm.
  - The 4 kHz preset gave 6 dB and 0.9 cm.
  - The 1 kHz preset gave 18 dB.
  - The frequency End key (8 kHz) gave "no change" at 20 µs.
  - 8 kHz with 0 µs gave "perfect".
  - At a 50% cycle shift (8 kHz with 62 µs, and 5 kHz with 100 µs), it gave 6 dB louder.
  - 50 Hz with 100 µs gave 30 dB.
  - Reset restored the defaults.
  - Keyboard Home and End work, and the focus ring is visible.
  - With JS disabled, the page shows the baked default waveform and tile values.
- One defect was found and fixed in the draft. Presets showed 999 Hz and 9,979 µs because the log slider quantised the value. The fix stores the exact preset frequency. A second defect was that the mobile chart was too small, which a fixed-height, non-scaling-stroke SVG fixed.
- I checked factual sentences against the records. One unsourced generalisation was removed: that feedback controllers always amplify noise outside their band (the waterbed effect). The distance from the microphone to the eardrum was also unsourced and removed. The NIOSH headset summary was corrected to match the paper.

## Gaps
- There are no accessible per-frequency measurements of current consumer headphones or earbuds. The numbers come from prototypes and from 2017 aviation and industrial headsets.
- The λ/10 zone of quiet comes from teaching slides as a rule of thumb for diffuse fields. It was not measured inside an ear cup.
- No source gives the latency of a specific commercial product, so the interactive's delays are illustrative.
- The venues of the 2017 and 2019 Helmut Schmidt University papers are inferred, not confirmed.
- Two exhibits (the Rivera figures) have rights unstated. They are embedded with attribution and the captions say so.
