---
name: skill-sessions
description: "Discover harness session/transcript stores and skills roots; ingest recent trajectories into normalized events. Use when any skill-evolution step needs session evidence, or user asks where agent history lives."
metadata:
  internal: true
  opencode/slash: "true"
---

# Skill sessions

Shared ingest. Output evidence; don't patch skills.

1. Name harness
2. Find sessions (native stores). Stuck → [references/harness-discovery.md](references/harness-discovery.md)
3. Find skills roots: project `skills/`, `.agents/skills`, harness project + global
4. Read recent (last 20 or since `.scratch/skill-evolution/LAST_RUN`)
5. Normalize: `{session_id, ts, skill?, role, text_or_tool, correction?, retry?, abort?}`
6. Segment by skill (SKILL.md read, `/name`, named invoke)
7. Redact secrets/PII from quotes

**Out:** harness, paths, skills roots, counts per skill. Huge notes → `.scratch/skill-evolution/ingest-*.md`

Unknown harness → ask once for session dir.
