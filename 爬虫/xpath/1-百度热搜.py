import requests
from lxml import etree  # pip install lxml


def main():
    """
    大标签:
        1. 肯定是相同名字的标签
        2. 一般都是兄弟关系
    :return:
    """
    # 1. 获取页面源代码
    # 1.1 先定义一个变量来描述要爬的网址
    url = 'https://www.baidu.com/'

    # 1.2 再定义一个变量来处理可能遇到的反爬
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0'
    }

    # 1.3 获取源代码 字符串类型
    r = requests.get(url, headers=headers).text

    # 2. 提取数据  xpath表达式==>xml类型   //div[@class="xx"]/text()
    # 2.1 先转换数据类型
    ret = etree.HTML(r)

    # 2.2 拿到所有的大标签
    # li_list = ret.xpath('//li')  # 任意位置的li标签
    li_list = ret.xpath('//ul[@id="hotsearch-content-wrapper"]/li')  # 任意位置的ul标签, 但是id属性的值为xx, 然后再拿下面的子为li的标签

    # 2.3 遍历所有的大标签, 从里面提取数据
    for li in li_list:
        li.xpath('./a/span[@class="title-content-title"]')  # 当前路径下的a标签下的span, 但是名字为xx
        li.xpath('./a/span[2]')  # 当前路径下的a标签下的第2个span标签
        li.xpath('.//span[2]')  # 当前路径下任意位置的span标签, 然后取其中的第2个
        # content = li.xpath('.//span[2]/text()')[0]  # 当前路径下任意位置的span标签, 然后取其中的第2个
        content = li.xpath('.//span[2]/text()')  # 当前路径下任意位置的span标签, 然后取其中的第2个
        content = ''.join(content)
        print(content)


if __name__ == '__main__':
    main()

"""
数字 字符串 列表 元组 集合 字典
"""
