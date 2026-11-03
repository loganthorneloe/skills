# Run notes

Elapsed: about 8 minutes by system clock (12:37 to 12:45 CST, 2026-11-03).

## Decisions
- Eight claims (C1-C8) in records/audit.md; ranked lag mechanism (C5-C7) and demand-to-prices step (C3) highest.
- One worked example carried through: rate rise 3% to 4%, a $300,000 variable-rate mortgage, and a furniture maker.
- No generated visual or interaction: the Bank of England diagram and Charts 1-2 plus the meta-analysis figures already cover the mechanism and timing; an interactive would restate them.
- Distilled draft (2,532 words) to report (1,386 words, ~55%). Kept all five figures. Removed bold run-in paragraph labels from the draft, unsourced claims (annual wage renegotiation, US 30-year fixed mortgage share, central banks "often pause"), and repeated quotes.

## Sources read
- Bank of England 1999, The transmission mechanism of monetary policy (full PDF).
- Federal Reserve FAQ, How does the Federal Reserve affect inflation and employment? (full page, updated July 2024).
- Havránek & Rusnák, Transmission Lags of Monetary Policy (CNB WP 10/2012 read partially; key numbers cross-checked in IJCB 2013 published PDF; erratum search found none).
- Nakamura & Steinsson 2008, Five Facts about Prices (author copy; abstract and introduction).

## Verification
- Quotations checked verbatim against extracted PDF/page text.
- Every report claim maps to a pass or conditional record; C5 model timing stated as illustrative; C6 price-stickiness link conditional (theory).
- Playwright render at 1280 and 390 px: all 5 images load; no page-level horizontal overflow (scrollWidth equals viewport); wide figures scroll inside focusable regions at 390 px; document.fonts.check for 600 Sora and 400 Inter both true after fonts.ready (fonts loaded from Google Fonts over network). Screenshots inspected; no clipping.
- No controls to operate.

## Gaps
- No post-2010 direct lag estimate; currentness handled by noting lags shift with fixed-rate borrowing and repricing frequency.
- Figure reuse rights unstated for Bank of England and CNB figures; embedded with attribution, stated in captions.
- Report depends on network for fonts.
