# Source audit records — active noise cancellation in headphones

Accessed 2026-11-03.

## Claims

- C1: Sound is a pressure wave; pressures from two sources add at a point (superposition), so a wave of equal amplitude and opposite phase cancels the original there.
- C2: ANC headphones measure noise with an outer (reference) microphone and/or an inner (error) microphone and drive the headphone speaker with anti-noise; feedforward uses the outer mic, feedback the inner mic, hybrid both.
- C3: The anti-noise must be produced in time; processing and acoustic delays (causality) limit the frequency range that can be cancelled. A fixed timing error is a larger fraction of a short (high-frequency) cycle.
- C4: The region of useful cancellation around the error microphone ("zone of quiet") is about a tenth of a wavelength across, so it shrinks as frequency rises.
- C5: Periodic (tonal) noise can be cancelled even at higher frequencies because it is predictable; broadband random noise is cancelled only at low frequencies. A feedback controller with loop delay must effectively predict the noise.
- C6: Passive isolation from the ear cup handles mid and high frequencies; ANC adds attenuation at low frequencies (typical figures: 10–20 dB below ~0.5–1 kHz). The ANC benefit grows with the low-frequency content of the noise and varies by device. Feedback ANC can amplify noise just above its band.
- C7: Speech spans roughly 100 Hz to beyond 5 kHz with structure that changes from moment to moment; fricatives such as /s/ peak at 3–8 kHz.
- C8: Engine and propeller noise is dominated by a fundamental tone and its harmonics; engine-noise ANC became commercial well before broadband road-noise ANC.

---

### Process of silencing sound oscillations (US Patent 2,043,416)
- url: https://patents.google.com/patent/US2043416A/en; text read from: https://patentimages.storage.googleapis.com/97/93/fc/19408ed05d22d6/US2043416.pdf
- byline: Paul Lueg · US patent · United States Patent Office · filed 8 March 1934 (German priority 27 Jan 1933), granted 9 June 1936
- verdicts: C1 pass (historical statement of the principle; physics is textbook)
- use: Fig. 1 (pipe T, microphone M, amplifier V, loudspeaker L, waves s1 and s2); description of Fig. 1
- credibility: Primary document; the patent widely cited (e.g., Shi et al. 2023 review co-authored by S. J. Elliott) as the origin of ANC.
- contribution: States the method: receive the sound with a microphone and reproduce it through a loudspeaker "in the form of sounds having an opposite phase"; Fig. 1 draws an opposite-phase wave s2 overlapping s1 in a duct.
- limits: A 1930s patent, not an experiment; it demonstrates the idea, not performance. OCR text of the PDF is imperfect; the drawing was checked visually.
- read: full (3 pages; OCR text plus rendered drawing page)

### Active Noise Control in The New Century: The Role and Prospect of Signal Processing
- url: https://arxiv.org/abs/2306.01425; text read from: https://arxiv.org/pdf/2306.01425v2
- byline: Dongyuan Shi, Bhan Lam, and colleagues (Woon-Seng Gan, Jordan Cheer, Stephen J. Elliott) · review paper (preprint) · arXiv eess.AS · June 2023 (v2 6 July 2023)
- verdicts: C1 pass; C3 pass (causality constraint, headphone processing window); C4 conditional (states only that the quiet zone shrinks with frequency; size from KU Leuven slides); C8 pass (aircraft blade-pass tones; engine vs road-noise history)
- use: Section 1 (Lueg, aircraft blade-pass frequency, car engine vs road noise, headphone history); Section 2 (causality constraint; fixed coefficients in commercial headphones); Section 3 (ANC most effective at low frequency)
- credibility: Authors are active ANC researchers at NTU Singapore and ISVR Southampton; Elliott co-wrote the field's foundational texts. Review statements are consistent with the primary papers read here.
- contribution: Historical and technical review: anti-noise is 180 degrees out of phase; processing must finish before the noise arrives, which is hardest in small headphones; engine (tonal) noise control commercialised in cars long before broadband road noise (Hyundai 2018).
- limits: Preprint labelled a proposed feature paper; no new measurements. Search found no retraction or erratum. Some typos (e.g., "Leug").
- read: full · version v2

