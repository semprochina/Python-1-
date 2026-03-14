import requests

# url = 'https://dl.zhutix.net/2025/09/Colorful-gemstone-wallpapers-hero-image-02.jpg'
# url = 'https://dl.zhutix.net/2025/08/minimalistic-palm-trees-wallpaper-02.jpg'
url = 'https://dl.zhutix.net/2025/03/Patagonia-01.jpg'

# 先获取图片的地址  bytes类型
img_code = requests.get(url).content
#print(img_code)
# with as 是上下文管理器
# w: write(写入, 创建) b: bytes  wb: 以bytes类型来写入
# 创建一个1.jpg的文件, 以bytes类型来写入, 这个动作赋值给到f
with open('2.jpg', 'wb') as f:
    # 向f的里面写入img_code(图片的数据)
    f.write(img_code)
