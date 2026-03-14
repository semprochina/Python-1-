import requests
from lxml import etree


def main():
    url = 'https://space.bilibili.com/3494358043068604/relation/follow?spm_id_from=333.1007.0.0'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
    }
    r = requests.get(url, headers=headers).text
    # print(r)

    ret = etree.HTML(r)
    # print(ret)

    li_list = ret.xpath('//div[@class="items"]/div[@class="item"]')
    print(len(li_list))


if __name__ == '__main__':
    main()
