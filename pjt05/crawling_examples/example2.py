from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_google_data(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    # Chrome 옵션 설정
    options = Options()
    options.add_argument('--headless')  # 브라우저를 숨기고 백그라운드에서 실행

    # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser")

    # div 태그 중 id 가 result-stats 인 요소 검색
    result_stats = soup.select_one("div#result-stats")
    print(result_stats.text)

    driver.quit()

# 검색 키워드 설정
keyword = "파이썬"
get_google_data(keyword)

