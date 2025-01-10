import pandas as pd
from dspipe import Pipe


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


df = pd.concat(Pipe("data/repos/contributors/", limit=None)(compute, -1))
print(len(df))
print(df)

cx = df["login"].value_counts()
print(cx[:20])
print(len(cx))
