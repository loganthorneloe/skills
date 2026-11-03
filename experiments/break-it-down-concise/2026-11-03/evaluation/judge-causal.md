# Blind judge: causal inference reports A, C, D, E, F, G

I read the reports A, C, D, E, F and G, the research packet (`research/causal`), the rubric and the topic probes. B was not in my brief, so I did not judge it. I rendered each report with Playwright at 1280px and 390px and read the rendered text. I also checked for overflow and console errors and clicked every widget. Screenshots and scripts are in `evaluation/scratch-judge-causal/`.

Measured facts (rendered text):

| Report | Words | Words before the core answer | Height at 390px | Interactive widget |
|---|---|---|---|---|
| A | 5,321 | 642 | 28,561 px | coin-flip simulator, adjustable effect |
| C | 4,571 | 785 | 26,163 px | tick-box six-student table plus a 1,000-draw histogram |
| D | 2,323 | 441 | 14,962 px | choose-or-coin model with a motivation slider, showing the bias tile |
| E | 1,588 | 356 | 10,796 px | coin flips at 6 or 600 students |
| F | 1,679 | 316 | 10,108 px | lottery histogram at 6/60/600 with a 95% range |
| G | 3,163 | 642 | 17,958 px | choose-or-coin model showing the bias tile |

All six reports put the source list before the answer, so every reader scrolls past 316–785 words of source entries first. No page scrolls sideways at 390px; wide tables and images sit in their own scroll boxes. I saw no console or page errors, and every button worked. The source entries mirror the audit notes on credibility and limits ("It covers specific products in their first year, used about a tenth of class time…"), which shows that a source-audit step produced them.

## Score table

Columns 1–9 follow the rubric, column 10 is signal density and column 11 is time to answer. Each column is scored 1–5, so the maximum total is 55.

| Report | 1 Prereq | 2 Order | 3 Mechanism | 4 Foundation evidence | 5 Accuracy | 6 Transfer | 7 Exhibits | 8 Readability | 9 Presentation | 10 Density | 11 Time to answer | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 3 | 4 | 3 | 2 | **46** |
| C | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 3 | 4 | 3 | 2 | **45** |
| D | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | **53** |
| E | 4 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 5 | 4 | **47** |
| F | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | 5 | 4 | **51** |
| G | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 4 | 3 | **48** |

Topic probes Q1–Q8, each scored 0–2:

| Report | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Sum |
|---|---|---|---|---|---|---|---|---|---|
| A | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 14 |
| C | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 14 |
| D | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 14 |
| E | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 1 | 13 |
| F | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 14 |
| G | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 14 |

Every report has the same two probe gaps. No report separates random assignment from random or representative sampling (Q6). All of them gesture at it, with lines like "results belong to one product, place, and test", but none says that a fair comparison inside the study does not make the participants representative. No report works through a fresh transfer case like Q8. Each ends with "ask who was compared with whom", and D's closing checklist comes closest. A is the only report that names the term "confounder", though every report explains the mechanism behind it. Five reports reach the same probe sum, so the probes barely separate them. The differences show up in per-minute value and accuracy.

## Per-report findings

### A (5,321 words)

**Errors and overclaims.** I found none of consequence. "The report says neither difference holds up once you account for testing nine characteristics at once" uses a count of nine that the packet does not confirm. The packet only says that "none is significant after correcting for multiple comparisons." The limits it gives for Mindspark ("gains showed up mainly on questions below the students' grade level and did not appear on their schools' own exams") match the audit record.

**What it teaches best.** A is the most complete account. It names the confounder ("A trait that drives both the choice and the outcome is called a confounder"). It shows the split "could be 2 + 16, or 18 + 0, or −3 + 21", gives the IV estimate (0.6 SD for 90 days) with its assumption, converts 0.37 SD to about the 64th percentile, and reads the HISP table against the $10 decision rule.

**Omissions.** It omits nothing important. Its problem is cost. The Mixtape tables (E2/E3) and the six-student table teach the same lesson twice. The simulator then rebuilds the six-student split a third time. Captions retell numbers the prose has already given, and the two-paragraph close recaps the whole report.

### C (4,571 words)

