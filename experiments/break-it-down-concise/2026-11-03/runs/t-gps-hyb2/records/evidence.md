# Evidence records

### E1: URE vs user accuracy graphic
- claim: C1, C7 (context)
- type: figure
- source: GPS Accuracy — https://archive.gps.gov/systems/gps/performance/accuracy/
- locator: graphic beside "URE is a measure of ranging accuracy"
- asset: assets/gpsgov-URE-vs-user-accuracy.jpg (300×200, original)
- inspected: opened at full size; all four satellites and both labels visible
- notice: several satellite ranges meet at one user; error on each range (URE) becomes a circle of position uncertainty.
- limits: schematic, not to scale
- rights: U.S. government graphic; page states no terms; GPS.gov image library is released to the public domain

### E2: Equation 1 and 1 ns = 30 cm
- claim: C2, C3 (support)
- type: quote+generated (equation transcribed)
- source: Ashby 2003 — https://doi.org/10.12942/lrr-2003-1
- locator: §1, Eq. (1)
- asset: c²(t − t_j)² = |r − r_j|², j = 1,2,3,4; "These four equations can be solved for the unknown space-time coordinates"; "Timing errors of one ns will lead to positioning errors of the order of 30 cm."
- inspected: equation image scratch/img11.png opened
- notice: the unknown reception time t sits inside every equation, which is why four are needed.
- limits: assumes inertial frame; ignores atmosphere
- rights: rights unstated (© Max-Planck-Gesellschaft)

### E3: Allan deviation, cesium vs quartz (Fig. 1)
- claim: C3, C4 (support)
- type: figure
- source: Ashby 2003, §1 Fig. 1
- asset: assets/ashby-fig1-allan-deviation.gif (818×483, original)
- inspected: opened at full size; axes, both curves, labels visible
- notice: quartz is better below ~1 s but rises steeply; cesium stays near 1e-13.5 out to ~1e6 s. A day ≈ 1e4.9 s.
- limits: nominal curves; "wide range of variation"; log axes
- rights: rights unstated

### E4: Net fractional frequency shift vs orbit radius (Fig. 2)
- claim: C5 (support)
- type: figure
- source: Ashby 2003, §5 Fig. 2
- asset: assets/ashby-fig2-frequency-shift.gif (848×532, original)
- inspected: opened at full size; GPS point ~ +446e-12; Shuttle negative; axis label "100000" clipped at right edge in the source itself
- notice: low orbits run slow (speed dominates), GPS orbits run fast (weaker gravity dominates).
- limits: circular orbits; sign flipped relative to Eq. 35
- rights: rights unstated

### E5: Eq. 35/36 values
- claim: C5
- type: metric
- source: Ashby 2003 §5
- asset: net fractional rate −4.4647×10⁻¹⁰ (Eq. 35: +2.5046e-10 − 6.9693e-10); proper frequency 10.22999999543 MHz (Eq. 36), adjusted "on the ground before the clock is placed in orbit"
- inspected: equation images img90/img91 opened
- notice: ×86,400 s = 38.6 µs/day (generated arithmetic) ≈ 11.6 km of light travel
- limits: excludes eccentricity term and quadrupole (~1e-14 effect)
- rights: rights unstated

### E6: FAA horizontal error histogram
- claim: C7
- type: figure+metric
- source: GPS Accuracy (archive)
- asset: assets/gpsgov-histogram.jpg (600×493); 95% horizontal error 1.82 m, Oct 1–Dec 31 2020, FAA high-quality single-frequency receivers
- inspected: opened at full size; title truncated "20" in the source itself, axes legible
- notice: peak under 1 m; long thin tail
- limits: high-quality receivers in good conditions, not phones
- rights: U.S. government graphic; terms not stated on the page

### E7: Smartphone 4.9 m and degrading factors
- claim: C7
- type: quote
- asset: "GPS-enabled smartphones are typically accurate to within a 4.9 m (16 ft.) radius under open sky"; blockage by buildings, bridges, trees; multipath
- limits: typical value attributed to ION.org

### E8: Urban canyon cartoon
- claim: C7 (support)
- type: figure
- asset: assets/gpsgov-urban-canyon.jpg (300×275)
- inspected: opened; schematic
- notice: blocked and reflected paths add range error
- rights: U.S. government graphic; terms not stated on the page

### E9: Constellation
- claim: C6 — metric: 31 operational satellites as of July 3, 2023; ~20,200 km; six planes; ≥4 visible

### E10: Clock-bias interactive (generated)
- claim: C3 — type: generated. 2D toy model, three satellites ~22,000 km away, true receiver at origin; pseudoranges = true range + c·b. Least squares with and without bias unknown.

## Claims still lacking evidence / omitted
- Assisted GPS, multi-GNSS: not covered.
- Constellation graphic from GPS.gov image library not extracted; constellation stated in text.
