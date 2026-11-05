# Form Filler

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [SA-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [6bd0143] |

---

## Purpose

Decide whether the data entry half of the Capstone works end to end: one Google Form response per listing, written with Selenium, and a Google Sheet that collects the answers.

## Deliverable

A merged pull request from branch `mil-003-form-filler` with the form filler under `src/`, unit tests with a fake driver, a Dockerfile and script that run Selenium headless in a container, and a Google Form and Sheet filled with all listings. The form link is read from an environment variable and is not stored in the repository.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A Google Form with three short-answer questions (address, price, link) exists; S01 confirmed it in chat | Confirmed | Not confirmed |
| 2 | The unit tests with a fake driver pass on the host without a browser | Exit code 0 | Fails |
| 3 | The end-to-end run in a Docker container (headless Chrome) exits 0 and writes a log and screenshots into a shared folder | Exit code 0 | Fails; the host desktop is never used as a fallback |
| 4 | The Google Sheet row count equals the listing count | Equal | Different |
| 5 | The form link and any token are not in `git ls-files` or in the history of the branch | Not found | Found |
| 6 | The code review against `qc-programming-python` is `Go` | `Go` | Otherwise |
| 7 | Screenshots of the form, the filled form and the sheet exist for the lecture steps | Present | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The form filler needs the three lists |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2 | [BC-001] |
| Success criterion 5 | [BC-001] |
| Concerns CN-002, CN-003 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-14 — inside the Business Case window 2026-11-05 to 2026-11-19.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create the Google Form | S01 creates a form with three short-answer questions (address, price, link) in their own Google account and links a Sheet; the AI asks before it submits anything. The link is kept in the environment variable `FORM_URL`. Needs S01 because it uses their Google sign-in. | No | |
| 2 | Write the form filler | Write a class that fills and submits the form for one listing through an injected Selenium driver, with the field locators in `constants.py`. Dependencies point inward so the driver can be faked. | No | |
| 3 | Write the main program | Wire the scraper and the form filler into one entry point that fills one response per listing. | No | |
| 4 | Write unit tests with a fake driver | Test that the filler enters three values per listing and submits once per listing, without a browser. | No | |
| 5 | Add the Docker setup for the end-to-end run | Add a Dockerfile and a script that run the program with headless Chrome in a Linux container and write a log and screenshots to a shared folder, as `framework/process/gui-testing.md` requires. Environment: Docker container. | No | |
| 6 | Run the end-to-end test in the container | Run the container with `FORM_URL` set from the environment and check that the Sheet row count equals the listing count. Environment: Docker container. The AI asks S01 before the form is submitted. | No | |
| 7 | Review the form filler code | Review `src/` and `tests/` against `qc-programming-python` and record the `RC-*` before the pull request. | No | |
| 8 | Capture the screenshots for the form lecture steps | Capture the empty form, the filled form and the Sheet as images for README and wiki. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-002]: ./mil-002-scraper.md
[6bd0143]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/commit/6bd0143f176299bca7c599c1cae0818f20eefcde
