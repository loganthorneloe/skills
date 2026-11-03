# Source audit records

Claims
- C1: Each GPS satellite broadcasts timing signals together with messages giving its transmission time and orbit (ephemeris), kept current by a ground control segment.
- C2: Range is the speed of light times signal travel time, so a 1 ns timing error is about 30 cm of range error.
- C3: The receiver treats its own clock offset as a fourth unknown alongside x, y, z, so it needs four satellites and can use a cheap quartz clock.
- C4: Satellite clocks are atomic (cesium/rubidium) because they must stay stable over hours to days; quartz drifts far more over those times.
- C5: Relativity makes orbiting clocks run fast by about 4.4647e-10 (about 38.6 microseconds per day); GPS offsets the clock frequency before launch to 10.22999999543 MHz and the receiver applies a small eccentricity correction.
- C6: The current constellation: about 31 operational satellites, ~20,200 km altitude, six planes, at least four visible almost anywhere.
- C7: Real-world accuracy: smartphones ~4.9 m under open sky; high-quality receivers ~1.82 m (95%); accuracy degrades with blockage and reflected signals; ranging error (URE) differs from position accuracy.

### Relativity in the Global Positioning System
- url: https://doi.org/10.12942/lrr-2003-1; text read from: EMIS mirror HTML archive https://www.maths.tcd.ie/EMIS/journals/LRG/Articles/lrr-2003-1/download/lrr-2003-1Html.tar.gz (Springer and PMC copies blocked by login redirect / reCAPTCHA)
- byline: Neil Ashby · invited review article · Living Reviews in Relativity 6:1, Max-Planck-Gesellschaft (now Springer) · January 2003
- verdicts: C1 pass; C2 pass; C3 pass; C4 pass; C5 pass; C6 conditional (2003 description of 24-satellite design; use gps.gov for current count); C7 fail (not about current user accuracy)
- use: §1 Introduction (segments, Eq. 1 four equations, "Timing errors of one ns will lead to positioning errors of the order of 30 cm", Fig. 1 Allan deviation of cesium vs quartz, ~4 ns per day for cesium); §5 Relativistic Effects on Satellite Clocks (Eq. 35 = -4.4647e-10, Eq. 36 = 10.22999999543 MHz, Fig. 2 net fractional frequency shift vs orbit radius, eccentricity correction made by receiver)
- credibility: Ashby is a University of Colorado physicist who worked on GPS relativity issues for the system's operators; the article is a peer-reviewed review in the field's main review journal and derives every number shown.
- contribution: derives the positioning equations from the constancy of light speed and computes each relativistic clock effect for GPS orbits.
- limits: 2003 text (archive dated 2005), not the 2007 revision; constellation description is historical. Equations are images in the HTML; values read from the rendered equation images. 38.6 µs/day is my arithmetic from Eq. 35 × 86,400 s, not a number quoted on the pages read. One targeted search found no erratum.
- read: partial (§1, §2 opening, §5 fully; §§3-4, 6-11 skimmed or not read) · version 2003 (lrr-2003-1, HTML archive 2005) · via EMIS mirror

### GPS Accuracy (GPS.gov)
- url: https://www.gps.gov/systems/gps/performance/accuracy/ (live URL returned 404 on fetch); text read from: https://archive.gps.gov/systems/gps/performance/accuracy/
- byline: National Coordination Office for Space-Based Positioning, Navigation, and Timing · U.S. government information page · GPS.gov · last modified March 3, 2022 (site notes no updates since February 2025)
- verdicts: C7 pass; C1 conditional (only implicitly, via the URE figure)
- use: definitions of URE and user accuracy; smartphone 4.9 m open-sky statement (cites ION.org); FAA histogram (1 Oct-31 Dec 2020, 95% horizontal error 1.82 m); list of degrading factors; URE-vs-user-accuracy and urban-canyon graphics
- credibility: official U.S. government site for the system's operators; the histogram comes from FAA monitoring of high-quality receivers.
- contribution: separates signal-in-space ranging error from what a user experiences and reports typical figures.
- limits: smartphone 4.9 m is a typical value attributed to ION.org, not a measured spec; FAA receivers are better than phones; page from 2022.
- read: full · via archive mirror

### GPS Space Segment (GPS.gov)
- url: https://www.gps.gov/systems/gps/space/; text read from: https://archive.gps.gov/systems/gps/space/
- byline: National Coordination Office for Space-Based Positioning, Navigation, and Timing · U.S. government information page · GPS.gov · last modified June 28, 2022 (count dated July 3, 2023)
- verdicts: C6 pass
- use: 31 operational satellites (as of July 3, 2023), ~20,200 km MEO, twice a day, six planes, "at least four satellites from virtually any point"
- credibility: official operator information.
- contribution: current constellation description.
- limits: count dated 2023; may differ today.
- read: full · via archive mirror

## Gaps
- C3: no source read states in words that phones use quartz; Ashby Fig. 1 caption says the quartz curve is "typically found in a GPS receiver" — used as is.
- Assisted GPS and multi-constellation use in phones: not researched; left out of the report rather than stated unsourced.
- Smartphone range-error study (PMC9921678) inaccessible (reCAPTCHA); not used.
