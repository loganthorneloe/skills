# Blind judgment: GPS pair gps3 (A vs B)

Both reports were rendered with Playwright (Chromium) at 1280px and 390px. Screenshots and the script are in `evaluation/scratch-judge-gps3/`. Neither page had console errors or horizontal page overflow at either width. Every image loaded. Each interactive's sliders, Solve and Reset were operated, and their readouts were checked against the drawing.

Words are visible text, including sources and captions, with script and style removed.

## Scores

Dimensions: 1 prerequisites, 2 dependency order, 3 mechanistic depth, 4 evidence for foundations, 5 accuracy, 6 transfer, 7 source/exhibit quality, 8 readability, 9 presentation, 10 signal density, 11 time to answer, 12 research quality, 13 visual explanation.

| Report | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | Total /65 | Probes /16 | Words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | **62** | **14** | 2,005 |
| B | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | **58** | **16** | 3,146 |

### Score rationale

- **Prerequisites and mechanism (1, 3).** Both teach the steps in order: PRN code, time stamp plus ephemeris, delay times c, spheres, the clock bias as a fourth unknown, linearize and iterate, least squares, why satellite clocks can't be solved away, and relativity. B goes deeper in three places. It gives the separate gravity and speed terms ("5.288 parts in 10^10 … 13.7 km"; "0.8228 parts in 10^10 … 2.13 km") and shows that they add up. It explains dilution of precision as a multiplier ("spheres cross at shallow angles, and a small error in a distance slides the crossing point a long way"). It also walks through the linearization step by step. A covers each of these in one or two sentences. It says only that "gravity wins" and that bunched satellites are worse, without saying why.
- **Transfer (6).** B states the general rule outright: "Anything that changes a signal's travel time without the receiver knowing … looks exactly like extra distance". A reader can apply that to a new case. A has the right ingredients ("reflect them into longer paths", "satellites spread across the sky fix a position better") but leaves the reader to connect them.
- **Exhibits and visuals (7, 13).** A has more teaching visuals, and they fit the argument better. Its sphere-intersection figure shows trilateration, and its error-budget figure sizes every term of a pseudorange. A also adds a careful caveat to that figure: the "< 13 m" relativistic entry "appears to be the elliptical-orbit term". Its URE and urban-canyon cartoons support the accuracy section, and its A-GNSS diagram supports the fast-fix section. B's Ashby navigation figure mostly repeats the equation as artwork. B has no exhibit for error sources or multipath. B's timing-to-distance table is useful.
- **Readability, density and time to answer (8, 10, 11).** Both put the short answer near the top, after the source list. B's seven source blurbs are longer. B's body is about 57% longer, mostly from added mechanism, with some repetition: section 6 and the closing section restate the clock argument, and the 30 cm per ns point appears three times. A says nearly everything once.
- **Presentation (9).** Both are clean on desktop and mobile. A has a close-up pane in its interactive, which makes the mismatch triangle readable. In B's interactive, at extreme slider values (for example −40 ticks) the crossing triangle runs off the bottom of the canvas. This is a minor defect.
- **Research quality (12).** A's records cite the primary interface specification, IS-GPS-200N, with section locators for the message contents, the −4.4647E-10 offset and the 10.2299999954326 MHz clock setting. They also cite the EU GSA white paper with page locators, Ashby's review, and GPS.gov. A notes and resolves a last-digit disagreement between sources. B's records are also careful: it read Ashby's AAPT paper in full, plus Navipedia and GPS.gov. But B takes the 4.9 m smartphone figure from a conference abstract only, which it admits, and it uses no primary specification. Both mark their read depth honestly.

## Visuals

### A

