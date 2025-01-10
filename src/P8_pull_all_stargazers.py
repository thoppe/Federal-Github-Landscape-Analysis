import pandas as pd
import requests
from dspipe import Pipe
import time
from common import tokens, headers, check_remaining

df = pd.read_csv("data/repos_by_cumulative_popularity.csv")
min_number_of_stars = 1

df = df[df["stargazers_count"] >= min_number_of_stars]
df = df[~df["fork"]]

drop_keys = [
    "avatar_url",
    "gravatar_id",
    "node_id",
    "url",
    "html_url",
    "followers_url",
    "following_url",
    "gists_url",
    "starred_url",
    "subscriptions_url",
    "organizations_url",
    "repos_url",
    "events_url",
    "received_events_url",
    "type",
]


def get_repo_contributors(full_name, f2):
    """
    Fetch all contributors for a given repository in an organization.
    """

    f2 = (f2.parent / full_name).with_suffix(".csv")
    f2.parent.mkdir(exist_ok=True, parents=True)

    if f2.exists():
        return

    org_name, repo_name = full_name.split("/")

    url = f"https://api.github.com/repos/{org_name}/{repo_name}/stargazers"
    contributors = []
    page = 1

    while True:
        token = next(tokens)
        headers["Authorization"] = f"Bearer {token}"
        params = {"per_page": 100, "page": page}
        print(f"{org_name}/{repo_name} - Contributors (Page {page})")

        try:
            response = requests.get(url, headers=headers, params=params)
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
            time.sleep(sleep_seconds)
            continue

        check_remaining(response)

        if not response.content:
            print(f"Warning repo {org_name}/{repo_name} is empty")
            data = []
        else:
            data = response.json()

        if "status" in data and data["status"] == "404":
            break

        # It's possible that we get this error, need to handle!
        # {'message': 'In order to keep the API fast for everyone, pagination is limited for this resource.', 'documentation_url': 'https://docs.github.com/v3/#pagination', 'status': '422'}

        if "status" in data and data["status"] == "422":
            break

        if not data:
            break

        if page > 100:
            print(data)

        contributors.extend(data)
        page += 1

    df = pd.json_normalize(contributors)

    for key in drop_keys:
        if key in df:
            del df[key]

    if len(df) > 0:
        try:
            df = df.set_index("id")
        except Exception as Ex:
            print("BROKEN?", df, Ex)
            return

    print(f"{full_name} : {len(df)}")
    if len(df):
        df.to_csv(f2)
    else:
        df.to_csv(f2, index=False)


# df = df[20:]

Pipe(df["full_name"], "data/repos/stargazers", limit=None, shuffle=False)(
    get_repo_contributors, 1
)

# print(df.columns)
