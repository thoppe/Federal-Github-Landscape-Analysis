import pandas as pd
from pathlib import Path
from dspipe import Pipe
import json

"""
Computes some stats about the data we've collected.
"""

stats = {}

# Gather information about the curation efforts
df = pd.read_csv("data/US_filtered_govs.csv").set_index("id")
dx = pd.read_csv("data/US_curated_govs.csv").set_index("id")
org = pd.read_csv("data/raw_extracted_govs.csv").set_index("id")
df["CURATION"] = dx["CURATION"].fillna("uncurated")
print(f"+ # Total number of .gov organizations {len(df)}")
print(df["CURATION"].value_counts())
# print(df.columns)

totals = df.groupby("CURATION")["public_repos"].sum()
totals /= totals.sum()
print("Total fractions of orgs by repo count")
print("(note this is skewed by global.gov false positives")
print(totals.sort_values(ascending=False))
# print(df.columns)

# Keep only those curated as Federal
df = df[df["CURATION"] == "FEDERAL"]
known_federal_ids = set(df.index.tolist())
# print(known_federal_ids)
print()
print(f"+ # Federal GH orgs {len(df)}")

repos = Pipe("data/organizations_repolist/", limit=None, input_suffix=".csv")(
    pd.read_csv, -1
)
repos = pd.concat(repos)

# Drop those without names
repos = repos.dropna(subset=["name"])

print(f"+ # Federal GH repos {len(repos)}")

repos = repos[~repos["fork"]]
print(f"+ # Federal GH repos [non-fork] {len(repos)}")

repos["fame"] = repos["stargazers_count"] + repos["watchers_count"]
repos = repos[repos["fame"] >= 1]
print(f"+ # Federal GH repos [non-fork, +1 fame] {len(repos)}")

print("+ Repo size")
print(repos["size"].describe().apply(lambda x: format(x, "0.2f")))
# print(repos.columns)

print("+ Repo fame (watchers+stars)")
print(repos["fame"].describe().apply(lambda x: format(x, "0.2f")))

exit()


# Count the exact total number of organizations and their various stats
# by going through each repo block

summation_columns = [
    "has_repository_projects",
    "public_repos",
    "public_gists",
    "followers",
    "following",
    "is_verified",
    "has_organization_projects",
]


def compute(f0):
    df = pd.read_csv(f0).set_index("id")

    # Only keep the Federal IDs
    idx = df.index.isin(known_federal_ids)
    df = df[idx]

    info = {}
    info["n"] = len(df)
    for key in summation_columns:
        info[key] = df[key].sum()
    return info


data = Pipe("data/organizations_info/", limit=1000)(compute, -1)
dq = pd.DataFrame(data)
for key in dq.columns:
    stats[key] = int(dq[key].sum().astype(int))

# Find the largest ID, this indicates the total number of users
F = sorted(map(str, Path("data/organizations").glob("*.gz")))
stats["max_user_id"] = int(F[-1].split("_")[1].split(".")[0])

js = json.dumps(stats, indent=2)
print(js)
