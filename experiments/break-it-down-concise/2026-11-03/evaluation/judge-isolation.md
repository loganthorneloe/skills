# Blind judge: transaction isolation (reports A–F)

I read the six reports at `blind/isolation/{A..F}/report.html`, rendered each one with Playwright at 1280px and 390px, and tested every interactive control. I checked claims against `research/isolation/` (claims, background, evidence records, audit records, tables.md), the rubric, and the topic probes. A `G/` directory also exists in `blind/isolation/`. The task named only A–F, so I did not read or score G.

Rendering summary: all images load (E uses `loading="lazy"`, so they load on scroll and show as incomplete before that). No page scrolls horizontally at 390px. Every wide table, image, and code block sits inside its own overflow scroller. No console or page errors. Every interactive control works and matches the sources: B's step-by-step deposit simulator (three modes), C's six-order by four-level selector, D's withdraw-race level selector, and E's animated deposit player with retry. All six reports open with a full source list before the answer, so time-to-answer depends mostly on how long that list is.

Approximate visible words: A 1,475 · D 1,417 · E 2,090 · F 2,721 · B 4,793 · C 4,885. Characters before "The short answer": A 2,032 · E 3,105 · F 3,785 · C 5,422 · B 5,539 · D about 2,000 (D has no heading; its answer paragraph follows the sources).

## Score table

Dimensions: 1 prerequisites, 2 dependency order, 3 mechanistic depth, 4 evidence for foundations, 5 accuracy and qualification, 6 transfer, 7 source and exhibit quality, 8 readability, 9 presentation, 10 signal density, 11 time to answer.

| Report | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | Total /55 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4 | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 3 | 46 |
| B | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 3 | 2 | 49 |
| C | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 3 | 2 | 49 |
| D | 5 | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 5 | 5 | 3 | 49 |
| E | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 54 |
| F | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 3 | 50 |

Coverage probes Q1–Q8 (0–2 each, out of 16): A 15 (Q6 = 1: locking is only "making a transaction wait"), B 16, C 16, D 16, E 16, F 16. The probes mostly hit the ceiling, so they separate the reports less than the rubric does. No report says that SELECT … FOR UPDATE cannot lock rows that do not exist yet, which matters for the Q8 insert-based double booking. B, C, and F come closest with "make a hidden conflict visible by writing a shared row."

## Per-report findings

### A (about 1,475 words)
- **Errors or overclaims.** None consequential. Reading Table 4, it says "Repeatable Read also stops lost updates and values shifting mid-transaction," then qualifies it: "The Repeatable Read row is the paper's locking definition; products differ from it." It reports the 7% cost correctly as "one 2012 study."
- **Teaches well.** The shortest complete causal chain in the set. It defines correctness by serializability, shows the withdraw race, runs Hermitage's two-session SQL ("Each session meant to add one, so the right answer is 12. The value ends at 11"), notes the single-statement exception, then covers Table 4, the doctors example, retry, and mislabelled level names.
- **Omits or underexplains** (compared with E). It never explains how locking enforces a level: read locks, how long they are held, two-phase locking. There is no conflict-ordering argument for why 130 matches no serial order, no read skew, and no product comparison table (only one prose paragraph). Five source cards (about 2,000 characters) come before the answer.

### B (about 4,800 words)
- **Errors or overclaims.** None found. The Hermitage excerpt, ACIDRain Table 2 reading ("0 remained (1 where the strongest level is snapshot isolation)"), and Figure 5 reading ("drops to under half in the in-memory run") all match the packet.
- **Teaches well.** The conflict-ordering explanation: "Because B read 100 before A wrote 120, B has to come before A… B also has to come after A. B cannot be both." Its step-by-step simulator, which lets the reader pick any order under three modes, makes "only the orders where both SELECTs happen before either write lose money" something the reader discovers.
- **Omits or underexplains.** Nothing important. The cost is length. Eight source cards (about 5,500 characters, some 4–5 sentences long) come before the answer, and several facts appear twice or three times.

