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

<details>
<summary>Human-curated categories</summary>

| **Category**                  | **Count** |
|-------------------------------|-----------|
| US Federal                    | 775       |
| US State or Local             | 293       |
| Not Gov (false positive)      | 53        |
| 404 (deleted by GitHub)       | 23        |
| Tribal                        | 5         |
| Hybrid-Gov Research Program   | 2         |

</details>

Organizations were categorized by their primary ownership. If an organization was perceived as government-run or self-identified as such, it was included. The 404 errors likely resulted from phishing organizations set up to imitate a government agency (they often had very recent creation dates). Government research programs (e.g., [MoTrPAC](https://github.com/MoTrPAC)) were counted when a non-government lab or entity conducted a government-funded project.

> **Limitations**: This project does not cover repositories hosted outside of GitHub or those not connected to a `.gov` organization.

Within these 775 U.S. Federal organizations, there are [25,276](src/data/repos_by_cumulative_popularity.csv) repositories in total. After excluding forks and repositories without at least one GitHub star or watcher (as indicators of influence), **12,468** repositories remained.

Within these repositories there were [27,382](src/data/users_by_repo_contributions.csv) unique contributors. Some of these are clearly provisioned automated bots, while other indicate extremely prolific human users.

### Interesting findings

<details>
<summary>🌟 Top 20 repositories by stars</summary>

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
</details>

<details>
<summary>📦 Top 20 repositories by size</summary>

| Repository                                                                                                         | Description                                                                                                                                                                                                                                      | Size      | Stargazers Count | Language          |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------|-------------------|
| [CROCUS-Urban/instrument-cookbooks](https://github.com/CROCUS-Urban/instrument-cookbooks/)                        | Instrumentation and Data Exploration                                                                                                                                                                                                           | 89241701  | 1                | Jupyter Notebook |
| [usnistgov/frvt](https://github.com/usnistgov/frvt/)                                                              | Repository for the Face Recognition Vendor Test (FRVT)                                                                                                                                                                                         | 27115423  | 267              | C++              |
| [CDCgov/spheres-auspice-data](https://github.com/CDCgov/spheres-auspice-data/)                                    | Data for the SPHERES Auspice site                                                                                                                                                                                                              | 22846208  | 2                | NaN              |
| [NEI-LSR/fMRI-Stimuli](https://github.com/NEI-LSR/fMRI-Stimuli/)                                                  | Psychtoolbox Scripts for fMRI Presentation                                                                                                                                                                                                     | 22705702  | 4                | MATLAB           |
| [NEFSC/NEFSC-illex_indicator_viewer](https://github.com/NEFSC/NEFSC-illex_indicator_viewer/)                      | NaN                                                                                                                                                                                                                                            | 13918749  | 4                | HTML             |
| [HistoryAtState/frus](https://github.com/HistoryAtState/frus/)                                                    | Foreign Relations of the United States - TEI XML source files                                                                                                                                                                                  | 13365003  | 36               | XSLT             |
| [COVID19PVI/data](https://github.com/COVID19PVI/data/)                                                            | This is the public data repository for the COVID-19 Pandemic Vulnerability Index (PVI) Dashboard.                                                                                                                                              | 12367838  | 24               | NaN              |
| [idaholab/repository-statistics](https://github.com/idaholab/repository-statistics/)                              | Tracking repository statistics over time for projects on GitHub under IdahoLab, IdahoLabResearch and IdahoLabUnsupported.                                                                                                                      | 11804873  | 1                | HTML             |
| [sPHENIX-Collaboration/QA-gallery](https://github.com/sPHENIX-Collaboration/QA-gallery/)                          | Plotting macro and result gallery for standardized QA plots                                                                                                                                                                                    | 11319893  | 0                | C                |
| [department-of-veterans-affairs/va.gov-team](https://github.com/department-of-veterans-affairs/va.gov-team/)      | Public resources for building on and in support of VA.gov. Visit complete Knowledge Hub:                                                                                                                                                        | 11154768  | 285              | HTML             |
| [lanl-ocs/laghos-sample-dataset](https://github.com/lanl-ocs/laghos-sample-dataset/)                              | Sample Laghos dataset for system prototyping and benchmarking                                                                                                                                                                                  | 10230034  | 2                | NaN              |
| [nasa/CFS-101](https://github.com/nasa/CFS-101/)                                                                  | NaN                                                                                                                                                                                                                                            | 9550757   | 78               | NaN              |
| [NREL/BESTEST-GSR-ARCHIVE](https://github.com/NREL/BESTEST-GSR-ARCHIVE/)                                          | Building Energy Simulation Test - Generation Simulation and Reporting (BESTEST-GSR)                                                                                                                                                            | 8831271   | 13               | Ruby             |
| [GEOS-ESM/MAPL](https://github.com/GEOS-ESM/MAPL/)                                                                | MAPL is a foundation layer of the GEOS architecture, whose original purpose is to supplement the Earth System Modeling Framework (ESMF)                                                                                                        | 6664730   | 24               | Fortran          |
| [USEPA/national-surface-water-quality-survey](https://github.com/USEPA/national-surface-water-quality-survey/)    | NaN                                                                                                                                                                                                                                            | 6201917   | 0                | NaN              |
| [NCIP/national-biomedical-image-archive](https://github.com/NCIP/national-biomedical-image-archive/)              | The National Biomedical Imaging Archive (NBIA) is a free and open source service and software application that enables users to securely store, search, and download diagnostic medical images.                                                  | 5946406   | 27               | Java             |
| [department-of-veterans-affairs/VA_Data_Assets_NCA](https://github.com/department-of-veterans-affairs/VA_Data_Assets_NCA/) | This is a a repository for open NCA Data Assets.                                                                                                                                                                                                | 5677870   | 3                | NaN              |
| [NCIP/caaers-docs](https://github.com/NCIP/caaers-docs/)                                                          | This is the documentation repository for Cancer Adverse Event Reporting System (caAERS) project that is under the NCIP channel                                                                                                                 | 5636468   | 2                | Groovy           |
| [NREL/resstock](https://github.com/NREL/resstock/)                                                                | Highly granular modeling of residential building stocks at national, regional, and local scales using OpenStudio/EnergyPlus.                                                                                                                   | 5561415   | 112              | Ruby             |
| [NREL/EnergyPlusBuildResults](https://github.com/NREL/EnergyPlusBuildResults/)                                    | NaN                                                                                                                                                                                                                                            | 5322545   | 4                | HTML             |

</details>


<details>
<summary>🔧 Top 20 users by total unique repo contributions</summary>

| Username                                               | Unique Repos | Total Contributions |
|--------------------------------------------------------|--------------|----------------------|
| [dependabot[bot]](https://github.com/dependabot)       | 1306         | 30723               |
| [jsf9k](https://github.com/jsf9k/)                     | 310          | 69911               |
| [felddy](https://github.com/felddy/)                   | 303          | 30348               |
| [mcdonnnj](https://github.com/mcdonnnj/)               | 296          | 107597              |
| [dav3r](https://github.com/dav3r/)                     | 293          | 14476               |
| [hillaryj](https://github.com/hillaryj/)               | 276          | 1360                |
| [jmorrowomni](https://github.com/jmorrowomni/)         | 240          | 3541                |
| [jasonodoom](https://github.com/jasonodoom/)           | 233          | 6899                |
| [arcsector](https://github.com/arcsector/)             | 231          | 248                 |
| [michaelsaki](https://github.com/michaelsaki/)         | 198          | 6360                |
| [afeld](https://github.com/afeld/)                     | 193          | 7654                |
| [github-actions[bot]](https://github.com/github)       | 147          | 11437               |
| [konklone](https://github.com/konklone/)               | 146          | 5505                |
| [snyk-bot](https://github.com/snyk-bot/)               | 138          | 1097                |
| [gbinal](https://github.com/gbinal/)                   | 135          | 6432                |
| [adborden](https://github.com/adborden/)               | 119          | 3305                |
| [mogul](https://github.com/mogul/)                     | 118          | 3121                |
| [jmcarp](https://github.com/jmcarp/)                   | 96           | 5236                |
| [apburnes](https://github.com/apburnes/)               | 94           | 1926                |
| [wslack](https://github.com/wslack/)                   | 91           | 2302                |
</details>


<details>
<summary>🔧 Top 20 users by total overall repo contributions</summary>

| Username                                               | Unique Repos | Total Contributions |
|--------------------------------------------------------|--------------|----------------------|
| [actions-user](https://github.com/actions-user/)       | 38           | 369641              |
| [mcdonnnj](https://github.com/mcdonnnj/)               | 296          | 107597              |
| [lattner](https://github.com/lattner/)                 | 4            | 94479               |
| [nrel-bot-3](https://github.com/nrel-bot-3/)           | 1            | 73117               |
| [nrel-bot-2](https://github.com/nrel-bot-2/)           | 1            | 70656               |
| [jsf9k](https://github.com/jsf9k/)                     | 310          | 69911               |
| [nrel-bot](https://github.com/nrel-bot/)               | 1            | 53470               |
| [matsapps](https://github.com/matsapps/)               | 1            | 32610               |
| [dependabot[bot]](https://github.com/dependabot)       | 1306         | 30723               |
| [nrel-bot-2b](https://github.com/nrel-bot-2b/)         | 1            | 30658               |
| [nrel-bot-2c](https://github.com/nrel-bot-2c/)         | 1            | 30539               |
| [felddy](https://github.com/felddy/)                   | 303          | 30348               |
| [alchemistmatt](https://github.com/alchemistmatt/)     | 82           | 27713               |
| [topperc](https://github.com/topperc/)                 | 3            | 25859               |
| [RKSimon](https://github.com/RKSimon/)                 | 3            | 22505               |
| [BarrySmith](https://github.com/BarrySmith/)           | 5            | 22006               |
| [espindola](https://github.com/espindola/)             | 3            | 20191               |
| [balay](https://github.com/balay/)                     | 6            | 19960               |
| [tkremenek](https://github.com/tkremenek/)             | 3            | 18322               |
| [shorowit](https://github.com/shorowit/)               | 15           | 17545               |

</details>

<details>
<summary>TBD: ✨ Top 20 users by total unique repo stars</summary>
</details>

<details>
<summary>TBD: ✨ Top 20 users by total overall repo stars</summary>
</details>

<details>
<summary>TBD: ✨ Total Programming Language Usage</summary>

| Language                           | Unique Repo Count | Star Weighted Count |
|------------------------------------|-------------------|----------------------|
| Python                             | 4581              | 50607               |
| JavaScript                         | 1462              | 35041               |
| HTML                               | 1320              | 19240               |
| C++                                | 1317              | 42808               |
| Jupyter Notebook                   | 1294              | 10771               |
| R                                  | 1161              | 4934                |
| Java                               | 874               | 62392               |
| Shell                              | 816               | 6988                |
| C                                  | 622               | 16138               |
| Ruby                               | 492               | 8821                |
| CSS                                | 475               | 4313                |
| TypeScript                         | 372               | 6298                |
| Fortran                            | 368               | 4977                |
| C#                                 | 268               | 1041                |
| HCL                                | 242               | 847                 |
| PHP                                | 218               | 2366                |
| MATLAB                             | 183               | 1487                |
| Julia                              | 154               | 3229                |
| Go                                 | 135               | 1920                |
| Perl                               | 112               | 840                 |
| Dockerfile                         | 108               | 201                 |
| TeX                                | 99                | 733                 |
| Makefile                           | 75                | 264                 |
| SCSS                               | 71                | 9857                |
| CMake                              | 62                | 1128                |
| XSLT                               | 57                | 1340                |
| Clojure                            | 52                | 1340                |
| Vue                                | 49                | 233                 |
| Groovy                             | 38                | 548                 |
| Rust                               | 36                | 191                 |
| Roff                               | 35                | 339                 |
| Objective-C                        | 35                | 820                 |
| Matlab                             | 31                | 243                 |
| Common Workflow Language           | 25                | 414                 |
| TSQL                               | 24                | 1608                |
| Nextflow                           | 22                | 186                 |
| PowerShell                         | 21                | 3308                |
| Cuda                               | 20                | 946                 |
| SAS                                | 20                | 226                 |
| Logos                              | 17                | 27                  |
| Scala                              | 17                | 204                 |
| Smarty                             | 16                | 20                  |
| PostScript                         | 15                | 79                  |
| Visual Basic                       | 15                | 11                  |
| Stata                              | 15                | 27                  |
| XQuery                             | 14                | 63                  |
| Batchfile                          | 14                | 17                  |
| Jinja                              | 14                | 24                  |
| FORTRAN                            | 14                | 642                 |
| PLpgSQL                            | 14                | 217                 |
</details>




---

### TO DO

- Finish the overlap analysis with CODE.GOV
- Download all star-users
- Analyze the programing languages (and another weighted by stars)
- Find a place for a deep and shallow copies for archiving effort
