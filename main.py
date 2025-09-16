from selenium import webdriver
from selenium_stealth import stealth
from bs4 import BeautifulSoup
import time

driver = None
html_source = None

try:
    # Chrome 드라이버 실행 관련 옵션 설정
    options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=options)

    # Stealth 기능 적용 
    # 해당 설정을 통해 봇 감지 옵션을 피할 수 있음.
    stealth(driver,
            languages=["ko-KR", "ko"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    url = "https://www.kopo.ac.kr/jungsu/content.do?menu=247"
    print("페이지 접속 중...")
    driver.get(url)
    time.sleep(2)

    html_source = driver.page_source

except Exception as e:
    print(f"오류가 발생했습니다: {e}")

finally:
    if driver:
        driver.quit()

if html_source:
    print("데이터 수집 완료. 가공 시작...")
    soup = BeautifulSoup(html_source, 'html.parser')
    arr_brakfast_menus = []
    arr_lunch_menus = []
    arr_dinner_menus = []

    # 학식 메뉴 정보 수집
    for i in range(1, 6):
        menu_row_brakfast = soup.select_one(f'#contents > div > div.meal_box > table.tbl_table.menu > tbody > tr:nth-child({i}) > td:nth-child(2)').text.replace('\n', '')
        menu_row_lunch = soup.select_one(f'#contents > div > div.meal_box > table.tbl_table.menu > tbody > tr:nth-child({i}) > td:nth-child(3)').text.replace('\n', '')
        menu_row_dinner = soup.select_one(f'#contents > div > div.meal_box > table.tbl_table.menu > tbody > tr:nth-child({i}) > td:nth-child(4)').text.replace('\n', '')

        arr_brakfast_menus.append(menu_row_brakfast)
        arr_lunch_menus.append(menu_row_lunch)
        arr_dinner_menus.append(menu_row_dinner)

    print("오늘의 조식: "+arr_brakfast_menus[0])
    print("오늘의 중식: "+arr_lunch_menus[0])
    print("오늘의 석식: "+arr_dinner_menus[0])
else:
    print("오류: HTML 소스를 가져오지 못했습니다.")
