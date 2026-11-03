# Run notes

Elapsed: about 17 minutes of wall clock (12:50 to 13:07 CST, 2026-11-03).

## Decisions
- Ten claims (records/claims.md). The ranking was C3/C4 (phase tolerance, and delay turning into a frequency-proportional phase error) as the core, then C6 (measured ~1 kHz ceiling) and C7/C8/C9 (hum versus voice). C5 (waterbed) and C10 (quiet zone, pinna) were treated as secondary.
- One worked example carried throughout: 50 µs of residual timing error, a 100 Hz hum (1.8°, −30 dB) against a 2 kHz consonant (36°, −4 dB).
- One interactive, a frequency slider and a timing-error slider with presets. It shows the waveform sum and a cancellation-versus-frequency curve, and closes the gap between "a fixed delay" and "fails at high frequency". The model is derived (2 − 2cos φ, φ = 360·f·τ), labelled as generated, and its assumptions are stated. The timing-error range is capped at 100 µs so that a whole-cycle delay (360°) cannot falsely show perfect cancellation of a pure tone.
- Exhibits embedded: Shi et al. Fig. 1 (Lueg patent), the RTINGS/Creative hybrid mic diagram, audioXpress Fig. 3 (mismatch heat map), audioXpress Fig. 8 (waterbed), the RTINGS ANC on/off graph, and Monson et al. Fig. 1 (speech spectrogram). The RTINGS range table was dropped from both versions because the on/off graph shows the same data per frequency.
- Rights: arXiv CC BY-NC-SA 4.0 and Frontiers CC BY, credited. RTINGS and audioXpress state no reuse terms, so those images are embedded with attribution and captions saying "reuse terms not stated."
- Distillation: body prose went from 1,973 words (draft.html) to 1,038 words (report.html), about 53%. Captions went from 402 to 369 words and source notes from 289 to 248. All six figures and the interactive were kept.

## Sources read
- Shi, Lam, Gan, Cheer, Elliott, arXiv 2306.01425v2: full PDF.
- Skovorodnikov, audioXpress, Nov 2023: full, rendered with headless Chromium.
- Lim, RTINGS (Apr 2024, updated Sep 2025): full, rendered with headless Chromium.
- Monson et al. 2014, Frontiers in Psychology, via PMC: partial (history, acoustics, Fig. 1). License checked on the Frontiers page.
- Dropped: Brammer & Pan, Canadian Acoustics (its metadata could not be verified because the article ID maps to a different paper) and Lu et al. survey (not needed).
- Inaccessible: MDPI Acoustics 6(4):60 (403), two IOA proceedings PDFs (HTML stubs/404), Liebich et al. 2018 (host unreachable).

## Verification
- Fonts: after document.fonts.ready, `document.fonts.check('600 1em Sora')` and `('400 1em Inter')` both return true at 1280 and 390 px, loaded from Google Fonts over the network.
- Layout: at 1280 and 390 px, scrollWidth equals clientWidth. There are no broken or upscaled images and no console errors. The only elements wider than the viewport are the two wide figures inside keyboard-focusable horizontal scroll regions, and each links to a full-size image. A first-pass bug, inline max-width overriding the 100% cap and overflowing at 390 px, was fixed and rechecked.
- Screenshots inspected in scratch/final-*.png and draft-*.png.
- Interactive, all values matching the formula:
  - Default 100 Hz / 50 µs gives 1.8°, −30.1 dB.
  - The 2 kHz preset gives 36°, −4.2 dB.
  - τ=0 gives "below −60 dB".
  - At 2 kHz with τ=100 µs: 72°, +1.4 dB.
  - At 5 kHz with τ=100 µs: 180°, +6.0 dB.
  - At 50 Hz with τ=100 µs: −30.1 dB.
  - Reset restores the defaults.
  - Keyboard Home/End and Tab work, with a visible red focus outline.
  - With JavaScript disabled, the static readout shows default values and a noscript summary appears.
  - The canvases have role=img labels; readout updates are aria-live.
  - Nothing animates, so no reduced-motion handling is needed.
- Fact checks: every quote was compared verbatim against the rendered source text. The audioXpress "2 dB / 20° → −10 dB" claim was spot-checked: each error on its own gives about −13.7 dB and −9.2 dB respectively, so the claim is approximate, and the draft says so. The RTINGS graph's 15–35 dB band was read off the figure.

## Gaps
- C7 (the tonal nature of engine hum) rests on Shi et al.'s aircraft blade-pass statement plus textbook background. No engine-tone spectrum was extracted.
- C10 (shrinking quiet zone) is conditional. Shi states it for car cabins, and the report frames it that way.
- The RTINGS and audioXpress images have unstated rights.
- The assets folder also keeps full-resolution copies (rtings *-large.jpg, shi2023-fig1-full.jpg) that serve as enlarged-view links.
