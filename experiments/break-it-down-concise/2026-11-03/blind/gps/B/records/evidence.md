# Evidence records

### E1: GPS constellation diagram
- claim: C1 (context)
- type: figure
- source: Space Segment, GPS.gov — https://archive.gps.gov/systems/gps/space/ (image library full-size https://archive.gps.gov/multimedia/images/constellation.jpg)
- locator: "Constellation Arrangement" image, Expandable 24-slot configuration
- asset: assets/gps-constellation.jpg (1700 × 1450, original file)
- inspected: opened at full size; orbits, satellites, Earth all visible; no labels to clip
- notice: Six tilted orbital rings spread so that several satellites are above any horizon at once; that overlap is what makes four simultaneous ranges possible.
- limits: Schematic, not to scale; shows the 24-slot baseline, not all 31 satellites.
- rights: public domain (U.S. Government)

### E2: Navigation equation figure
- claim: C2, C3 (support)
- type: figure+quote
- source: Relativistic Effects in the Global Positioning System — https://www.aapt.org/doorway/tgru/articles/ashbyarticle.pdf (dated July 18, 2006)
- locator: Fig. 1, page 3; Sec. III.A
- asset: assets/ashby-2006-fig1-navigation.png (rendered at 220 dpi from page 3, cropped to the embedded image bounds plus margin); quote "An error of 3 nanoseconds (ns) in time would correspond to a position error of about 1 meter."
- inspected: opened at full size; equation, four satellites, and "distance = c times Δt" label all inside the crop
- notice: Each line from receiver to satellite is one equation, distance = speed of light × travel time; four lines for four unknowns.
- limits: Satellite artwork not to scale; equation written for synchronized clocks (receiver bias handled separately).
- rights: rights unstated (embedded with attribution)

### E3: Clock stability, cesium vs quartz
- claim: C4 (support)
- type: figure+metric
- source: Relativity in the Global Positioning System — https://pmc.ncbi.nlm.nih.gov/articles/PMC5253894/
- locator: Figure 1 and following paragraph
- asset: assets/ashby-fig1-allan-deviation.jpg (634 × 374, PMC original); metric: cesium about 5 parts in 10^14 after one day, about 4 ns
- inspected: opened at full size; both axes, both curves, labels legible
- notice: Lower is steadier. Quartz (receiver-type) is fine for a second or two but its curve climbs steeply; cesium stays near 10^-13.5 out to a day. So a phone can trust its clock over the instant of a fix but not over time.
- limits: "Typical" curves; real clocks vary around them; GPS also flies rubidium clocks.
- rights: Creative Commons per journal policy, specific license not confirmed; attributed.

### E4: Net relativistic frequency shift vs orbit radius
- claim: C5 (support)
- type: figure+metric
- source: Relativity in the Global Positioning System — https://pmc.ncbi.nlm.nih.gov/articles/PMC5253894/; companion numbers from Ashby 2006 Eqs. 23 and 30
- locator: Figure 2; NTS-2 paragraph; Ashby 2006 Eq. 23, Eq. 30
- asset: assets/ashby-fig2-orbit-frequency-shift.jpg (684 × 421); metrics: gravitational +5.288 × 10^-10 (≈13.7 km/day if uncorrected), time dilation −8.228 × 10^-11 (≈2.13 km/day), net ≈ +4.465 × 10^-10 (derived: ×86,400 s ≈ 38.6 µs/day; × c ≈ 11.6 km/day); NTS-2 measured +442.5 vs predicted +446.5 parts in 10^12
- inspected: opened at full size; axes, GPS/GLONASS/Geostationary/Shuttle labels legible
- notice: At GPS radius (~26,600 km from Earth's centre) the curve sits near +440 parts in 10^12: the clock gains. Low orbit (Shuttle) loses, because speed dominates there.
- limits: Circular orbits; eccentricity adds a periodic term up to ~23 ns that receivers correct.
- rights: as E3.

### E5: Signal versus device accuracy
- claim: C6 (support)
- type: metric+quote
- source: GPS Accuracy, GPS.gov — https://archive.gps.gov/systems/gps/performance/accuracy/
- locator: "What is the government's commitment", "How accurate is GPS?"
- asset: URE ≤ 2.0 m (95%, daily global average, healthy satellites); measured ≤ 0.643 m (95%) on April 20, 2021; phones typically within 4.9 m radius under open sky; quote "To be clear, URE is not user accuracy."
- inspected: not applicable
- notice: The satellites' ranging error is well under the phone's position error; geometry and local effects make up the difference.
- limits: 4.9 m comes from the 2014 crowdsourced ION lab (conditional).
- rights: U.S. government work

### E6: Geometry multiplies error (DOP)
- claim: C7 (support)
- type: quote
- source: Positioning Error, Navipedia — https://gssc.esa.int/navipedia/index.php/Positioning_Error
- locator: "Predicted Accuracy: Dilution of Precision"
- asset: "DOP represents an approximate ratio factor between the precision in the measurements ... and in positioning."
- inspected: not applicable
- notice: Same ranging error, different satellite spread, different position error.
- limits: Equal-error model.
- rights: quote only

### E7 (generated): clock-offset demonstration
- claim: C3, C4 (context)
- type: generated
- source: constructed 2D toy, three transmitters, exaggerated scale
- asset: interactive SVG in report.html
- notice: Only one assumed clock offset makes all range circles meet; that is how the receiver solves its clock.
- limits: Flat 2D analog (2 position unknowns + clock = 3 transmitters); toy units, not real distances.

## Omitted / not extracted
- Ashby 2003 Eqs. 35–36 (image-rendered equations): used text values from Ashby 2006 instead.
- ION 2015 full paper (paywalled): only the abstract's 4.9 m figure used.
- Navipedia equations: described in prose rather than reproduced.
