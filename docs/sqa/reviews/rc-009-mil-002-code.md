# Review of MIL-002 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [dc74332] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002] (the code of its tasks: tasks 3 to 6)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules snake_case, classes `Listing`, `ScrapeListings`, `RequestsPageFetcher`, `BeautifulSoupListingParser`, `ScrapeError`; constants UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose and keep the assignment's names (`get_links`, `get_addresses`, `get_prices`, `all_links`, `all_addresses`, `all_prices`). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` and `ruff format --check src tests` pass, no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function and method in src and tests is annotated, `-> None` included (mypy --strict passes). |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `RequestsPageFetcher.fetch` catches `requests.RequestException` and raises `ScrapeError ... from err`; no bare except; test checks `__cause__`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults (`header=None` copied from `REQUEST_HEADERS`); no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | N-A: the source opens no file, lock or connection itself; `requests.get` is a single call. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a docstring and Doxygen `##` block; `doxygen Doxyfile` prints no warning. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | N-A: no logging in this milestone; nothing secret or personal is logged or stored. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | N-A: the project has no DCD; the tasks are technical (see PP-001 Planning Assumptions); the classes follow the design in the pull request description. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 23 tests pass without network; names state behaviour, for example `test_clean_price_when_multi_property_text`. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src` reports no issues in 20 source files; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | requests and beautifulsoup4 are used; selenium is declared for MIL-003 and not yet imported, accepted because the plan delivers it next. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Selectors, timeout and headers are defined once in constants.py; cleaning rules are defined once in domain/rules. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports nothing from application or infrastructure; application imports only domain; infrastructure imports requests and bs4 and implements the ports; no cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One reason to change per class; the parser and fetcher are replaceable through the `PageFetcher` and `ListingParser` ports (open/closed, dependency inversion). |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers and folders match the clean-architecture wireframe: domain/{entities,errors,rules}, application/{ports,use_cases}, infrastructure. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names English, no spaces; fixture `zillow_clone.html` uses `_`. |

## Overall Verdict

Go — every Mandatory criterion passes or is N-A with a reason. The review is not independent: the code was written by the `python-developer` agent and reviewed by the AI acting as stand-in for S01.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-002]: ../../milestones/mil-002-scraper.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[dc74332]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/commit/dc74332c290ed72d0751d6dd543898db1f4ba5f4
