# Source audit records (accessed 2026-11-03)

### Active Noise Control in The New Century: The Role and Prospect of Signal Processing
- url: https://arxiv.org/abs/2306.01425v2; text read from: https://arxiv.org/pdf/2306.01425v2 (PDF, 6 pp.)
- byline: Dongyuan Shi, Bhan Lam, Woon-Seng Gan, Jordan Cheer, Stephen J. Elliott · conference paper preprint (submitted to Inter-Noise 2023, Chiba) · arXiv · v1 2 June 2023, v2 6 July 2023
- verdicts: C1 pass; C4 pass (causality constraint and short acoustic delay in headphones; the frequency-proportional phase arithmetic is derived, not stated by the source); C7 conditional (supports tonal blade-pass noise in aircraft and ~30 dB on tonal duct noise; not a headphone measurement); C9 pass (fixed coefficients in commercial headphones); C10 conditional (quiet-zone shrinkage is stated for in-cabin zones, used only as a general principle)
- use: Sec. 1 (Lueg patent, Fig. 1; headset history), Sec. 2 (causality constraint, fixed filters), p.3 (blade-pass tones, 7–13 dB), p.2–3 (Kuo ~30 dB tonal), p.6 (quiet zone vs frequency)
- credibility: Authors run ANC research groups at NTU Singapore and ISVR Southampton; Elliott co-wrote the field's standard 1993 tutorial and textbook. Firsthand research expertise.
- contribution: Historical and technical review of ANC; states the physics (destructive interference), the headphone causality constraint, and that ANC is most effective at low frequencies.
- limits: Short review paper (6 pp.), not peer-reviewed journal; claims are mostly summary statements citing others, not new measurements. The 30 dB figure is for a 1-D duct, not a headphone.
- read: full · version v2 · via arXiv PDF. Retraction/erratum search: none found; one index lists only four authors, the PDF lists five.

### Development & Design: The Impact of Microphone Specifications on Active Noise Cancellation Performance
- url: https://audioxpress.com/article/development-design-the-impact-of-microphone-specifications-on-active-noise-cancellation-performance; text read from: same (rendered with a headless browser)
- byline: Nikolay Skovorodnikov (Senior Manager, Applications Engineering, MEMS Microphones, Knowles) · trade-magazine engineering article · audioXpress · print November 2023, web 3 January 2024
- verdicts: C2 pass; C3 pass (Fig. 3 and text; spot-checked with the interference formula, see limits); C4 pass (latency limits high-frequency FF ANC; target phase cannot be fit without violating causality); C5 pass (Fig. 8, waterbed text); C10 conditional (pinna resonance 2–3 kHz limits FF fit; one design example)
- use: Figure 3 (sinewave cancellation vs magnitude and phase difference), text after Fig. 3 (−10 dB within 2 dB / 20°), Fig. 4 text (causality, pinna resonance), Fig. 5 text (latency → high-frequency limit), Figs. 7–8 text (FB tuning, >15 dB at ~200 Hz, amplification 1–3 kHz)
- credibility: Written by an applications engineer at a major maker of the MEMS microphones used in earbuds; the analysis uses measured transfer functions and standard control theory. Firsthand practice.
- contribution: Shows how precisely anti-noise must match, why latency caps the upper frequency, and how feedback tuning trades low-frequency cancellation for high-frequency amplification.
- limits: Vendor author with an interest in microphone specs (conflict of interest is in emphasis, not the physics). Figs. 3 and 8 are computed/design examples, not measurements of a commercial product. Spot-check: phase error alone of 20° gives −10·log10(2−2cos20°) ≈ −9.2 dB; magnitude error alone of 2 dB gives ≈ −13.7 dB; both together ≈ −8.6 dB, so "up to 2 dB and 20°" for −10 dB is approximate, roughly per error on its own.
- read: full · via headless render. Erratum search: none found.

### ANC Headphones vs Earmuffs: How We Used Both To Improve Our Noise Isolation Tests
- url: https://www.rtings.com/headphones/learn/research/noise-isolation; text read from: same (rendered with a headless browser)
- byline: Nicholas Lim · lab methodology article · RTINGS.com · published 4 April 2024, updated 10 September 2025
- verdicts: C2 pass (mic placement diagrams, credited to Creative); C6 pass (measured ANC on/off curves for three headphones converge ~1 kHz; range table); C7 conditional (only says bass range includes airplane and engine rumble); C9 pass (AirPods Max take ~3 s to reach full attenuation on a 1 kHz tone)
- use: "Comparing performance" graph (ANC on/off, Sony WH-1000XM6, Bose QC Ultra, AirPods Max), range table, response-time paragraph, feedforward/feedback/hybrid section
- credibility: Independent test lab that buys products and measures them on a head simulator with a documented method (pink noise, 5 s priming, pseudo-diffuse field). Firsthand measurement.
- contribution: Measured evidence that ANC's gain is confined to low frequencies on today's flagship headphones.
- limits: Three products, one rig and one fit; RTINGS earns affiliate revenue. Graph's y-axis is reduction relative to no headphones; "ANC Off" is the passive curve. Bass band in its table includes passive effect.
- read: full · via headless render. Correction search: changelog only (Sep 2025 graphics update).

### The perceptual significance of high-frequency energy in the human voice
- url: https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00587/full; text read from: https://pmc.ncbi.nlm.nih.gov/articles/PMC4059169/
- byline: Brian B. Monson, Eric J. Hunter, Andrew J. Lotto, Brad H. Story · review article · Frontiers in Psychology 5:587 · 16 June 2014
- verdicts: C8 pass (Fig. 1 spectrogram; telephone band 300 Hz–3.4 kHz; ~95% accuracy for speech low-passed at 4 kHz)
- use: Figure 1 (broadband spectrogram of a male talker), "History" section (articulation index, telephone band), "Acoustical characteristics" (energy above 5 kHz 20–40 dB down)
- credibility: Speech scientists (National Center for Voice and Speech, Harvard Medical School, University of Arizona) reviewing acoustic measurements of speech; peer-reviewed open-access journal.
- contribution: Shows where speech energy sits and that intelligibility depends on content up to about 4 kHz.
- limits: Focus is on energy above 5 kHz; Fig. 1 is one male talker. Used only to locate speech energy, not for ANC claims.
- read: partial (abstract, history, acoustical characteristics, Fig. 1; fricative and perception sections skimmed) · via PMC. Erratum search: none found.

## Dropped
- Brammer & Pan, "Opportunities for active noise control in communication headsets" (Canadian Acoustics, JCAA PDF): content relevant (feedback headsets up to 1 kHz, conditionally stable) but the journal page for the downloaded ID shows a different article, so volume/date could not be verified; RTINGS and audioXpress cover the same claims. Not used.
- Lu et al., arXiv 2110.00531 (ANC survey Part I): algorithm survey, not needed for any claim.
- MDPI Acoustics 6(4):60 (ANC headphone measurement) and IOA Wu/Qiu papers: inaccessible (403 / HTML stub).

## Gaps
- C7: only conditional sources — no audited open measurement of a headphone cancelling an engine tone specifically; hum's tonal nature rests on Shi et al. (aircraft blade-pass tones) and settled background on rotating machines.
- C10: only conditional sources — stated as a secondary limit.
