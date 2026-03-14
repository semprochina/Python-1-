'''
防盗链：
    1. 请求头中添加Referer ---> 限制   在img_code = requests.get(src，headers=headers).content
    2. 请求头中添加User-Agent ---> 模拟浏览器
'''
# 通常防盗链为本身url或者IP大网址


import os
import requests
from lxml import etree


def main():
    url = 'https://sc.chinaz.com/tupian/26030436551.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
    }
    r = requests.get(url, headers=headers).content.decode()
    # print(r)

    ret = etree.HTML(r)
    # print(ret)
    src = ret.xpath('//div[@class="img-box"]/img')
    src = 'https:'+src[0].xpath('./@src')[0]
    # print(src)

    img_code = requests.get(src).content
    # print(img_code)

    with open('站长图片.png','wb')as f:
        f.write(img_code)


if __name__ == '__main__':
    word = '站长图片'
    if not os.path.exists(word):
        os.mkdir(word)
        print('加载完成')
    main()
