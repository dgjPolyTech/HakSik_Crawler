# 라이브러리 불러오기
# requests는 페이지에서 데이터들을 긁어오는 역할, BeautifulSoup는 그걸 보기좋게 파싱하는 역할
import requests
from bs4 import BeautifulSoup

# 크롤링할 목표 사이트의 주소 설정
url = "https://www.kopo.ac.kr/jungsu/content.do?menu=247"

# 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)
#contents > div > div.meal_box > table.tbl_table.menu > tbody > tr:nth-child(2) > td:nth-child(3) > span
#contents > div > div.meal_box > table.tbl_table.menu > tbody > tr:nth-child(3) > td:nth-child(3) > span

soup = BeautifulSoup(response.text, 'html.parser')
lunchs = soup.select('#contents > div > div.meal_box > table.tbl_table.menu > tbody')

print(lunchs)
# if(section):
#     news_titles = section.find_all('strong', class_="sa_text_strong")

#     for title in news_titles:
#         print(title.get_text())

# else:
#     print("뉴스 정보를 찾을 수 없습니다.")