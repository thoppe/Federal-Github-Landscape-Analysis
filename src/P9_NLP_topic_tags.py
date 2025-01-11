import pandas as pd
from pathlib import Path
from dspipe import Pipe
import json
import re
from openai import OpenAI
import os
from pydantic import BaseModel


class CategoryResponse(BaseModel):
    categories: list[str]


# Retrieve the OpenAI API key from environment variables
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)

# Save the responses so we don't have to rerun
# cache = Cache("data/cache/GPT_summerization")

cats = pd.read_csv("data/Topics_Descriptions.csv")


def remove_html_tags(text):
    """Remove HTML tags from the text."""
    html_pattern = re.compile(r"<.*?>")
    return re.sub(html_pattern, "", text)


def remove_markdown_syntax(text):
    """Remove common Markdown syntax from the text."""
    markdown_patterns = [
        r"\!\[.*?\]\(.*?\)",  # Images
        r"\[.*?\]\(.*?\)",  # Links
        r"`{1,3}.*?`{1,3}",  # Inline code and code blocks
        r"\*{1,2}.*?\*{1,2}",  # Bold and italic
        r"_.*?_",  # Italic
        r"\~{2}.*?\~{2}",  # Strikethrough
        r"^#{1,6}\s+",  # Headers
        r"^>\s+",  # Blockquotes
        r"^\s*[-*+]\s+",  # Unordered lists
        r"^\s*\d+\.\s+",  # Ordered lists
        r"\-{3,}",  # Horizontal rules
    ]

    for pattern in markdown_patterns:
        text = re.sub(pattern, "", text, flags=re.MULTILINE)

    return text


def compute(full_name):

    org_name, repo_name = full_name.split("/")
    f1 = Path("data/repos/topic_tags/") / f"{org_name}_{repo_name}.json"
    f1.parents[0].mkdir(exist_ok=True, parents=True)

    if f1.exists():
        return

    # Get the README
    f_readme = Path("data/repos/readme") / Path(org_name) / (repo_name + ".md")
    assert f_readme.exists()
    rtxt = open(f_readme).read()

    rtxt = remove_html_tags(rtxt)
    rtxt = remove_markdown_syntax(rtxt)

    readme_tokens = 100
    rtxt = " ".join(rtxt.split()[:readme_tokens])
    desc = df.loc[full_name]["description"]

    model_name = "gpt-4o-mini"

    categories = cats.set_index("Topic").to_string()

    prompt = f"Assign the categories to the project description. The categories are\n{categories}"

    text = f"{desc}\n{rtxt}"

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": text},
    ]

    chat_completion = client.beta.chat.completions.parse(
        messages=messages,
        model=model_name,
        response_format=CategoryResponse,
    )

    response = chat_completion.choices[0].message.content
    response = json.loads(response)
    response["full_name"] = full_name

    input_tokens = chat_completion.usage.prompt_tokens
    output_tokens = chat_completion.usage.completion_tokens

    input_cost = 0.150 * input_tokens / 1_000_000
    output_cost = 0.150 * output_tokens / 1_000_000

    cost = input_cost + output_cost
    response["cost"] = cost

    named_cats = set(cats["Topic"].tolist())

    for key in response["categories"]:
        if key not in named_cats:
            print("** ERROR", full_name)
            print(response)
            print(key, named_cats)
            return

    js = json.dumps(response, indent=2)
    with open(f1, "w") as FOUT:
        FOUT.write(js)

    print(js)


f_repos = "data/repos_by_cumulative_popularity.csv"
df = pd.read_csv(f_repos)
df = df[~df["fork"]]
df = df[df["stargazers_count"] >= 1]

df = df.set_index("full_name")
P = Pipe(df.index, shuffle=True)(compute, 1)
