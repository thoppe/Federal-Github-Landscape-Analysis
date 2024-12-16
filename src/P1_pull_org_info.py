import time
import os
import requests
from dspipe import Pipe
import gzip
import json
import pandas as pd
from pathlib import Path
from common import tokens, headers, check_remaining

#########################################################################
time_between_API_calls = 0.05
#########################################################################


def download(f0, f1, df=None):
    url = df.loc[f0]["url"]
    params = {}

    # Cycle through the list of tokens
    token = next(tokens)
    headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(url, headers=headers, params=params)
    except Exception as EX:
        print(f"Response error: {EX}")
        time.sleep(200)
        return None

    if response.ok:
        json_string = response.json()
        print(json.dumps(response.json(), indent=2))

    elif response.status_code == 404:
        print(f"** 404 Error for {f0}")
        json_string = df.loc[f0].to_dict()
        json_string["error_code"] = 404

    elif response.status_code == 403:
        # Handle rate limiting
        sleep_seconds = check_remaining(response)
        print(f"Rate limit exceeded. Sleeping for {sleep_seconds} seconds.")
        time.sleep(sleep_seconds)
        return None

    else:
        print(response)
        print("BUG OUT!", response.status_code, response.headers)
        time.sleep(200)
        return None

    js = json.dumps(json_string)
    with open(f1, "w") as FOUT:
        FOUT.write(js)

    check_remaining(response)
    time.sleep(time_between_API_calls)
    return js


#########################################################################


def download_from_file(f0):
    with gzip.open(f0) as FIN:
        js = json.load(FIN)

    df = pd.DataFrame(js).set_index("login")
    P = Pipe(df.index, "data/organizations_records", output_suffix=".json")
    P(download, 1, df=df)


def consolidate(f0, f1):
    with gzip.open(f0) as FIN:
        js = json.load(FIN)

    df = pd.DataFrame(js)[["login"]]
    base = Path("data/organizations_records")

    df["fx"] = df["login"].map(lambda x: (base / (x + ".json")))
    df["has_downloaded"] = df["fx"].map(lambda x: x.exists())

    # if df["has_downloaded"].mean() == 0:
    #    return

    if df["has_downloaded"].mean() < 1:
        print(f0, df["has_downloaded"].mean())

        try:
            download_from_file(f0)
        except Exception as EX:
            print(f"FAILED WITH {EX}")
            return

        consolidate(f0, f1)
        return

    assert df["has_downloaded"].mean() == 1

    data = []
    for fx in df["fx"]:
        with open(fx) as FIN:
            jx = json.load(FIN)
            data.append(jx)
    dx = pd.DataFrame(data).set_index("id")
    assert len(dx) == len(df)

    print(f1)
    dx.to_csv(f1, compression="gzip")

    for fx in df["fx"]:
        os.unlink(fx)
        # print(fx)


n_threads = 2
P = Pipe(
    "data/organizations",
    "data/organizations_info",
    shuffle=True,
    output_suffix=".csv.gz",
)
P(consolidate, n_threads)


# Pipe("data/organizations", limit=3, shuffle=True)(download_from_file, 1)
# for row in Pipe("data/organizations/", limit=None)(compute, 1):
#    data.extend(row)
# df = df.sample(frac=1)
# print(f"Total samples {len(df)}")
# Pipe(df.index, "data/organizations_records", output_suffix=".json")(download, 1)
