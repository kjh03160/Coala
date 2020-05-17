import requests
from bs4 import BeautifulSoup as bs

for i in range(1, 5):
    url = 'https://series.naver.com/ebook/top100List.nhn?page='
    url += str(i)

    raw = requests.get(url)
    html = bs(raw.text, 'html.parser')

    lists = html.select('div.lst_thum_wrap li')
    for i in lists:
        title = i.select_one('strong').text
        writer = i.select_one('span.writer').text

        print(title, writer, sep='\n')
        print()