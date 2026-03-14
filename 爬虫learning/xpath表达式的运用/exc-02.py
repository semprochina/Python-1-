""""
    1.获取源代码
    2.获取数据
    3.保存数据
"""

import requests
from lxml import etree


def main():
    url = 'https://www.baidu.com/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
    }
    '字符串类型'
    response = requests.get(url, headers=headers).text
    'print(response)'  # 验证输出源代码
    # 2.提取数据Element span at 0x20633b34800
    'xpath表达式==>xml类型'  # //div[@class="xx"]/text()

    # 2.1转换数据类型
    ret = etree.HTML(response)
    print(ret)
    li_list = ret.xpath('//ul[@id="hotsearch-content-wrapper"]/li')  # 任意位置的ul标签，但是id的属性值为xx
    print(len(li_list))  # 2.2拿到大标签

    # 2.3遍历所有大标签，获取数据
    for li in li_list:
        li.xpath('./a/span[@class="title-content-title"]')
        # li.xpath('./a/span[2]')
        # li.xpath('.//span[2]')
        content = li.xpath('.//span[2]/text()')
        content = ''.join(content)
        print(content)


if __name__ == '__main__':
    main()