**Errors and overclaims.** It calls the 0.23 SD Hindi gain large: "+0.37 SD in math and +0.23 SD in Hindi, large by the rule of thumb above". On the rule of thumb the report itself quotes, 0.23 falls in 0.10–0.25, which is "encouraging", not large. The source entry's "including researchers at the poverty-research center J-PAL" is not in the packet; the packet only says J-PAL funded the Mindspark study.

**What it teaches best.** C states most clearly that statistical significance is not causation: "reports a difference of −$14.46 … with a t-statistic of −49 … It is still the wrong answer". Its tick-box table lets the reader change who uses the app and watch selection bias move.

**Omissions.** It does not use the term "confounder". It has the same doubled worked example as A (Mixtape tables plus six students). At 785 words, its source entries form the longest preamble in the set, with sentences like "A review by education economists, including researchers at … J-PAL, that included only randomized and similarly rigorous studies because…".

### D (2,323 words)

**Errors and overclaims.** "Yet their full table shows 10 of 20 would die either way, so the treatment does nothing" is a slight overstatement, since only the average effect is zero. The numbers themselves are right. Its decomposition is the most precise in the set: "observed gap = true average effect for users + selection bias".

**What it teaches best.** D links each idea to the next and states the key limits in single lines. One example is "A p-value addresses luck, not bias, so a self-selected comparison can be highly 'significant' and still wrong." The design table, with columns for what each design compares and what must be true, covers Q7 in four rows. Its simulation shows that "drawing more students only pins that wrong number down more precisely." That point answers the sample-size misconception directly. The closing checklist is the most usable transfer tool in the set.

**Omissions.** It does not name "confounder", and it has no spillover point. It has nothing else important that A has and it lacks.

### E (1,588 words)

**Errors and overclaims.** It says "winners led by 0.37 in math and 0.23 in Hindi in the published estimates, large by the same scale". Hindi at 0.23 is "encouraging" on that scale. "Grades 4 and 6 showed the same pattern" leaves out algebra, which is harmless.

**What it teaches best.** E carries the whole core chain in the fewest words: the counterfactual, then the six-student split (18 = 2 + 16), then LaLonde, coin flips and the two trials.

**Omissions.** Relative to D, it omits the point that significance is not causation; there is no t = −49 or "luck, not bias" line. Its quasi-experiments get a single unnamed sentence ("an as-if-random event, a score cutoff for eligibility, or groups that were changing alike"), which is too thin to act on. It gives no attrition detail, and the before-and-after trap appears only through the Delhi losers. Its widget offers only 6 or 600 students and has no histogram, so chance variation stays less concrete than in F.

### F (1,679 words)

**Errors and overclaims.** "In a made-up example from Hernán and Robins, 54% of treated patients died against 43% of untreated ones, yet the treatment changed nobody's outcome" goes beyond the packet. The packet supports only a zero *average* effect (10/20 vs 10/20), not zero effect for every individual. Everything else checks out. It correctly rates Delhi "large for math and encouraging for Hindi", and its "overstated the randomized answer by about 40%" matches −14.46 against −10.14.

**What it teaches best.** F makes chance concrete better than any other report. Its histogram text quantifies the result: "Across 2,000 lotteries of this size, 95% of gaps fall between −2.1 and +6.3", and "one in 20 reproduces the self-chosen split". Instead of embedding the soft scan, it rebuilds the three LaLonde rows as a readable table. It also packs four traps (sign reversal, reverse causation, before and after, and dose) into one paragraph.

**Omissions.** It does not cover attrition or spillovers. Its quasi-experiment section is two sentences, though it does name regression discontinuity and difference-in-differences and their assumption, and matching is covered earlier. Its sources come first with no heading, which is a little disorienting.

### G (3,163 words)

**Errors and overclaims.** It repeats the overclaim ("although the treatment changes nobody's outcome: in the full 'what if' table, 50% die either way"). It applies "large on the scale above" to both 0.37 and 0.23. Its follow-up rates (16% vs 12% dropout) and the reweighting and bounding checks match the audit record.

**What it teaches best.** Its explanation of why adjustment cannot be checked is the clearest in the set. It quotes the line "cannot empirically verify" and then glosses conditional exchangeability in plain words. It also calculates that a before-and-after look "would have roughly doubled" the Delhi effect.