### C (about 4,900 words)
- **Errors or overclaims.** None found. "Any non-serializable outcome… shows such a loop" is accurate for the conflict graph it describes. MySQL's read skew "Prevented only for read-only transactions" matches Hermitage's R/O mark.
- **Teaches well.** The most complete account of the general mechanism. It walks through the serialization graph (Figure 3): "T1 must come before T2, and T2 must come before T1. No serial order satisfies both." The six-order selector shows that "Four of the six orders lose an update at the default level of both databases."
- **Omits or underexplains.** Nothing. It carries the most marginal exhibits: Berenson Figure 2 (the hierarchy), the Bailis 2013 defaults table, and both Figure 5 and the RUBiS numbers. Each repeats a point already made. The answer arrives as late as in B.

### D (about 1,420 words)
- **Errors or overclaims.** The opening, "Each operation is correct only if nothing changes the data between its read and its write," is loose: correctness is defined by running alone, which D itself says correctly one paragraph later. "In Ports and Grittner's benchmarks this cost less than 7%" leaves the 2012 hardware and 9.1 limits to the source card only. No hard errors. The widget's Serializable state ("Hermitage found that Serializable prevents lost updates in PostgreSQL, MySQL, and Oracle") holds, because Oracle's "serializable" is snapshot isolation, which prevents P4.
- **Teaches well.** The level-selector widget is the best transfer device in the set. The same four withdraw steps end "Wrong. $198 paid out" at Read Committed and at MySQL Repeatable Read ("Same name as PostgreSQL's level, weaker guarantee"), and "Correct… the retry saw the new balance" at PostgreSQL Repeatable Read and Serializable. That one widget teaches the anomaly, retry, and "names are not portable" together. D also covers locks and snapshots in one compact paragraph.
- **Omits or underexplains** (compared with E). It has no conflict-ordering argument for why the result matches no serial order. Its Berenson coverage is prose only, with no Table 4, so the reader never sees "snapshot misses write skew, locking RR misses phantoms." It omits read skew, and the anomaly list is brief.

