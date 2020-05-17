import requests
from bs4 import BeautifulSoup as bs

query = input('query : ')
url = 'http://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page={page}&q=' + query

for i in range(1, 4):
    url = url.format(page=str(i))
    raw = requests.get(url)

    html = bs(raw.text, 'html.parser')

    lists = html.select('div.cont_inner')

    # print(lists)

    for k in lists:
        title = k.select_one('a.f_link_b').text.strip()
        p = k.select_one('p.f_eb.desc').text.strip()


        print(title, p, sep='\n')
        print()


