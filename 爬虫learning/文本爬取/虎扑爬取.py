import requests
from lxml import etree


def main():
    url = 'https://bbs.hupu.com/all-gambia'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
    }
    r = requests.get(url, headers=headers).text
    # print(r)

    ret = etree.HTML(r)
    # print(ret)

    div_list = ret.xpath('//div[@class="text-list-model"]/div')
    # print(len(div_list))

    for div in div_list:
        # 标题
        title = div.xpath('.//span[@class="t-title"]/text()')
        title = ''.join(title)
        # print(title)

        # 点亮数
        light = div.xpath('.//span[@class="t-lights"]/text()')
        light = ''.join(light)
        # print(light)

        # 回复数
        reply = div.xpath('.//span[@class="t-replies"]/text()')
        reply = ''.join(reply)
        # print(reply)

        print(title, light, reply)


if __name__ == '__main__':
    main()
