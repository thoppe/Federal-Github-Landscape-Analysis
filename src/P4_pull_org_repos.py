from dspipe import Pipe
import requests
import pandas as pd
import time
from common import tokens, headers, check_remaining

#########################################################################
time_between_API_calls = 0.10
#########################################################################

drop_keys = [
    "forks_url",
    "keys_url",
    "collaborators_url",
    "teams_url",
    "hooks_url",
    "issue_events_url",
    "events_url",
    "assignees_url",
    "branches_url",
    "tags_url",
    "blobs_url",
    "git_tags_url",
    "git_refs_url",
    "trees_url",
    "statuses_url",
    "languages_url",
    "stargazers_url",
    "contributors_url",
    "subscribers_url",
    "subscription_url",
    "commits_url",
    "git_commits_url",
    "comments_url",
    "issue_comment_url",
    "contents_url",
    "compare_url",
    "merges_url",
    "archive_url",
    "downloads_url",
    "issues_url",
    "pulls_url",
    "milestones_url",
    "notifications_url",
    "labels_url",
    "releases_url",
    "deployments_url",
    "git_url",
    "ssh_url",
    "clone_url",
    "svn_url",
    "owner.avatar_url",
    "owner.gravatar_id",
    "owner.url",
    "owner.html_url",
    "owner.followers_url",
    "owner.following_url",
    "owner.gists_url",
    "owner.starred_url",
    "owner.subscriptions_url",
    "owner.organizations_url",
    "owner.repos_url",
    "owner.events_url",
    "owner.received_events_url",
]


def get_org_repos(org_name, f1):
    """
    Fetch all repository names for a given GitHub organization.

    Parameters:
        org_name (str): The name of the organization.

    Returns:
        list: A list of repository names.
    """

    url = f"https://api.github.com/orgs/{org_name}/repos"
    repos = []
    page = 1

    while True:

        token = next(tokens)
        headers["Authorization"] = f"Bearer {token}"
        params = {"per_page": 100, "page": page}
        print(f"{org_name} ({page})")

        try:
            response = requests.get(url, headers=headers, params=params)
        except Exception as EX:
            print(f"Response error: {EX}")
            time.sleep(200)
            return None

        if response.ok:
            pass
            # print(json.dumps(response.json(), indent=2))
        elif response.status_code == 403:
            # Handle rate limiting
            sleep_seconds = check_remaining(response)
            print(f"Rate limit exceeded. Sleeping for {sleep_seconds} seconds.")
            exit()

        check_remaining(response)

        data = response.json()
        if not data:
            break

        repos.extend(data)
        page += 1

    df = pd.json_normalize(repos)
    for key in drop_keys:
        if key in df:
            del df[key]

    if len(df) == 0:
        return df

    df = df.set_index("id")
    df.to_csv(f1)
    return df


f_data = "data/US_curated_govs.csv"
df = pd.read_csv(f_data)

# Data quality checks
assert (df["base_id"] == df["id"]).all()
assert (df["base_html_url"] == df["html_url"]).all()

df = df[df["CURATION"] == "FEDERAL"]
df["orgname"] = df["html_url"].str.strip("/").str.split("/").str[-1]

P = Pipe(df["orgname"], "data/organizations_repolist", output_suffix=".csv")
P(get_org_repos, 1)

# Example code
# organization = "WhiteHouse"
# df = get_org_repos(organization)
# df.to_csv("demo.csv")
