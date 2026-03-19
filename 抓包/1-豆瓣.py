import requests


def main():
    url = 'https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?start=0&limit=20&category=%E7%83%AD%E9%97%A8&type=%E5%85%A8%E9%83%A8'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
        , 'referer': 'https://movie.douban.com/explore'
    }

    # r = requests.get(url, headers=headers).text
    r = requests.get(url, headers=headers).json()

    items = r['items']
    for item in items:
        title = item['title']
        print(title)


if __name__ == '__main__':
    main()
