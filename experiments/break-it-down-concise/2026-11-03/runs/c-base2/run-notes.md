# Run notes

Elapsed: about 8 minutes of wall-clock time (11:10 to 11:18 CST, 2026-11-03). Steps 3–6 only; research packet used as the audit and evidence records; no new sources searched or opened.

## Decisions
- Structure follows the packet's prerequisite order: association → potential outcomes/counterfactual → average effect vs. group gap → selection bias (constructed six-student example, E16) → other routes (reverse causation, before-after, usage correlation) → why controls fail (LaLonde) → randomization (simulator + IES balance) → real trials (IES null, Mindspark gain, Escueta counts) → practical wrinkles → quasi-experiments (World Bank synthesis table) → implications.
- Exhibits embedded (copied to `assets/`): E1, E2, E3, E5, E6, E8 (captioned render), E9. E4, E7, E13, E14, E15 used as metrics/paraphrase; E7 p. xii quote (public domain) used as a blockquote. E12 rebuilt as an HTML synthesis table labeled as such. E10a/E10b/E11 omitted (E12 carries their numbers). E16 presented as an HTML table labeled constructed.
- Rights: E1 (Hernán, all rights reserved) embedded with attribution for commentary and the caption says so; Mixtape, LaLonde, Mindspark rights unstated or publisher-held, embedded with attribution and captions say so. Copyrighted text quoted only once (Hernán, one short sentence); other sources paraphrased.
- One interaction: coin-flip simulator (input: true effect −3..+6, school size 20/100/1,000; output: self-chosen gap vs. coin-flip gaps, strip plot of repeated flips). It addresses why randomization works only on average and why size matters (C7, C8). Population is invented and labeled as such; seeded RNG so the static (no-JS) initial numbers match the scripted initial state.
- Mindspark: published AER headline numbers (0.37/0.23, IV 0.6) cited; figure is from the 2017 working paper and the source entry says so.

## Verification
- Voice pass: removed colon-label phrasing, checked definitions precede use (association, potential outcomes, counterfactual, selection bias, confounder, regression/matching, random assignment, balance, p-value, SD, intent-to-treat). Fixed one misplaced IES quote (replaced a volunteer-schools quote with the usage-correlation quote it was meant to support), softened a paraphrase of Escueta et al., corrected Mindspark attendance wording to "attended 58% of the time on average".
- Claims C1–C11 each map to pass/conditional records; C5 reverse causation stated as settled reasoning (no source record claimed); spillovers stated definitionally.
- Playwright (Python, Chromium) at 1280 and 390 px: Sora 600 and Inter 400 `document.fonts.check` true after `fonts.ready` (loaded from Google Fonts over network); all 7 images load; no image rendered above natural width; no horizontal page overflow at either width (fixed a 15px overflow from the six-student table and an oversized E1 at 390); no console or page errors. Wide tables/figures sit in keyboard-focusable horizontal scroll regions on narrow screens with full-size links.
- Simulator operated: default (+2, 100 students: self-chosen +18.8, first flip +3.9), sizes 20/100/1,000 with 100 flips (typical miss ≈4.7 / 1.9 / 0.6 points, matching the prose), effect min −3 and max +6 via keyboard Home/End, effect 0 (self-chosen +16.6, coin-flip average 0.0), reset (restores default state exactly), keyboard Tab focus with visible outline and Enter activation, aria-live summary updates. No-JS render shows the same initial numbers and summary text; the strip plot is empty without JS (described by the summary text).
- Fixed after inspection: narrow-screen plot labels too small (plot now redraws at container width with sparser ticks; legend moved below axis on narrow screens); dot stacks now rescale instead of clipping when many flips land in one bin.

## Gaps
- Fonts depend on network access to Google Fonts; system sans-serif fallbacks otherwise.
- No randomized evaluation of a consumer self-study phone app in the packet; the report says so.
- Reduced-motion: page has no animation; rule included defensively.
