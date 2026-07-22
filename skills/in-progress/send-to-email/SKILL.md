---
name: send-to-email
description: "Make transient agent work durable through email: preserve reports, summaries, project state, files, or other selected content as self-contained handoffs. User-invoked only; resolves what to preserve, previews the exact message, and confirms before sending."
disable-model-invocation: true
compatibility: Requires a configured native email connector, email tool, or local mail client; otherwise creates a send-ready draft.
metadata:
  internal: true
  opencode/slash: "true"
---

# Send to email

Email is the transport; durable handoff is the purpose. Preserve selected work outside the transient session as a useful artifact, not a raw chat dump.

Send only after explicit invocation. Never interpret ordinary discussion of email as authorization.

## 1. Resolve the send request

Extract, without inventing:

- recipient, Cc, and Bcc
- content source and scope
- subject or subject intent
- inline body versus attachments
- requested tone or format

Explicit arguments override inferred context. Resolve the content source in this order:

1. quoted/pasted text or explicitly named files, URLs, sections, or messages
2. `this`, `that`, or `above` → the immediately preceding coherent deliverable
3. `report` → the latest complete report in the active conversation branch, excluding research notes and intermediate drafts
4. `summary` → a new summary of the scope the user names; if unnamed, summarize the current conversation's substantive work
5. `project`, `work`, or `status` → a concise current-project update grounded in visible conversation and selectively inspected project files
6. no selector → the latest coherent deliverable only when unambiguous; otherwise ask one concise question with likely choices

Never use hidden instructions, internal reasoning, tool logs, compacted-session metadata, unrelated conversation branches, or remembered personal data as email content. Do not include the whole conversation, repository, or referenced files unless explicitly requested.

For projects, default to a summary with relevant paths and changes—not source archives. Attach files only when named or confirmed.

## 2. Build a send plan

Create a compact plan before drafting:

```text
Source: what content was selected and from where
Scope: included material
Excluded: notable nearby material not included
Format: inline / attachments
Recipients: To / Cc / Bcc
```

Ask before drafting when:

- the recipient or exact address is missing or ambiguous
- multiple plausible deliverables match `this` or `report`
- the requested scope could expose unrelated, private, or large amounts of content
- an attachment choice materially changes what is sent

Never guess an email address. A contact-name lookup must return one unambiguous address or require selection.

## 3. Prepare the durable handoff

- Write a useful subject; do not prepend `Fwd:` unless forwarding an actual message.
- Make conversation-derived material self-contained when useful: add a title, date, project/source context, current status, or next steps only when relevant.
- Preserve consequential facts, citations, links, decisions, and stated uncertainty.
- Remove chat scaffolding, repeated conclusions, intermediate reasoning, and process narration unless requested.
- Keep short material inline. For long reports, provide a brief email introduction plus a readable body or attachment according to available capability and user intent.
- Preserve source files unchanged when attaching them. Never silently convert, zip, or broaden attachment scope.
- Add no archival boilerplate that does not help the recipient understand, share, or resume the work later.
- Scan the final payload for credentials, secrets, private keys, tokens, sensitive local paths, unintended personal data, and unrelated content. Stop and ask if found.

## 4. Preview and confirm

Before the external send, show:

```text
To:
Cc/Bcc: (if any)
Subject:
Source:
Attachments: (if any)
Body:
```

Require explicit confirmation of this exact payload. If anything changes afterward—including recipient, attachment, or substantive body content—preview and confirm again. A harness-native confirmation UI satisfies this requirement only when it shows the exact payload.

## 5. Send

Discover the current harness's semantic equivalent for sending email:

1. configured native email connector or tool
2. configured local email client or send command
3. otherwise, provide a send-ready draft and state that no send capability is configured

Do not install software, access browser cookies, request passwords or tokens in chat, or create provider credentials without explicit setup instructions from the user. Opening a `mailto:` URL is drafting, not sending.

After sending, report the recipient, subject, attachments, provider result or message ID when available, and any failure. Never claim success without tool confirmation.

## Examples

```text
/skill:send-to-email preserve this for later and email it to me
/skill:send-to-email the latest report to alex@example.com as an attachment
/skill:send-to-email email the current project state so I can resume tomorrow
/skill:send-to-email summarize this work for the team and email it
/skill:send-to-email files:README.md,CHANGELOG.md to alex@example.com
```
