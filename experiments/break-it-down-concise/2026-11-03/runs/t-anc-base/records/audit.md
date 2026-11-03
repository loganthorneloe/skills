# Source audit records

Claims
- C1: Sound is a pressure wave; pressures from two sources add at a point (superposition), so an equal and opposite wave cancels. (textbook background, no record)
- C2: ANC headphones sense noise with microphones (outside the cup for feedforward, inside for feedback), compute an inverted signal, and play it through the speaker.
- C3: Cancellation depends on matching amplitude and timing; the anti-noise must be produced in time (causality), and a fixed delay is a larger phase error at higher frequency.
- C4: Measured active reduction is largest roughly 50–400 Hz (about 10–30 dB) and falls to near zero or below (amplification) around 800 Hz–1 kHz and above.
- C5: The zone of quiet a local system creates is about one tenth of a wavelength across, so it shrinks at higher frequency.
- C6: Narrowband, predictable noise tolerates lateness better than broadband noise.
- C7: Voice energy spreads from about 100 Hz to 8 kHz, and the bands most important for intelligibility are about 1–4 kHz.
- C8: Passive isolation of the earcup is weak at low frequency and grows with frequency.
- C9: Feedback ANC can add noise in the mid band (above ~800 Hz).

### Hybrid Feedforward-Feedback Active Noise Control
- url: https://skoge.folk.ntnu.no/prost/proceedings/acc04/Papers/0511_ThM09.1.pdf; text read from: same (NTNU-hosted copy of ACC 2004 proceedings)
- byline: Alexander D. Streeter, Laura R. Ray, Robert D. Collier (Thayer School of Engineering, Dartmouth) · conference paper · Proceedings of the 2004 American Control Conference (AACC) · June 2004
- verdicts: C2 pass; C4 pass; C6 conditional (pure tones described as the most ideal case because gains can be tuned per frequency; not a direct predictability test); C8 pass; C9 pass
- use: Introduction and Fig. 1 (p. 2876); system description p. 2877; noise-source description p. 2878; abstract figures
- credibility: Experimental control-engineering group that built and measured a hybrid earcup in a low-frequency acoustic test cell; Fig. 1 combines their own measurements with published commercial-headset data.
- contribution: Compiles measured active noise reduction vs frequency for feedback and feedforward earcups; reports 10–20 dB feedback ANR over 50–400 Hz, negative ANR above 800 Hz, and 5–30 dB hybrid performance 50–800 Hz for tones.
- limits: 2004 hardware, circumaural hearing-protector earcup in a test cell, not current consumer earbuds; modern products may reach higher, but the frequency trend is structural. Rights unstated (AACC copyright line on page).
- read: full for pp. 1–3 (intro, architecture, setup); results pages skimmed · via NTNU proceedings mirror
- retraction/errata search: one search, none found.

### Head tracking extends local active control of broadband sound to higher frequencies
- url: https://pmc.ncbi.nlm.nih.gov/articles/PMC5876390/ (doi 10.1038/s41598-018-23531-y); text read from: PMC via fetch tool
- byline: Stephen J. Elliott, Woomin Jung, Jordan Cheer (ISVR, University of Southampton) · peer-reviewed research article · Scientific Reports 8:5403 · 29 March 2018
- verdicts: C4 conditional (states headphones reduce noise up to about 1 kHz, as background, not a headphone measurement); C5 pass
- use: Abstract and Introduction statements on zone-of-quiet size (about 1/10 wavelength), 5 cm head movement, headphones up to about 1 kHz
- credibility: Elliott is an author of the standard textbooks on active control (Nelson & Elliott, Active Control of Sound; Elliott, Signal Processing for Active Control), and the paper reports their own measured experiments.
- contribution: Restates the established zone-of-quiet limit and shows head tracking extends local control to about 1 kHz with ~20 dB attenuation for a headrest system.
- limits: Headrest (loudspeakers away from the ear), not headphones; used only for the zone-of-quiet principle. Read through fetch-tool summary with verbatim excerpts, counted as partial. CC BY 4.0.
- read: partial (abstract, introduction, results excerpts via fetch tool)
- retraction/errata search: one search, none found.

### Causality study on a feedforward active noise control headset with different noise coming directions in free field
- url: https://doi.org/10.1016/j.apacoust.2014.01.004; text read from: https://opus.lib.uts.edu.au/handle/10453/118176 (author manuscript PDF)
- byline: Limin Zhang, Xiaojun Qiu (Institute of Acoustics, Nanjing University) · peer-reviewed journal article · Applied Acoustics 80:36–44, Elsevier · June 2014
- verdicts: C2 pass (feedforward architecture: reference mic, error mic, secondary source); C3 pass (causality constraint, delay sources); C6 pass (Fig. 2, reduction vs non-causal delay for different bandwidths)
- use: Introduction pp. 2–4; Section 2 pure-delay model and Fig. 2; Conclusions
- credibility: Acoustics researchers who derive the delay model and confirm predictions with headset measurements in anechoic and reverberant chambers.
- contribution: Shows that when anti-noise is late (non-causal), noise reduction falls, and falls much faster for broadband noise than narrowband noise; feedforward headsets need a causal margin.
- limits: Fig. 2 is a simplified model with low-pass-shaped noise at 16 kHz sampling (1 sample = 62.5 µs); "bandwidth" here is the -3 dB bandwidth of low-pass noise, so narrow bandwidth means both low frequency and more predictable. Manuscript version, not the typeset article. Rights unstated (Elsevier copyright in abstract; repository marks open access).
- read: full text of manuscript (intro, model, conclusions; experiment sections skimmed)
- retraction/errata search: one search, none found.

### Facts about speech intelligibility
- url: https://www.dpamicrophones.com/mic-university/facts-about-speech-intelligibility; text read from: same via fetch tool; images downloaded
- byline: Eddy Bøgh Brixen · educational article · DPA Microphones Mic University · undated, accessed 3 November 2026
- verdicts: C7 conditional (manufacturer education page; importance chart credited to French & Steinberg 1947, JASA; voice spectra chart uncredited)
- use: "Voice spectra (1/3 octave) depending on efforts" graphic; importance graphic credited to French & Steinberg 1947; text on vowel and consonant bands
- credibility: Brixen is an audio engineer and AES author whose cited preprints measure voice spectra; the importance chart reproduces a classic Bell Labs intelligibility study.
- contribution: Shows that ordinary speech has energy from 125 Hz to 8 kHz peaking near 500 Hz, and that bands 1–4 kHz carry most intelligibility.
- limits: Commercial microphone maker's page, undated; voice-spectra measurement conditions not stated; band edges approximate. I did not read French & Steinberg 1947 itself. Rights unstated.
- read: partial (fetch-tool extraction of text and figure list; two figures opened)

Failed / dropped
- Brammer et al. 2004, Canadian Acoustics 32(3) — passes for C8 but redundant with Streeter; dropped.
- Bryanston/ISVR animation page — fetched copy, origin unclear; not needed.
- Leventhall IOA papers, Benois IOA paper, Liebich EUSIPCO 2016 — not retrievable (404 / connection refused).

Gaps
- C3: no audited source gives measured latency of a current consumer headphone; the interactive uses illustrative delays.
- C7: only a conditional source (manufacturer education page) for speech spectrum.
- C4: measurements are 2004 circumaural earcups; current consumer products not independently measured here.
