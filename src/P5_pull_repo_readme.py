import requests
import time
import base64
from dspipe import Pipe
from pathlib import Path
import pandas as pd
from common import tokens, headers, check_remaining

#########################################################################
time_between_API_calls = 0.10
#########################################################################


def compute(repo_string):

    org_name, repo_name = repo_string.split("/")
    f1 = Path("data/repos/readme") / Path(org_name) / (repo_name + ".md")
    f1.parents[0].mkdir(exist_ok=True, parents=True)

    if f1.exists():
        return

    url = f"https://api.github.com/repos/{org_name}/{repo_name}/readme"

    token = next(tokens)
    headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(url, headers=headers)
    except Exception as EX:
        print(f"Response error: {EX}")
        time.sleep(200)
        return None

    if response.ok:
        pass

    elif response.status_code == 403:
        # Handle rate limiting
        sleep_seconds = check_remaining(response)
        print(f"Rate limit exceeded. Sleeping for {sleep_seconds} seconds.")
        check_remaining(response)
        return None

    elif response.status_code == 404:
        with open(f1, "w") as FOUT:
            FOUT.write("404")
        print("** MISSING **", repo_string)
        return None

    js = response.json()

    assert js["encoding"] == "base64"

    decoded_content = base64.b64decode(js["content"]).decode("utf-8")

    with open(f1, "w") as FOUT:
        FOUT.write(decoded_content)

    print(decoded_content[:500])
    check_remaining(response)


def process_organization(f0):
    df = pd.read_csv(f0)
    print(df["full_name"])
    Pipe(df["full_name"])(compute, 1)


P = Pipe("data/organizations_repolist", input_suffix=".csv")(process_organization, 1)

# repo_string = "GSA/project-open-data-dashboard"
# ITR = [
#    repo_string,
# ]
# P = Pipe(ITR)(compute, 1)

# df["orgname"] = df["html_url"].str.strip("/").str.split("/").str[-1]
# P = Pipe(df["orgname"], "data/organizations_repolist", output_suffix=".csv")
# P(get_org_repos, 1)
