import requests
from lxml import etree


def main(page):
    # 列表页
    if page == 1:
        url = 'https://www.6v520.net/dy/'
    else:
        url = f'https://www.6v520.net/dy/index_{page}.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
    }
    r = requests.get(url, headers=headers).content.decode('gbk')

    ret = etree.HTML(r)

    li_list = ret.xpath('//ul[@class="list"]/li')
    for li in li_list:
        # 电影名
        name = li.xpath('./a//text()')
        name = ''.join(name)

        if '佳片推荐' in name:
            continue

        # 发布时间
        date = li.xpath('./span/text()')
        date = ''.join(date)

        # 详情页地址
        href = li.xpath('./a/@href')
        href = "https://www.6v520.net" + ''.join(href)
        print(name, href)

        # 1. 获取页面的源代码

        r = requests.get(href, headers=headers).content.decode('gbk')

        # 2.提取数据
        ret = etree.HTML(r)

        tr_list = ret.xpath('//div[@id="endText"]/table/tbody/tr')

        for tr in tr_list:
            # 下载方法
            method = tr.xpath('./td/text()')
            method = ''.join(method)[:-1]

            # 下载地址
            download = tr.xpath('.//a/@href')
            download = ''.join(download)

            with open('6v520.csv', 'a', encoding='utf-8') as f:
                f.write(f'{name},{date},{href},{method},{download}\n')


if __name__ == '__main__':
    with open('6v520.csv', 'w', encoding='utf-8') as f:
        f.write('电影名, 发布时间, 详情页地址, 下载方法, 下载地址\n')

    for page in range(1, 11):
        main(page)
        print(f'===========第{page}页爬取成功===========')
