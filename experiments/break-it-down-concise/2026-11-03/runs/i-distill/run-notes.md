# Run notes

Elapsed: about 25 minutes of writing and checking (system clock read 11:07 at start, 11:16 at the final check; that clock looked unreliable, so the 25-minute estimate is from turn count).

## Decisions

- Started at step 3 with the frozen packet in `research/isolation`. No new sources were searched or opened.
- Primary worked example: the lost-update deposits (E1, E13), followed by the ACIDRain withdraw figure (E17). Secondary: the doctors write-skew figure (E8).
- One interaction: a two-transaction stepper with a level selector (PostgreSQL Read Committed vs Repeatable Read). The reader controls the interleaving. The visible result is the final balance, a wait, or a serialization error with retry. What it adds is that the stronger level refuses the bad interleaving rather than fixing it, and that the serial orders are unaffected. Behavior follows PG 18 §13.2.1–13.2.2 and Hermitage postgres.md (E13). A noscript fallback and the static table carry the same result.
- Hermitage table excerpt rebuilt as HTML from tables.md values (CC BY 4.0). The draft has P4, G-single, and G2-item; the final keeps only P4 and G2-item.
- The final version uses Sora, Inter, and the light palette. Tables and wide figures sit in keyboard-focusable scroll regions.

## Draft vs distilled

- `draft.html` was saved after its checks. It runs about 4,180 words including the audit, with 9 exhibits (E3, E4, E8, E9, E14, E15, E16, E17, E18), plus quotes and a mytab example.
- `report.html` is the distilled version at about 2,130 words (51%). Cuts and merges:
  - The two "correct" sections merged into one.
  - Dropped the anomaly glossary table. Its definitions moved inline where the reader needs them.
  - Dropped the read-skew transfer example, Table 1, PostgreSQL Table 13.1, the locks/snapshots tiles (now one paragraph), the mytab example, the HAT table (now one sentence), Fig. 5 (kept Fig. 6 and the 7% figure), and the ACIDRain Table 2 (now numbers in text).
  - Shortened audit entries to 1–2 sentences each.
  - Kept C2–C4, C6–C8, C10–C11, C13, C15, and C17 with their caveats.
- Two fixes in the draft before saving it:
  - "which is why these bugs rarely appear in testing" became the "silent data corruption" quote from E20.
  - Removed "names appear in error messages".
- Two fixes in the distilled version:
  - "Each row down forbids more" became "generally". Table 4 is not monotone: Snapshot allows write skew where Repeatable Read does not.
  - The locking write-skew prevention sentence no longer says the second writer simply waits. Both writers block, and one must wait or be cancelled.

## Verification (Python Playwright, Chromium headless)

- Fonts, after `document.fonts.ready`: `document.fonts.check('600 1em Sora')` and `document.fonts.check('400 1em Inter')` both returned true at 1280 and 390, on both the draft and the final. Fonts load from Google Fonts, so a network connection is needed.
- Layout: document scrollWidth equals the viewport at 1280 and 390, and no element overflows outside a scroll region. The draft at first overflowed at 390 (scrollWidth 521, from the Hermitage table). I fixed that by wrapping the tables in scroll regions and rechecked.
- Images: every image loaded (complete and naturalWidth > 0), and none is upscaled; display widths are below natural widths. On mobile, Table 4 scrolls horizontally at 640px, and a full-size link was added for it and for the doctors figure.
- Console: no errors on either page.
- Interaction:
  - The default state reads 100 with no verdict.
  - At RC, the bad order ends at 130 with the lost-update verdict.
  - At RR, the bad order makes B abort and the balance read 120; retrying B ends at 150.
  - The blocking path at RC (B writes while A is uncommitted) leaves B waiting with its button disabled. After A commits, B overwrites, and the end is 130.
  - The same blocking path at RR aborts B.
  - The serial order at RR ends at 150.
  - Reset returns to the default.
  - Keyboard: Enter on a focused button steps the transaction, Tab moves to the next control, and the focus outline is visible in the screenshot.
  - With JavaScript disabled, the page renders the noscript text and the static table.
  - The log and verdict are aria-live regions.
- Claims check: I checked each factual sentence against audit-records.md and evidence-records.md. Every claim used has a pass or conditional record. C12's cross-vendor figure is framed as January 2013. The C14 numbers are framed as one PostgreSQL 9.1 study. Oracle is described only "by these tests". Jepsen is not quoted verbatim.
- Not performed:
  - No screen-reader test.
  - No dark mode, since it wasn't requested.
  - The fonts are not embedded for offline use.

## Gaps carried from the packet

- No current Oracle documentation was read.
- Adya 2000 was inaccessible.
- The Jepsen report was read only through a summary.
- The cost evidence is a single study (C14).
