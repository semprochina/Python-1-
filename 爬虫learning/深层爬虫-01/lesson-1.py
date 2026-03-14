import os
import requests
from lxml import etree


def main():
    url = 'https://sc.chinaz.com/tupian/'

    headers = {
        'user-agent': 'Safari/537.36 Edg/145.0.0.0Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 '
    }

    r = requests.get(url, headers=headers).content.decode()  # 解码utf-8型
    # print(r)

    ret = etree.HTML(r)
    # print(ret)
    div_list = ret.xpath('//div[@class="item"]')  # 源代码和元素不一样
    # print(len(div_list))

    n = 1
    for div in div_list:
        src = div.xpath('./img/@data-original')
        src = ''.join(src)
        src = 'https:'+src
        # print(src)

        '''
        name = div.xpath('.//a[@class="name]/text()')
        name = ''.join(name)
        print(name)
        '''

        img_code = requests.get(src).content
        # print(img_code)

        with open(f'{word}/{n}.png','wb')as f:
            f.write(img_code)

        n += 1


if __name__ == '__main__':
    word = '站长图片'
    if not os.path.exists(word):
        os.mkdir(word)

    main()
