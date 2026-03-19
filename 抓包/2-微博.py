import requests


def main():
    # 热搜
    url = 'https://stats.cdnjtzy.com/stats/PKD-DXST-C.json?t=1773567147612'

    # 文娱
    # url = 'https://weibo.com/ajax/statuses/entertainment'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
        , 'referer': 'https://weibo.com/hot/search'
        ,
        'cookie': 'SINAGLOBAL=2575623069553.9263.1763469863922; ULV=1765975324054:2:1:1:3775720075307.9824.1765975323897:1763469864067; SCF=Aqf3I5UKlXUtpWp1XAear8hNmFDx_FSTvAFillmmHrej3QdtC_Rgddm1JfXRy7phzsprTvJDq9yjTRIsHYwLRRQ.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWXm7JNpqZOSEdgWh5qNTno5JpX5KMhUgL.Fo-4e02pS0BfShz2dJLoI7pyIgSoqcSodgf_dgXt; ALF=1772716264; SUB=_2A25EhYO4DeRhGeNH6FMQ9yrJzz6IHXVn-plwrDV8PUJbkNANLWfdkW1NSt0WghcgHxCm6rpsG21gWltGmeD42-KB; XSRF-TOKEN=-100etBGduyJuV8mKmkAgPDz; WBPSESS=CDPi94QcVK6yYxfOyZbFf5AnOD-Mlrx_cAzbDRAHffREf90KXBYP6_xTRjUPJ9CtSkUjQObrufcaB9r0SR1f7gxUGSP58ipRZQI62TmWgSndWwGZGf8pbGd69vdt9Zv85xcJOAFzCO2tiZuRWiovdg=='
    }

    # 字符串
    # r = requests.get(url, headers=headers).text
    # 热搜
    r = requests.get(url, headers=headers).json()
    realtime = r['data']['realtime']
    for i in realtime:
        word = i['word']
        print(word)

    # 文娱
    # 字典类型
    # r = requests.get(url, headers=headers).json()
    #
    # band_list = r['data']['band_list']
    #
    # for band in band_list:
    #     word = band['word']
    #     print(word)


if __name__ == '__main__':
    main()
