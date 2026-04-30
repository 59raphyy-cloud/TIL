import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


service = Service("../chromedriver-win64/chromedriver.exe")


def search_company(company_name):
    driver = webdriver.Chrome(service=service)

    # [F103] 입력된 회사명을 기준으로 외부 증권 서비스에서 회사를 검색한다.
    driver.get("https://www.tossinvest.com/")
    time.sleep(1) 

    # [그림3] 토스증권 홈페이지 검색창 호출 로직
    # body 태그를 선택하여 '/' 입력 → 검색창 열림
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys("/")
    time.sleep(1)

    # [그림4] 모달창 내 검색어 입력 
    # 검색 입력창 요소를 찾고, 회사명을 입력 후 Enter 입력
    # XPATH //태그명[@속성명='속성값']
    # //div[@id='login-box'] (ID가 login-box인 div)
    # //*[text()='확인'] (태그 상관없이 '확인'이라는 글자가 적힌 모든 것)
    search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='검색어를 입력해주세요']")))
    search_input.send_keys(company_name)
    # [F103] 검색 결과 중 최상단에 노출된 회사를 자동으로 선택한다.
    #   예시) 삼성 검색 시 삼성전자 자동 검색
    search_input.send_keys(Keys.ENTER)
    time.sleep(3)

    # [F103] 스트리밍 기능을 활용하여 크롤링 진행 상황을 적절히 출력한다.
    print(f"'{company_name}' 검색 완료")
    driver.quit()


if __name__ == "__main__":
    # [F101] 사용자로부터 회사명을 입력받는다.
    user_input = input("수집할 회사 이름을 입력하세요: ").strip()

    # [F101] 입력값이 없는 경우 데이터 수집 절차를 수행하지 않는다.
    if not user_input:
        print("[에러] 회사명이 입력되지 않았습니다. 프로그램을 종료합니다.")
    else:
        # 검증 통과 시 함수 호출
        search_company(user_input)