### Digital Audio Signal Processing, Chapter 6: Sound Field Control (lecture slides)
- url: https://homes.esat.kuleuven.be/~dspuser/dasp/material/Slides_2023_2024/Chapter-6%20Sound%20Field%20Control-pp40.pdf; text read from: same
- byline: Jesper Brunnström and Marc Moonen · university lecture slides · KU Leuven, Dept. of Electrical Engineering (ESAT-STADIUS) · version 2023–2024
- verdicts: C2 pass (feedforward and feedback set-ups); C4 pass (zone of quiet ≈ λ/10 for 10 dB); C5 pass (with loop delay the feedback controller must act as a predictor); C6 conditional (headset figure "10–15 dB for 30–500 Hz" is given as an example, not sourced on the slide)
- use: slides 16–17 (passive vs active, 100 Hz → λ = 3.4 m, zone of quiet), 18–20 (feedforward), 33 and 37 (feedback ANC, predictor)
- credibility: Moonen is a long-standing professor of signal processing at KU Leuven teaching this course; slide content agrees with Elliott's published zone-of-quiet results.
- contribution: Compact teaching statement of the physics and control structures.
- limits: Slides, not peer-reviewed; numbers are rules of thumb without citations on the slide. The λ/10 rule is for a pressure-minimising error microphone in a diffuse field; inside a small ear cup the geometry differs.
- read: full (40 slides on 20 pages)

### Hybrid Active Noise Control Structures: A Short Overview
- url: https://www.hsu-hh.de/ant/wp-content/uploads/sites/699/2019/01/Hybrid-Active-Noise-Control-Structures_-A-Short-Overview-Rivera-Nowak-Zoelzer.pdf; text read from: same
- byline: Piero Rivera Benois, Patrick Nowak, and Udo Zölzer · conference paper · DAGA (German Acoustical Society annual meeting), Helmut Schmidt University (unverified venue; inferred from upload folder and format) · 2019 (upload date)
- verdicts: C2 pass; C3 pass (feedback bandwidth limited by loop delays; feedforward causality condition); C5 conditional (feedforward attenuates only noise correlated with the reference — supports, but does not itself contrast tones and speech)
- use: Section 1 and Section 2 (MVC, IMC, feedforward; Eq. 1–4)
- credibility: The group builds and measures real-time ANC headphone prototypes (see the two papers below).
- contribution: Defines the microphones, paths, and the three classical control structures in a headphone context.
- limits: Venue and date inferred from the host page; overview without measurements.
- read: partial (sections 1–2 and start of 3 read; hybrid combinations skimmed)

### Psychoacoustic Hybrid Active Noise Control Structure for Application in Headphones
- url: https://www.hsu-hh.de/ant/wp-content/uploads/sites/699/2018/08/ICSV25_full_paper_Rivera_Papantoni_Zoelzer.pdf; text read from: same
- byline: Piero Rivera Benois, Veatriki Papantoni, and Udo Zölzer · conference paper · 25th International Congress on Sound and Vibration (ICSV25), Hiroshima · July 2018
- verdicts: C2 pass (Fig. 1); C6 conditional (passive materials handle mid/high frequencies; ANC handles low; but their lab feedforward attenuated up to ~7.5 kHz under a fixed noise direction — used as a qualifier)
- use: Introduction and Fig. 1; Evaluation and Figs. 5–6
- credibility: Real-time FPGA prototype on a Beyerdynamic DT 770 PRO, measured on a Neumann KU100 dummy head.
- contribution: Labels the microphones and paths in an ANC headphone; shows measured residual spectra; finds passive damping dominates perceived pleasantness.
- limits: One prototype, one loudspeaker position, synthetic noise; not a commercial product.
- read: full

