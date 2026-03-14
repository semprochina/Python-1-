import requests
from lxml import etree


def main():
    url = 'https://ssr1.scrape.center/'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
        ,'referer': 'https://ssr1.scrape.center/'
    }

    response = requests.get(url, headers=headers).text
    # print(response)

    ret = etree.HTML(response)
    print(ret)

    div_list = ret.xpath('//div[@class="el-card item m-t is-hover-shadow"]')
    print(len(div_list))
    for div in div_list:
        # 电影名
        title = div.xpath('.//h2[@class="m-b-sm"]/text()')
        title = ''.join(title)
        title = title.split('-')[0]
        print(title)

        # 上映地点
        place = div.xpath('.//div[@class="m-v-sm info"][1]/span[1]/text()')
        place = ''.join(place)
        print(place)

        # 上映日期
        date = div.xpath('.//div[@class="m-v-sm info"][2]//text()')
        date = ''.join(date).strip().replace('-','.')
        print(date)

        # 时长
        times = div.xpath('.//div[@class="m-v-sm info"][1]/span[3]/text()')
        times = ''.join(times)
        print(times)

        # 评分
        score = div.xpath('.//p[@class="score m-t-md m-b-n-sm"]/text()')
        score = ''.join(score).strip()
        print(score)

        # 分类
        categories = div.xpath('.//div[@class="categories"]//span/text()')
        categories = '-'.join(categories)
        print(categories)




if __name__ == '__main__':
    main()
