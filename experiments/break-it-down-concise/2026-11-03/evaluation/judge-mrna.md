# Blind judgment: mRNA vaccines (A vs B)

Both reports were rendered with Playwright at 1280px and 390px. Neither had console errors, failed requests or page-level horizontal overflow. Neither has interactive controls. On mobile, wide figures and SVGs sit in horizontal-scroll containers on purpose. Words are counted from the rendered body text, including the sources list. Screenshots and the render script are in `evaluation/scratch-judge-mrna/`.

## Scores

| | 1 Prereq | 2 Order | 3 Mech | 4 Evid | 5 Acc | 6 Transfer | 7 Exhibits | 8 Read | 9 Present | 10 Density | 11 Time | 12 Research | 13 Visual | Total /65 | Probes /16 | Words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 4 | 57 | 14 | 3055 |
| B | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 57 | 14 | 1583 |

### Score notes

A teaches more of the foundations. It explains what proteins do, the innate and adaptive layers of immunity, how receptor diversity lets rare matching cells find spike, how the ionizable lipid gets mRNA out of the endosome, and the cap and poly-A tail. Its six sources each come with a full credibility and limits note. The cost is length: the source block alone runs to about 450 words before the short answer.

B covers the same chain in about half the words. Its short answer and "The biology you need" section get a novice to the core answer within about a minute. B leaves out the innate versus adaptive framing, receptor diversity, and LNP chemistry. That costs some depth on mechanism (3) and prerequisites (1), but nothing the core question depends on.

Research quality (12) is strong in both. Both have per-claim verdicts and say what they read, with stated gaps such as "no human genome-sequencing study". A primary-sources its trial evidence from Polack and uses Röltgen for persistence in lymph nodes. B uses the FDA briefing, Turner for germinal centres, and Fertig for mRNA in blood. B's own Fertig record notes that Fertig's introduction cites lymph-node detection out to 60 days, but B's report never uses that.

## Visuals

### A
- Nobel Fig. 3 (U vs pseudouridine). Teaches that modified mRNA yields far more protein. The caption correctly calls it an illustration, not data.
- Nobel Fig. 4 (nanoparticle to ribosome to surface spike to B-cell receptor). Traces the whole in-cell path and shows the mRNA never entering the nucleus. The caption names its limits: B cells only.
- Polack Fig. 3 (cumulative incidence with efficacy table). Teaches that the curves overlap for about 12 days and then split. The table is tiny on mobile.
- Generated SVG (DNA to mRNA to protein, with the "no route back" path crossed out). Teaches the one-way flow and where the vaccine enters.
- Four-cell grid (B cells, helper T, killer T, memory). A structured text panel.
- A should have had B's mRNA-persistence data figure or a timeline. Its persistence claim (day 37 and day 60 in lymph nodes) is prose only. It also lacks a single diagram of the immune half of the story.

### B
- Generated mechanism SVG (six steps: bubble, ribosomes, spike, mRNA breakdown, B/T cells, memory). Shows the whole causal chain in one picture, immune side included.
- Turner Fig. 2 (germinal-centre B cells, weeks 3 to 15). Teaches that training continues for months. The figure is dense flow cytometry. The caption points the reader to panel e, but the figure is still heavy for a novice.
- FDA Fig. 2 (cumulative incidence). Same lesson as A's Polack figure, with a caption that explains the axis units.
- Fertig Fig. 1 (vaccine mRNA in plasma and white blood cells). Teaches that vaccine mRNA is temporary but lasts about two weeks, not hours.
- Three barrier cards (reach DNA, become DNA, get spliced in).
- Generated timeline SVG (mRNA in blood, trial protection, germinal centres). Shows that protection outlasts the vaccine material, with honest caveats about sampling windows.
- B should have had A's Nobel Fig. 3 on base modification. B links it only, citing reuse terms. B also lacks a DNA-flow diagram like A's, although its barrier cards partly cover it.

## Probes (0/1/2)

| Probe | A | B | Note |
|---|---|---|---|
| Q1 mRNA's normal job | 2 | 2 | Both explain copy, ribosomes, destruction. |
| Q2 What it encodes, what happens | 2 | 2 | Both cover spike, LNP uptake, translation and display. |
| Q3 How it trains immunity | 2 | 2 | Both cover B cells, antibodies, helper and killer T cells, memory. B adds Tfh selection. |
| Q4 LNP and modification | 2 | 2 | A goes deeper (enzymes shred bare mRNA, TLRs, m1Ψ). B is sufficient. |
| Q5 Why no DNA change | 2 | 2 | Both give the three barriers plus Aldén/LINE-1 with its limits. |
| Q6 How long things last | 2 | 2 | A gives lymph nodes to day 60. B says "Protection is immune memory, not lingering mRNA". |
| Q7 Evidence and limits | 1 | 1 | Both give 95%, waning and variants. Neither mentions myocarditis or other rare side effects (A mentions only a sore arm). |
| Q8 Transfer to a new virus | 1 | 1 | Both say only the spike recipe changes. Neither says what still takes time (manufacturing, trials, approval). |
| **Total** | **14** | **14** | |

## Factual errors and overclaims

### A
- The Polack caption says "8 in the vaccine group against 162 with placebo, out of roughly 21,700 people in each group". The 8-vs-162 endpoint was in the evaluable population without prior infection, about 18,200 per arm. The 21,700 figure is the dose-1 population. This is a minor error.
- The short answer says the mRNA "never goes where your DNA is kept". That is stated absolutely, but the body later qualifies it properly, and the LINE-1 discussion acknowledges that human cells do have a reverse transcriptase.
- No consequential errors.

### B
- B says the mRNA "is broken down within days to a couple of weeks", in the short answer, the diagram and the timeline. The Turner caption adds "long after the mRNA is gone". This rests on blood data only. Lymph-node germinal centres held vaccine mRNA to day 37 to 60 (Röltgen, a study A cites; B's own Fertig record notes the 60-day figure). So "gone" by weeks 3 to 15 is an overclaim for the very tissue the Turner figure shows.
- "Cells do not use one [reverse transcriptase] on ordinary mRNA". This is slightly too strong, and B itself later introduces LINE-1 reverse transcriptase without reconciling the two statements.
- "36,621 participants without prior infection" is attributed to the FDA briefing. That is plausible for the FDA's count (Polack reports 36,523), so it is not flagged as an error.

## Verdict

B gives a reader real understanding faster. It answers both of the user's questions in about half the words (1,583 vs 3,055), and its diagram and timeline show the whole chain from shot to memory, and why protection outlasts the vaccine material.

The shorter report lost some things. On the text side, it dropped the innate versus adaptive framing, receptor diversity, and LNP endosomal-escape detail. On the visual side, it dropped the base-modification figure (linked instead of shown). Most importantly, it dropped the lymph-node persistence evidence, and without it B's "days to two weeks" claim reads as overconfident. None of this changes the probe scores (14 vs 14).

A is the more complete and slightly more careful teaching document, but much of its extra length is the long source preamble and supporting depth, not the core answer. Overall it is a tie at 57/65. B wins on density and speed. A wins on prerequisites, mechanism and exhibits.