### Fully Digital Implementation of a Hybrid Feedback Structure for Broadband Active Noise Control in Headphones
- url: https://www.hsu-hh.de/ant/wp-content/uploads/sites/699/2017/11/Rivera-Nowak-Zölzer-2017-Fully-Digital-Implementation-of-a-Hybrid-Feedback-Structure-for-Broadband-Active-Noise-Control-in-Headphones.pdf; text read from: same
- byline: Piero Rivera Benois, Patrick Nowak, and Udo Zölzer · conference paper (IEEE-style proceedings; venue not printed in PDF, unverified) · Helmut Schmidt University · 2017
- verdicts: C3 pass (sigma-delta converter and DSP delays "substantially decrease the noise attenuation frequency bandwidth"; 2.03 µs latency restores it); C5 pass (Fig. 6: tones at 105.5, 398.5, 2004.2 Hz attenuated 40, 21, 22 dB by IMC while broadband feedback attenuation stops near 870 Hz); C6 pass (10–20 dB up to ~870 Hz; ~10 dB amplification near 2.6 kHz)
- use: Abstract, Section I, Section V and Fig. 6
- credibility: Measured on a headphone prototype on a KU100 dummy head with a known test signal; numbers in text match the plotted spectra on inspection.
- contribution: Direct measured contrast between broadband random noise and steady tones on the same headphone.
- limits: Lab prototype; IMC needed 15 minutes of adaptation; stationary synthetic tones, not real engines. Venue unconfirmed.
- read: full (6 pages)

### Rating the Performance of Active Noise Cancellation Devices
- url: https://stacks.cdc.gov/view/cdc/210761; text read from: https://stacks.cdc.gov/view/cdc/210761/cdc_210761_DS1.pdf
- byline: Hilary L. Gallagher (Air Force Research Laboratory) and William J. Murphy (NIOSH) · trade/society article · NHCA Spectrum, Vol. 34(1) · July 2017
- verdicts: C6 pass (ANC targets low frequency, "typically at 500 Hz and below"; Fig. 1 shows ANC-on protection staying high as low-frequency content rises while passive falls; other headsets show little benefit)
- use: p.13 introduction; p.14 Fig. 1; p.15 results for four headsets
- credibility: Government hearing-protection researchers; measurements followed ANSI S12.6 (REAT) and S12.42 (MIRE) with ten listeners.
- contribution: Real-ear measurements of four commercial ANC headsets showing benefit depends on low-frequency content and device.
- limits: Aviation/industrial headsets (2017), not current consumer earbuds; x-axis is C-minus-A level difference, a proxy for low-frequency content, not frequency itself.
- read: full (5 pages)

### The perceptual significance of high-frequency energy in the human voice
- url: https://doi.org/10.3389/fpsyg.2014.00587; text read from: https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00587/full
- byline: Brian B. Monson, Eric J. Hunter, Andrew J. Lotto, and Brad H. Story · review article · Frontiers in Psychology 5:587 · June 2014
- verdicts: C7 pass
- use: Fig. 1 spectrogram; Introduction (fricative energy 3–8 kHz and 5–10 kHz; energy above 5 kHz 20–40 dB lower)
- credibility: Speech and voice scientists; peer-reviewed open-access review; CC BY licence.
- contribution: Shows a real spectrogram of a male talker with energy from ~100 Hz to over 10 kHz, changing syllable by syllable.
- limits: One male talker in the figure; women's and children's voices sit higher. Read via fetch tool (partial: introduction and figure captions read, later sections skimmed).
- read: partial (introduction, Fig. 1 caption, licence; later sections not read)

## Failed or unused

- Kuo & Morgan (1999) Proc. IEEE tutorial; Elliott & Nelson (1993) IEEE SPM: no accessible full text — not used.
- Wu, Qiu, Ma, Guo, ICSV 2016 (UTS): closed access; abstract only — not used.
- MDPI Acoustics 6(4):60, RTINGS, Stereophile: pages blocked or script-rendered; not read — not used.

## Gaps

- C6: only conditional and prototype sources give per-frequency numbers for consumer headphones; commercial spectra not accessible. Report gives ranges with that restriction.
- C4: λ/10 rule comes from teaching slides and Elliott's diffuse-field work (search abstracts only); not measured inside an ear cup.
- C3: no accessible source gives a specific commercial headphone's latency; the interactive uses illustrative delay values labelled as assumptions.
- Disputed premise: "voices are high-frequency" is only partly true — voice fundamentals sit near 100–250 Hz, inside the ANC band. The harder part is that speech changes from moment to moment and much of its energy lies above ~1 kHz.
