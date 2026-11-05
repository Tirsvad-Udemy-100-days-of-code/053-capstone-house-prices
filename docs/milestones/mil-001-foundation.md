# Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [6bd0143] |

---

## Purpose

Decide whether the project foundation is ready for feature work: the structure, tooling, documentation entry point and the repository's public face are in place, so the next gates only add behaviour.

## Deliverable

A merged pull request from branch `mil-001-foundation` that contains: the `src/` and `tests/` skeleton, `pyproject.toml`, `constants.py`, a Python `.gitignore`, a `Doxyfile`, a README built from the framework template, and a repository on the git host with a description and topics. A passing smoke test proves the toolchain.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python = ">=3.13"`, and the runtime dependencies are only `requests`, `beautifulsoup4` and `selenium` | Yes | Any other runtime dependency |
| 2 | On a fresh clone, the README steps (create `.venv`, `python -m pip install --upgrade pip`, install, `python -m pytest`) run and the smoke test passes | Exit code 0 | Any step fails |
| 3 | `.gitignore` ignores `.venv/`, `__pycache__/`, `.env` and `/docs/ai-prompts/` | All four present | Any missing |
| 4 | `doxygen Doxyfile` runs without error | Exit code 0 | Error |
| 5 | The repository description and at least five topics are set on the git host (checked by the host's API) | Both set | Either empty |
| 6 | `git ls-files` contains no `.env` and no token value | Neither found | Found |
| 7 | `check-readme.sh` of the framework passes on the README | Exit code 0 | Fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3, O5 | [BC-001] |
| Success criteria 4, 6, 9 | [BC-001] |
| Concerns CN-001, CN-003, CN-005, CN-007, CN-008 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-07 — inside the Business Case window 2026-11-05 to 2026-11-19.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create project skeleton and pyproject.toml | Create `src/` and `tests/` per the clean-architecture folder wireframe, `pyproject.toml` (`requires-python >=3.13`, runtime dependencies `requests`, `beautifulsoup4`, `selenium`, dev dependency `pytest`, pytest settings) and `constants.py`. Keeps S03's dependency concern (CN-008) and the constants constraint of the Business Case. | No | |
| 2 | Add Python .gitignore | Add the standard Python `.gitignore` plus `.env`, `.venv/` and `/docs/ai-prompts/`, because the repository is public and `.env` holds personal tokens (CN-003). | No | |
| 3 | Add Doxyfile | Add a `Doxyfile` that documents `src/` from Doxygen comments, so that the source comment constraint of the Business Case can be checked by running `doxygen`. | No | |
| 4 | Write README with venv and test instructions | Build `README.md` from the framework template: what the project is, how to create a local `.venv`, how to run `python -m pip install --upgrade pip`, install, run and test (CN-005). Screenshots are added in MIL-004. | No | |
| 5 | Add smoke test for the toolchain | Add one `pytest` test that imports the package and reads a constant, so the venv, install and test steps in the README can be proved on a fresh clone. | No | |
| 6 | Set repository description and topics | Set a description and topics on the git host with its REST API, using the token in `.env` read by the shell only, never imported into the project and never printed (CN-007, CN-003). | No | |
| 7 | Start the AI prompt log | Create `docs/ai-prompts/session-001/prompts.md` as `framework/process/ai-prompt-log.md` says; the folder is ignored by git because the repository is public. | No | |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[6bd0143]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/commit/6bd0143f176299bca7c599c1cae0818f20eefcde
