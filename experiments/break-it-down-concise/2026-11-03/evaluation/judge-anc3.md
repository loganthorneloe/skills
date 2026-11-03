# Judge anc3: active noise cancellation, A vs B

I rendered both reports at 1280px and 390px with Playwright, using scripts and screenshots in `evaluation/scratch-judge-anc3/`. Neither page scrolls horizontally, every image loads, and the console shows no errors. I operated every control. A's presets, both sliders, and Reset work: 2 kHz at 50 µs reads 36° and −4.2 dB, and 100 µs at 2 kHz reads +1.4 dB (louder). B's three sliders and Reset work: 4 kHz at 50 µs reads 72° and 1.4 dB louder, 0 µs at a 90% match reads 20 dB, and Reset returns 30 dB. I also checked both reports' arithmetic by hand, including the 2−2cos φ values and B's table, and it is correct.

## Scores

| | 1 Prereq | 2 Order | 3 Mech | 4 Evid | 5 Acc | 6 Transfer | 7 Exhibits | 8 Read | 9 Present | 10 Density | 11 Time | 12 Research | 13 Visual | Total /65 | Probes /16 | Words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | **61** | 15 | 1,862 |
| B | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | **58** | 15 | 2,891 |

The word counts are visible text, including the interactive's labels.

## Probes (0/1/2)

| | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 |
|---|---|---|---|---|---|---|---|---|
| A | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 |
| B | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 |

On Q4, neither report explains that the speaker-to-ear path changes amplitude and phase differently at each frequency, which is why a filter has to model it. A mentions fixed versus adaptive filters and the pinna resonance that limits filter fit. B says the chip adjusts for how the cup "muffles and colours" sound and keeps adapting.

On Q8, A gives 60° at 3.3 kHz, after which the sum grows louder. It also explains the feedback waterbed, the cut in controller strength at high frequencies, and passive isolation hiding the waterbed. B states the one-sixth-cycle rule, shows 4 kHz coming out louder in its model, and says designs concentrate below 1 kHz with padding handling the rest.

## Visuals

**A**
- Lueg 1936 patent drawing (Shi 2023 Fig. 1) shows the whole idea: microphone, inverter, speaker, and mirror wave.
- Hybrid ear-cup diagram (RTINGS/Creative) shows where the feedforward and feedback mics, the speaker, and the ANC circuit sit.
- Magnitude/phase cancellation heat map (Skovorodnikov Fig. 3) shows how small the window for good cancellation is.
- Interactive with presets, frequency, and timing error. The waveform plot shows the residual, and the cancellation-versus-frequency curve shows one delay ruining high frequencies, with a + region where the sum gets louder.
- Feedback ANC curve (Skovorodnikov Fig. 8) shows the waterbed amplification between about 600 Hz and 3 kHz.
- RTINGS ANC on/off curves for three 2025 flagship headphones show measured on-off gaps of roughly 15–35 dB in the bass, with the curves merging near 1 kHz.
- Monson spectrogram of a male voice shows harmonics up to about 4 kHz, changing with every syllable.
- A should have had B's French & Steinberg intelligibility-by-band chart. A covers the same point in text through the telephone-band fact, so the gap is small. B's worked table is also cleaner than A's prose numbers.

**B**
- Interactive with pitch, lateness, and loudness match. It shows the waveform residual and reads out phase, leftover, dB, and wavelength. Its loudness slider teaches the amplitude limit, which A covers with its heat map.
- Worked table of 50 µs at 100 Hz, 300 Hz, 1 kHz, and 3 kHz shows the delay arithmetic at a glance.
- Zhang & Qiu Fig. 2 shows reduction against non-causal delay by bandwidth. It is the only exhibit in either report that addresses predictability directly.
- Streeter 2004 Fig. 1 shows measured ANR against frequency for older headsets, with the peak at 50–400 Hz, a fall to about 0 by 1 kHz, and negative feedback values.
- DPA voice spectra by effort show where speech energy sits.
- French & Steinberg intelligibility by octave shows the 1–4 kHz bands carrying about three quarters of intelligibility.
- B should have had A's hardware diagram, which is the main gap for Q2/Q3 and leaves feedforward/feedback text-only. It should also have had a modern ANC on/off measurement, since its only measured headsets are from 2004, and the waterbed figure. A static superposition figure (A's Lueg drawing) would also help.

## Errors and overclaims

**A**
- "The mirror image must land within a few degrees of the right point in the wave's cycle." This overstates. The report's own source gives 20° for an audible 10 dB, and "a few degrees" is only true for 25–30 dB.
- "Below about 200 Hz the cups alone do almost nothing" is a fair reading of RTINGS. I found no other errors. The Skovorodnikov "2 dB and 20°" quote is approximate, and A's records flag this.

**B**
- "Measurements show exactly that" is a little strong for a 2004 compilation.
- "This fits the timing problem in the model, since at those pitches the loop's correction arrives late enough that it adds to the noise" puts feedback amplification down to plain lateness. It is really a loop-stability (waterbed) trade-off, so this is a simplification.
- "When the anti-noise cannot be on time, the chip has to guess what the noise will do next" is a loose description of how fixed or causal filters behave, though acceptable for a novice.
- B qualifies its evidence honestly. It says the 2004 hardware may underperform today's products, the DPA spectra have unstated conditions, and the Elliott paper was a partial read.

## Research quality (records)

A read four sources in full. Its records include per-claim verdicts and a spot-check of Skovorodnikov's numbers against the interference formula, which found the source's figure approximate. They also disclose a conflict of interest (Knowles) and affiliate revenue (RTINGS). The sources are current and on target, including a 2025 measurement of real products.

B's records are solid and carry claim-level verdicts. However, one key source, Elliott 2018, was a partial read through a fetch summary. The voice-spectrum chart is uncredited, French & Steinberg was not read at first hand, and the headphone measurements are 20 years old. Zhang & Qiu is a strong, well-chosen peer-reviewed source.

## Verdict

A gets a reader to real understanding faster. Its short answer carries the whole argument in four sentences. Its interactive goes further than B's by plotting cancellation across every frequency for one delay. Its exhibits cover hardware, precision, waterbed, modern measured headphones, and the voice, in about 1,860 words.

As the shorter report, A did not lose anything important. B's real extras are a gentler start on pressure and wavelength, the loudness slider, the Zhang & Qiu predictability chart, and the intelligibility bar chart. A covers the first two in its heat map and prose. Of the rest, only the predictability exhibit is a real gap in A, and A partly makes up for it with the RTINGS three-second adaptation finding.

B is the more patient read for a total novice. But it is about 55% longer, has no hardware diagram, and relies on 2004 measurements, so it scores slightly lower on visuals, research currency, and density.
