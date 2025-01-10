import pandas as pd

f_repos = "data/repos_by_cumulative_popularity.csv"
df = pd.read_csv(f_repos)


df = df.sort_values("size", ascending=False)

print(df.columns)
cols = ["full_name", "description", "size", "stargazers_count", "language"]
df = df[cols]

base_username = "https://github.com"
df["Repository"] = df["full_name"].apply(lambda x: f"[{x}]({base_username}/{x}/)")
df = df.rename(columns={"full_name": "Repository"})
df = df.rename(columns=lambda x: x.title())
df = df.set_index("Repository")

print(df[:20].to_string())

exit()


##########################################################################

df = df.sort_values("stargazers_count", ascending=False)

print(df.columns)
cols = ["full_name", "description", "size", "stargazers_count", "language"]
df = df[cols]

base_username = "https://github.com"
df["Repository"] = df["full_name"].apply(lambda x: f"[{x}]({base_username}/{x}/)")
df = df.rename(columns={"full_name": "Repository"})
df = df.rename(columns=lambda x: x.title())
df = df.set_index("Repository")

print(df[:20].to_string())
