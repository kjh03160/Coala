import requests
from bs4 import BeautifulSoup
import openpyxl

keyword = input("검색어를 입력해주세요: ")

try:
    wb = openpyxl.load_workbook("navernews.xlsx")
    sheet = wb.active
    print("불러오기 완료")
except:
    wb = openpyxl.Workbook()
    sheet = wb.active
    #############################################
    # 수정1

    # 파일의 헤더 부분에 "검색어"를 추가해줍니다.
    sheet.append(["검색어", "제목", "언론사"])
    print("새로운 파일을 만들었습니다.")

    #############################################

for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=" + keyword + "&start=" + str(n),
                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너: ul.type01 > li
    # 기사제목: a._sp_each_title
    # 언론사: span._sp_each_source

    # 1. 컨테이너 수집
    articles = html.select("ul.type01 > li")

    # 2. 기사 데이터 수집

    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text

        #############################################
        # 수정2

        # 출력 및 파일 저장 양식에 검색어(keyword)를 추가해줍니다.
        print(keyword, ":", title, source)
        sheet.append([keyword, title, source])

        #############################################

wb.save("navernews.xlsx")