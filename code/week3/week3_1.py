import requests
from bs4 import BeautifulSoup

url = "https://tv.naver.com/r"
raw = requests.get(url)

bs = BeautifulSoup(raw.text, 'html.parser')

divs = bs.select("div.inner")
print(divs)

for i in divs:
    title = i.select_one("dt.title").text.strip()
    chn = i.select_one("dd.chn").text.strip()
    hit = i.select_one("span.hit").text.strip()
    like = i.select_one("span.like").text.strip()

    print(title, chn, hit, like, sep="\n")
    print()

divs = bs.select("div.cds")

for i in divs:
    title = i.select_one("dt.title").text.strip()
    chn = i.select_one("dd.chn").text.strip()
    hit = i.select_one("span.hit").text.strip()
    like = i.select_one("span.like").text.strip()

    print(title, chn, hit, like, sep="\n")
    print()