1. **GPS constellation diagram (GPS.gov).** Six tilted planes keep four or more satellites in view anywhere.
2. **Sphere/circle intersection (GSA white paper, Fig. 1).** Three ranges meet at one point in the ideal case. This is the core trilateration picture.
3. **Interactive with two sliders (true clock error and solver's correction), Solve, Reset, and a 50 km close-up pane.** One correction value shrinks the mismatch triangle to a point. The readout converts µs to km (0.2998 km/µs). It works and is legible at both widths.
4. **Allan deviation, quartz vs cesium (Ashby, Fig. 1).** Quartz is stable for seconds and cesium for about a day, which explains why the phone re-solves its clock.
5. **Fractional frequency shift vs orbit radius (Ashby, Fig. 2).** Clocks at GPS altitude run fast (about +440 parts per 10^12), while the Shuttle's ran slow.
6. **Pseudorange error budget (GSA, Fig. 8).** It gives typical sizes of every error term: clock terms of hundreds of km, atmospheric delays of 2 to 30 m.
7. **URE vs user accuracy cartoon (GPS.gov).** Per-satellite range errors combine into a position error circle.
8. **Urban canyon cartoon (GPS.gov).** Buildings block some signals and reflect others.
9. **A-GNSS diagram (GSA, Fig. 15).** The network delivers assistance data while timing still comes from the satellites.

B has a timing-error-to-distance table that A should have had, and A also lacks a breakdown of the gravity and speed terms.

### B

1. **GPS constellation diagram (GPS.gov).** It teaches the same point as A's.
2. **Ashby 2006 navigation figure.** It shows four lines with |r − r_j| = c(t − t_j). This is mostly decorative, because it restates the equation.
3. **Timing-error-to-distance table (1 ns, 3 ns, 1 µs, 1 ms, 38.6 µs).** It makes the clock-precision scale concrete.
4. **Interactive with one slider (assumed clock error), Solve, Reset.** The circles meet only at the right bias, and the readout says whether the circles are too large or too small. It works. The triangle runs off the canvas at extremes, and there is no zoom pane.
5. **Allan deviation (Ashby, Fig. 1).** It teaches the same point as A's.
6. **Frequency shift vs orbit radius (Ashby, Fig. 2).** It teaches the same point as A's, and the caption adds the roughly 23 ns eccentricity term.

B lacks four of A's visuals that it should have had: the sphere-intersection figure, the error-budget figure (B describes these errors only in prose), the urban-canyon/multipath cartoon (relevant to the transfer probe), and the URE vs accuracy cartoon. The A-GNSS diagram falls outside B's declared scope.

## Probes (0/1/2)

| Probe | A | B | Notes |
|---|---|---|---|
| Q1 What satellites broadcast | 2 | 2 | Both cover the time stamp, ephemeris and clock corrections. A quotes IS-GPS-200. |
| Q2 Signal to distance | 2 | 2 | Both give ρ = c(t_rx − t_tx) and a worked 67 ms example. |
| Q3 Distances to position | 2 | 2 | Both explain sphere → circle → two points. |
| Q4 Why four | 2 | 2 | Both treat the clock bias as a solved fourth unknown and say why it is common to all ranges. |
| Q5 Clock precision | 2 | 2 | Both give 30 cm/ns and atomic clocks. B also gives 1 µs = 300 m. A gives 1 ms = 300 km and 0.2998 km/µs. |
| Q6 Relativity | 1 | 2 | A gives a net 38.6 µs/day, more than 11 km/day, the pre-launch offset and NTS-2, but no magnitudes for the gravity and speed terms (only "gravity wins"). B gives about 45 vs about 7 µs/day as 13.7 km and 2.13 km. |
| Q7 Accuracy limits | 2 | 2 | Both cover the atmosphere, multipath, geometry, 4.9 m, 2.0 m URE and dual frequency. |
| Q8 Urban 50 m jump | 1 | 2 | A says buildings block and reflect "into longer paths" and that spread satellites are better, but never links these to an overestimated range or an amplified error. B states both links explicitly. |
| **Total** | **14** | **16** | |

## Factual errors or overclaims

**A.** No consequential errors were found. These are minor:
- "circle the Earth twice a day" is slightly rounded (the orbit takes about 11 h 58 min). B says the same.
- The phrase "corrected even for relativity" in the short answer is fine, but the body never says that the gravity term is roughly six times the speed term. This is an omission, not an error.
- The statement that the error figure's "< 13 m" is the eccentricity term is hedged as "appears to be". It is plausible, because about 23 ns at e ≈ 0.01 gives several meters and e up to about 0.02 roughly doubles that.

**B.** No consequential errors were found. I checked the numbers: 5.288e-10 × 86,400 s × c ≈ 13.7 km, 0.8228e-10 ≈ 2.13 km, the net 4.465e-10 ≈ 38.6 µs ≈ 11.6 km, and NTS-2 at 442.5 vs 446.5. These are minor:
- "the clock gains roughly 445 parts in 10^12" is fine, and is close to the figure's roughly 440.
- "high-end receivers … reach centimetres" is true for RTK/PPP but is stated without a source.
- The claim that "phones' urban accuracy tracked building height" rests on an abstract only, which the records admit.
- The source blurbs reveal the research process ("The live address now fails", "Only the abstract was available to me"). This is not an error.

## Verdict

**A gives real understanding faster.** At about 2,000 words it covers the whole causal chain once. It has more and better-integrated exhibits, including the sphere intersection, the error budget, the urban canyon, A-GNSS, and an interactive with a zoom pane. It also cites the primary GPS specification.

The shorter report lost three things. It drops the numbers for the gravity and speed terms behind the 38 µs net. It asserts rather than explains why bunched satellites amplify error. And it never states outright that a reflected signal reads as extra distance, which is the link the urban transfer probe needs. Those gaps cost A two probe points, and they are where B's extra 1,100 words go. Some of B's extra length, however, is repetition and long source blurbs, and B leaves out A's error-source and multipath visuals.

On balance A is the better concise report. B is the more complete one for a reader who needs to reason through the urban-canyon or relativity breakdown cases.
