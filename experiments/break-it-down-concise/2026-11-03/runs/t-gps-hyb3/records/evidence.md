# Evidence records

### E1: GPS constellation
- claim: C1 (context)
- type: figure
- source: GPS.gov Space Segment — https://archive.gps.gov/systems/gps/space/
- locator: Constellation Arrangement, "Expandable 24-Slot satellite constellation" image
- asset: assets/gps-constellation-large.jpg (1700x1450)
- inspected: opened at full size; all orbits and satellites visible
- notice: Six tilted orbital rings, several satellites per ring; from any spot on Earth several are above the horizon.
- limits: Schematic, not to scale; shows the 24-slot baseline, not the full ~31 operational satellites.
- rights: U.S. government work (public domain), rights not stated on page

### E2: Intersecting spheres
- claim: C3, C4 (support)
- type: figure
- source: GSA White Paper — gnss_raw_measurement_web_0.pdf
- locator: Figure 1, p.7
- asset: assets/gsa-fig1-spheres.png
- inspected: opened; three circles, three ranges and r label, caption visible
- notice: Each range is a circle/sphere around a satellite; the receiver is where they meet.
- limits: Drawn in 2D with perfect ranges; real ranges include clock bias so spheres miss.
- rights: excerpt permitted with source statement "Source: White Paper on using GNSS Raw Measurements on Android devices, copyright © European GNSS Agency, 2017"

### E3: Pseudorange equation and four unknowns
- claim: C3, C4 (support)
- type: quote
- source: GSA White Paper
- locator: §1.6 p.13; §1.2 p.7
- asset: "The pseudorange can be computed as ρ = (tRx − tTx)·c" ; "Due to the impact of the receiver clock, the three spheres do not intersect at a common point."
- inspected: not applicable
- notice: Distance is measured as time; the clock error is why a fourth satellite is required.
- limits: Ignores atmospheric delays as the text states.
- rights: as E2

### E4: 1 ns ≈ 30 cm
- claim: C5 (support)
- type: quote+metric
- source: Ashby 2003 — PMC5253894
- locator: §2 after Eq. (1)
- asset: "Timing errors of one ns will lead to positioning errors of the order of 30 cm."
- notice: Converts timing precision to distance via c.
- limits: Order of magnitude; geometry can amplify it.
- rights: quotation

### E5: Allan deviation, Cesium vs Quartz
- claim: C5 (support)
- type: figure
- source: Ashby 2003 — PMC
- locator: Figure 1
- asset: assets/ashby-fig1-allan.jpg (634x374)
- inspected: opened; axes, both curves and labels visible
- notice: Quartz (in receivers) wanders off quickly beyond ~100 s; cesium stays near 1e-13.5 over a day — about 4 ns/day per Ashby.
- limits: "Typical" curves; log-log axes (averaging time in seconds, log10).
- rights: rights unstated (© The Author(s) 2003)

### E6: Relativistic frequency shift vs orbit radius
- claim: C6 (support)
- type: figure
- source: Ashby 2003 — PMC
- locator: Figure 2
- asset: assets/ashby-fig2-offset.jpg (684x421)
- inspected: opened; axes, GPS/GLONASS/Shuttle/Geostationary points visible
- notice: GPS sits around +446 parts in 10^12: gravity speeding the clock outweighs motion slowing it; low orbits (Shuttle) go negative.
- limits: Circular-orbit model; y-axis is fractional frequency ×10^12.
- rights: rights unstated

### E7: Factory clock offset
- claim: C6 (support)
- type: quote+metric
- source: IS-GPS-200N — §3.3.1.1, p.13–14
- asset: "The clock rates are offset by Δf/f = -4.4647E-10 ... This is equal to 10.2299999954326 MHz." ; derived: 4.4647e-10 × 86,400 s = 38.6 µs/day; × c = 11.6 km/day
- notice: Clock is deliberately set slow before launch so it ticks at 10.23 MHz as seen from the ground.
- limits: Constant part only; eccentricity term corrected in receiver (Ashby).
- rights: Distribution Statement A (public release)

### E8: NTS-2 measurement
- claim: C6 (support)
- type: metric
- source: Ashby 2003
- locator: text after Figure 2
- asset: measured +442.5 vs predicted +446.5 parts in 10^12 (NTS-2, 1977, ~20 days)
- notice: The effect was measured in orbit, not just predicted.
- limits: ~1% agreement.

### E9: Error budget
- claim: C7 (support)
- type: figure
- source: GSA White Paper, Figure 8 p.15
- asset: assets/gsa-fig8-errors.png
- inspected: opened full size; all labels incl. Reception visible
- notice: Receiver clock offset (<300 km) and satellite clock offset (up to hundreds of km) dwarf atmospheric delays (2–30 m) — clocks dominate until solved/corrected.
- limits: Typical ranges before corrections; not a phone measurement.
- rights: as E2

### E10: URE vs user accuracy; urban canyon
- claim: C7 (support)
- type: figure
- source: GPS.gov Accuracy
- asset: assets/gps-URE-vs-user-accuracy.jpg (300x200), assets/gps-urban-canyon.jpg (300x275)
- inspected: opened; legible at natural size only (small)
- notice: Range errors per satellite combine into a position error circle; reflected signals travel longer paths.
- limits: Cartoons; small native size.
- rights: U.S. government work

### E11: Accuracy metrics
- claim: C7
- type: metric
- source: GPS.gov Accuracy
- asset: smartphones "typically accurate to within a 4.9 m (16 ft.) radius under open sky"; URE commitment ≤2.0 m (95%), actual ≤0.643 m on 20 Apr 2021
- limits: open sky; worsens near buildings.

### E12: Navigation message rate
- claim: C2, C8
- type: metric+quote
- source: IS-GPS-200N §3.2.2, §20.3.1–20.3.2
- asset: LNAV "includes SV ephemerides, system time, SV clock behavior data..."; 50 bps; 1500-bit frame of five 300-bit subframes → 30 s per frame (derived)
- limits: legacy LNAV only.

### E13: Assisted GNSS
- claim: C8
- type: figure+quote
- source: GSA White Paper §3.1 p.28, Figure 15
- asset: assets/gsa-fig15-agnss.png; "The main aim of A-GNSS is to reduce TTFF"
- inspected: opened; all labels visible
- notice: Phone fetches ephemeris, clock correction, iono model, approx position and time over the network instead of waiting for the broadcast.
- rights: as E2

## Omitted
- GPS.gov FAA histogram: not needed for the answer.
- Physics Today figures: not retrieved (summary read only).
