import requests
from bs4 import BeautifulSoup
import json
import os
import timeit

start_time = timeit.default_timer()

sum = 0

for i in range(100000000):
    sum += i


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://news.google.com/articles/CBMiMWh0dHBzOi8vd3d3LmJiYy5jb20vbmV3cy93b3JsZC11cy1jYW5hZGEtNTM2MjY1NDbSATVodHRwczovL3d3dy5iYmMuY29tL25ld3MvYW1wL3dvcmxkLXVzLWNhbmFkYS01MzYyNjU0Ng?hl=en-US&gl=US&ceid=US%3Aen')

html = req.text

soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    '.story-body__list-item a'
)

data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)

terminate_time = timeit.default_timer()
print("%fsec" % (terminate_time - start_time))

header = req.headers

status = req.status_code

is_ok = req.ok

