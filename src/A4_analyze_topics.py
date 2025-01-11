from pathlib import Path
from dspipe import Pipe
import pandas as pd
import json


def compute(f0):
    with open(f0) as FIN:
        js = json.load(FIN)
    return js


F_JSON = Path("data/repos/topic_tags/").glob("**/*.json")

df = pd.json_normalize(Pipe(F_JSON, limit=None)(compute, -1))
del df["cost"]

f_repos = "data/repos_by_cumulative_popularity.csv"
info = pd.read_csv(f_repos).set_index("full_name")
df = df.set_index("full_name")
df["stars"] = info["stargazers_count"]


n_repos = len(df)
n_stars = df["stars"].sum()

df = df.explode("categories").reset_index()

cx = pd.DataFrame(df["categories"].value_counts()).reset_index()
cx["fraction"] = round((cx["categories"] / n_repos) * 100)
cx["fraction"] = cx["fraction"].apply(
    lambda x: f"![](https://geps.dev/progress/{int(x)})"
)
cx = cx.set_index("index")
print(cx)

cx = pd.DataFrame(df.groupby("categories").sum("stars")).reset_index()
cx = cx.sort_values("stars", ascending=False)
cx["fraction"] = round((cx["stars"] / n_stars) * 100)
cx["fraction"] = cx["fraction"].apply(
    lambda x: f"![](https://geps.dev/progress/{int(x)})"
)
cx = cx.set_index("categories")

print(cx)
