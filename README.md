## Federal GitHub Landscape Analysis

_Survey, analyze, and report on all Federal GitHub code_

As of December 2024, there is no consolidated inventory of all U.S. Federal open-source code repositories. This project surveys all Federal open-source code across GitHub.

---

### Project Description

Despite growing adoption of open-source practices, there is no single, comprehensive hub for U.S. Federal agencies to manage and track source code—from research projects to software and web development. Code.gov was launched to fill this need but has faced challenges with compliance and broader adoption. This project aims to expand the open-source movement in government by:

1. Conducting a comprehensive survey of Federal open-source code on GitHub through direct identification of relevant organizations.  
2. Analyzing the ecosystem, including trends in programming languages and collaboration networks.  
3. Archiving Federal repositories to ensure continued accessibility, especially in anticipation of potential disruptions during administrative transitions.

---

### Methodology and Reporting

Given over 192.1 million GitHub users, evaluating every account is infeasible. Instead, this project focuses on _organizations_ that associate themselves with a `.gov` domain in their registered email or listed URL.
There are 8,003,003 organizations\* listed on GitHub as of December 2024. Among them [3,203](src/data/raw_extracted_govs.csv) organizations indicated a `.gov` domain in at least one of the following fields: `email`, `blog`, `description`, `company`, `location`, or `name`. From these [1,599](src/data/US_filtered_govs.csv) `.gov`-affiliated organizations that were US-based, [1,151](src/data/US_curated_govs.csv) organizations with at least one public repository remained.

\* Compressed dataset of all [8,003,003](src/data/raw_all_organizations.csv.tar.bz2) organizations.

These were human-curated and placed into categories:

| **Category**                  | **Count** |
|-------------------------------|-----------|
| US Federal                    | 775       |
| US State or Local             | 293       |
| Not Gov (false positive)      | 53        |
| 404 (deleted by GitHub)       | 23        |
| Tribal                        | 5         |
| Hybrid-Gov Research Program   | 2         |

