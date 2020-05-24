import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve


#  영화의 제목 / 평점 / 장르 / 감독 / 배우
url = "http://ticket2.movie.daum.net/Movie/MovieRankList.aspx"

raw = requests.get(url)
html = bs(raw.text, "html.parser")

mv_list = html.select("div.desc_boxthumb")
main_url = "https://movie.daum.net/"

for i in mv_list:
    title = i.select_one("div.desc_boxthumb > strong.tit_join > a")
    url = title.attrs['href']

    title_txt = title.text.strip()
    rate = i.select_one("div.raking_grade > em").text.strip()

    inner = requests.get(url)
    inner_html = bs(inner.text, 'html.parser')

    genre = inner_html.select("dd.txt_main")[0].text.strip()

    text_ = inner_html.select("dd.type_ellipsis")

    try:
        print("제목:", title_txt)
        print("평점:", rate)
        print("장르:", genre)
        director = text_[0].text.split(")")[1].strip().replace("\t", "")
        star = text_[1].text.split(")")[1].strip().replace("\t", "")
        print("감독:", director)
        print("주연:", star)

    except:
        pass
    print()



