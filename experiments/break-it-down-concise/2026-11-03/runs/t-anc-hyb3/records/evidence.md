# Evidence records

### E1: Lueg's 1936 patent drawing of noise and anti-noise
- claim: C1 (support), C2 (context)
- type: figure
- source: Shi et al., Active Noise Control in The New Century — https://arxiv.org/abs/2306.01425v2 (v2)
- locator: Figure 1, p. 2
- asset: assets/shi2023-fig1.jpg (1600 px, resized from embedded 4531×2244 original); full: assets/shi2023-fig1-full.jpg
- inspected: opened resized image; all four panels (a)–(d), labels A, M, V, L, S1, S2 legible
- notice: Panel (a): microphone M samples the noise S1 in a duct, circuit V drives loudspeaker L, which emits S2 (dashed), a mirror image of S1; panel (b) shows a waveform and its inversion. The whole idea of ANC in one drawing.
- limits: 1930s duct, not a headphone; drawn waves, not measured.
- rights: CC BY-NC-SA 4.0 (arXiv listing); figure reproduced from Lueg's patent by the authors.

### E2: Feedforward, feedback and hybrid microphone placement
- claim: C2 (support)
- type: figure
- source: RTINGS, ANC Headphones vs Earmuffs — https://www.rtings.com/headphones/learn/research/noise-isolation
- locator: "Different Types Of ANC Implementation", hybrid illustration (credited "Source: Creative")
- asset: assets/rtings-hybrid-800.jpg (from 3840 px original assets/rtings-hybrid-illustration-large.jpg)
- inspected: opened; ear cup, feedback mic, speaker, feedforward mic, ANC circuit, music input labels all visible
- notice: One speaker plays both music and anti-noise; the feedforward mic hears noise before it enters the cup, the feedback mic hears what is left near the ear.
- limits: Schematic; earbuds place the mics differently.
- rights: rights unstated (RTINGS page; drawing credited to Creative)

### E3: Cancellation versus magnitude and phase mismatch
- claim: C3 (support)
- type: figure+quote
- source: Skovorodnikov, audioXpress — URL above
- locator: Figure 3 and the paragraph after it
- asset: assets/ax-20231225085347_Figure3.jpg (1200×983, original upload); quote: "a -10dB or better noise reduction target is achieved with a magnitude mismatch of up to 2dB and phase deviation from the ideal of 180° up to 20°"
- inspected: opened full size; axes (phase difference 135–180°, magnitude difference 0–10 dB), colour bar −30 to +5 dB legible
- notice: Only the small black corner (within a few degrees and a fraction of a dB) gives 25–30 dB; by ~45° off or ~6 dB off there is no cancellation, and further out the sum gets louder.
- limits: Computed for a pure sine, not measured. "Up to 2 dB and 20°" is approximate (spot-check in audit).
- rights: rights unstated

### E4: Tuned feedback ANC curve with waterbed
- claim: C5 (support)
- type: figure+metric
- source: Skovorodnikov, audioXpress
- locator: Figure 8 and preceding paragraph
- asset: assets/ax-20231225085613_Figure8.jpg (1200×992); metric: "more than -15dB at around 200Hz"; amplification 1–3 kHz per text (curve is above 0 dB from roughly 600 Hz to 3 kHz, peaks ~+7 dB at ~800 Hz and ~+8 dB near 3 kHz)
- inspected: opened full size; axes and grid legible
- notice: The same controller that removes ~17 dB around 100–200 Hz adds noise above roughly 600 Hz; past 5 kHz it does nothing.
- limits: One design example built from a bandpass 1–425 Hz filter; not a commercial product; also +15 dB peak near 25 Hz from the filter's low-frequency edge.
- rights: rights unstated

