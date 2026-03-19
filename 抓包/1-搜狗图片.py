import os
import time
import requests


def main():
    url = "https://pic.sogou.com/napi/pc/searchList"
    params = {
        "mode": "1",
        "start": "0",
        "xml_len": 48,
        "query": word,  # 关键字
        "channel": "pc_pic",
        "scene": "pic_result"
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
        , 'cookie': 'SUID=A819CA78CB51A20B0000000068ECEE03; cuid=AAHerB+UVgAAAAuiVGR0YQEANgg=; SUV=1760357891442222; wuid=1760357895892; SNUID=F9F039D066612DF6D8FC9D1E6762746D; FUV=6456e15b18d6e6b244be465cedc676c6; search_tip=1771934905976; ABTEST=0|1771935843|v1'
        # 获取包数据的时候, 一定要用最新的包
        # , 'x-time4p': '1771935846412'
        # , 'x-time4p': f'{int(time.time() * 1000)}'  # 请求头中的数据不能是数字类型
        , 'x-time4p': str(int(time.time() * 1000))  # 请求头中的数据不能是数字类型
    }

    # 响应体
    items = requests.get(url, headers=headers, params=params).json()['data']['items']

    n = 1
    for item in items:
        # 图片地址
        oriPicUrl = item['oriPicUrl']
        print(oriPicUrl)

        img_headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0'
            , 'referer': oriPicUrl
        }

        try:
            # 保存图片  timeout: 超时
            img_code = requests.get(oriPicUrl, timeout=1, headers=img_headers).content
        except:
            continue  # 跳过当前循环, 进入到下一次循环

        with open(f'{word}/{n}.jpg', 'wb') as f:
            f.write(img_code)

        n += 1


if __name__ == '__main__':
    word = input('请输入你想要爬取的图片: ')
    if not os.path.exists(word):
        os.mkdir(word)

    main()

# Not A Directory Error
