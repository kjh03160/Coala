import requests
from bs4 import BeautifulSoup as bs

for i in range(1, 4):
    url = "https://news.ycombinator.com/news?p="
    url += str(i)
    html = requests.get(url)
    html = bs(html.text, 'html.parser')

    lists = html.select("tr.athing")

    for i in lists:
        rank = i.select_one("span.rank").text
        title = i.select_one("a.storylink").text
        print(rank, title, sep='\n')

        print()