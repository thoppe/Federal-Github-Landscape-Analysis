import pandas as pd
from pathlib import Path
import time
import os
from tqdm import tqdm
import tempfile
import requests
import shutil
from dspipe import Pipe

f_save = "data/repos_by_cumulative_popularity.csv"
sleep_time = 2.5
min_number_of_stars = 1

load_dest = "data/organizations_repolist"
df = pd.concat(Pipe(load_dest, input_suffix=".csv")(pd.read_csv))
df = df.sort_values("stargazers_count", ascending=False)
df.to_csv(f_save, index=False)


def download_file(url, output_path):
    try:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_path = temp_file.name

            # Stream the download
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Write content to the temporary file
            for chunk in tqdm(response.iter_content(chunk_size=8192 * 8)):
                temp_file.write(chunk)

        # Use shutil.move to handle cross-device link issues
        shutil.move(temp_path, output_path)
        print(f"Download completed successfully: {output_path}")

    except Exception as e:
        # Clean up the temporary file if anything goes wrong
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"Download failed: {e}")


"""
Now keep only a subset of repos that are not forks and have at least
five watchers and or stars.
"""

df = pd.read_csv(f_save)
df = df[df["stargazers_count"] > min_number_of_stars]
df = df[~df["fork"]]

# print(df['size'].describe())
total_bytes = int(df["size"].sum())
print(f"Expected space for full clone: {total_bytes:,}")

save_dest = Path("data/clone")

print(f"Total repos: {len(df)}")

for url, branch in tqdm(zip(df["html_url"], df["default_branch"]), total=len(df)):
    _, _, _, user, repo_name = url.split("/")
    dest = save_dest / user
    dest.mkdir(parents=True, exist_ok=True)

    # This one came in through my personal API key, it's not public
    # and it fails the public download.
    if user == "cdcent":
        continue

    f_save = dest / f"{repo_name}.tar.gz"

    if (f_save).exists():
        print(f"✔️  already exists {user}/{repo_name}")
        continue

    print(f_save)

    target = f"https://github.com/{user}/{repo_name}/"
    target += f"archive/refs/heads/{branch}.tar.gz"

    download_file(target, f_save)
    print(f"✔️  finished        {user}/{repo_name}")

    # cmd = f"git clone --depth 1 {url}"
    # os.system(cmd)

    time.sleep(sleep_time)
