import bs4
import pandas as pd

with open("code.gov.html") as FIN:
    soup = bs4.BeautifulSoup(FIN.read(), "lxml")

# with open("code2.gov.html", 'w') as FOUT:
#    FOUT.write(soup.prettify())

data = []
for a in soup.find_all("a", attrs={"href": True}):
    link = a["href"]
    if "github.com" not in link:
        continue
    if a.parent.name != "span":
        continue
    block = a.parent.parent.parent.parent.parent.parent
    name = block.find("h3").get_text()
    print(link, name)
    data.append({"agency": name, "url": link})

df = pd.DataFrame(data)
print(df)

df.to_csv("agencies_org_codegov.csv", index=False)
