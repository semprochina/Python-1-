import requests

url = 'https://dl.zhutix.net/2025/03/Patagonia-01.jpg'

# 获取图片地址  bytes类型
img_code = requests.get(url).content

"""
with as 上下文管理器
w:write(写入，创建) b:bytes wb:以bytes类型来写入
创建一个文件，以bytes类型来写入，动作复制到f 
"""
# print(img_code)
with open('1.jpg', 'wb') as f:
    f.write(img_code)
