import os
import requests
from lxml import etree


class SimpleSpider:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def fetch(self, url):
        response = requests.get(url, headers=self.headers)
        response.encoding = 'utf-8'
        return response.text

    def parse(self, html, xpath_expr):
        tree = etree.HTML(html)
        return tree.xpath(xpath_expr)

    def save(self, data, filename):
        os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)


if __name__ == '__main__':
    spider = SimpleSpider()
    url = 'https://example.com'

    html = spider.fetch(url)
    titles = spider.parse(html, '//title/text()')

    for title in titles:
        print(title)
        spider.save(title, 'output/result.txt')