Organizations were categorized by their primary ownership. If an organization was perceived as government-run or self-identified as such, it was included. The 404 errors likely resulted from phishing organizations set up to imitate a government agency (they often had very recent creation dates). Government research programs (e.g., [MoTrPAC](https://github.com/MoTrPAC)) were counted when a non-government lab or entity conducted a government-funded project.

> **Limitations**: This project does not cover repositories hosted outside of GitHub or those not connected to a `.gov` organization.

Within these 775 U.S. Federal organizations, there are [25,276](src/data/repos_by_cumulative_popularity.csv) repositories in total. After excluding forks and repositories without at least one GitHub star or watcher (as indicators of influence), **12,468** repositories remained.

### Top 20 repositories by stars)

| Repository                                                                                       | Description                                                                                                              | Size    | Stars | Language   |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------|-------|------------|
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)               | Ghidra is a software reverse engineering (SRE) framework                                                                 | 374316  | 52552 | Java       |
| [nasa/openmct](https://github.com/nasa/openmct)                                                 | A web based mission control framework.                                                                                  | 85348   | 12105 | JavaScript |
| [nasa/fprime](https://github.com/nasa/fprime)                                                   | F´ - A flight software and embedded systems framework                                                                   | 437745  | 10118 | C++        |
| [nasa-jpl/open-source-rover](https://github.com/nasa-jpl/open-source-rover)                     | A build-it-yourself, 6-wheel rover based on the rovers on Mars!                                                         | 3019978 | 8644  | Prolog     |
| [uswds/uswds](https://github.com/uswds/uswds)                                                   | The U.S. Web Design System helps the federal government build fast, accessible, mobile-friendly websites.               | 172115  | 6839  | SCSS       |
| [uswds/public-sans](https://github.com/uswds/public-sans)                                       | A strong, neutral, principles-driven, open source typeface for text or display                                          | 401514  | 4497  | HTML       |
| [WhiteHouse/api-standards](https://github.com/WhiteHouse/api-standards)                         |                                                                                                                          | 599     | 3086  |            |
| [nasa/NASA-3D-Resources](https://github.com/nasa/NASA-3D-Resources)                             | Here you'll find a growing collection of 3D models, textures, and images from inside NASA.                              | 4154815 | 3044  |            |
| [NASA-SW-VnV/ikos](https://github.com/NASA-SW-VnV/ikos)                                         | Static analyzer for C/C++ based on the theory of Abstract Interpretation.                                               | 5280    | 2759  | C++        |
| [cisagov/RedEye](https://github.com/cisagov/RedEye)                                             | RedEye is a visual analytic tool supporting Red & Blue Team operations                                                  | 16705   | 2678  | TypeScript |
| [GSA/data](https://github.com/GSA/data)                                                         | Assorted data from the General Services Administration.                                                                 | 11381   | 2119  | HTML       |
| [kokkos/kokkos](https://github.com/kokkos/kokkos)                                               | Kokkos C++ Performance Portability Programming Ecosystem: The Programming Model - Parallel Execution and Memory Abstraction | 35390   | 2037  | C++        |
| [NREL/api-umbrella](https://github.com/NREL/api-umbrella)                                       | Open source API management platform                                                                                     | 30654   | 2032  | Ruby       |
| [cisagov/Malcolm](https://github.com/cisagov/Malcolm)                                           | Malcolm is a powerful, easily deployable network traffic analysis tool suite for full packet capture artifacts (PCAP files), Zeek logs and Suricata alerts. | 189179  | 2002  | Python     |
| [GSA/datagov-wptheme](https://github.com/GSA/datagov-wptheme)                                   | Data.gov WordPress Theme (obsolete)                                                                                     | 17512   | 1882  | JavaScript |
| [cisagov/ScubaGear](https://github.com/cisagov/ScubaGear)                                       | Automation to assess the state of your M365 tenant against CISA's baselines                                             | 31308   | 1847  | PowerShell |
| [usnistgov/macos_security](https://github.com/usnistgov/macos_security)                         | macOS Security Compliance Project                                                                                       | 6685    | 1826  | YAML       |
| [idaholab/moose](https://github.com/idaholab/moose)                                             | Multiphysics Object Oriented Simulation Environment                                                                     | 577167  | 1795  | C++        |
| [NASA-AMMOS/3DTilesRendererJS](https://github.com/NASA-AMMOS/3DTilesRendererJS)                 | Renderer for 3D Tiles in Javascript using three.js                                                                      | 55389   | 1651  | JavaScript |
| [cisagov/cset](https://github.com/cisagov/cset)                                                 | Cybersecurity Evaluation Tool                                                                                           | 2185716 | 1474  | TSQL       |


### Top 10 repositories by reported size

| Repository                                                               | Description                                                                          | Size       | Stars | Language          |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------|------------|-------|-------------------|
| [CROCUS-Urban/instrument-cookbooks](https://github.com/CROCUS-Urban/instrument-cookbooks) | Instrumentation and Data Exploration                                                | 89241701   | 1     | Jupyter Notebook  |
| [usnistgov/frvt](https://github.com/usnistgov/frvt)                      | Repository for the Face Recognition Vendor Test (FRVT)                              | 27115423   | 267   | C++               |
| [CDCgov/spheres-auspice-data](https://github.com/CDCgov/spheres-auspice-data) | Data for the SPHERES Auspice site                                                   | 22846208   | 2     |                   |
| [NEI-LSR/fMRI-Stimuli](https://github.com/NEI-LSR/fMRI-Stimuli)          | Psychtoolbox Scripts for fMRI Presentation                                          | 22705702   | 4     | MATLAB            |
| [NEFSC/NEFSC-illex_indicator_viewer](https://github.com/NEFSC/NEFSC-illex_indicator_viewer) |                                                                                      | 13918749   | 4     | HTML              |
| [CDCgov/covid19-forecast-hub-archive-fork](https://github.com/CDCgov/covid19-forecast-hub-archive-fork) | Projections of COVID-19, in standardized format                                     | 13748704   | 0     | Jupyter Notebook  |
| [HistoryAtState/frus](https://github.com/HistoryAtState/frus)            | Foreign Relations of the United States - TEI XML source files                       | 13365003   | 36    | XSLT              |
| [COVID19PVI/data](https://github.com/COVID19PVI/data)                    | This is the public data repository for the COVID-19 Pandemic Vulnerability Index (PVI) Dashboard. | 12367838   | 24    |                   |
| [idaholab/repository-statistics](https://github.com/idaholab/repository-statistics) | Tracking repository statistics over time for projects on GitHub under IdahoLab, IdahoLabResearch and IdahoLabUnsupported. | 11804873   | 1     | HTML              |
| [sPHENIX-Collaboration/QA-gallery](https://github.com/sPHENIX-Collaboration/QA-gallery) | Plotting macro and result gallery for standardized QA plots                          | 11319893   | 0     | C                 |


---

### TO DO

- Finish the overlap analysis with CODE.GOV
- Download all contributors and star-users
- Find a place for a deep and shallow copies for archiving effort