### E5: Measured ANC on vs off on three flagship headphones
- claim: C6 (support)
- type: figure
- source: RTINGS, ANC Headphones vs Earmuffs
- locator: "Comparing Performance" graph (Sony WH-1000XM6, Bose QuietComfort Ultra, Apple AirPods Max)
- asset: assets/rtings-anc-on-off-1600.jpg (resized from 3840×2800 original assets/rtings-noise-isolation-anc-on-and-off-2025-large.jpg)
- inspected: opened medium and large; legend, axis 20 Hz–20 kHz, −60 to +10 dB legible
- notice: Light lines (ANC on) sit 20–35 dB below dark lines (ANC off) from ~50 to ~400 Hz; the pairs merge near 1 kHz; above that, all curves sit at −25 to −35 dB from passive isolation alone.
- limits: Three products, one head simulator, pink noise after 5 s priming; y-axis is reduction relative to no headphones, so ANC's own contribution is the gap between the paired curves.
- rights: rights unstated

### E6: Bass / mid / treble averages
- claim: C6 (context)
- type: table
- source: RTINGS, ANC Headphones vs Earmuffs
- locator: range-performance table
- asset: not embedded (image removed from assets); values (overall/bass/mid/treble, dB): 3M Peltor X5A −29.61/−18.79/−37.28/−34.32; Sony WH-1000XM6 −28.40/−20.10/−32.30/−34.19; Sony WH-1000XM4 −27.13/−24.80/−25.37/−31.92; Bose QC Ultra −27.00/−20.79/−29.81/−31.42; Sony WH-1000XM5 −25.81/−17.63/−28.25/−33.04; AirPods Max −26.06/−19.54/−30.62/−28.95; Sonos Ace −26.43/−23.54/−24.82/−31.71
- inspected: opened; all seven rows, five columns visible
- notice: Passive earmuffs beat every headphone in mids, but lose in bass to the best ANC models.
- limits: Band averages blend passive and active effects. Not embedded in final report if redundant with E5 (decided: omitted; E5 shows the same data per frequency).
- rights: rights unstated

### E7: Speech spectrogram
- claim: C8 (support)
- type: figure+metric
- source: Monson et al. 2014, Frontiers in Psychology — https://doi.org/10.3389/fpsyg.2014.00587
- locator: Figure 1; History section
- asset: assets/monson2014-fig1.jpg (767×554, PMC original); metrics: telephone band 300 Hz–3.4 kHz; ~95% articulation accuracy for speech low-pass filtered at 4 kHz
- inspected: opened full size; axes (log frequency ~30 Hz–20 kHz, 0–3 s) and HFE marker legible
- notice: The red bands (harmonics) start near 100 Hz and stack up to ~4 kHz, bend as the pitch moves, and stop and start with each syllable; bursts above 3 kHz are consonants.
- limits: One male talker singing/speaking a phrase; female and child voices sit higher.
- rights: CC BY (© 2014 Monson, Hunter, Lotto and Story)

### E8: Metric — adaptation time
- claim: C9 (support)
- type: metric+quote
- source: RTINGS
- locator: "ANC Response Times"
- asset: "After the introduction of a 1000Hz tone at ~0.5s, the Apple AirPods Max take around three full seconds to reach their maximum attenuation."
- inspected: not applicable
- notice: An adaptive system needs the noise to hold still for seconds; speech changes in tens of milliseconds.
- limits: One product; Sony XM4 settled "relatively quickly".
- rights: quote, fair use

### E9: generated — timing error vs frequency model
- claim: C3, C4 (generated)
- type: generated
- source: derived from superposition: residual power = 1 + a² − 2a·cos(φ), φ = 360°·f·τ
- asset: in-page interactive (canvas + sliders)
- notice: Same delay, different frequency → different cancellation.
- limits: Assumes a pure tone and a pure timing error with perfect amplitude; real systems compensate fixed delays, so τ stands for the uncompensated error.

## Claims lacking evidence / omitted
- C7: no extracted exhibit of an engine-tone spectrum; text relies on Shi et al. statements.
- C10: no exhibit; stated in prose.
- Omitted: audioXpress Fig. 5 (latency comparison) — redundant with E3 + E9 for this reader; Shi Fig. 2 (publication counts) irrelevant.
