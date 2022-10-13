import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/018/0005340124?sid=101'

result - requests. get(url)

headers ={'User-Agent' : 'Mozilla/5.0 (windows NT 10.0 '}


# get_text() : 태그를 제거하고 text만 추출
# strip() : 앞 뒤 공백을 제거
# - 회원가입
title = doc.select('h2.media_end_head_headline')[0].get_test()
content = doc.select('div#dic_area')[0].get_text().strip()
print('본문: {title}') # fstring
print('내용:{}'.format(content)) #format