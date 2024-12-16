import json
from pathlib import Path
import pandas as pd
import requests
import gzip
import time
from common import tokens, headers, check_remaining

#########################################################################
time_between_API_calls = 0.05
#########################################################################

save_dest = Path("data/organizations")
save_dest.mkdir(exist_ok=True, parents=True)

while True:
    url = "https://api.github.com/organizations"

    prior_files = [f for f in save_dest.glob("*.gz")]
    prior_files = [int(f.stem.split("_")[1].split(".")[0]) for f in prior_files]

    # Cycle through the list of tokens
    token = next(tokens)
    headers["Authorization"] = f"Bearer {token}"

    if prior_files:
        since = max(prior_files)
    else:
        since = 0  # Starting point for user IDs
    print(f"Starting on {since:010d} {token}")

    params = {"since": since, "per_page": 100}  # Maximum allowed per page
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        js = response.json()
        if not js:
            print("All organizations enumerated!")
            exit()

        # Use pandas (bc lazy) to find the max and min user
        df = pd.DataFrame(js)
        min_user = df["id"].min()
        max_user = df["id"].max()

        # Choose a filename that records the first and last user ID we found
        f_save = save_dest / f"{min_user:010d}_{max_user:010d}.json.gz"

        # Save the information to a zipped json
        with gzip.open(f_save, "wt", encoding="utf-8") as FOUT:
            json.dump(js, FOUT)

        check_remaining(response)
        time.sleep(time_between_API_calls)

    elif response.status_code == 403:
        # Handle rate limiting
        sleep_seconds = check_remaining(response)
        print(f"Rate limit exceeded. Sleeping for {sleep_seconds} seconds.")
        time.sleep(sleep_seconds)
    else:
        print(f"Failed to fetch users: {response.status_code}")
        print(response.text)
        break
