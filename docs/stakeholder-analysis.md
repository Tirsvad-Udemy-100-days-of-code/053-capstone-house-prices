# Stakeholder Analysis: House Prices Capstone

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-05 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

This analysis names the people who have a stake in the House Prices Capstone and records what each one needs, so that the Business Case, the plan and the reviews can cite stable IDs. It follows the power/interest grid (Mendelow) and maps each concern to a FURPS+ attribute.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the Capstone with reviewed, documented work and record what each lecture step taught |
| S02 | Udemy coursists | Course participants who share code and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README steps to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | MEDIUM | Keep Informed | A clear repository description, topics and README, and no runtime dependencies beyond the need |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, owns every artifact and reviews it. Power and interest are both high.
- **Keep Informed (S02, S03):** they cannot change the project but they judge its usefulness. They are served by the README, the wiki and the repository page. S02 has high interest because the code is written for comparison; S03 has medium interest because they visit once and leave.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The work is planned, reviewed and traceable through branches and pull requests | Supportability |
| CN-002 | S01 | The program scrapes all listings and fills one form response per listing | Functionality |
| CN-003 | S01 | Secrets in `.env` never enter the project or its history | Functionality (security) |
| CN-004 | S02 | The code is readable and uses the assignment's function names | Supportability |
| CN-005 | S02 | A newcomer can run the program and its tests from the README | Usability |
| CN-006 | S02 | Each lecture step is explained, with a screenshot, in the wiki in a language they read (English, Danish, Bahasa Malaysia) | Usability |
| CN-007 | S03 | The repository has a clear description and topics | Usability |
| CN-008 | S03 | Install pulls in no unneeded runtime dependency | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat and pull request | Once per milestone | Pull request with review records, for S01 to read | Every milestone |
| CR-002 | Repository README | Once, updated per milestone | Run and test instructions with screenshots, for S02 and S03 | MIL-001, MIL-004 |
| CR-003 | Repository wiki | Once, in three languages | What each lecture step taught, with screenshots, for S02 | MIL-004 |
| CR-004 | Repository description and topics | Once | Short text and topics, for S03 | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 wants a quick finish; S02 wants complete documentation in three languages | S01, S02 | The wiki is its own milestone (MIL-004) after the code is done, so a slip there never blocks the code |
| S03 wants no dependencies; the assignment needs `requests`, `beautifulsoup4` and `selenium` | S03, S01 | Only those three are runtime dependencies; test tools are optional (dev) dependencies |
| S02 wants to run the program; running it needs S01's Google Form | S02, S01 | The form link is read from an environment variable, and the README explains how to create the form |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-003 | [BC-001] O5 |
| S01 | CN-002 | [BC-001] O1, O2 |
| S02 | CN-004, CN-005 | [BC-001] O1, O3 |
| S02 | CN-006 | [BC-001] O4 |
| S03 | CN-007 | [BC-001] O5 |
| S03 | CN-008 | [BC-001] O3, O5 |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | pending review | |

---

[BC-001]: ./business-case.md
