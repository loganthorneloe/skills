# Source audit records

Claims
- C1: GPS satellites carry atomic clocks and broadcast timing signals plus messages giving each transmission's time and the satellite's position; the constellation keeps at least four satellites in view almost everywhere.
- C2: A receiver converts signal travel time into distance by multiplying by the speed of light; 1 ns of timing error is about 30 cm of range error.
- C3: The receiver's own clock offset is a fourth unknown alongside x, y, z, so at least four satellites are needed; the nonlinear equations are solved by linearizing around a guess and iterating, using least squares when more than four satellites are seen.
- C4: Satellite cesium clocks hold time to a few ns per day; a receiver's quartz oscillator drifts far more over long intervals, which is why the receiver's offset is solved rather than trusted; ground control broadcasts clock corrections.
- C5: Relativity makes orbiting GPS clocks run fast relative to ground clocks (gravitational blueshift larger than time-dilation slowing); net about 4.465 parts in 10^10, corrected by lowering the clock frequency before launch; NTS-2 confirmed the effect to about 1%.
- C6: Delivered accuracy: signal-in-space URE commitment and measured value; smartphones typically about 4.9 m under open sky, worse near buildings and trees; error sources include blockage, multipath, atmosphere; dual-frequency removes atmospheric distortion.
- C7: Satellite geometry scales measurement error into position error (dilution of precision).

### Relativity in the Global Positioning System
- url: https://doi.org/10.12942/lrr-2003-1; text read from: PubMed Central copy https://pmc.ncbi.nlm.nih.gov/articles/PMC5253894/
- byline: Neil Ashby · invited review article · Living Reviews in Relativity 6:1 · January 2003 (fast-track revision June 2007)
- verdicts: C1 pass; C2 pass; C3 pass; C4 pass; C5 pass; C6 fail (not about consumer accuracy); C7 fail (not covered)
- use: Introduction (24 satellites, four in view, Eq. 1 and "one ns ... 30 cm"), Figure 1 (Allan deviation cesium vs quartz, ~4 ns/day), discussion of Eqs. 35–36 (clock beats too fast, adjusted lower in frequency before launch), Figure 2 (net fractional frequency shift vs orbit radius), NTS-2 story (+442.5 measured vs +446.5 predicted parts in 10^12), TOPEX section (pseudorange, receiver clock bias is why four satellites are needed), clock correction polynomial in the navigation message.
- credibility: Ashby is a University of Colorado physicist who worked on relativistic corrections for GPS and NIST; Living Reviews articles are invited, refereed reviews. The article reports firsthand data (TOPEX receiver analysis) and the NTS-2 measurement.
- contribution: Derives each relativistic clock effect for GPS from first principles and states their sizes; explains the navigation equations and the role of the receiver clock bias.
- limits: Numeric values in Eqs. 35–36 are rendered as images in the PMC copy; I took the net offset from the text-searchable companion paper (Ashby 2006) and the NTS-2 values in text. Constellation description (24 satellites) reflects 2003; current counts come from gps.gov. Searched for errata or retraction: none found; only blog-level disputes from non-mainstream authors.
- read: partial (introduction, clocks, reference frames, Eqs. 28–40 narrative, NTS-2, TOPEX pseudorange section, figure captions; skipped detailed TOPEX results and later applications) · 2003 article as hosted on PMC · via PMC
- rights: journal states its articles are distributed under a Creative Commons license stated in each article; the specific license was not visible in the copy read.

### Relativistic Effects in the Global Positioning System
- url: https://www.aapt.org/doorway/tgru/articles/ashbyarticle.pdf; text read from: same
- byline: Neil Ashby · teaching article (dated July 18, 2006) · hosted by the American Association of Physics Teachers, Teaching General Relativity to Undergraduates collection · July 2006
- verdicts: C1 pass; C2 pass; C3 pass; C5 pass; C4 conditional (only "a few parts in 10^14 after a day", corroborated by the 2003 review)
- use: Sec. III.A Navigation equations and Fig. 1 (|r − rj| = c(t − tj), at least four satellites, linearize and iterate, 3 ns ≈ 1 m, ionosphere/troposphere delays); Eq. 23 gravitational shift +5.288 × 10^-10 ≈ 13.7 km/day; Eq. 30 time dilation −8.228 × 10^-11 ≈ 2.13 km/day.
- credibility: Same author as the review, writing for physics instructors; values agree with the refereed review and the NTS-2 measurement.
- contribution: Gives the two main clock effects separately as text-searchable numbers and their navigational consequence per day.
- limits: Teaching paper, not peer-reviewed as far as the copy shows; its figure uses satellite photographs of unstated origin.
- read: full (16 pages, text extracted with PyMuPDF; Fig. 1 page rendered)
- rights: rights unstated.

