---
name: edit
description: 'Load when the user says "edit this article", "edit this passage", "clean up this paragraph", "proofread this text", or asks to edit writing for grammar, spelling, and clarity while preserving voice and meaning.'
---

# Edit Skill

Edit prose directly inline for grammar, spelling, and clarity while strictly preserving the author's voice, tone, and technical meaning.

This skill works across any scope, including a single paragraph, an excerpt, or a full article. Edits are applied directly inline, accompanied by a concise report detailing exactly what was changed and why in short bullets.

## 1. Establish the Editing Scope

1. Read the complete target passage or document before making modifications.
2. Determine whether the input is a local file path, a markdown document, or an inline passage.
3. Establish preservation boundaries. Maintain the author's voice, direct tone, rhythm, technical claims, arguments, code snippets, identifiers, and markdown structure.
4. Consult [references/editing-rubric.md](references/editing-rubric.md) to review voice preservation rules and editing standards.

Criterion. Target text and preservation boundaries are clear before modifying content.

## 2. Apply Conservative Inline Edits

1. Edit the text directly inline for spelling, typos, punctuation, grammatical slips, and accidental syntactic ambiguity.
2. For file inputs, edit the file directly in place using available file editing tools.
3. For inline text or passages, output the complete edited text directly in the response.
4. Never alter the author's underlying arguments, opinions, technical conclusions, or vocabulary.
5. Do not inject synthetic transitions, academic hedging, introductory filler, or generic smoothing.
6. Preserve all exact literals, including code blocks, CLI commands, package names, and API signatures.

Criterion. All corrections are applied directly inline without modifying voice or meaning.

## 3. Generate the Change Report

After applying the inline edits, compile a concise report in short bullets detailing each modification.

1. State the exact location or original text snippet.
2. State what was changed.
3. Provide the concrete grammatical or clarity reason why the edit was made.
4. If an ambiguity or technical contradiction exists that cannot be resolved safely without guessing author intent, flag it under Author Decisions for the author to review.

Criterion. Every inline change is accounted for in a short, bulleted change report.

## 4. Formatting and Proof Gates

Enforce strict formatting constraints across all report text and edited prose.

* Zero colons rule. Never use a colon anywhere in headings, bullet labels, or prose notes. Colons are permissible only inside verified markdown link protocol prefixes like https.
* Zero parentheses rule. Never use parentheses in prose notes or explanations. Rewrite sentences smoothly with commas or periods. Parentheses are strictly reserved for markdown link syntax.
* Zero em dashes. Use commas, periods, or hyphens instead.
* Zero buzzwords. Eliminate words like game-changing, delve, tapestry, landscape, revolutionize, crucial, and foster.
* Zero metaphors. Describe systems using literal technical terminology.

## Hard Exit

Verify each condition before concluding.
* The edits are made directly inline in the target file or returned in the conversation.
* The author's voice, tone, and technical meaning remain intact.
* Every modification is recorded in the change report with what changed and why in short bullets.
* The output contains zero colons outside https links, zero parentheses in prose notes, and zero em dashes.
