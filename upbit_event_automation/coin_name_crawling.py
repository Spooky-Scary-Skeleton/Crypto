import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

#브라우저 안띄우기
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')

#웹 드라이버와 URL 설정
driver = webdriver.Chrome(options=options)
driver.get('https://upbit.com/event')

time.sleep(4)

#BS 적용
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
coin_name_source = soup.select('#UpbitLayout > div:nth-child(4) > div > section > article.eventAirDrop__aside.eventAirDropDesc > div.eventAirDropDesc__table > dl:nth-child(2) > dd')

#이벤트 코인명 출력
coin_name_str = str(coin_name_source)
filt = ['[<dd>', '</dd>]']

for word in filt:
    coin_name_str = coin_name_str.replace(word,'')

print('현재 업비트 이벤트 코인은 {} 입니다.'.format(coin_name_str))
