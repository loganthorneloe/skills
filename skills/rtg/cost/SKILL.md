---
name: cost
description: 'Load when the user says "/cost", "show session cost", "how much did this session cost?", or asks for current-session token usage.'
metadata:
  opencode/slash: "true"
---

# Session cost

Report token usage and cost from the active harness transcript. Use recorded usage/cost fields; never substitute fabricated defaults.

## Workflow

1. Resolve this skill's directory.
2. Run:

   ```bash
   python3 <cost-skill-dir>/scripts/cost.py
   ```

3. Return the script output without re-estimating it.

Hard exit: output names the source transcript and whether cost is recorded or unavailable. A missing/unreadable transcript is **blocked**, not a reason to print placeholder usage.

## Gotchas

- Transcript schemas differ; the script discovers common harness locations and parses explicit usage objects.
- Subscription-backed harnesses may record tokens but no billable API cost. Report cost unavailable rather than `$0`.
- Cache and reasoning tokens remain separate when the transcript records them.
- “A plausible fallback is better than none” is false here; unsupported numbers look authoritative. Block instead.
