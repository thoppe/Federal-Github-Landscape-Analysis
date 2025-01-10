import pandas as pd
from dspipe import Pipe

f_save = "data/stargazers_by_repo_contributions.csv"


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
df = pd.concat(Pipe("data/repos/stargazers/", shuffle=True, limit=n_limit)(compute, -1))

print(df.columns)
cx = pd.DataFrame(df["login"].value_counts())
cx.columns = ["Unique stared repos"]
cx = cx.reset_index()
cx = cx.rename(columns={"index": "username"})

cx.to_csv(f_save, index=False)

base_username = "https://github.com"
cx["username"] = cx["username"].apply(lambda x: f"[{x}]({base_username}/{x}/)")
cx = cx.set_index("username")

cx = cx.sort_values("Unique stared repos", ascending=False)
print(cx[:20])
