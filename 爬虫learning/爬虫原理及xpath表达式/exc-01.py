'''
    1.获取源代码
    2.提取数据
    3.保存数据
'''
import requests


# 定义函数
# 1.首先获取页面源代码
def main():
    '''requests.get(网址)'''  # 通过requests获取浏览器中的数据
    # 1.定义变量，描述目标网址
    url = 'https://search.bilibili.com/all?vt=53453038&keyword=%E9%99%88%E7%BF%94%E5%85%AD%E7%82%B9%E5%8D%8A&from_source=webtop_search&spm_id_from=333.788'

    # 再定义一个变量，处理可能存在的反爬
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
    }

    # 获取网页源代码
    response = requests.get(url, headers=headers).text
    print(response)


# 调用函数
if __name__ == '__main__':  # 程序入口（自动补全）
    main()
