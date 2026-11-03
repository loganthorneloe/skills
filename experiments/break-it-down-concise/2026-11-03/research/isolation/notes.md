# Research notes

Started 10:53, finished about 11:08 CST, 2026-11-03 (about 15 minutes elapsed).

## Sources read

| Source | Access route | Read |
|---|---|---|
| Berenson et al., A Critique of ANSI SQL Isolation Levels (SIGMOD 1995 / MSR-TR-95-51) | arXiv cs/0701157 PDF, text extracted with PyMuPDF | full |
| PostgreSQL 18 docs §13.2 Transaction Isolation and §13.1 Introduction | postgresql.org HTML (curl + text conversion); Table 13.1 screenshot via headless Chrome | full |
| MySQL 8.4 Reference Manual §17.7.2.1 | dev.mysql.com HTML | §17.7.2.1 full; linked sections not read |
| Ports & Grittner, Serializable Snapshot Isolation in PostgreSQL (VLDB 2012) | arXiv 1208.4179 PDF | §1–3, §8–9 full; §4–7 skimmed |
| Bailis et al., Highly Available Transactions (VLDB 2014, extended) | arXiv 1302.0309v2 PDF | §1–3 (Table 2) read; rest skimmed/not relevant |
| Warszawski & Bailis, ACIDRain (SIGMOD 2017) | bailis.org author PDF | abstract, §1–2, §4.2.4–4.2.5, Table 2 read; §3, appendices skimmed |
| Kleppmann, Hermitage | raw GitHub README.md, postgres.md (master @ 2026-01-23); GitHub API for commit dates | full (README, postgres.md) |
| Jepsen, PostgreSQL 12.3 (2020) | WebFetch summary only | partial (summary) |
| PostgreSQL 12.4 release notes | postgresql.org HTML | relevant item read |
| PostgreSQL Licence page | WebFetch | for reuse terms |
| ACM Turing Award page (Jim Gray); Jim Melton bio | web search results | for credential checks only |
| Flexcoin closure news coverage (March 2014) | web search results | corroboration only, not a source record |

## Access gaps

- Adya, Liskov, O'Neil, "Generalized Isolation Level Definitions" (ICDE 2000) at pmg.csail.mit.edu: connection refused, so it wasn't read. Its framework is known only through Hermitage and a mailing-list summary.
- hackingdistributed.com write-up on Flexcoin/Poloniex: connection refused.
- Jepsen PostgreSQL 12.3 analysis: read only through the fetch tool's summary, so it can't be quoted verbatim. The PostgreSQL 12.4 release notes are used for exact wording.
- No current Oracle or SQL Server documentation was read. Their behavior rests on Hermitage (older versions) and the 2013 survey.
- The browser pane's viewport was 0×0 while hidden, so the PostgreSQL table screenshot was taken with headless Chrome instead.

## Tooling

- PDFs rendered and cropped with PyMuPDF 1.28 in a temporary venv under the session scratchpad. HTML was converted with a short Python regex script, and crops were made with Pillow.
- Every image in assets/ was opened at full size after cropping. The ACIDRain Table 2 crop was redone to remove a stray line from the text above it.
- The scratchpad was shared with another process: a helper script was overwritten mid-session. I recreated it in a private subfolder, and all assets were checked after that.
