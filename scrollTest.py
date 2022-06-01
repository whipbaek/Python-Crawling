import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "각자의 User-Agent를 넣어주자",
    "Accept-Language": "ko-KR,ko"
}

from selenium import webdriver

browser = webdriver.Chrome('C:\chromedriver.exe')
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

prev_height = browser.execute_script("return document.body.scrollHeight")
print("prev :" , prev_height)

# 웹페이지 맨 아래까지 무한 스크롤
while True:
    # 스크롤을 화면 가장 아래로 내린다
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(2)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    print("curr : " , curr_height)

    if (curr_height == prev_height):
        break
    else:
        prev_height = browser.execute_script("return document.body.scrollHeight")