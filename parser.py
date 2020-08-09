import requests
from bs4 import BeautifulSoup
import json
import os
import time
import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

start = time.time()

req = requests.get('https://news.google.com/articles/CAIiEOiW0x9C3ZmcabpDppguU_AqFQgEKg0IACoGCAowrqkBMKBFMLKAAg?hl=en-US&gl=US&ceid=US%3Aen')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    '.fs-article p'
)

data = {}

for title in my_titles:
    data[title.text] = title.get_text()

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)

later = time.time()
print("google news url")
print(later - start)


header = req.headers

status = req.status_code

is_ok = req.ok

