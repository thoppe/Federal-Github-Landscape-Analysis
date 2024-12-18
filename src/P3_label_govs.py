import pandas as pd
import re
from urlextract import URLExtract
from urllib.parse import urlparse

"""
Scan through the repos that have .gov in them. Identify those that are likely
not US based, e.g. vmr.gov.ua or sindhpolice.gov.bk. Need to look in all the
categories that have a .gov and take special care with the emails.

This still needs human intervention, the organization can be lying, it could
be a state or local government or it could be a made up URL like
icecream.joebiden.gov
"""

f_data = "data/raw_extracted_govs.csv"
f_save = "data/US_filtered_govs.csv"

df = pd.read_csv(f_data).set_index("id")

data_columns = ["email", "blog", "description", "company", "location", "name"]

extractor = URLExtract()
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

for key in data_columns:
    df[key] = df[key].astype(str)

col0 = []
col1 = []
for _, row in df.iterrows():

    is_US_gov = False
    target_gov_URLs = []

    for key in data_columns:
        text = row[key]
        if ".gov" not in text:
            continue

        emails = re.findall(email_pattern, text)
        email_urls = [x.split("@")[1] for x in emails]

        urls = extractor.find_urls(text)
        urls += email_urls

        if not urls:
            continue

        parsed = [urlparse(url) for url in urls]
        domains = [url.netloc if url.netloc else url.path for url in parsed]

        is_TLD_gov = [url for url in domains if url.split(".")[-1] == "gov"]

        if not is_TLD_gov:
            continue

        is_US_gov = True
        target_gov_URLs.extend(is_TLD_gov)

    # Remove duplicates
    target_gov_URLs = list(set(target_gov_URLs))

    col0.append(is_US_gov)
    col1.append(";".join(target_gov_URLs))

df["is_US_gov"] = col0
df.insert(0, "potential_URLS", col1)

df = df[df["is_US_gov"]]
del df["is_US_gov"]

print(df)
df.to_csv(f_save)
