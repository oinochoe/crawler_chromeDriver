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

req = requests.get('https://www.bbc.com/news/world-us-canada-53626546')

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

