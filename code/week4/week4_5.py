import requests
from bs4 import BeautifulSoup
import openpyxl as xl

# 입력문(input)을 활용해서 검색어를 입력받습니다.
keyword = input("검색어를 입력해주세요: ")

wb = xl.Workbook()
sheet = wb.active
sheet.append(["제목", "언론사"])
#############################################

keyword = input("검색어를 입력해주세요: ")

# 반복1: 기사번호를 변경시키면서 데이터 수집을 반복하기
# 1 ~ 100까지 10단위로 반복(1, 11, ..., 91)
for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=" + keyword + "&start=" + str(n),
                       headers={'User-Agent': 'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")

    articles = html.select("ul.type01 > li")

    # 반복2: 기사에 대해서 반복하면 세부 정보 수집하기
    # 리스트를 사용한 반복문으로 모든 기사에 대해서 제목/언론사 출력
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text

        print(title, source)
        #############################################
        # 추가2

        # 수집한 제목, 언론사를 엑셀 파일에 써줍니다.
        sheet.append([title, source])
        #############################################

#############################################
# 추가3

# 작성한 워크북(엑셀파일)을 navertv.xlsx로 저장합니다.
wb.save("navertv.xlsx")
#############################################