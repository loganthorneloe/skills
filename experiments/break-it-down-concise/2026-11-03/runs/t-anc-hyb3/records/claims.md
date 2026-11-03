# Claims

- C1: Sound is a travelling pressure wave; two sounds at one point add (superposition), so an equal and opposite (180° out of phase) wave cancels the first. Settled background; Shi et al. corroborate.
- C2: ANC headphones sense noise with microphones (outside the cup = feedforward, inside = feedback, both = hybrid), compute an inverted signal, and play it through the same speaker as the music.
- C3: Cancellation is very sensitive to mismatch: about 10 dB of reduction already requires amplitude within about 2 dB and phase within about 20° of exact opposition.
- C4: A fixed timing error becomes a phase error that grows in proportion to frequency, so the delay budget that is harmless for a 100 Hz hum ruins cancellation in the kHz range; headphones are small, so the acoustic head start is short (causality constraint). Lower latency raises the upper frequency limit.
- C5: Feedback ANC must roll off its gain at high frequencies to stay stable, and tuning for deep low-frequency cancellation amplifies noise in a band around 1–3 kHz (waterbed effect).
- C6: Measured on current headphones, ANC adds roughly 20–30 dB of reduction in the bass and its benefit disappears around 1 kHz, above which passive isolation (ear cups and pads) does the work.
- C7: Engine and propeller hum is concentrated at low frequencies and is tonal: steady tones at a rotation rate and its harmonics, which repeat predictably; ANC reaches large reductions on such tonal noise.
- C8: Speech spreads energy from about 100 Hz to several kHz, with the cues that make it intelligible (consonants) mostly between about 1 and 4 kHz, and its pitch and harmonics shift from moment to moment.
- C9: Noise that changes quickly defeats adaptation: adaptive ANC can take seconds to settle; most commercial headphones use fixed filters because of compute/latency limits.
- C10: The zone where cancellation holds shrinks as frequency rises, and the ear's own resonance (2–3 kHz) makes the sound at the microphone differ from the sound at the eardrum.
