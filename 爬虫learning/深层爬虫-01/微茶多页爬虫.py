import os
import requests
from lxml import etree


def main(page):
    url = f'https://www.wxcha.com/touxiang/nvsheng/update_{page}.html/'
    # 设置请求头，模拟浏览器访问，防止被网站屏蔽

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
    }
    # 发送GET请求获取网页内容，并转换为文本格式
    response = requests.get(url, headers=headers).text
    # print(response)

    ret = etree.HTML(response)
    # print(ret)
    li_list = ret.xpath('//ul[@class="newtx_ul cl"]/li')
    # print(len(li_list))

    for li in li_list:
        src = li.xpath('.//img/@data-src')
        src = ''.join(src)

        name = li.xpath('.//a[@class="wz"]/text()')
        name = ''.join(name)
        # print(name, src)

        img_code = requests.get(src).content
        # print(img_code)

        with open(f'{word}/{name}.jpg', 'wb') as f:
            f.write(img_code)


if __name__ == '__main__':
    word = '微茶多页'
    if not os.path.exists(word):
        os.mkdir(word)

    for page in range(1, 4):
        main(page)
    print('爬取完成')