# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [6bd0143] |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Add RC-010 for MIL-003 code | pending |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's cross-artifact traceability success criterion is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-003] |
| [MIL-001] | MIL | en | it | [PP-001] | - | [RC-004], [RC-008] |
| [MIL-002] | MIL | en | it | [PP-001], [MIL-001] | - | [RC-005], [RC-009] |
| [MIL-003] | MIL | en | it | [PP-001], [MIL-002] | - | [RC-006], [RC-010] |
| [MIL-004] | MIL | en | it | [PP-001], [MIL-002], [MIL-003] | - | [RC-007] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [PP-001], [MIL-001] | - | - | Planned |
| CN-002 | [MIL-002], [MIL-003] | - | - | Planned |
| CN-003 | [MIL-001], [MIL-003] | - | - | Planned |
| CN-004 | [MIL-002] | - | - | Planned |
| CN-005 | [MIL-001], [MIL-004] | - | - | Planned |
| CN-006 | [MIL-004] | - | - | Planned |
| CN-007 | [MIL-001] | - | - | Planned |
| CN-008 | [MIL-001] | - | - | Planned |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None found | - | Closed | - |

## Coverage Notes

- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet.
- Code is traced through its milestone: RC-008 reviews the code of MIL-001, RC-009 that of MIL-002 and RC-010 that of MIL-003.
- No `AD`, `TP`, `ADR` or view exists yet; concerns are `Planned` until a milestone answers them.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-scraper.md
[MIL-003]: ../milestones/mil-003-form-filler.md
[MIL-004]: ../milestones/mil-004-docs-wiki.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-foundation.md
[RC-005]: ./reviews/rc-005-mil-002-scraper.md
[RC-006]: ./reviews/rc-006-mil-003-form-filler.md
[RC-007]: ./reviews/rc-007-mil-004-docs-wiki.md
[RC-008]: ./reviews/rc-008-mil-001-code.md
[RC-009]: ./reviews/rc-009-mil-002-code.md
[RC-010]: ./reviews/rc-010-mil-003-code.md
[6bd0143]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/commit/6bd0143f176299bca7c599c1cae0818f20eefcde
