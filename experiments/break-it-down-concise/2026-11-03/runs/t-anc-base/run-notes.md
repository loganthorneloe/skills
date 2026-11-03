# Run notes

Elapsed: roughly 11 minutes by system clock (12:37–12:48 CST), research through final checks.

## Decisions
- Claims C1–C9 defined in records/audit.md. C1 (superposition) treated as settled textbook background; speed of sound 343 m/s is textbook.
- Main measured exhibit is Streeter et al. 2004 Fig. 1 (ANR vs frequency). Zhang & Qiu 2014 Fig. 2 carries the predictability/lateness point. Elliott et al. 2018 supplies zone-of-quiet and ~1 kHz statements as quotes. DPA/Brixen page supplies two speech charts (conditional source).
- One generated interactive (pure tone + delayed, scaled anti-noise) added because no source exhibit shows how a fixed delay converts into a pitch-dependent phase error. Delay values are stated as illustrative. Frequency range capped at 4 kHz so 200 µs never reaches a full 360° cycle (which would show misleading "complete" re-alignment for a pure tone).
- Worked-values table doubles as the no-JS fallback; default SVG paths and result values are embedded statically.
- Brammer et al. 2004 dropped as redundant.

## Sources read
- Streeter, Ray, Collier 2004 ACC paper (NTNU PDF): pp. 1–3 full, rest skimmed.
- Zhang & Qiu 2014 Applied Acoustics (UTS author manuscript PDF): full text, experiments skimmed.
- Elliott, Jung, Cheer 2018 Sci Rep (PMC): partial, via fetch tool excerpts.
- Brixen, DPA Mic University page: partial, via fetch tool; two images downloaded and opened.
- Brammer et al. 2004 Canadian Acoustics: full (2 pages), not used.
- Unreachable: Leventhall IOA papers and Benois IOA paper (404), Liebich EUSIPCO 2016 (connection refused), ISVR tutorial (VPN-only), PMC4336616 (captcha).
- One retraction/erratum search each for Streeter, Elliott, Zhang & Qiu: none found.

## Verification
- Fonts: after document.fonts.ready, document.fonts.check('600 1em Sora') and ('400 1em Inter') both true at 1280 and 390 (Google Fonts loaded over network).
- Layout: no horizontal page overflow at 1280 or 390 (scrollWidth == clientWidth) after fixing a table overflow and a figure max-width override. Wide three-panel voice chart and the table sit in keyboard-focusable horizontal scroll regions on narrow screens. All four images load at or below natural size. No console errors.
- Interactive: default 100 Hz/50 µs/100% → 1.8°, 3%, 30 dB quieter, 3.4 m (matches hand calculation 30.06 dB). 3 kHz/50 µs → 54°, 91%, 0.9 dB. 3 kHz/100 µs → 108°, 4.2 dB louder. Boundary 4 kHz/200 µs → 288°, 1.4 dB louder. 0 µs/90% → 20 dB; 80% and 120% → 14 dB; perfect → "complete". Reset restores defaults; ArrowRight on delay slider steps 5 µs; focus outline 2px red. JS disabled: static waves and default results render.
- Screenshots in scratch/ (shot-1280*, shot-390*, lab-*.png) inspected; fixed result-tile nested-border bug and double rule under sources.

## Gaps
- No audited source for current consumer-headphone latency; model delays illustrative.
- Measured curves are 2004 circumaural earcups; current earbuds not independently measured.
- Speech spectrum comes only from a conditional manufacturer education page; French & Steinberg 1947 not read directly.
- All embedded figures have unstated reuse rights; embedded with attribution and stated as such in captions.
- Report depends on network for Google Fonts; falls back to system sans-serif offline.
