# Run notes

Elapsed: roughly 10–15 minutes of wall-clock by the system clock (12:37 to about 12:48 CST).

## Decisions
- Seven claims (C1–C7) are listed in records/audit.md. Ranked by how much the answer depends on each: C2 (time to distance) and C3 (clock as fourth unknown) got full mechanism, plus the one interactive. C4/C5 (atomic clocks, relativity) got one source figure each. C1, C6 and C7 are brief.
- Primary source is Ashby's 2003 Living Reviews article, read from the EMIS mirror's HTML archive because the Springer and PMC copies were blocked by a login redirect and reCAPTCHA. The equations are images there, so I read the values (Eq. 1, 35, 36, a ≈ 9545 km, 23 ns) from the rendered equation images.
- GPS.gov accuracy and space-segment pages came from archive.gps.gov, because the live accuracy URL returned 404 when fetched. The report links the canonical URLs.
- Exhibits: GPS.gov URE graphic, FAA histogram, urban-canyon cartoon, Ashby Fig. 1 (Allan deviation) and Fig. 2 (frequency shift vs radius). All 5 are kept in both draft and report. The Ashby figures' reuse terms are unstated and the captions say so.
- One generated interactive: a 2D clock-bias least-squares model. Input is the phone clock error. The visible consequence is that the range arcs miss the true position and the clock-ignoring fix lands about 400 m down per µs. The added insight is that the bias leaks into height, and that solving for it removes it exactly.
- Derived arithmetic, not quoted: 67 ms travel time, 4.4647e-10 × 86,400 s = 38.6 µs/day, 11.6 km, the quartz day-drift read off Fig. 1 as "a few microseconds".
- Left out: assisted GPS and multi-constellation phone behaviour. No source was audited for them, so I did not state them.
- Distillation: prose outside sources, figures and the lab went from 1,782 words (draft.html) to 981 words (report.html), about 55%. No visuals were removed.

## Sources read
- Ashby, Relativity in the Global Positioning System (2003): §1, §2 opening and §5 read; the rest skimmed. One erratum search found nothing.
- GPS.gov GPS Accuracy (archive, modified March 2022): read in full, 3 images downloaded.
- GPS.gov Space Segment (archive, modified June 2022): read in full.
- GPS.gov image library: checked for its public-domain statement.
- Failed or blocked: PMC copy of Ashby (reCAPTCHA), Springer (auth redirect), PMC9921678 smartphone range-error study (reCAPTCHA), DOAJ (403).

## Verification (Playwright Chromium, scratch/check.py)
- At 1280 and 390 px: no horizontal overflow, no broken images, no upscaled images, no console errors.
- `document.fonts.check` returned true for both 600 Sora and 400 Inter.
- Slider states, all matching the offline Node prototype (scratch/model.js):
  - −3 µs gives −899 m range offset and a fix 1,199 m upward. Solving with the clock gives 0.00 m and recovers −3.00 µs.
  - 0 µs gives 0 everywhere.
  - +2.5 µs gives a fix 999 m downward.
  - +3 µs gives a fix 1,199 m downward.
  - Reset returns to +1.00 µs and 400 m downward.
- Keyboard: Home and End reach the ±3 µs limits, the arrow key steps 0.05, and Tab moves on to Reset.
- With JavaScript disabled, the tiles show the default values and a noscript sentence explains the result. The SVG plot stays empty.
- Fixes made after screenshots:
  - The plot was too short to show the ±3 µs estimate.
  - Satellite labels were off-canvas or clipped on mobile.
  - SVG labels were too small on mobile; they now scale with width.
  - Spacing under the paired figures was missing.
  - On narrow screens the Ashby figures now sit in focusable horizontal scroll regions at 600 px.
- Fact check: every factual sentence was compared with the records. I removed unsourced claims about phone antennas, an unsourced quartz-offset size and "fixed sites" for the FAA receivers.

## Gaps
- Fonts load from Google Fonts, so they need network access.
- The Ashby figure titles in the source carry their own clipping: the "100000" axis label is cut off in Fig. 2.
- No source was audited for the claim that "height is usually the weakest coordinate". It is stated as general background.
- The satellite count is dated July 2023.
