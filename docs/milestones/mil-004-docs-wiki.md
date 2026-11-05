# Docs and Wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [SA-001], [MIL-002], [MIL-003] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the project can be published: the README is complete with screenshots and the wiki explains, in three languages, what each lecture step taught.

## Deliverable

A merged pull request from branch `mil-004-docs-wiki` with the final `README.md` (screenshot per lecture step), a flat `docs/wiki/` with `Home`, `_Sidebar`, `_Footer` and one page per lecture step in English, Danish (`-da`) and Bahasa Malaysia (`-ms`), the screenshots, and a Doxygen run that succeeds.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every English wiki page has a `-da` and a `-ms` page with the same page set | Equal sets | Any page missing |
| 2 | Every page starts with the language line and `_Sidebar.md` lists the pages once in English and the three languages last | Both true | Either false |
| 3 | The count of screenshots in README equals the count of lecture steps, and each wiki page shows its step's screenshot | Equal | Different |
| 4 | The wiki review against `QC-WIKI-001` has the verdict `Go` | `Go` | Otherwise |
| 5 | `check-readme.sh` passes and every link in README resolves | Exit code 0 | Fails |
| 6 | `doxygen Doxyfile` exits 0 with no warning about an undocumented public item | Exit code 0 | Warning or error |
| 7 | No token, form link or personal data appears in any screenshot | None | Any |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Screenshots of the scraping steps |
| [MIL-003] | Screenshots of the form steps |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3, O4 | [BC-001] |
| Success criteria 6, 7, 8 | [BC-001] |
| Concerns CN-004, CN-005, CN-006 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-19 — the last day of the Business Case window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | List the lecture steps and what each taught | Using the two open Udemy lectures and the assignment text, write the step list (set up the form, scrape, clean, fill the form, build the sheet) and one paragraph per step on what skill it trained. This list is the page set of the wiki. | No | |
| 2 | Collect the screenshot for each lecture step | Gather the screenshots from MIL-002 and MIL-003 under `docs/images/`, and check they show only the participant's own work. | No | |
| 3 | Write the English wiki | Write `Home.md`, `_Sidebar.md`, `_Footer.md` and one page per step, flat in `docs/wiki/`, with the language line and the screenshot. | No | |
| 4 | Write the Danish wiki | Translate every page to `-da` files, keeping code, commands and file names in English. | No | |
| 5 | Write the Bahasa Malaysia wiki | Translate every page to `-ms` files, keeping code, commands and file names in English. | No | |
| 6 | Finish the README with screenshots | Add the screenshot of each lecture step to `README.md` and link the wiki in all three languages. | No | |
| 7 | Review the wiki | Review the wiki against `QC-WIKI-001`, and the README with `check-readme.sh`, and record the `RC-*`. | No | |
| 8 | Run Doxygen and fix warnings | Run `doxygen Doxyfile` and add any missing Doxygen comment, so the generated documentation is complete. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-002]: ./mil-002-scraper.md
[MIL-003]: ./mil-003-form-filler.md
