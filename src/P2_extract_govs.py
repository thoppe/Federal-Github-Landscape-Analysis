import numpy as np
from dspipe import Pipe
import pandas as pd

"""
Extracts all the organizations that have ".gov" within at least one of their:

    "email", "blog", "description", "company", "location", "name"

Exports this list to a file.
"""

f_save = "data/raw_extracted_govs.csv"


def compute(f0):
    try:
        df = pd.read_csv(f0)
    except Exception:
        # This is bad, likely a write-error, should delete and redownload
        print(f"ERROR WITH {f0}")
        return None, None

    # df = df[df['public_repos']>0]

    stats = {}
    stats["n_repos"] = len(df)
    stats["largest_id"] = df["id"].max()

    idx = np.zeros(len(df), dtype=bool)
    for key in ["email", "blog", "description", "company", "location", "name"]:

        try:
            df[key] = df[key].astype(str)
            idx += df[key].str.find(".gov") > -1
        except KeyError:
            # This is OK, we are generally missing one in our 100 batch
            pass

    stats["matching_govs"] = idx.sum()

    idx = idx.astype(bool)
    df = df[idx]
    return df, stats


stats, data = [], []
P = Pipe("data/organizations_info", limit=None)
for row, stat in P(compute, -1):
    if row is None:
        continue

    stats.append(stat)
    data.append(row)

df = pd.concat(data).sort_values("id").set_index("id")
cx = pd.DataFrame(stats)


print(f"Total users: {cx.largest_id.max():,d}")
print(f"Total orgs : {cx.n_repos.sum():,d}")
print(f"Total govs : {cx.matching_govs.sum():,d}")

columns = [
    "description",
    "name",
    "company",
    "blog",
    "location",
    "email",
    "twitter_username",
    "is_verified",
    "has_organization_projects",
    "has_repository_projects",
    "public_repos",
    "public_gists",
    "followers",
    "following",
    "html_url",
    "created_at",
    "updated_at",
    "archived_at",
]

df = df[columns]
df.to_csv(f_save)
# print(df)
