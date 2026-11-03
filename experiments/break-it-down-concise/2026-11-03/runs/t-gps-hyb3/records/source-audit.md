# Source audit records (accessed 2026-11-03)

### Using GNSS Raw Measurements on Android Devices (White Paper)
- url: https://www.gsc-europa.eu/sites/default/files/sites/all/files/gnss_raw_measurement_web_0.pdf; text read from: same (PDF, PyMuPDF text + page renders)
- byline: GSA GNSS Raw Measurements Task Force · white paper · European GNSS Agency (Publications Office of the EU), doi 10.2878/449581 · 2017
- verdicts: C2 pass; C3 pass; C4 pass; C7 pass (error magnitudes as typical ranges); C8 pass; C1 conditional (says ~20,000 km generically for GNSS)
- use: §1.2 p.7 (Fig. 1 spheres, PRN alignment, four unknowns); §1.6 p.13 (pseudorange = (tRx - tTx)·c); §1.7.1 p.14 (iterative linearization, least squares); Fig. 8 p.15 (error budget); §3.1 p.28 (A-GNSS, Fig. 15, TCXO/XO).
- credibility: Written by the EU agency responsible for Galileo with a task force of receiver makers, universities and Google review; it explains how phone chipsets actually produce measurements.
- contribution: Plain-language synthesis of textbook GNSS positioning, tied specifically to smartphone receivers and Android raw measurements.
- limits: Part I is explicitly a synthesis of textbook literature (RD-03..05), not new research; 2017, so Android API details are dated, but positioning principles are unchanged. Fig. 8 magnitudes are generic ranges, not measurements of a particular phone. Reuse: excerpts allowed with stated source line, no alteration.
- read: partial (§1 fully, §3.1 fully; §2 API sections skimmed) · via canonical PDF

### Relativity in the Global Positioning System
- url: https://doi.org/10.12942/lrr-2003-1; text read from: PubMed Central PMC5253894
- byline: Neil Ashby · review article · Living Reviews in Relativity 6:1 · January 2003 (revised June 2007)
- verdicts: C3 pass; C4 pass; C5 pass; C6 pass; C1 conditional (describes 24-satellite baseline as of 2003)
- use: §2 Eq. (1) and "Timing errors of one ns will lead to positioning errors of the order of 30 cm"; Fig. 1 (Allan deviation, Cesium vs Quartz) and the "about 4 nanoseconds" per day statement; Fig. 2 (net fractional frequency shift vs orbit radius); NTS-2 story (+442.5 measured vs +446.5 predicted parts in 10^12).
- credibility: Ashby is a University of Colorado physicist who worked on the GPS relativistic corrections for decades; the review is the standard technical reference on the topic.
- contribution: Derives the relativistic clock offsets and explains how GPS is built around the constancy of c.
- limits: Equations in PMC are images, so exact Eq. (35) values were not transcribed; constellation description is from 2003. The 38 us/day figure is computed here from Ashby's 446.5e-12 and IS-GPS-200's 4.4647e-10 (x 86,400 s). No erratum found in one targeted search; the 2007 revision only added sections. Figure reuse rights unstated in the copies read.
- read: partial (§1-§5 read; later sections on TOPEX and augmentation skimmed) · revision 2007 as served by PMC

### Relativity and the Global Positioning System
- url: https://physicstoday.aip.org/features/relativity-and-the-global-positioning-system; text read from: same via fetch-tool summary (partial)
- byline: Neil Ashby · feature article · Physics Today 55(5), American Institute of Physics · May 2002
- verdicts: C6 pass (">11 km" in one day; net 4.4645 parts in 10^10); C4 conditional (corroboration only)
- use: quotes on net correction and on the 11 km per day consequence.
- credibility: Same author as the review; popular-level magazine of a physics society.
- limits: Read through a fetch tool's extraction, so counted partial; its 4.4645e-10 differs in the last digit from IS-GPS-200N's 4.4647e-10 (rounding/model difference; report uses the spec value).
- read: partial (fetch summary with quoted sentences)

### IS-GPS-200N: NAVSTAR GPS Space Segment / Navigation User Segment Interfaces
- url: https://archive.gps.gov/technical/icwg/IS-GPS-200N.pdf; text read from: same
- byline: Space Systems Command, MilComm & PNT Directorate · interface specification · U.S. Space Force / GPS.gov · 1 August 2022 (Rev N)
- verdicts: C2 pass; C6 pass; C8 conditional (provides 50 bps / 1500-bit frame / 25-frame structure; time-to-first-fix consequence is inference)
- use: §3.2.2 p.12 (LNAV contents); §3.3.1.1 p.13-14 (10.23 MHz, -4.4647E-10, 10.2299999954326 MHz); §20.3.1-20.3.2 p.79 (50 bps, 1500-bit frame of five 300-bit subframes); §20.3.3.4.1 p.103 (subframes 2 and 3 contain ephemeris).
- credibility: The governing technical specification that every GPS receiver is built against.
- limits: Specification of the legacy L1 C/A / LNAV signal; modern signals (L1C, L2C, L5) use other message formats. A later change notice (IS-200N RFC544, 2025) exists; the clock offset value is the same in the notice per search result (unverified).
- read: partial (sections listed) · Rev N

### GPS.gov: Space Segment
- url: https://www.gps.gov/systems/gps/space (now 404); text read from: https://archive.gps.gov/systems/gps/space/
- byline: National Coordination Office for Space-Based PNT · government web page · GPS.gov · last modified 28 June 2022; site notes no updates since February 2025
- verdicts: C1 pass (constellation as of July 2023: 31 operational)
- use: Constellation Arrangement section; "Expandable 24-slot" figure.
- credibility: The U.S. government's official public information site for GPS.
- limits: Satellite count is dated July 2023; the count changes as satellites launch and retire.
- read: full

### GPS.gov: GPS Accuracy
- url: https://archive.gps.gov/systems/gps/performance/accuracy/; text read from: same
- byline: National Coordination Office for Space-Based PNT · government web page · GPS.gov · last modified 3 March 2022
- verdicts: C7 pass (URE commitment, causes of error); C7 conditional for the 4.9 m smartphone figure (gps.gov cites an ION paper; not independently read)
- use: "How accurate is GPS?", "Why does GPS sometimes show me in the wrong place?", URE vs user accuracy figure, urban canyon figure.
- credibility: Official; states government commitments directly from the SPS Performance Standard.
- limits: The 4.9 m figure is a typical open-sky value from one cited study; phones now often use dual-frequency and multi-constellation receivers, which this page does not address.
- read: full

## Gaps
- C1: only government pages and dated papers — current satellite count changes; reported as "about 31 (July 2023)".
- C7: smartphone 4.9 m figure via gps.gov's citation of an ION paper not read directly — stated as gps.gov's figure.
- C8: time-to-first-fix values not sourced numerically; report states only that the broadcast message takes 30 s per frame (derived from 1500 bits at 50 bps) and that A-GNSS aims to reduce TTFF.
