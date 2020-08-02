## parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

## Python 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

## HTTP GET Requests
req = requests.get('http://blog.irangyeongmin.com/')

## HTML 소스 가져오기
html = req.text

## BeautifulSOup으로 html 소스를 python객체로 변환
soup = BeautifulSoup(html, 'html.parser')

## BeautifulSoup select기능을 사용하면 일치하는 모든 객체들을 List로 반환해줌.
my_titles = soup.select(
    'div.PostList__post-list___IWx36 > h2 > a'
)

data = {}

## my_titles는 list 객체
for title in my_titles:
    ## Tag 안의 텍스트
    print(title.test)
    ## Tag의 속성을 가져오기(ex: href속성)
    print(title.get('href'))

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)

## HTTP Header 가져오기
header = req.headers

## HTTP Status 가져오기 (200: 정상)
status = req.status_code

## HTTP가 정상적으로 되었는지 (TRUE/FALSE)
is_ok = req.ok

## 위 코드에서 우리가 사용할 것은 HTML 소스를 이용하는 것이므로, html=req.text를 사용하는 것이다.
## requests는 정말 좋은 라이브러리지만, html을 '의미있는', 즉 Python이 이하해는 객체구조로 만들어주지 않는다.
## 위에서 req.text는 python의 문자열(str) 객체를 변환할 뿐이기 때문에 정보를 추출하기가 어렵다.
## 따라서 BS4를 이용하자. BS4는 html 코드를 Python이 이해하는 객체 구조로 변화하는 Parsing을 맡고있다.
## pip install bs4
## BeautifulSoup을 직접 치는 것보다 bs4라는 wrapper 라이브러리를 통해 설치하는 방법이 더 쉽고 안전
