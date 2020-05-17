import requests
from bs4 import BeautifulSoup
import openpyxl as xl

# 새로운 워크북 만들기
wb = xl.Workbook()
# 현재 시트 선택
sheet = wb.active
# 헤더 추가하기
sheet.append(["제목", "채널", "재생 수", "좋아요 수"])

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

# 1위 - 100위 컨테이너 선택자: dl.cds_info
clips = html.select("dl.cds_info")

for cl in clips:
    # 수정된 부분
    title = cl.select_one("dt.title").text.strip()
    chn = cl.select_one("dd.chn").text.strip()
    hit = cl.select_one("span.hit").text.strip()
    like = cl.select_one("span.like").text.strip()

    print("제목", title)
    print("채널명", chn)
    print(hit)
    print(like)
    print("="*50)

    # 워크북에 데이터를 추가합니다.
    # append함수에는 리스트 형식으로 데이터를 넣어줍니다.
    sheet.append([title, chn, hit, like])

# 데이터 수집결과를 navertv.xlsx
wb.save("navertv.xlsx")