### Space Segment (GPS.gov)
- url: https://www.gps.gov/systems/gps/space/; text read from: https://archive.gps.gov/systems/gps/space/ (the live URL returned "page not found")
- byline: National Coordination Office for Space-Based PNT · official U.S. government web page · GPS.gov · undated, accessed 2026-11-03 (site notes content not updated since February 2025; satellite count dated July 3, 2023)
- verdicts: C1 pass (constellation shape and coverage; counts current as of the page's date)
- use: "Constellation Arrangement": at least 24 operational satellites 95% of the time, 31 flown, about 20,200 km altitude, twice a day, six planes, at least four in view from virtually any point; constellation image.
- credibility: Official public information office of the agencies that run GPS.
- contribution: Current-ish description of the constellation.
- limits: Archived snapshot; the operational count may have changed since 2023.
- read: full (constellation and generations sections)
- rights: Image library states all images "released into the public domain"; cite "United States Government".

### GPS Accuracy (GPS.gov)
- url: https://www.gps.gov/systems/gps/performance/accuracy/; text read from: https://archive.gps.gov/systems/gps/performance/accuracy/
- byline: National Coordination Office for Space-Based PNT · official U.S. government web page · GPS.gov · undated, accessed 2026-11-03 (content frozen February 2025)
- verdicts: C6 pass
- use: "How accurate is GPS?", "Why does GPS sometimes show me in the wrong place?", "government's commitment" (URE ≤ 2.0 m, 95%; measured ≤ 0.643 m on April 20, 2021), military vs civilian (dual frequency corrects atmospheric distortion).
- credibility: Official statement of the U.S. government's performance commitment; phone figure cited to an ION paper.
- contribution: Separates signal-in-space ranging error from what a device delivers and lists common error causes.
- limits: The 4.9 m phone figure is secondhand from an ION paper (see next entry); the 2021 URE value is one day.
- read: full
- rights: U.S. government work.

### The World's first GPS MOOC and Worldwide Laboratory using Smartphones
- url: https://www.ion.org/publications/abstract.cfm?jp=p&articleID=13079; text read from: abstract page only
- byline: Frank van Diggelen and Per Enge · conference paper · Proceedings of ION GNSS+ 2015, Institute of Navigation · September 2015
- verdicts: C6 conditional (mean open-sky accuracy of 4.9 m from about 1,000 participants' phones in 2014; urban accuracy tracked building height)
- use: abstract
- credibility: Van Diggelen designed assisted-GPS receivers and Enge directed Stanford's GPS lab; the measurement is a crowdsourced class lab.
- contribution: The origin of GPS.gov's 4.9 m smartphone figure.
- limits: Abstract only (full paper paywalled); phones from 2014, self-reported lab, not a controlled test; modern dual-frequency phones may do better.
- read: partial (abstract via fetch summary)
- rights: not reused.

### Code Based Positioning (SPS) (Navipedia)
- url: https://gssc.esa.int/navipedia/index.php/Code_Based_Positioning_(SPS); text read from: same
- byline: J. Sanz Subirana, J.M. Juan Zornoza and M. Hernández-Pajares (Technical University of Catalonia) · reference wiki article · Navipedia, European Space Agency · 2011
- verdicts: C3 pass
- use: Eqs. 1–6: pseudorange model, four unknowns (x, y, z, receiver clock offset), linearization around an approximate position, least squares when n > 4, iteration.
- credibility: Authors are the gAGE research group who wrote ESA's GNSS data-processing textbook; Navipedia is ESA-curated.
- contribution: The standard navigation solution in explicit linear-algebra form.
- limits: Written for advanced readers; I use only the structure, not formulas.
- read: full
- rights: not reused.

### Positioning Error (Navipedia)
- url: https://gssc.esa.int/navipedia/index.php/Positioning_Error; text read from: same
- byline: J. Sanz Subirana, J.M. Juan Zornoza and M. Hernández-Pajares (Technical University of Catalonia) · reference wiki article · Navipedia, European Space Agency · 2011
- verdicts: C7 pass
- use: "Predicted Accuracy: Dilution of Precision": DOP is computed only from satellite-receiver geometry and scales measurement precision into position precision.
- credibility: As above.
- contribution: Defines DOP and how geometry multiplies ranging error.
- limits: Assumes equal, independent measurement errors.
- read: full (DOP section), partial elsewhere
- rights: not reused.

## Gaps
- C6: only conditional source for the smartphone 4.9 m figure (abstract read; 2014 phones).
- Phone-specific extras (assisted GPS, other constellations, Wi-Fi and cell fusion) were left out of scope rather than sourced.
