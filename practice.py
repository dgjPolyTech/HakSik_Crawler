# 라이브러리 불러오기
# requests는 페이지에서 데이터들을 긁어오는 역할, BeautifulSoup는 그걸 보기좋게 파싱하는 역할
import requests
from bs4 import BeautifulSoup

# 크롤링할 목표 사이트의 주소 설정
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"

# 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

# 4. 가져온 HTML을 BeautifulSoup으로 파싱(parsing)하기
# requests로 가져온 데이터는 그저 일렬로 나열된 텍스트들에 불과함. 파싱 과정을 거쳐야, 원하는 요소를 찾기 쉬워짐.
soup = BeautifulSoup(response.text, 'html.parser')
section = soup.find('ul', class_="sa_list") # 가져올 데이터의 태그 유형 및 클래스명을 기입. 이러면 section은 해당하는 데이터들만 모인 변수가 됨.

if(section):
    news_titles = section.find_all('strong', class_="sa_text_strong")

    for title in news_titles:
        print(title.get_text())

else:
    print("뉴스 정보를 찾을 수 없습니다.")