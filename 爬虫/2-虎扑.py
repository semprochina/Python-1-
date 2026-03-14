import requests
from lxml import etree


def main():
    # 1. 获取页面的源代码
    url = 'https://bbs.hupu.com/all-gambia'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
    }

    r = requests.get(url, headers=headers).text

    # 2. 提取数据
    ret = etree.HTML(r)

    div_list = ret.xpath('//div[@class="list-item-wrap"]')

    for div in div_list:
        # 标题
        title = div.xpath('.//span[@class="t-title"]/text()')
        title = ''.join(title)

        # 点亮
        lights = div.xpath('.//span[@class="t-lights"]/text()')
        lights = ''.join(lights)

        # 点赞
        replies = div.xpath('.//span[@class="t-replies"]/text()')
        replies = ''.join(replies)

        print(title, lights, replies)


if __name__ == '__main__':
    main()
