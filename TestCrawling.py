import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\chromedriver.exe')
driver.maximize_window()
driver.get('https://knuin.knu.ac.kr/public/stddm/lectPlnInqr.knu')

print("+" * 100)
print(driver.title)  # 크롤링한 페이지의 title 정보
print(driver.current_url)  # 현재 크롤링된 페이지의 url
print("경북대 강의 계획서 크롤링")
print("-" * 100)

f = open('TestCrawling.txt', 'w')

time.sleep(3)  # 페이지 로딩 시간을 고려

# 검색 조건 셋팅 하기
select = Select(driver.find_element(By.ID, "schSbjetCd1"))
select.select_by_visible_text("대학")  # select_by_index,  select_by_value 등 다른 값 으로도 검색 가능
time.sleep(0.5)

select = Select(driver.find_element(By.ID, "schSbjetCd2"))
select.select_by_visible_text("IT대학")
time.sleep(0.5)

# IT 대학들 모두 크롤링
for i in range(0, 19):
    if i == 3 or (8 <= i <= 15):  # 융복합관 수업이 없는 과들 패스!
        continue
    select = Select(driver.find_element(By.ID, "schSbjetCd3"))
    select.select_by_index(i)
    time.sleep(0.5)

    driver.find_element(By.ID, "btnSearch").click()
    time.sleep(0.5)

    driver.execute_script("window.scrollTo(0, 1000)")  # 외부 스크롤
    time.sleep(1)

    elem = driver.find_element(By.ID, f"grid01_body_tbody")

    # 내부 스크롤 element
    itemList = driver.find_element(By.ID, "grid01_scrollY_div")

    classList = []
    escapeCnt = 0

    while True:
        j = 0
        possible = True
        try:
            while True:

                seq = elem.find_element(By.ID, f"_headerRowNumber_bodyRow_{j}").text
                if escapeCnt > 10:
                    possible = False
                    break

                if seq in classList:
                    j += 1
                    continue

                classList.append(seq)

                # 강의 번호
                print(seq)
                # f.write(seq)
                # f.write('\n')

                print(elem.find_element(By.ID, f"grid01_cell_{j}_7").find_element(By.TAG_NAME, "nobr").text)  # 강의명
                f.write(elem.find_element(By.ID, f"grid01_cell_{j}_7").find_element(By.TAG_NAME, "nobr").text)
                f.write('\n')

                times = elem.find_element(By.ID, f"grid01_cell_{j}_13").find_element(By.TAG_NAME, "nobr").text
                timeList = times.split(',')
                for a in timeList:
                    print(a)
                    f.write(a)
                    f.write('\n')

                print(elem.find_element(By.ID, f"grid01_cell_{j}_14").find_element(By.TAG_NAME, "nobr").text)  # 건물 명
                f.write(elem.find_element(By.ID, f"grid01_cell_{j}_14").find_element(By.TAG_NAME, "nobr").text)
                f.write('\n')
                print(elem.find_element(By.ID, f"grid01_cell_{j}_15").find_element(By.TAG_NAME, "nobr").text)  # 호수 명
                f.write(elem.find_element(By.ID, f"grid01_cell_{j}_15").find_element(By.TAG_NAME, "nobr").text)
                f.write('\n')
                f.write('\n')

                # time.sleep(0.2)
                j += 1
                print()
        # 현재 스크롤에서 데이터를 모두 크롤링 하였다면
        except NoSuchElementException as e:
            # print("theres no element!, should scroll more")
            driver.execute_script("arguments[0].scrollBy(0, 320)", itemList)  # 내부 스크롤
            escapeCnt += 1

        if not possible:
            print("Crawling end")
            break

    time.sleep(1.5)
