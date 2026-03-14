import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
}

r = requests.get(url, headers=headers).text
# print(r)
soup = BeautifulSoup(r, 'html.parser')
title_list = soup.find_all("span", attrs={'class': 'title'})
for title in title_list:
    if '/' not in title.string:
        print(title.string)
