# Review of MIL-003 code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f5e0653] |

---

## Artifact Under Review

- Instance reviewed: [MIL-003] (the code of its tasks: tasks 2 to 5: form filler, CLI, unit tests, container setup, and the readiness fix found in task 6)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules snake_case, classes `FillForm`, `SeleniumFormSubmitter`, `FormError`; constants UPPER_SNAKE in `constants.py`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`FillForm.execute`, `SeleniumFormSubmitter.submit`, `create_chrome_driver`); the CLI flags are `--scrape-only`, `--headless`, `--screenshot-dir`. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` and `ruff format --check src tests` pass, no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function and method in src and tests is annotated, `-> None` included (mypy --strict passes on 27 source files). |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `SeleniumFormSubmitter.submit` catches `WebDriverException` and raises `FormError ... from err`; the CLI maps `ScrapeError` and `FormError` to exit code 1; no bare except; a test checks `__cause__`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | The CLI quits the driver in a `finally` block, so the browser closes on success and on error; a CLI test checks it. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a docstring and Doxygen `##` block; `doxygen Doxyfile` prints no warning. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | The form link is read from the environment variable `FORM_URL` and never logged or stored in the repository; exit code 2 when it is missing; the log holds only the count of submitted responses. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | N-A: the project has no DCD; the tasks are technical (see PP-001 Planning Assumptions); the classes follow the pull request description. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 37 unit and integration tests pass without network or browser (`pytest -m 'not e2e'`), using a fake driver; the end-to-end test against a local mock form passed in Docker. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src` reports no issues in 27 source files; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Runtime dependencies are `requests`, `beautifulsoup4` and `selenium`, all imported; `pillow` was used only outside the project to crop a screenshot. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Locators, timeouts and window size are defined once in `constants.py`; the readiness check `_inputs_ready` exists once; the real Google Form needed `?hl=en` and a wait for displayed inputs, both found by running it and documented in README. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports nothing from application or infrastructure; application depends on the `FormSubmitter` port; selenium is imported only in infrastructure; the CLI is the composition root; no cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | The use case `FillForm` has one reason to change and the submitter is replaceable through the `FormSubmitter` port (open/closed, dependency inversion). |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers and folders match the clean-architecture wireframe; presentation holds `cli.py` and `__main__.py`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names English, no spaces; Docker files live in `docker/`. |

## Overall Verdict

Go — every Mandatory criterion passes or is N-A with a reason. The review is not independent: the code was written by the `python-developer` agent and reviewed by the AI acting as stand-in for S01.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-003]: ../../milestones/mil-003-form-filler.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[f5e0653]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/commit/f5e0653de014dd4c826ad56f797eb7326f1faf19
