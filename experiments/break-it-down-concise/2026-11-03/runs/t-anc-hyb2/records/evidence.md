# Evidence records

### E1: Lueg's opposite-phase wave in a pipe
- claim: C1 (support, context)
- type: figure+quote
- source: Process of silencing sound oscillations, US 2,043,416 — https://patents.google.com/patent/US2043416A/en
- locator: drawing sheet, Fig. 1; description column 1
- asset: assets/lueg-1936-fig1.png (rendered at 220 dpi from the patent PDF page 1, clip 80,190–470,338 pt); quote: "reproduced by a reproducing apparatus in the form of Sounds having an opposite phase"
- inspected: opened at full size; pipe, M, V, L, s1 and dashed s2 all visible; small fragment of Fig. 3 (G1) at lower left retained rather than altered
- notice: s2 (dashed) is the same wave shifted half a cycle so its peaks sit on s1's troughs downstream of L.
- limits: idealised drawing of a single tone in a duct.
- rights: US patent drawing, public domain

### E2: Microphones and paths in an ANC headphone
- claim: C2 (support)
- type: figure
- source: Psychoacoustic Hybrid Active Noise Control Structure for Application in Headphones — https://www.hsu-hh.de/ant/wp-content/uploads/sites/699/2018/08/ICSV25_full_paper_Rivera_Papantoni_Zoelzer.pdf
- locator: Fig. 1, p. 2
- asset: assets/rivera-2018-fig1-anc-headphone-signals.png (220 dpi crop; caption removed and restated)
- inspected: opened full size; outer mic, speaker, inner mic, all labels visible
- notice: outer mic x(n) hears noise first (feedforward reference); inner mic e(n) hears what is left at the ear (feedback/error); the speaker plays y(n), subtracted from leaked noise d(n).
- limits: notation is control-engineering shorthand; explained in caption.
- rights: rights unstated

### E3: Broadband vs tonal cancellation on one headphone
- claim: C3, C5, C6 (support)
- type: figure+metric
- source: Fully Digital Implementation of a Hybrid Feedback Structure for Broadband ANC in Headphones — https://www.hsu-hh.de/ant/wp-content/uploads/sites/699/2017/11/Rivera-Nowak-Zölzer-2017-Fully-Digital-Implementation-of-a-Hybrid-Feedback-Structure-for-Broadband-Active-Noise-Control-in-Headphones.pdf
- locator: Fig. 6 (p. 6); Section V (p. 5)
- asset: assets/rivera-2017-fig6-measured-spectra.png (220 dpi crop, caption removed and restated). Metrics: feedback (MVC) 10–20 dB attenuation up to ~870 Hz, ~10 dB amplification near 2600 Hz; IMC after 15 min adaptation: 40 dB at 105.5 Hz, 21 dB at 398.5 Hz, 22 dB at 2004.2 Hz; test noise = pseudo-random noise plus three sinusoids 20 dB louder; 89 dB SPL at the ear cup; loop latency 2.03 µs.
- inspected: opened full size; three panels, axes, legends, and tone peaks visible
- notice: in (a) blue sits below black only up to ~900 Hz then rises above it near 2.6 kHz; in (b) the three tone spikes vanish, including the one at 2 kHz, while the random noise floor barely moves.
- limits: lab prototype, synthetic stationary tones, long adaptation; the paper's venue is not printed.
- rights: rights unstated

### E4: Speech spectrogram
- claim: C7 (support)
- type: figure
- source: The perceptual significance of high-frequency energy in the human voice — https://doi.org/10.3389/fpsyg.2014.00587
- locator: Fig. 1
- asset: assets/monson-2014-fig1-speech-spectrogram.jpg (publisher image, 892×644)
- inspected: opened; axes 0–3 s and log frequency ~30 Hz–20 kHz legible; HFE marker visible
- notice: energy bands start near 100 Hz but stack up to several kHz, and the pattern changes every syllable with gaps between.
- limits: one male talker; colour scale not shown in figure.
- rights: CC BY (© 2014 Monson, Hunter, Lotto and Story)

### E5: ANC benefit grows with low-frequency content
- claim: C6 (support, qualify)
- type: figure+metric
- source: Rating the Performance of Active Noise Cancellation Devices — https://stacks.cdc.gov/view/cdc/210761
- locator: Fig. 1, p. 14; results p. 15
- asset: assets/niosh-2017-fig1-bose-a20.png (250 dpi crop including original caption)
- inspected: opened full size; axes, legend, and caption legible; low-resolution source raster
- notice: red (ANC off) protection drops from ~27 to ~2–5 dB as the noise gets bassier; blue (ANC on) stays ~24–33 dB.
- limits: one aviation headset; paper reports the Telex and Sennheiser headsets showed little ANC benefit; x-axis is C-minus-A level, a proxy for low-frequency content.
- rights: US government work (AFRL/NIOSH authors), public release, distribution unlimited

### E6: Zone of quiet
- claim: C4 (support)
- type: quote
- source: KU Leuven DASP Chapter 6 slides — https://homes.esat.kuleuven.be/~dspuser/dasp/material/Slides_2023_2024/Chapter-6%20Sound%20Field%20Control-pp40.pdf
- locator: slide 17
- asset: "e.g. 10dB reduction in zone approx λ/10"; slide 16: "100 Hz → λ=3,4m"
- inspected: not applicable
- notice: the useful zone scales with wavelength.
- limits: rule of thumb for diffuse fields.
- rights: quoted briefly with attribution

### E7: Causality in headphones
- claim: C3 (support)
- type: quote
- source: Shi et al., arXiv 2306.01425v2 — https://arxiv.org/abs/2306.01425
- locator: Section 2, p. 4
- asset: "This requirement poses a causality constraint on practical ANC systems."
- inspected: not applicable
- notice: the anti-noise must be ready before the noise arrives at the ear.
- limits: review statement.
- rights: arXiv licence; short quote

### E8: Timing error vs frequency (generated)
- claim: C3 (context)
- type: generated
- source: physics of two sinusoids, residual amplitude = 2|sin(πfτ)| for a pure timing error τ with equal amplitudes
- asset: inline interactive in report
- notice: the same timing error that is harmless at 100 Hz ruins cancellation at a few kHz.
- limits: ignores amplitude error, room/ear-cup acoustics, and controller compensation; τ values are illustrative.
- rights: original

## Gaps / omitted
- No accessible per-frequency measurement of a current consumer headphone (RTINGS, Stereophile, MDPI blocked).
- ICSV25 Fig. 5 (residual spectra) not embedded: E3 shows the same kind of data more clearly; mentioned as a qualifier only.
