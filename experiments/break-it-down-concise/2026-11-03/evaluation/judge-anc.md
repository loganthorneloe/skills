# Blind judge — active noise cancellation (A vs B)

Rendered both at 1280px and 390px with Playwright (screenshots and scripts in `evaluation/scratch-judge-anc/`). No console errors and no horizontal page scroll in either. I operated every control: A's two sliders, three presets, Reset and keyboard arrows; B's three sliders and Reset. I checked both models' readouts by hand and they are correct (A at 8 kHz/100 µs reads "1 dB louder", B at 4 kHz/50 µs reads "1.4 dB louder"). Word counts are visible text, including source cards, captions and widget labels.

## Scores

Dimensions 1–9 come from the rubric. 10 is signal density, 11 time to answer, 12 research quality, and 13 visual explanation.

| Report | 1 Prereq | 2 Order | 3 Mech | 4 Evid | 5 Acc | 6 Transfer | 7 Exhibits | 8 Read | 9 Present | 10 Density | 11 Time | 12 Research | 13 Visual | Total /65 | Probes /16 | Words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | **56** | **14** | 1,717 |
| B | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 3 | 3 | 4 | 4 | **54** | **15** | 2,891 |

### Score notes

- A is compact and teaches each prerequisite in a sentence or two: frequency, wavelength, phase, superposition and dB. Some passages are dense, such as the Fig. 6 caption, which packs in five numbers. The source list comes before the short answer, so about 350 words come first.
- A has the strongest exhibits. Five original figures each have provenance, rights and a stated limit, and the captions say what to notice. Its records hold 8 sources with per-claim verdicts and qualifiers, such as the 7.5 kHz prototype figure, and the report numbers match the records (Fig. 6 values are 870 Hz, 2.6 kHz, and 40/21/22 dB).
- B builds the prerequisites more patiently: pressure, the eardrum, the "half a cycle" equivalence, and the 20 dB = 10× pressure rule. Its mechanism is fuller. It covers loudness mismatch as a separate, pitch-independent limit, a computed timing table, the causality head start, and predictability with a model figure. Its transfer is the best, because the "one sixth of a cycle" threshold plus the intelligibility chart let a reader work through a new case.
- B costs more reading time, about 70% more words for a modest gain. It also puts the source list first. Its timing table is cramped at 390px.
- B's research is solid with 4 sources and audited verdicts. Its speech-spectrum chart comes from a manufacturer page with unstated method, which B flags. It has fewer primary measurements of a real headphone's behaviour.

## Visuals

### A
1. Lueg 1936 patent Fig. 1 shows the inverted wave added in a duct, the core idea in its simplest form.
2. Rivera Benois 2018 Fig. 1 is an ear-cup cutaway with the outer and inner microphones, the speaker, and the P(z)/S(z) paths. It teaches the hardware and the feedforward/feedback signals.
3. An interactive (frequency and delay, with presets) shows the noise, the late anti-noise and the residual wave. It reads out cycle length, error %, dB, and the λ/10 quiet zone, which teaches delay as a fraction of a cycle and shows that cancellation can flip to "louder".
4. Rivera Benois 2017 Fig. 6 shows measured spectra at the ear for feedback, tone-learning, and hybrid control. It shows broadband reduction stopping near 870 Hz, amplification near 2.6 kHz, and steady tones cancelled even at 2 kHz, so predictability matters as well as pitch.
5. A Monson 2014 spectrogram shows that a voice spreads into the kHz range and changes every syllable.
6. Gallagher & Murphy 2017 Fig. 1 (Bose A20) compares protection with ANC off and on against how bass-heavy the noise is. It shows ANC filling the low-frequency gap that passive blocking leaves.

A should have had B's measured active-reduction-versus-frequency chart (Streeter), which shows the answer's shape most directly. B's speech intelligibility-by-band chart and its timing table would also help.

