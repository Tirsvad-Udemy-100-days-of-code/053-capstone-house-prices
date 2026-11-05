# 🚀 House Prices Capstone

Scrapes rental listings from the Zillow clone with BeautifulSoup and fills a Google Form with Selenium, one response per listing. It is the Day 53 Capstone of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", written for course participants who want to compare solutions and for visitors who browse the repository for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The program does two jobs, as the assignment asks:

1. **Scrape** https://appbrewery.github.io/Zillow-Clone/ with `requests` and BeautifulSoup into three lists: links, prices (`$1,234`) and addresses (no newlines, pipes or extra whitespace).
2. **Fill** a Google Form of your own with Selenium, once per listing. The form's Sheet then holds one row per property.

The repository is laid out as follows:

| Path | What it is for |
| --- | --- |
| `src/house_prices/` | The program, in Clean Architecture layers (`domain`, `application`, `infrastructure`, `presentation`) |
| `src/house_prices/constants.py` | All constants (URLs, headers, locators) |
| `tests/` | `pytest` tests; they use a saved copy of the page and need no network |
| `docs/` | Project documents (business case, plan, milestones, reviews) and the wiki |
| `Doxyfile` | Doxygen configuration for the source comments |

The wiki explains in English, Danish and Bahasa Malaysia what each lecture step taught.

## 📋 Requirements

- Python 3.13 or later: the language of the project (`requires-python = ">=3.13"`).
- `requests`, `beautifulsoup4` and `selenium`: the only runtime dependencies, installed from `pyproject.toml`.
- A Google Form with three short-answer questions (address, price, link) in your own Google account: the target of the form filler.
- Doxygen (optional): builds the API documentation from the source comments.
- Docker (optional): runs the browser end-to-end test in a container, so it never takes your mouse and keyboard.

## 🛠️ Setup

Create a local virtual environment named `.venv` in the project root, upgrade `pip`, and install the project with its development tools.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. Never commit `.venv/` or a `.env` file; both are in `.gitignore`.

## ▶️ Run

Put the link of your Google Form in the environment variable `FORM_URL` (it is not stored in the repository), then start the program:

```bash
export FORM_URL="https://docs.google.com/forms/d/e/<your-form-id>/viewform"
python -m house_prices
```

On Windows PowerShell use `$env:FORM_URL = "https://docs.google.com/forms/d/e/<your-form-id>/viewform"`.

Google shows the form in the language of the visitor's location, and the program finds the "Submit" button and the confirmation text in English. Add `?hl=en` to the link (`.../viewform?hl=en`) so the form always opens in English. The form must be open to anyone with the link, because the browser the program starts is not signed in.

Generate the API documentation with `doxygen Doxyfile`; the result is in `docs/doxygen/html/`.

## 🧪 Tests

With the environment active:

```bash
python -m pytest
```

The tests use a saved copy of the Zillow clone page and a fake browser driver, so they need neither the network nor a browser.

## 📄 License

See the [LICENSE][license] file.

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[license]: ./LICENSE
[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/issues
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
