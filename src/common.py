import os
import itertools
import time

"""
Common helper code across the data pulls from github
"""

# Set these as needed!
ENV_tokens = ["GITHUB_TOKEN", "GITHUB_TOKEN2", "GITHUB_TOKEN3"]

headers = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

tokens = []
for key in ENV_tokens:
    val = os.environ.get(key)
    if not val:
        print(f"Error: {val} environment variable is not set.")
    tokens.append(val)
tokens = itertools.cycle(tokens)

#########################################################################


def check_remaining(response):
    reset_time = int(response.headers.get("X-RateLimit-Reset", time.time() + 60))
    sleep_seconds = max(reset_time - int(time.time()), 0)
    remaining_requests = response.headers.get("X-RateLimit-Remaining")

    print(f"Remaining requests {remaining_requests}, time left {sleep_seconds}")
    return sleep_seconds
