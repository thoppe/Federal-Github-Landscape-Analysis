code_directory=

pipeline:
	python P0_enumerate_orgs.py
	python P1_pull_org_info.py
	python P2_extract_govs.py
	python P3_pull_org_repos.py

lint:
	black *.py $(code_directory)
	flake8 *.py $(code_directory) --ignore=E501
