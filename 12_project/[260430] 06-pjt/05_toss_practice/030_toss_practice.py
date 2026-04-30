import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

service = Service("../chromedriver-win64/chromedriver.exe")


def get_stock_code(company_name):
    driver = webdriver.Chrome(service=service)

    # TossInvest 접속
    driver.get("https://www.tossinvest.com/")
    time.sleep(1)

    # body에서 '/' 입력 → 검색창 열기
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys("/")
    time.sleep(1)

    # 검색창에 회사명 입력 후 Enter
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='검색어를 입력해주세요']")
        )
    )
    search_input.send_keys(company_name)
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)

    # /order 페이지로 이동 완료될 때까지 대기
    WebDriverWait(driver, 15).until(EC.url_contains("/order"))

    # 현재 URL에서 종목 코드 추출
    current_url = driver.current_url
    print(current_url)
    stock_code = current_url.split("/")[current_url.split("/").index("stocks") + 1]
    time.sleep(1)

    print(f"종목 코드 추출 완료: {stock_code}")
    driver.quit()
    return stock_code


if __name__ == "__main__":
    # [F101] 사용자로부터 회사명을 입력받는다.
    user_input = input("수집할 회사 이름을 입력하세요: ").strip()

    # [F101] 입력값이 없는 경우 데이터 수집 절차를 수행하지 않는다.
    if not user_input:
        print("[에러] 회사명이 입력되지 않았습니다.")
    else:
        code = get_stock_code(user_input)
