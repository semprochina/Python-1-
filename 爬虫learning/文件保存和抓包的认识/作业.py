import requests
from lxml import etree


def main(page):
    if page == 1:
        url = 'https://www.6v520.net/dy/'
    else:
        url = f'https://www.6v520.net/dy//index_{page}.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
        , 'referer': 'https://www.6v520.net/dy/'
    }
    r = requests.get(url, headers=headers).content.decode('gbk')
    # print(r)
    ret = etree.HTML(r)
    # print(ret)
    li_list = ret.xpath('//ul[@class="list"]/li')
    # print(len(li_list))
    for li in li_list:
        # 电影名
        name = li.xpath('./a/text()') or li.xpath('./a/font/text()')
        name = ''.join(name)
        # print(name)

        # 电影详情页地址
        address = 'https://www.6v520.net/' + li.xpath('./a/@href')[0]
        address = ''.join(address)
        # print(address)

        r = requests.get(address, headers=headers).content.decode('gbk')
        ret = etree.HTML(r)
        tr_list = ret.xpath('//table[@cellspacing="1"]/tbody/tr')
        # print(len(tr_list))

        # 发布日期
        date = li.xpath('./span/text()')
        date = ''.join(date)
        # print(date)

        # 下载方法
        for tr in tr_list:
            method = tr.xpath('./td/text()')
            method = ''.join(method).strip()[:-1]
            # print(method)

            # 下载地址
            download = tr.xpath('./td/a/@href')
            download = ''.join(download)
            # print(download)

            with open('6v520.csv', 'a', encoding='utf-8') as f:
                f.write(f'{name},{address},{date},{method},{download}\n')


if __name__ == '__main__':
    with open('6v520.csv', 'w', encoding='utf-8') as f:
        f.write('电影名,电影详情页地址,发布日期,下载方法,下载地址\n')

    for page in range(1,11):
        main(page)
        print(f'=========第{page}页爬取完成=========')
