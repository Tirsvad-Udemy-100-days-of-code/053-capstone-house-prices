# Scraper

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [SA-001], [MIL-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decide whether the scraping half of the Capstone is correct and tested: all listings of the clone page become three clean lists (links, prices, addresses).

## Deliverable

A merged pull request from branch `mil-002-scraper` with the scraper under `src/`, a saved copy of the clone page as a test fixture, and unit tests. A run against the saved page returns three lists of equal length with clean values.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The count of links, prices and addresses is equal and equals the number of listing cards in the saved page | Equal | Any difference |
| 2 | Every price matches `^\$[\d,]+$` (no `+`, no `/mo`, no `bd` text) | All match | Any mismatch |
| 3 | No address contains a newline, a pipe or leading and trailing whitespace | None found | Any found |
| 4 | Every link starts with `http` | All do | Any not |
| 5 | The request sends a `User-Agent` and `Accept-Language` header (hint 1 of the assignment) | Both sent | Missing |
| 6 | `python -m pytest` passes without network access | Exit code 0 | Fails or needs the network |
| 7 | Every public function and class in `src/` has a Doxygen comment and the code review against `qc-programming-python` is `Go` | Both true | Either false |
| 8 | A screenshot of the scrape output exists for the lecture step | File present | Missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | The structure, tooling and constants must exist first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 | [BC-001] |
| Success criteria 1, 2, 3 | [BC-001] |
| Concerns CN-002, CN-004 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 — inside the Business Case window 2026-11-05 to 2026-11-19.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Verify the assignment's function names | Read the solution gists named in the assignment and the two open Udemy lectures, and list the function and variable names the solution uses, so the code uses them (S02 concern CN-004). Record the list in the task's pull request. | No | |
| 2 | Save the clone page as a test fixture | Download https://appbrewery.github.io/Zillow-Clone/ once into `tests/fixtures/` so unit tests never need the network. | No | |
| 3 | Fetch the page with browser headers | Write a function that requests the page with `User-Agent` and `Accept-Language` headers (hint 1), with the URL and headers in `constants.py`. | No | |
| 4 | Scrape links, prices and addresses | Parse the saved HTML with BeautifulSoup into the three lists, one entry per listing card, in page order. | No | |
| 5 | Clean prices and addresses | Strip `+`, `/mo` and `bd` text from prices (hint 3) and newlines, pipes and extra whitespace from addresses (hint 2), as pure functions that are easy to test. | No | |
| 6 | Write unit tests for the scraper | Cover the three lists, equal lengths, price and address formats, and the cleaning functions with the saved page and small hand-made inputs. | No | |
| 7 | Review the scraper code | Review `src/` and `tests/` against `qc-programming-python` and record the `RC-*` before the pull request. | No | |
| 8 | Capture the screenshot for the scraping lecture step | Capture the scrape output (the three lists) as an image for README and wiki. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[MIL-001]: ./mil-001-foundation.md
