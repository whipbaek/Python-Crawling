import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

chromedriver = 'C:\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080) # 창 사이즈
driver.get('https://knuin.knu.ac.kr/public/stddm/lectPlnInqr.knu')

print("+" * 100)
print(driver.title)  # 크롤링한 페이지의 title 정보
print(driver.current_url)  # 현재 크롤링된 페이지의 url
print("경북대 강의계획서 크롤링")
print("-" * 100)
'''
element = driver.find_element(By.ID,"udcBtns_btnSync1")
element.click()
'''
time.sleep(3)  # 페이지 로딩 시간을 고려

# 검색 조건 셋팅 하기
select = Select(driver.find_element(By.ID, "schSbjetCd1"))
select.select_by_visible_text("대학")  # select_by_index,  select_by_value 등 다른 값 으로도 검색 가능
time.sleep(0.5)

select = Select(driver.find_element(By.ID, "schSbjetCd2"))
select.select_by_visible_text("IT대학")
time.sleep(0.5)

select = Select(driver.find_element(By.ID, "schSbjetCd3"))
select.select_by_visible_text("컴퓨터학부")
time.sleep(0.5)

driver.find_element(By.ID, "btnSearch").click()
time.sleep(0.5)

driver.execute_script("window.scrollTo(0, 1000)") # 외부 스크롤 내리기
time.sleep(1)

elem = driver.find_element(By.ID, f"grid01_body_tbody")

for i in range(0, 13):
    print(elem.find_element(By.ID, f"grid01_cell_{i}_7").find_element(By.TAG_NAME, "nobr").text, end=', ')
    print(elem.find_element(By.ID, f"grid01_cell_{i}_12").find_element(By.TAG_NAME, "nobr").text, end=', ')
    print(elem.find_element(By.ID, f"grid01_cell_{i}_13").find_element(By.TAG_NAME, "nobr").text, end=', ')
    print(elem.find_element(By.ID, f"grid01_cell_{i}_14").find_element(By.TAG_NAME, "nobr").text, end=', ')
    print(elem.find_element(By.ID, f"grid01_cell_{i}_15").find_element(By.TAG_NAME, "nobr").text)
    print()

time.sleep(2)

itemlist = driver.find_element(By.ID,"grid01_scrollY_div")
driver.execute_script("arguments[0].scrollBy(0, 600)", itemlist) # 내부 스크롤 내리기