**Omissions.** It omits nothing important relative to A. It costs extra words in two ways. Source entries restate body content: the IES entry already gives "132 schools … 16 … programs … a tenth of class time", and the body repeats it. Long figure captions retell the prose.

## Overall ranking for a reader who wants real understanding fast

1. **D**: the full understanding of A or C in under half the words, with the best transfer checklist and the sharpest line on significance versus bias.
2. **F**: nearly D's understanding in about 70% of D's length, and the best treatment of chance; one overclaim, and thin on what can go wrong inside a real trial.
3. **G**: complete and accurate apart from one overclaim, but sources and captions repeat each other.
4. **E**: the fastest core answer, but it loses the significance-versus-causation point and any usable account of quasi-experiments.
5. **A**: the most complete reference, at roughly 2.3 times D's length, with the same lesson taught three times.
6. **C**: as complete as A, but it has the longest preamble, the same duplication, and the Hindi overclaim.

**Shorter reports that match the best long report.** D matches A and C on every probe and on mechanism, and its transfer guidance is better. F matches them on the core mechanism and on chance, and loses only secondary wrinkles (attrition, spillovers, the HISP table). E does not match them: its quasi-experiment coverage and its significance-versus-causation point are both too thin.

## Patterns: words that paid off and words that were wasted

**Worth their words**

- **The six-student constructed table with one decomposition sentence** (all reports): "Users average 80 and non-users 62, an 18-point gap. Only 2 points of it are the app." This one exhibit carries Q1–Q4.
- **LaLonde as a known-answer test of adjustment.** It is the only real-data evidence that adjustment fails. F's three-row rebuilt table delivers it in about 60 words plus the table, where A and C use an image and a 120-word caption.
- **One-line distinctions that block a misconception.** D: "A p-value addresses luck, not bias." D: "drawing more students only pins that wrong number down more precisely." G: "A users-versus-non-users gap is therefore not evidence against the app either."
- **Widgets that show a hidden quantity.** D and G show a "Selection bias" tile that is "normally hidden", and F reports a 95% range. A widget that only reprints the static example adds little; C's tick-box table is the borderline case.
- **Design-plus-assumption tables** (D, G) answer Q7 in four rows.

**Wasted words**

- **Audit-style source entries placed before the answer** (all reports; worst in C and A at 785 and 642 words). C's entry for Hernán reads: "Its opening chapters define a causal effect as a comparison of the same people under two 'what if' conditions, show with a small invented population how treated and untreated groups can differ…" That entry previews the body, and the body then teaches it again.
- **Repeated worked examples.** A and C show Mixtape Tables 4.2 and 4.3 *and* the six-student table *and* a simulator of the same split. The Mixtape tables add only the sign flip, which D, E and F give in one sentence: "surgery adds 0.6 years … the observed comparison says it costs 0.4 years".
- **Exhibit commentary that repeats the prose.** In A's LaLonde passage, the prose gives $886, and the caption then repeats $886, $15,578 and $8,067, the adjustment list and the later-reanalysis caveat. G's Mindspark caption repeats the before-and-after point made two sections earlier.
- **Recap closings.** A's final section ("What this means when you read a claim", two paragraphs) restates the short answer, the LaLonde result and the trial limits. D's checklist close does the same job in one paragraph and turns it into questions the reader can ask.
- **Source caveats repeated in body and entry.** For example, "None of these trials tested a phone app that students use on their own" appears in body text in A, C, F and G as well as being implied in the source entries. Saying it once is enough.

## Five-line summary

1. Ranking: D > F > G > E > A > C (totals out of 55: 53, 51, 48, 47, 46, 45).
2. D gives the full understanding of the long reports in 44% of A's words. F nearly matches it in 32% of A's words and is the best on chance.
3. Two accuracy slips recur. C, E and G call the 0.23 SD Hindi gain "large" (it is "encouraging" on the cited scale). F and G say Hernán's treatment "changed nobody's outcome" (only the average effect is zero).
4. Shared gaps: none separates random assignment from representative sampling (Q6), and none works a fresh transfer case (Q8). Every report puts 300–800 words of source entries before the answer.
5. Words went furthest on the six-student split, LaLonde, one-line "luck, not bias" distinctions and widgets that reveal hidden bias. They were wasted on audit-style source entries, the Mixtape tables doubling the six-student example, captions retelling the prose, and recap endings.
