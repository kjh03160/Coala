import requests
from bs4 import BeautifulSoup

#############################################
# 추가1

# openpyxl 패키지 불러오기
import openpyxl

# 엑셀 파일 작성을 위해서 Workbook, Sheet 구성해주기
wb = openpyxl.Workbook()
sheet = wb.active

# 파일에 헤더 입력해주기
sheet.append(["제목", "저자"])
#############################################

for p in range(1, 6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(p),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    books = html.select("div.lst_thum_wrap li")
    for b in books:
        title = b.select_one("a strong").text
        author = b.select_one("span.writer").text

        print(title, author)
        #############################################
        # 추가2

        # 수집한 제목, 저자를 엑셀 파일에 추가하기
        sheet.append([title, author])
        #############################################

#############################################
# 추가3

# naverebook.xlsx 엑셀파일 저장하기
wb.save("naverebook.xlsx")
#############################################