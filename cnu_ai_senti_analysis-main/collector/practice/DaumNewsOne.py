# 파이썬의 경로
# 1. 프로젝트(cnu_ai_senti_analysis-main)
#  2. python package(collector)
#   3. python file(test.py, DaumNewsOne.py.)
# - python package : python file들을 모아두는 폴더
#                   폴더아이콘안에 구멍 뚫려있음

# import와 Library(module)
# - Python 코드를 직접 작성해서 개발할수도 있지만
# - 다른개발자가 이미 만들어 놓은 코드를 사용하면 편리함
# - 이미 개발되어있는 코드들의 묶음 = 라이브러리(module)
#  1. built in library : Python 설치하면 자동으로 제공
#                      예: math, sysm os 등
#  2. 외부 Library : 여러분이 직접 추가해서 사용!
#                     예 : requests, beautifilsoup4

# Library를 사용하기위해서는 import 작업 진행
# - import는 도서관에서 필요한 책을 빌려오는 개념



import requests # 책 전체를 빌려옴
from bs4 import BeautifulSoup   # bs4라는 책에서 BeautifulSoup 1개 파트만 빌려옴


# 목표 : Daum 뉴스 웹페이지의 제목과 본문 데이터를 수집!
# 1. url: https://v.daum.net/v/20221006105548970
url = 'https://v.daum.net/v/20221006105548970'
# 2. requests로 해당 url의 html 전체 코드를 수집
result = requests.get(url)
# print(result.text)
# 3. bautifulsoup을 통해서 '제목과 본문'만 추출
doc = BeautifulSoup(result.text, 'html.parser')
# python은 []: List Type
# index 0 1 2 3 4
#    - [5, 6, 9, 10, 15] : List 내에는 다양한 데이터 저장 가능
title = doc.select('h3.tit_view')[0].get_text()

# html -> tag + 선택자
#   - tag : 기본적으로 정의 되있음(h3, p, div, span, ...)
contents = doc. select('section p') # section 태그를 부모를 둔 모든 저
print(f'뉴스제목:{title}')

# contents = [<p1>, <p2>, <p3>, <p4>, ...] : 복수의 본문 포함
# <p1> = <p>1111111111111111111111111111</p>
# <p2> = <p>22222222222222222222222222</p>
content = ''
for line in contents
    content += line.get_text()
print(f'뉴스본문: {content}')


