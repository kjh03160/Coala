import requests
from bs4 import BeautifulSoup
import openpyxl as xl

wk = xl.Workbook()
header = ['제목', '내용']

sheet = wk.active
sheet.append(header)

for n in range(1, 4):
    raw = requests.get("https://search.daum.net/search?w=news&q=코알라&p="+str(n))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.wrap_cont")

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb.desc").text

        print(title)
        print(summary)

        sheet.append([title, summary])
        print("="*50)

wk.save('ch2.xlsx')