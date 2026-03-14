a = 10

# 单分支嵌套
# 在嵌套结构里面大家只需要去注意 缩进问题即可
# 缩进一定要统一
# 这种就是 缩进不统一 会导致报错
# if a == 10:
#     print("嘻嘻")
#      print("哈哈")
if a == 10:
    print("下一关")
    if a == 20:
        print("通过了")
        # if a == 30:
        #     print("笑一个")
        #     if  a==40:
        #         print("嘻嘻嘻")

if a == 10:
    print("xx")
    if a==10:
        print("lll")
    if a==20:
        print("xx")
    else:
        print("xx")
else:
    print("lll")
    if a==20:
        print("xx")
    else:
        print("xx")
