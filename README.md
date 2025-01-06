## Federal GitHub Landscape Analysis

_Survey, analyze, and report on all Federal GitHub code_

As of December 2024, there is no consolidated inventory of all U.S. Federal open-source code repositories. This project surveys all Federal open-source code across GitHub.

---

### Methodology and Assumptions

Given over 192.1 million GitHub users, evaluating every account is infeasible. Instead, this project focuses on _organizations_ that associate themselves with a `.gov` domain in their registered email or listed URL.

There are 8,003,003 organizations listed on GitHub as of December 2024. Among them, 1,600 indicate a U.S.-based `.gov` domain in at least one of the following fields: `email`, `blog`, `description`, `company`, `location`, or `name`.

From these `.gov`-affiliated organizations with at least one repository, human review placed them into categories:

| **Category**                  | **Count** |
|-------------------------------|-----------|
| US Federal                    | 775       |
| US State or Local             | 293       |
| Not Gov (false positive)      | 53        |
| 404 (deleted by GitHub)       | 23        |
| Tribal                        | 5         |
| Hybrid-Gov Research Program   | 2         |

Organizations were categorized by their primary ownership. If an organization was perceived as government-run or self-identified as such, it was included. The 404 errors likely resulted from phishing organizations set up to imitate a government agency (they often had very recent creation dates). Government research programs (e.g., [MoTrPAC](https://github.com/MoTrPAC)) were counted when a non-government lab or entity conducted a government-funded project.

> **Note**: This project does not cover repositories hosted outside of GitHub or those not connected to a `.gov` organization.

Within these 775 U.S. Federal organizations, there are 25,276 repositories in total. After excluding forks and repositories without at least one GitHub star or watcher (as indicators of influence), **12,468** repositories remained.

**TO DO: OVERLAP WITH CODE.GOV**

---

### Project Description

Despite growing adoption of open-source practices, there is no single, comprehensive hub for U.S. Federal agencies to manage and track source code—from research projects to software and web development. Code.gov was launched to fill this need but has faced challenges with compliance and broader adoption. This project aims to expand the open-source movement in government by:

1. Conducting a comprehensive survey of Federal open-source code on GitHub through direct identification of relevant organizations.  
2. Analyzing the ecosystem, including trends in programming languages and collaboration networks.  
3. Archiving Federal repositories to ensure continued accessibility, especially in anticipation of potential disruptions during administrative transitions.

---

### Goals

- Provide an archive of the data with a user-friendly front-end interface.  
- Publish a research report detailing the survey findings and ecosystem analysis.

---

### Current Progress

A shallow copy of identified repositories has begun as part of the archiving effort.
