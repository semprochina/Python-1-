import requests
from lxml import etree


def main():
    # 1. 获取页面的源代码
    url = 'https://ssr1.scrape.center/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
    }

    r = requests.get(url, headers=headers).text

    # 2. 提取数据
    ret = etree.HTML(r)

    div_list = ret.xpath('//div[@class="el-card item m-t is-hover-shadow"]')
    print(len(div_list))

    for div in div_list:
        # 电影名
        name = div.xpath('.//h2[@class="m-b-sm"]/text()')
        name = ''.join(name)
        name = name.split('-')[0]  # ['霸王别姬 ', ' Farewell My Concubine']
        print(name)

        # 上映地点
        address = div.xpath('(.//div[@class="m-v-sm info"])[1]/span[1]/text()')
        address = ''.join(address)
        print(address)

        # 上映时间
        date = div.xpath('(.//div[@class="m-v-sm info"])[2]/span[1]/text()')
        date = ''.join(date)
        print(date)

        # 时长
        times = div.xpath('(.//div[@class="m-v-sm info"])[1]/span[3]/text()')
        times = ''.join(times)
        print(times)

        # 评分
        score = div.xpath('.//p[@class="score m-t-md m-b-n-sm"]/text()')
        score = ''.join(score).strip()
        print(score)

        # 红色区域的内容(电影名下面的内容)
        categories = div.xpath('.//div[@class="categories"]/button/span/text()')
        categories = ' '.join(categories)

        print(categories)


if __name__ == '__main__':
    main()
