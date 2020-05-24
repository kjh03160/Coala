import requests
from bs4 import BeautifulSoup as bs

raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd")
html = bs(raw.text, 'html.parser')

lists = html.select('div.mode-detail')

for i in lists:
    title = i.select_one('h3>a').text.strip()
    dir_stars = i.select('p')[2]

    text = dir_stars.text.strip().replace("\n", "")

    genre = i.select_one('span.genre').lowercase()

    if 'action' in genre:
        continue

    print('Title:', title)
    print(text)

    try:
        rate = i.select_one('span.ipl-rating-star__rating')
        print('rate:', rate)

    except:
        pass

    print()


