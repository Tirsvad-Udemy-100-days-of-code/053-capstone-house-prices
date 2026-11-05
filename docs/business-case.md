# Business Case: House Prices Capstone

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [6bd0143] |

---

## Executive Summary

The Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" ends its web scraping block with a Capstone project (Day 53): automate a data entry task. A program scrapes rental listings (price, address, link) from a stable clone of a real-estate site, then fills a Google Form once per listing so that the answers collect in a Google Sheet. This project delivers that Capstone as a small, tested, documented Python 3.13 repository, with a README and a three-language wiki (English, Danish, Bahasa Malaysia) that explains what each lecture step taught and shows a screenshot of it.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/` (Business Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues, then code, each step reviewed). Quality criteria are tagged with ISO/IEC 25010:2023 characteristics. Code follows the Python conventions and the Clean Architecture skill of the framework, with Doxygen comments in the source, `pytest` for tests and a `venv` for the environment.

## Problem Statement

A course participant who finishes the Capstone has working code on a local disk only. Three problems recur:

- The code is not tested, so a change to the scraped page breaks it without warning.
- It is not documented, so other participants cannot run it or compare it with their own solution.
- The learning is not recorded: nobody can see which skill each lecture step trained.

## Business Opportunity

A clean, runnable, documented solution lets S02 compare solutions and lets S03 find ideas. It also trains the participant (S01) in the full delivery chain: plan, code, test, document, review.

## Objectives

- **O1.** Deliver a Python 3.13 program with the function names of the assignment that scrapes all listings from the Zillow clone into three lists: links, prices and addresses.
- **O2.** Deliver a form filler that submits one Google Form response per listing with Selenium.
- **O3.** Deliver a repository that a stranger can run from the README alone: local `.venv`, upgrade of `pip`, tests, run.
- **O4.** Deliver a wiki in English, Danish and Bahasa Malaysia that explains what was gained in each lecture step, with a screenshot per step in the wiki and the README.
- **O5.** Deliver a repository on the git host with a description and topics, work done through branches and pull requests, and no runtime dependency beyond what the assignment needs.

## Scope

### In Scope

- Scraping with `requests` and BeautifulSoup from https://appbrewery.github.io/Zillow-Clone/ : links, prices ("$1,234" form) and addresses (no newlines, pipes or extra whitespace).
- Filling a Google Form with Selenium, one response per listing.
- Project structure `src/`, `tests/`, `docs/`; `pyproject.toml`; `constants.py`; Python `.gitignore`; Doxyfile and Doxygen comments.
- Unit tests with `pytest`, run against a saved copy of the page so that they do not need the network.
- README from the framework template with run and test instructions and a screenshot per lecture step.
- Wiki in English, Danish and Bahasa Malaysia with a screenshot per lecture step.
- Repository description and topics on the git host.

### Out of Scope

- Scraping the real Zillow site.
- Storing the Google Form link, tokens or credentials in the repository.
- A graphical user interface or a web service.
- Running any GUI or browser test on the host desktop (framework rule: container or sandbox only).
- Importing `.env` into the project; it holds personal tokens for the author only.

## Expected Benefits

### Tangible Benefits

- A runnable repository with passing tests and a README.
- A three-language wiki with one screenshot per lecture step.
- A Google Sheet with one row per listing, as the assignment's objective shows.

### Intangible Benefits

- The participant practises the whole delivery chain, not only the code.
- Other participants and visitors find a readable reference solution.

## Strategic Alignment

The project supports the participant's learning goal (finish the 100 Days of Code course with documented, reviewed work) and the framework's goal of showing the plan-first workflow on a small, real project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Listings scraped | All listings of the saved copy of the clone page | A test compares the count of links, prices and addresses; all three are equal and equal the number of listing cards in the saved page |
| 2 | Price format | 100 % of prices match `^\$[\d,]+$` | A test checks every scraped price |
| 3 | Address format | 0 addresses contain a newline or a pipe | A test checks every scraped address |
| 4 | Tests | All `pytest` tests pass on a clean `.venv` | `python -m pytest` exits 0 |
| 5 | Form filling | One form response per listing | The Google Sheet row count equals the listing count |
| 6 | Reproducibility | README steps run from a fresh clone without edits other than the form link | The author runs the steps once on a clean clone |
| 7 | Wiki languages | 3 languages, same page set | The wiki has English, Danish and Bahasa Malaysia pages for every lecture step |
| 8 | Screenshots | 1 screenshot per lecture step in README and wiki | Count of lecture steps equals count of screenshots |
| 9 | Runtime dependencies | At most `requests`, `beautifulsoup4` and `selenium` | `pyproject.toml` `dependencies` list |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The clone page changes | Scraper and tests break | Tests use a saved copy of the page; the live fetch is a thin wrapper |
| Creating and submitting the Google Form needs the author's Google sign-in | The form step cannot be run by the AI alone | The AI asks before it submits; the form link is read from an environment variable, not stored in the repository |
| A browser test on the host desktop takes the author's mouse and keyboard | Disturbs the author | Selenium runs headless in a Docker container; unit tests mock the driver |
| Tokens leak into the repository | Security incident | `.env` is in `.gitignore`, tokens are read only for git host calls, never printed or imported |
| Screenshots of Udemy lectures contain course material | Copyright concern | Screenshots show the participant's own program, form and sheet, not the lecture video |
| Three languages double or triple the writing effort | Schedule slip | One page set, written in English first, then Danish and Bahasa Malaysia; translations reviewed by S01 |

## Assumptions

- S01 is Product Owner, developer and reviewer; an AI stand-in reviews in autonomous mode and the record says it is not independent.
- The Zillow clone page stays online during the project.
- The git host accepts pull requests from branches and exposes a REST API for description and topics.
- Python 3.13 or later is installed (3.13.14 at the time of writing).
- The author can create the Google Form in their own Google account.

## Constraints

- Python 3.13 or later, `venv`, `pytest`, `pyproject.toml`, constants in `constants.py`.
- Folders `src/`, `tests/`, `docs/`.
- Doxygen comments in source and a `Doxyfile`.
- Duration: two weeks, 2026-11-05 to 2026-11-19.
- One pull request per milestone, each from its own branch.
- No commit to `main` directly; no secret in any file under version control.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About 40 hours of AI and author effort, no money | Documented course deliverable that others can reuse |
| Hosting on the existing git host: none | Practice of the plan, test, review and documentation chain |
| Review time of S01 for each artifact | Wiki in three languages that widens the audience |

The assessment is qualitative because the project is a learning project with no revenue; the costs are time only.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants reviewed, documented work (CN-001, CN-002, CN-003) |
| S02 | Wants readable, runnable code and a wiki in their language (CN-004, CN-005, CN-006) |
| S03 | Wants a clear description, topics and no extra dependencies (CN-007, CN-008) |

## Recommendation

Proceed — the scope is small, all risks have a mitigation and the result is useful to all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[6bd0143]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/commit/6bd0143f176299bca7c599c1cae0818f20eefcde