### B
1. An interactive (pitch, lateness, loudness match) shows the noise, the anti-noise and the residual. It reads out phase in degrees, leftover %, dB and wavelength, which teaches both timing and amplitude error.
2. A computed table of 50 µs lateness at 100, 300, 1,000 and 3,000 Hz shows the frequency scaling in one glance.
3. Zhang & Qiu 2014 Fig. 2 plots noise reduction against non-causal delay for four noise bandwidths. It shows that narrow, low-frequency noise survives lateness and broadband noise does not.
4. Streeter 2004 Fig. 1 plots measured active reduction against frequency for several headsets. Reduction peaks at 50–400 Hz and is gone by about 1 kHz, and feedback goes negative in the 1–3 kHz band.
5. A DPA voice-spectra chart shows voice energy by band and vocal effort.
6. A French & Steinberg intelligibility-by-band chart shows that 1–4 kHz carries about 3/4 of intelligibility. This links "voices" to the frequencies where ANC fails.

B should have had a hardware diagram (A's ear-cup cutaway), because feedforward and feedback are explained only in prose. A speech spectrogram showing that speech changes over time would also help (B only states it).

## Probes (0/1/2)

| Probe | A | B | Notes |
|---|---|---|---|
| Q1 superposition / inversion | 2 | 2 | |
| Q2 hardware | 2 | 2 | A also has a diagram. |
| Q3 feedforward vs feedback vs hybrid | 2 | 2 | |
| Q4 why filtered/adaptive, not simple inversion | 1 | 1 | Neither explains that the acoustic path changes amplitude and phase with frequency. A shows P(z)/S(z) and "learning vs fixed filters". B mentions the cup that "muffles and colours" the sound and a filter that keeps adjusting. Neither names LMS. |
| Q5 latency as a fraction of the period | 2 | 2 | Both give worked numbers. |
| Q6 hum vs voice | 2 | 2 | Both cover frequency and predictability. |
| Q7 passive isolation for high frequencies | 2 | 2 | |
| Q8 3 kHz made louder, and how designers avoid it | 1 | 2 | A shows that half a cycle doubles the noise and that feedback amplifies near 2.6 kHz, but gives no threshold and leaves the design limit implicit. B says "past one sixth of a cycle late … adds" and "every design concentrates its effort below about 1 kHz" plus passive blocking. |
| **Total** | **14** | **15** | |

## Factual errors and overclaims

No hard errors in either report. Both models' formulas and worked numbers check out: A gives 38 dB and 6 dB, and 5% and 1.6% of a cycle for 10 and 20 dB. B gives 30, 21, 10 and <1 dB, the 60° threshold, and 20 dB for a 10% mismatch.

A:
- "A tone repeats every cycle, so a controller can produce anti-noise for a cycle it has not heard yet, and its delay stops mattering." This overstates the case. Delay matters less, but adaptation, drift and amplitude error remain, and A's own caption notes the tones "took 15 minutes to learn".
- "Only frequency times delay matters" is true only inside the pure-tone model. A does caveat that amplitude and fit errors also matter.
- "Above about 1 kHz (1,000 Hz), headphones rely on the ear cup" is a reasonable rule of thumb, and A later qualifies it with the 7.5 kHz fixed-source prototype.

B:
- "Measurements show exactly that." and "By about 1 kHz, every curve has fallen to about zero." The feedforward triangles in Streeter Fig. 1 still show roughly 8–12 dB near 1 kHz and about 5 dB at 1.6 kHz.
- It attributes feedback amplification in the 1–3 kHz band to "the timing problem in the model". That is plausible but simplified: feedback amplification also comes from the loop's stability trade-off (the "waterbed" effect), which B doesn't explain.
- "Those two facts are why every design concentrates its effort below about 1 kHz." This is a mild generalisation from 2004 hardware and one review sentence.

## Verdict

A gives a reader real understanding faster. It answers both questions in about 60% of B's words, with a better visual set (a hardware diagram plus measured spectra that separate predictability from pitch). B is the more complete teacher. The shorter report, A, lost a few things that matter: the explicit "one sixth of a cycle → amplification" threshold, which is the Q8 transfer point; loudness mismatch as a separate limit; the at-a-glance timing table; the measured reduction-versus-frequency chart; and the intelligibility chart that links "voices" to 1–4 kHz. None of these breaks A's core explanation. They mainly weaken transfer.
