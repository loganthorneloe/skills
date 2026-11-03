# Blind judge: GPS (A vs B)

Rendered both at 1280px and 390px with Playwright (screenshots and script in `evaluation/scratch-judge-gps/`). There were no console errors and no horizontal page scroll. Both interactives were exercised: A's slider at −3, 0 and +3 µs plus Reset; B's slider at −40, 50 and 140, plus Solve and Reset. Every image loaded at its native size. Word counts cover the visible text, scripts and styles excluded, sources lists included.

## Scores

Dimensions: 1 prerequisites, 2 order, 3 mechanism, 4 evidence for foundations, 5 accuracy, 6 transfer, 7 source/exhibit quality, 8 readability, 9 presentation, 10 signal density, 11 time to answer, 12 research quality, 13 visual explanation.

| Report | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | Total /65 | Probes /16 | Words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4 | 5 | 4 | 4 | 4 | 3 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | **55** | **14** | 1,477 |
| B | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 4 | **61** | **16** | 3,146 |

### Score notes

- **A** builds the argument cleanly, in order: broadcast, time to distance, spheres, Ashby's Eq. 1, the clock as the fourth unknown, why satellites can't use that trick, Allan deviation, relativity, and limits. The mechanism is tight. It leaves out the atmosphere (ionosphere and troposphere) and satellite geometry (DOP) as error sources, and corrections such as dual frequency. Its only hint at geometry is the toy's "height is the weakest coordinate." Transfer suffers as a result. The "What limits your phone" section is one paragraph built on blockage and multipath.
- **A presentation.** The three GPS.gov source links point to `www.gps.gov/...` URLs, and both return 404 today. A's own audit record says it read archive copies because the live URL 404'd, yet it links the dead URLs. On desktop the FAA histogram is squeezed into a half-width cell (318px of 600px), so its axis labels are unreadable without clicking "full size." On mobile the lab's satellite labels sit close to the arcs but stay legible.
- **B** covers everything A does and adds four things. It explains linearize-and-iterate solving and least squares with more than four satellites (§5). It gives the gravity and speed effects as separate numbers (5.288 and 0.8228 parts in 10¹⁰, or 13.7 km and 2.13 km a day) and shows that 13.7 − 2.13 ≈ 11.6 km. It tells the NTS-2 1977 test story (442.5 vs 446.5). Its accuracy section covers DOP geometry, atmospheric delay with dual-frequency removal, and multipath, and it ties urban error to building height. Its links go to the working archive URLs. It loses a point on readability and density: §7 is one long, dense paragraph, and a seven-entry sources block sits ahead of the answer.
- **Research.** A used three sources, audited well. It honestly flags 38.6 µs/day as its own arithmetic and the 4.9 m figure as secondhand. B used seven sources. It traced GPS.gov's 4.9 m back to the van Diggelen and Enge ION abstract and qualified it (2014 phones, student-measured). It brought in Navipedia for the solver and DOP, and cross-checked the 2003 review against the 2006 teaching paper. Both list scope gaps (A-GPS, multi-GNSS) honestly.

## Visuals

### A
1. **GPS.gov URE vs user-accuracy graphic.** Several range lines meet at the user, and the error on each range becomes a region of position uncertainty. It is small (300px) but clear.
2. **Interactive clock-bias lab** (generated, 2D, three satellites, slider from −3 to +3 µs). It shows that ignoring the clock moves the fix by more than the range error (1 µs gives about 400 m, mostly downward), while solving for the clock brings it back to 0.00 m and recovers the bias exactly. It uses real-scale numbers (a 2.8 km view, 500 m grid). This is the strongest single visual in either report.
3. **Ashby Fig. 1, Allan deviation of quartz vs cesium.** Quartz is fine for about a second and then drifts, while cesium stays steady for days. The caption explains how to read the log axes. It is integrated into the argument.
4. **Ashby Fig. 2, net frequency shift vs orbit radius.** Low orbits lose time and GPS orbits gain. It is integrated with Eq. 35 and the 10.22999999543 MHz offset.
5. **FAA horizontal-error histogram.** High-quality receivers put 95% of fixes within 1.82 m. Its labels are illegible at desktop width.
6. **GPS.gov urban-canyon cartoon.** The direct signal is blocked and a reflected, longer path arrives instead. It sets up multipath directly.

A should have had a geometry/DOP explanation and something on atmospheric delay. B has neither as a figure, but B's prose covers both. A's constellation is described in text only, which is adequate.

