# 分数输出
scores = int(input("请输入你的分数"))
if scores == 100:
    print("优秀++")
if scores>=90 and scores<100:
    print("优秀")
if scores>=80 and scores<90:
    print("良好")
if scores>=70 and scores<80:
    print("差")
if scores<70:
    print("你有资格打游戏吗？？？？")
else:
    print("非法输入")




scores = int(input("请输入你的分数"))
if scores == 100:
    print("优秀++")
elif scores>=70 and scores<80:
    print("差")
elif scores>=90 and scores<100:
    print("优秀")

elif scores>=80 and scores<90:
    print("良好")

elif scores<70 and scores>=0:
    print("你有资格打游戏吗？？？？")
# elif scores>100 or scores<0:
#     print("非法输入")
else: #   一般的else都是表示否定的结果
    print("非法输入")
# 优化版本

# scores = int(input("请输入你的分数"))
# if scores == 100:
#     print("优秀++")
# elif 90<= scores<100:
#     print("优秀")
# elif 70 <=  scores<80:
#     print("差")
# elif 80 <= scores<90:
#     print("良好")
# elif scores >= 0:
#     print("你有资格打游戏吗？？？？")

# elif scores>100 or scores<0:
#     print("非法输入")
# else: #   一般的else都是表示否定的结果
#     print("非法输入")
