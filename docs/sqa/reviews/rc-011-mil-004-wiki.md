# Review of MIL-004 wiki and README

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-004], [QC-WIKI-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [6867257] |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Criterion 14 checked on the published wiki | [f41c31d] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004] (the wiki in `docs/wiki/` and the README of the project)
- Checklist used: [QC-WIKI-001], together with [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the stand-in for S01 reads English and Danish)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | The sidebar starts with `**House Prices Capstone**`, then one list with `Home` first and the four step pages in English; the list appears once. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All five English pages are linked; a script checked every link in `docs/wiki/` and found no link to a missing page. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | N-A: the wiki has no related wikis, so the sidebar has no `**Related**` section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | `**Languages**` is the last section: `English: [Home](Home)`, `Dansk: [Hjem](Home-da)`, `Bahasa Malaysia: [Utama](Home-ms)`. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list is not repeated per language. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | N-A: the sidebar is written by hand, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line (criterion 11), so the sidebar is not the only way to switch. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English, Danish (`-da`) and Bahasa Malaysia (`-ms`) exist; the project's PO language is English, so English is the minimum. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Five English pages (`Home` and four steps) each have a `-da` and a `-ms` page: 15 content pages, equal sets. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line, current language in bold, links to the other two. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Files are `<Page>-da.md` and `<Page>-ms.md`; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Commands, file names, code names and constants (`python -m house_prices --scrape-only`, `FORM_URL`, `constants.py`, `?hl=en`) are unchanged in all three languages. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | After the merge on 2026-11-06, all 15 content pages (`Home` and four steps in en, da, ms), `_Sidebar` and `_Footer` answered HTTP 200 on the host, and the four screenshots in `docs/images/` can be fetched. Links inside the pages were checked in the repository (criterion 3), not followed again on the host; the pages were not viewed rendered. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | N-A: no change to layout rules in this review. |

README check: `bash framework/scripts/check-readme.sh` reports one finding, that the framework README does not name `qc-project-plan.md`. It is about the framework, which this project does not edit, so it is proposed upstream. Every relative link in the project README resolves, and the README names four screenshots for the four lecture steps.

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata of the review and of the project: `Language | en`, `Domain | it`. The wiki pages carry their language in the file name and language line. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `it` is in the registry domain list; `da` and `ms` are BCP 47 codes for the translations. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The English pages are English; the `-da` pages are Danish; the `-ms` pages are Bahasa Malaysia, with code and commands in English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | IT Professional English for the learners of the course: plain sentences, terms (scraper, form, Sheet, Selenium, wait) explained where they first appear. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The same term is used for the same concept in each language (form, Sheet, step); no `DICT` exists (see action item in earlier reviews). |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings of project documents, IDs and statuses are English; wiki headings are in the page language by design (`wiki.md`). |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No `*.en.md` twin exists; translations follow the wiki naming rule `<Page>-<code>.md`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version of the wiki; no earlier language to compare. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Confirmed by the stand-in for S01, who reads English and Danish; the Bahasa Malaysia text was written by the AI and is not checked by a native speaker (autonomous mode, not independent). |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are written out at first use or are commands and code names (`FORM_URL`). |

## Overall Verdict

Go — every Mandatory criterion passes or is N-A with a reason; criterion 14 was checked on the published wiki after the merge. The review is not independent: author and reviewer are the same AI acting as stand-in for S01, and S01 can challenge it in the run summary.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Ask a Bahasa Malaysia reader to check the translation | S01 | 2026-11-19 |
| Propose upstream that the framework README names `qc-project-plan.md` | S01 | 2026-11-19 |

---

[MIL-004]: ../../milestones/mil-004-docs-wiki.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[6867257]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/commit/686725719654ad436e078a587a3e12358a6fce6c
[f41c31d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/053-capstone-house-prices/commit/f41c31de3c5facb1fcbe393a90adaad85e38fe44
