import pandas as pd
from dspipe import Pipe

f_save = "data/users_by_repo_contributions.csv"


def read_single(f0):
    try:
        df = pd.read_csv(f0)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()

    df = df.dropna()

    try:
        df["id"] = df["id"].astype(int)
    except Exception:
        print(df)
    return df


def compute(f0):
    # Pipe('data/repos/contributors/')(compute)
    data = Pipe(f0, progressbar=False)(read_single)
    df = pd.concat(data)
    return df


n_limit = None
df = pd.concat(Pipe("data/repos/contributors/", limit=n_limit)(compute, -1))
print(len(df))
print(df)


cx = pd.DataFrame(df["login"].value_counts())
cx.columns = ["Unique repos"]
cx["Total Contributions"] = df.groupby("login")["contributions"].sum()

cx = cx.reset_index()
cx = cx.rename(columns={"index": "username"})

for col in cx.columns:
    if "username" in col:
        continue
    cx[col] = cx[col].astype(int)

cx.to_csv(f_save)

base_username = "https://github.com"
cx["username"] = cx["username"].apply(lambda x: f"[{x}]({base_username}/{x}/)")
cx = cx.set_index("username")

print(cx[:20])
print()

cx = cx.sort_values("Total Contributions", ascending=False)
print(cx[:20])
