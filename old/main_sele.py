# 1. 라이브러리 불러오기
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time

driver = None
html_source = None

# Selenium으로 브라우저 열기
try:
    driver = uc.Chrome(auto_quit=False)
    url = "https://www.kopo.ac.kr/jungsu/content.do?menu=247"
    driver.get(url)

    # 페이지가 로딩되고 JavaScript로 데이터를 가져올 떄까지 대기
    time.sleep(3) # 명시적 대기로 교체할 것

    # 페이지 전체 html 코드 로드
    html_source = driver.page_source

    soup = BeautifulSoup(html_source, 'html.parser')
    print("내ㅐㅐㅐㅐㅐㅐ", soup)

    #print(html_source)
finally:
    if driver:
        driver.quit()
        time.sleep(3)

if html_source:
    # bs4를 통해 html 데이터 사이에서 원하는 데이터 추출하는 단계
    soup = BeautifulSoup(html_source, 'html.parser')
    print("내ㅐㅐㅐㅐㅐㅐ", soup)
else:
    print("오류 발생")