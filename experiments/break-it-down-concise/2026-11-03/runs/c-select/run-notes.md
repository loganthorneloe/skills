# Run notes

Elapsed: about 20 minutes of work; system clock read 11:09 to 11:16 CST, 2026-11-03.

## Inputs followed

- Skill files read directly from `variants/select/` (break-it-down, voice, source-audit for the reader-facing entry rules, find-evidence for exhibit handling). Skill tool not used.
- Research packet `research/causal` used as the audit and evidence records. No new sources searched or opened.

## Decisions

- Claim ranking: C1, C2, C4, C7 get full mechanism; C6 and C9 carry the main evidence; C3, C5, C8, C10, C11 are a paragraph or a table each.
- Exhibits embedded (copied to `assets/`): E1 Hernán & Robins Fig 1.1; E9 LaLonde Table 5; E8 Mindspark Fig 2 (captioned render, 1356 px, so the note is legible); E6 IES Table II.6. E14, E4, E7, E13, E15, E12 used as quotes/metrics in prose. E2/E3 Mixtape tables, E5 IES balance, E10/E11 World Bank tables not embedded; their numbers appear in prose where needed, to keep length proportional.
- Rights: Hernán figure is "all rights reserved"; embedded with attribution and a caption note on rights, for commentary. LaLonde and Mindspark figures have unstated reuse rights; embedded with attribution and "reuse rights unstated" in captions. IES public domain; World Bank CC BY 3.0 IGO (credited in the synthesis-table caption).
- One worked example (six-student table from background/E16, labeled constructed) carried through; Mixtape sign reversal and Hernán 54% vs 43% stated in a sentence each.
- One interaction: a seeded simulation (constructed, labeled) with assignment mode, true effect (0–10), and sample size (40/400/4,000). Gap it closes: the six-student example cannot show that selection bias does not shrink with more data while coin-flip chance error does. Static default values are written into the HTML, matching the JS default run (seed 1), so the no-JS state is readable.
- Synthesis table of quasi-experimental designs, labeled as a restatement of World Bank Table 11.2.
- Mindspark figures: published AER values (0.37/0.23) used for effects; the figure itself is from the 2017 working paper, stated in its caption and source entry.

## Verification

- Voice pass: removed colon-label phrasing, checked definitions precede use (counterfactual, association, selection bias, p-value, standard deviation, intent-to-treat concept described without the term), cut recap. Report ends on implications and limits.
- Fact check against records: fixed four overstatements during review (IES balance description, Mixtape quote wording, Mindspark attrition handling now says only "reweighting and bounding checks", CI wording). Every claim C1–C11 maps to a pass or conditional record; C5 reverse causation stated as settled reasoning (gap noted in audit), C10 spillover stated by definition only.
- Rendering (Playwright Chromium, headless): 1280 px and 390 px full-page screenshots inspected. No horizontal page overflow at either width (scrollWidth equals clientWidth). All 4 images load; none displayed above natural size. LaLonde table sits in a keyboard-focusable horizontal scroll region at 390 px with a full-size link; worked-example and design tables scroll inside their regions. Mobile control text clipping found and fixed by stacking controls.
- Fonts: after `document.fonts.ready`, `document.fonts.check('600 1em Sora')`, `('400 1em Inter')`, `('500 1em Inter')` all true at both widths. Fonts load from Google Fonts, so offline viewing falls back to system sans-serif.
- Console: no errors or page errors.
- Controls: default (choose, 2 pts, 400: gap 10.9 = 2.0 + 8.9), changed (coin flip 400: gap 0.9; coin 40 reruns: 5.9, 0.7, 5.3, 2.4, 0.9; coin 4,000: 2.1, bias 0.1; choose 4,000: bias 9.8), boundaries (effect 0: gap equals bias 9.8; effect 10: 19.8), reset returns to default exactly. Keyboard: ArrowRight/Home on the slider, Enter on the button, Tab order works; red focus outline styled. Results region is `aria-live="polite"`. JS disabled: static default values and a noscript note render.

## Gaps

- No source tests a self-study phone app; report says so.
- Reverse causation has no education source; stated as reasoning.
- Hernán figure embedded under an "all rights reserved" notice; a publisher would need to confirm fair use or switch to a link.
- Shared scratchpad was also used by other processes; verification was rerun from an isolated subfolder to make sure results came from this report.
