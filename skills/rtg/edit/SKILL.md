---
name: edit
description: 'Load when the user says "edit this article", "review this draft", "proofread this document", or asks for a grammar, spelling, and clarity review of prose without changing its voice or content.'
metadata:
  opencode/slash: "true"
---

# Edit

Review prose rigorously; revise conservatively. Default to two phases: diagnose first, then apply only after the user has seen and explicitly approved the proposed edits.

## 1. Fix the editing contract

Read the complete source before commenting. Preserve its meaning, claims, examples, organization, voice, tone, audience, technical detail, and formatting. Follow the document's existing conventions unless the user supplies a style guide.

Review grammar, spelling, punctuation, usage, consistency, ambiguity, referents, sentence logic, and readability. In technical writing, also inspect terminology, definitions, units, identifiers, internal contradictions, and whether instructions can be followed as written.

Unless requested, do not fact-check, alter arguments, rewrite for another audience, or edit quoted material, citations, code, commands, API names, or other exact literals.

Criterion: the source and preservation boundaries are clear. Ask only when missing context makes a reliable review impossible.

## 2. Diagnose—do not edit

Return findings before changing the source. Be exhaustive about concrete problems, but do not manufacture criticism or substitute personal style preferences.

Use this structure:

### Necessary edits

Number findings in document order. For each, give:

- location or a short unique excerpt;
- the problem and why it impairs correctness or understanding;
- the smallest replacement that fixes it.

Group repeated mechanical issues only when every affected location remains identifiable. If none exist, say so plainly.

### Author decisions

List ambiguities, apparent contradictions, unsupported transitions, or technical questions that deserve attention but have no safe correction without changing meaning, voice, or content. Explain the risk; do not invent a fix. Omit this section when empty.

End by asking: **“Apply all necessary edits, or tell me which item numbers to apply or skip?”** The initial request to edit is not approval: the user must first see the findings. Do not mutate a file or return a silently revised document in this phase.

## 3. Resolve approval

Treat “yes,” “apply,” or equivalent confirmation as approval for all **Necessary edits** only. Apply a subset when the user names item numbers. Author decisions require specific author direction; never fold them into a general approval.

If the user changes a proposed replacement, use that wording. If approval is ambiguous, ask one narrow question before editing.

Criterion: every planned change maps to an approved finding or explicit author instruction.

## 4. Apply minimally

Make only the approved replacements. Preserve surrounding wording and document structure. Do not opportunistically polish adjacent prose. If edits interact, use the smallest combined correction and disclose the interaction.

For a source file, edit that file in place unless the user requests another output. For pasted prose, return the complete revised prose. Never overwrite a file merely because pasted text resembles its contents.

## 5. Verify and report

Compare the revision against the original. Confirm:

- every change maps to an approved item;
- each approved problem is resolved;
- meaning, voice, tone, claims, numbers, citations, literals, and formatting remain unchanged except where explicitly approved;
- no unapproved edit slipped in.

For file edits, inspect the resulting diff. Hard exit: without post-review confirmation, produce findings only.

Return the revised artifact, applied item numbers, skipped items, and unresolved author decisions. Keep the report brief.

## Gotchas

- A large critique does not justify a large rewrite. Findings may be extensive; edits remain minimal.
- “Make it clearer” does not authorize simplification, added explanation, reordered ideas, or a new voice.
- Unfamiliar technical terms are not misspellings. Correct them only from document evidence or author confirmation.
- A technically questionable claim is an author decision unless fact-checking was requested.
- A document's suggestion/track-changes mode, or returning an already rewritten preview, does not bypass approval.
