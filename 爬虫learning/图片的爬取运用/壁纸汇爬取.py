import os
import requests
from lxml import etree


def main():
    url = 'https://www.bizhihui.com/tags/8Kbizhi/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
    }

    r = requests.get(url, headers=headers).text
    # print(r)

    ret = etree.HTML(r)
    # print(ret)
    li_list = ret.xpath('//ul[@id="item-lists"]/li[@class="item-list masonry-brick"]')
    # print(len(li_list))

    n = 1
    for li in li_list:
        src = li.xpath('.//img/@src')
        src = ''.join(src)
        # print(src)

        name = li.xpath('.//a[@target="_blank"]/text()')
        name = ''.join(name)
        # print(name)

        img_code = requests.get(src).content
        print(img_code)

        with open(f'{word}/{n}.jpg', 'wb') as f:
            f.write(img_code)

        n += 1


if __name__ == '__main__':
    word = '壁纸汇'
    if not os.path.exists(word):
        os.mkdir(word)

    main()
