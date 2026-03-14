# 导入库
import os
import requests
from lxml import etree


# 创建函数
def main():
    # 爬取网址
    url = "https://zhutix.com/mobile/"
    # 处理可能的反爬
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers).text
    # print(response)
    # 转换数据格式
    ret = etree.HTML(response)
    li_list = ret.xpath('//div[@id="post-list"]//li')
    # print(len(li_list))
    # 定位并提取网页中图片的相对路径，最终拼接成完整可用的字符串
    n = 1
    for li in li_list:
        src = li.xpath('.//img/@src')
        src = ''.join(src)  # 用空字符串 '' 拼接起来

        name = li.xpath('.//a[@class="imglist-char shu"]/text()')
        name = ''.join(name)

        # print(src)
        # 转换数据类型
        img_code = requests.get(src).content
        # 保存数据
        with open(f'{word}/{n}.jpg', 'wb') as f:
            f.write(img_code)

        n += 1


if __name__ == '__main__':
    word = '致美化'
    if not os.path.exists(word):
        os.mkdir(word)
    main()
