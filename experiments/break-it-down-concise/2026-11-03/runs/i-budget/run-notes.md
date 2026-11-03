# Run notes

Elapsed: about 4 minutes by the system clock (11:07 to 11:11 CST, 2026-11-03), steps 3–6 only; research was supplied.

## Decisions

- Reading-text budget about 1,000–1,200 words. Final count about 1,225 words (prose, headings, source entries, inline code; excludes metadata lines, figure captions, the code block, alt text). Slightly over the "about" target; trimmed twice from 1,325.
- Sources shown: 5 of 8 passing/conditional records (Berenson 1995, PostgreSQL 18 docs, Ports & Grittner 2012, Hermitage, ACIDRain). Dropped MySQL 8.4 manual, HAT 2013 survey, and Jepsen/12.4 release notes to fit the budget. MySQL's default and lost-update behavior are stated via Hermitage (★ default marker, P4 column); C12's 2013 cross-vendor survey and C17's PostgreSQL 2020 bug are therefore not in the report. C17 survives only as the general limit that implementations can be wrong and tests cannot prove absence (Hermitage caveat).
- Exhibits embedded: E17 (ACIDRain Fig. 1), E1 (Berenson H4, quoted in prose), E13 (Hermitage lost-update script, verbatim), E4 (Berenson Table 4), E8 (Ports & Grittner Fig. 1), E7 serializable definition quote, E9 retry quote, E14/E15 metrics in prose, E18 counts in prose. Not embedded: E2, E3, E5, E6, E10, E11, E12 table, E16, E19, E20, PostgreSQL Table 13.1 (budget; Table 4 carries the ladder).
- No generated visual or interaction: the source figures and the runnable SQL script cover each comprehension step; an interleaving stepper would restate them.
- Vocabulary: Berenson names (lost update, write skew, phantom), with Hermitage results described in those terms (P4 = lost update).
- Rights stated in each caption; ACIDRain and Ports & Grittner reuse beyond personal/classroom use is unstated and said so.

## Fact checks against records

- H4 arithmetic (+30 and +20 from 100; interleaved 130; serial 150) per E1.
- Hermitage script copied verbatim from E13 (an early draft added "sees 10" comments; removed).
- Single-statement UPDATE not losing updates at PostgreSQL Read Committed per E9 limits.
- "Under 7%" and "under half" (RUBiS 208/435 ≈ 0.48; DBT-2++ ~0.43x) per E14/E15, framed as one 2012 study.
- 22 vulnerabilities, 5 level-based, 17 scope-based per E18.
- "Repeatable Read" in Table 4 discussion flagged as the paper's locking definition.

## Verification (Playwright, Chromium)

- 1280px and 390px full-page screenshots inspected. No horizontal page overflow (scrollWidth = clientWidth at both widths). No console errors.
- All 3 images loaded; none upscaled (natural 1059/2218/1043 px; shown 520/892/600 at 1280, 350/720/350 at 390).
- Table 4 sits in a keyboard-focusable horizontal scroll region at 390px (760 vs 390 px) with a full-size link; ACIDRain figure also has a full-size link.
- After document.fonts.ready: fonts.check('600 1em Sora') = true, fonts.check('400 1em Inter') = true at both widths (fonts loaded from Google Fonts; network dependency).
- Code block scrolls horizontally on mobile rather than clipping.
- No controls, so step 6.4 not applicable.
- Voice pass: checked colon-label phrasing (none), analogies (none), term order (transaction, invariant, serializable defined before use; snapshot isolation defined at first use in the ladder section).

## Gaps

- Oracle behavior rests on Hermitage tests of older versions; stated as "Hermitage found".
- Cost figures from one 2012 study only.
