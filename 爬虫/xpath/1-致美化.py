#import os
import requests
from lxml import etree


def main():
    # 1. 获取页面源代码
    # 1.1 先定义一个变量来描述要爬的网址
    url = 'https://zhutix.com/mobile/'

    # 2.2 再定义一个变量来处理可能遇到的反爬
    headers = {
        # 更好的模拟浏览器
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0'
    }

    # 1.3 使用requests模拟浏览器来获取源代码
    r = requests.get(url, headers=headers).text

    # 2. 提取图片数据
    # 2.1 数据类型的转换 str --> xml
    ret = etree.HTML(r)

    # 2.2 通过xpath表达式拿所有的大标签
    # li_list = ret.xpath('//li[@class="post-list-item item-post-style-12"]')
    li_list = ret.xpath('//div[@id="post-list"]/ul/li')

    n = 1
    # 2.3 遍历大标签, 来拿里面的图片数据
    for li in li_list:
        # 图片地址
        # li.xpath('./div/div/a/img')
        src = li.xpath('.//img/@src')  # 当前路径下, 任意位置的img标签, 它里面的src属性
        src = ''.join(src)

        # 图片名字
        #name = li.xpath('.//a[@class="imglist-char shu"]/text()')
        #name = ''.join(name)

        print(src)

        # 3. 保存图片
        #img_code = requests.get(src).content

        #with open(f'{word}/{name}.jpg', 'wb') as f:
        #    f.write(img_code)

        #n += 1


if __name__ == '__main__':
    #word = '致美化'
    #if not os.path.exists(word):
    #    os.mkdir(word)

    main()
