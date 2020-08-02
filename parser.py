## parser.py
import requests

## HTTP GET Requests
req = requests.get('https://oinochoe.github.io/LandingPage/dist/index.html')

## HTML 소스 가져오기
html = req.text

## HTTP Header 가져오기
header = req.headers

## HTTP Status 가져오기 (200: 정상)
status = req.status_code

## HTTP가 정상적으로 되었는지 (TRUE/FALSE)
is_ok = req.ok

## 위 코드에서 우리가 사용할 것은 HTML 소스를 이용하는 것이므로, html=req.text를 사용하는 것이다.
## requests는 정말 좋은 라이브러리지만, html을 '의미있는', 즉 Python이 이하해는 객체구조로 만들어주지 않는다.
## 위에서 req.text는 pythone의 문자열 (str)을 객체를 변환할 뿐이기 때문에 정보를 추출하기가 어렵다.