### B
1. **GPS.gov constellation diagram.** Six tilted planes keep four or more satellites visible. It is useful but mostly context, and the image is large for what it teaches.
2. **Timing-error to distance-error table** (1 ns, 3 ns, 1 µs, 1 ms, 38.6 µs). It makes the "why precise clocks" scaling concrete in one glance.
3. **Ashby 2006 Fig. 1, the navigation equation with four satellites.** It shows that each line is one equation. The caption flags that the figure omits the bias.
4. **Interactive "find the clock error that makes the circles meet"** (toy units, slider, Solve button). Only one assumed offset makes the three circles meet, which shows how the solver finds the clock error. It is honest that "Solve" scans values where a real receiver uses algebra. It teaches the same idea as A's lab but in abstract "ticks." A's real-metre scale and its ignore-vs-solve comparison teach more.
5. **Ashby Fig. 1, Allan deviation.** Same figure as A's, with a better caption ("lower is better", 4 ≈ 3 h, 5 ≈ a day).
6. **Ashby Fig. 2, frequency shift vs radius.** Same figure as A's, captioned with the eccentricity caveat.

B should have had A's urban-canyon/multipath graphic and a picture of the signal error versus device accuracy distinction (A's URE graphic or FAA histogram). B's Q8-relevant content is prose-only.

## Probes (0/1/2, from the report alone)

| Probe | A | B | Notes |
|---|---|---|---|
| Q1 broadcast | 2 | 2 | Both give transmit time plus position from the ephemeris and navigation message. |
| Q2 time to distance | 2 | 2 | Both give distance = c × (arrival − send), about 67 ms from overhead. |
| Q3 spheres | 2 | 2 | Both explain sphere, then circle, then two points. |
| Q4 four satellites | 2 | 2 | Both treat the shared clock offset as a fourth unknown that is solved, not assumed. |
| Q5 clock precision | 2 | 2 | Both give 30 cm/ns, 300 m/µs, and atomic clocks. |
| Q6 relativity | 2 | 2 | A gives the net 38.6 µs/day (11.6 km) with the gravity-vs-speed direction stated qualitatively. B gives the separate magnitudes. Both describe the pre-launch frequency offset. |
| Q7 accuracy limits | 1 | 2 | A covers blockage, multipath and 4.9 m but has no atmosphere, no DOP and no dual-frequency correction. B covers all of them. |
| Q8 urban canyon | 1 | 2 | A explains that a reflection makes a distance read long and can't be solved away, with the cartoon, but never connects blocked satellites to worse geometry. B covers blockage worsening geometry, multipath reading long, and accuracy tracking building height. |
| **Total** | **14** | **16** | |

## Factual errors and overclaims

### A
- "Most remaining error comes from the signal's path." Defensible in context, but the list that follows omits the atmosphere, which GPS.gov itself also discusses. The omission makes the error picture incomplete, though nothing in it is false.
- "the quartz curve at a day implies a few microseconds, close to a kilometre." This is the author's own extrapolation from a log plot. It is roughly consistent (about 3×10⁻¹¹ × 86,400 s ≈ 2.6 µs ≈ 780 m) but is presented as reading the figure.
- The source links `https://www.gps.gov/systems/gps/performance/accuracy/` and `.../space/` return 404. This is a usability and provenance defect, not a factual error.
- No hard errors.

### B
- "high-end receivers that use two frequencies and correction services reach centimetres." True in practice (RTK/PPP) but unsourced in its records.
- "The satellite moves faster than a point on the rotating ground." Correct, though loose about the reference frame. Fine.
- No hard errors. Numbers check against Ashby: 5.288e-10, 8.228e-11, 4.465e-10, NTS-2 442.5 vs 446.5, and 13.7 − 2.13 ≈ 11.6 km.

## Verdict

A answers the core question faster. Its short answer plus the real-scale clock-bias lab gets a reader to the four-unknowns and why-atomic-clocks insight in about half B's words. B gives fuller understanding, and its extra length buys substance rather than padding.

The shorter report lost real content. It drops atmospheric delay, satellite geometry and DOP, dual-frequency correction, and the iterative least-squares solve. That costs A the urban-canyon transfer and the accuracy probes (14 vs 16). On the visual side, B lost A's multipath cartoon and its ignore-vs-solve comparison.

Overall B wins (61 vs 55). A is the better model of concision but cut past the limits section the request implies. Adding about 150 words on atmosphere and geometry to A would likely match B in half the length.
