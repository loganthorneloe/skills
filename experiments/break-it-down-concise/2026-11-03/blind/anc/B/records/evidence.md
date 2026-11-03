# Evidence records

### E1: Measured active noise reduction vs frequency
- claim: C4 (support), C9 (support), C2 (context)
- type: figure
- source: Streeter, Ray & Collier, Hybrid Feedforward-Feedback Active Noise Control — https://skoge.folk.ntnu.no/prost/proceedings/acc04/Papers/0511_ThM09.1.pdf
- locator: Fig. 1, p. 2876
- asset: ../assets/streeter-fig1-anr-vs-frequency.png (rendered from PDF at 250 dpi, 758x588)
- inspected: opened at full size; axes, all five legend entries, 25–6400 Hz axis and caption-free crop visible
- notice: Every curve peaks between ~50 and ~400 Hz (10–30 dB) and drops to 0 dB around 800 Hz–1 kHz; the feedback lower bound goes negative (adds noise) between ~800 Hz and 3 kHz.
- limits: 2004 earcups on a flat plate/MIRE; feedforward points are single pure tones (best case).
- rights: rights unstated (AACC copyright notice on page)

### E2: Late anti-noise hurts broadband noise far more than narrowband
- claim: C3 (support), C6 (support)
- type: figure
- source: Zhang & Qiu 2014, Applied Acoustics — https://opus.lib.uts.edu.au/handle/10453/118176 (author manuscript)
- locator: Fig. 2, manuscript p. 26
- asset: ../assets/zhang-qiu-fig2-noncausal-delay.png (250 dpi, 1209x953)
- inspected: opened at full size; both axes, legend with four bandwidths visible
- notice: At one sample of lateness (62.5 µs at 16 kHz), the 268 Hz-wide noise still drops ~7 dB, while the 5639 Hz-wide noise drops almost nothing.
- limits: Simplified pure-delay model with low-pass noise; absolute dB values are model outputs, not headphone measurements.
- rights: rights unstated (Elsevier; repository open access)

### E3: Zone of quiet size
- claim: C5 (support)
- type: quote
- source: Elliott, Jung & Cheer 2018, Scientific Reports — https://pmc.ncbi.nlm.nih.gov/articles/PMC5876390/
- locator: Abstract
- asset: "a zone of quiet which only extends to about one tenth of an acoustic wavelength"
- inspected: not applicable
- notice: Ties how far cancellation reaches to wavelength, which shrinks as frequency rises.
- limits: Diffuse-field theory for local control; headphones place the speaker close to the ear, which helps.
- rights: CC BY 4.0

### E4: Headphones reduce noise up to about 1 kHz
- claim: C4 (support, conditional)
- type: quote
- source: Elliott, Jung & Cheer 2018
- locator: Introduction
- asset: "active sound control headphones, which can reduce noise levels for frequencies up to about 1 kHz"
- inspected: not applicable
- notice: Independent statement of the same ~1 kHz ceiling seen in E1.
- limits: Background statement, not a measurement in this paper.
- rights: CC BY 4.0

### E5: Voice spectra by vocal effort
- claim: C7 (support)
- type: figure
- source: Brixen, Facts about speech intelligibility, DPA Microphones — https://www.dpamicrophones.com/mic-university/facts-about-speech-intelligibility
- locator: "Voice spectra (1/3 octave) depending on efforts" graphic
- asset: ../assets/dpa-voice-spectra-by-effort.jpg (1170x304, original file)
- inspected: opened; three panels, axes 125 Hz–8 kHz and legend visible
- notice: Normal speech (red) sits within about 10–15 dB of its peak from ~250 Hz up to ~4 kHz.
- limits: Measurement conditions unstated.
- rights: rights unstated

### E6: Where intelligibility lives
- claim: C7 (support)
- type: figure
- source: Brixen (DPA), chart credited to French & Steinberg 1947, JASA 19(1)
- locator: importance bar chart
- asset: ../assets/dpa-french-steinberg-importance.jpg (1170x352, original file)
- inspected: opened; all seven bars and axis labels visible
- notice: Bands at 1, 2 and 4 kHz carry roughly 75% of intelligibility; 125 and 250 Hz carry about 5%.
- limits: Octave-band importance from a 1947 study; read from the reproduction, not the original paper.
- rights: rights unstated

### E7: Passive attenuation grows with frequency
- claim: C8 (support)
- type: quote
- source: Streeter et al. 2004, p. 2876
- asset: "Passive attenuation provided by circumaural hearing protectors is minimal at low frequencies and increases with frequency."
- inspected: not applicable
- notice: Explains why ANC and the earcup divide the work.
- limits: Circumaural protectors; earbuds depend on seal.
- rights: rights unstated

### E8 (generated): Residual vs timing and level error
- claim: C3 (support)
- type: generated
- asset: in-page interactive; residual = |1 - g·e^(-j2πfτ)|, attenuation = -20·log10(residual)
- notice: The same delay costs little at 100 Hz and everything at a few kHz.
- limits: Single pure tone, ideal speaker; delay values illustrative.

Claims lacking evidence: none uncovered; C3 latency magnitudes for current products are unsourced (illustrative only).
Omitted: Elliott Fig. 2 (headrest spectra, not headphones); Brammer Fig. 1 (difference curves, hard to read).
