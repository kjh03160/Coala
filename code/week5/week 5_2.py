import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve

raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd")
html = bs(raw.text, 'html.parser')

lists = html.select('div.mode-detail')

for i in lists:
    title = i.select_one('h3 > a')
    url = title.attrs['href']
    main_url = "https://www.imdb.com/"

    inner = requests.get(main_url + url)
    innr_html = bs(inner.text, "html.parser")

    img = innr_html.select_one("div.poster img").attrs["src"]
    urlretrieve(img, 'poster/' + title.text.strip()[:4] + '.png')
