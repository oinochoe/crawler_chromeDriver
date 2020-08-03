import requests
from bs4 import BeautifulSoup
import json
import os
import timeit

start_time = timeit.default_timer()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sum = 0

for i in range(100000000):
    sum += i


req = requests.get('https://www.washingtonpost.com/us-policy/2020/08/03/congress-stimulus-coronavirus-trump/')

terminate_time = timeit.default_timer()
print("%fsec" % (terminate_time - start_time))


html = req.text


soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    '.font--body.font-copy'
)

data = {}

for title in my_titles:
    data[title.text] = title.get_text()

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)

header = req.headers

status = req.status_code

is_ok = req.ok

