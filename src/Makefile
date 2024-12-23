code_directory=

pipeline:
	python P0_enumerate_orgs.py
	python P1_pull_org_info.py
	python P2_extract_govs.py
	python P3_label_govs.py
	python P4_pull_org_repos.py
	python P5_pull_repo_readme.py

lint:
	black *.py $(code_directory)
	flake8 *.py $(code_directory) --ignore=E501
