import pandas as pd
from pathlib import Path
from dspipe import Pipe

"""
Computes some stats about the data we've collected.
"""

stats = {}

# Gather information about the curation efforts
df = pd.read_csv("data/US_filtered_govs.csv").set_index("id")
dx = pd.read_csv("data/US_curated_govs.csv").set_index("id")
df["CURATION"] = dx["CURATION"].fillna("uncurated")

totals = df.groupby("CURATION")["public_repos"].sum()
totals /= totals.sum()
print("Total fractions by repos")
print(totals)
# print(df.columns)

# Find out how many repos are unique vs forks
print(df.columns)
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
    df = pd.read_csv(f0)
    info = {}
    info["n"] = len(df)
    for key in summation_columns:
        info[key] = df[key].sum()
    return info


data = Pipe("data/organizations_info/", limit=100)(compute, -1)
df = pd.DataFrame(data)
for key in df.columns:
    stats[key] = df[key].sum().astype(int)
print(stats)
exit()

# Find the largest ID, this indicates the total number of users
F = sorted(map(str, Path("data/organizations").glob("*.gz")))
stats["max_user_id"] = int(F[-1].split("_")[1].split(".")[0])
print(stats)