### E (about 2,090 words)
- **Errors or overclaims.** None found. Its computed RUBiS ratio ("about 97%") matches 422/435, and it bounds the result: "PostgreSQL 9.1 on 2012 hardware against a locking version they built themselves."
- **Teaches well.** It packs the full mechanism into a few sentences: "B must come before A, because B read the old value, and after A, because B overwrote A's write. No serial order satisfies both." The deposit player then shows retry as the real price: "The stronger level did not compute the right answer; it refused the wrong one and handed the work back to the application." It covers locks and snapshots, Table 4, the doctors example with how both a locking engine and SSI catch it, a compact Hermitage table, the limits of isolation, and the single-statement exception.
- **Omits or underexplains.** Read skew is not named. There is no serialization-graph generalization (C's strength). These are minor.

### F (about 2,720 words)
- **Errors or overclaims.** "Ports and Grittner's court-system users… chose Serializable rather than checking every pair" goes slightly beyond the packet, which treats the court system as the authors' motivation and argument rather than a recorded user decision. Otherwise accurate, including "5 came from the databases' default weak isolation (4 lost updates and 1 phantom)."
- **Teaches well.** It states the two necessary conditions for a failure plainly: "The transactions must conflict… And one of them must base a decision or a write on a value that the other changes." It adds the useful converse: "Steps that do not conflict can be reordered freely… which is why databases can interleave most work safely." It gives the clearest account of how each locking level differs in how long read locks are held.
- **Omits or underexplains.** Nothing substantive. It has no interactive, and its figure captions are long, so it reads denser than E without teaching more.

## Overall ranking (for real understanding, fast)

1. **E.** Full understanding in about 2,100 words: mechanism, both enforcement families, write skew, product differences, retry, and limits, with a working demo.
2. **D.** In about 1,400 words it reaches nearly E's understanding. Its widget does the work of several paragraphs. It loses some mechanism (no ordering argument, no Table 4).
3. **F.** As complete and accurate as B and C at about 55% of their length. It is slower than E and has no interactive.
4. **B.** Complete, accurate, excellent simulator. About 5,500 characters of source cards come before the answer, and facts repeat.
5. **C.** As strong as B, plus the serialization graph, but it carries the most surplus exhibits and is the longest.
6. **A.** Fast and accurate, but the thinnest on how levels are enforced and on product differences.

The totals tie D with B and C at 49 and put F at 50. I still rank D above F for this reader because D gets them to working understanding fastest.

## Do shorter reports match the best long report?

Yes. **E** matches B and C in understanding. Every Q1–Q8 probe scores 2, and every core mechanism the long reports teach is present, at about 43% of their length. The long reports add read skew, the serialization graph (C), the Bailis defaults table, and the Jepsen bug in more detail. None of these changes what the reader can do. **F** also matches in understanding at about 55% of the length. **D** comes close at about 29% of the length. It lacks only the "before and after at once" ordering argument and the Table 4 exhibit. **A** falls short on enforcement mechanisms.

## Patterns that made words worthwhile or wasted

**Worthwhile**
- **One sentence that shows the ordering contradiction.** E: "B must come before A… and after A… No serial order satisfies both." B and C spend a paragraph each on this. E and F get it into two or three sentences. This is the single highest-value idea for the reader's "why" question.
- **A step table with a stored-balance column** (B, E, F): "Step | A | B | Stored balance … 130 (A's 20 is gone)." It replaces paragraphs of narration.
- **Interactives that change the level, not just replay the bug.** D's selector and E's player each teach the anomaly, retry, and the MySQL-versus-PostgreSQL naming split in one control.
- **The single-statement exception** (A, B, C, E, F): "The bug needs the value to pass through application code." It is short, bounds the claim accurately, and changes how the reader writes code.
- **Exhibit commentary that says what to read.** "Read the last column" (D, about PG Table 13.1). "Read across the Snapshot row" (B, C, F).

**Wasted**
- **Long source cards before the answer.** B's ACIDRain card already states "Five came from the database's default weak isolation; the other 17 came from code that never grouped its steps," which the body and the Table 2 caption repeat. B's Ports and Grittner card gives "within about 7%," which the Figure 5 caption and body text repeat. The cards push the answer about 5,500 characters down (more than 4,300px on mobile in B and C).
- **Captions that retell the body.** B's Figure 1 caption ("Two concurrent calls both read $100, both pass the check, and $198 leaves") is followed by body text making the same point.
- **Redundant exhibits.** C shows PG Table 13.1, Berenson Table 4, and Berenson Figure 2, three views of the same ladder. B, C, and F show Figure 5 and also quote the RUBiS numbers, two exhibits for one "cost depends on implementation" point. C also adds the 2013 defaults table, whose message ("defaults are weak") fits in one sentence (E, F).
- **Repeated examples.** C narrates the withdraw race, then H4 in notation, then Hermitage SQL, then a six-order widget: four presentations of one lost update. A and E use two.
- **Closing recaps.** B's and C's final paragraphs restate "check your version's tested behavior," already made in the naming section. E ends with an actionable three-part rule instead: "put each read-decide-write sequence in one transaction, learn what your database's level actually means, and use Serializable with retries, or explicit locks, where a rule spans rows."

## Process signals visible in the reports

All six share the same source set, licence-note style, and caveat phrasing, such as "can show an anomaly but not prove its absence" and "one measured example, not a general rule." This suggests a common research packet and template. B, C, E, and F have audit-style source cards that discuss trust, for example "The Jepsen report was read only in summary, so wording here follows the release notes." That is research-process disclosure. It costs reader time for little gain.
