a = range(10) # 这里10 表示的结束位置   包头不包尾
print(a)# range(0, 10)  表示开0开始 到10结束

# 遍历
"""
for 的语法格式

for 变量名 in 可迭代数据:
    代码块
"""
# for i in a:
#     print(i)
# 与while循环做对比
# i = 0
# while i < len(a):
#     print(a[i])
#     i+=1


# 第一种: 不写开始 不写步长
for i in range(10):
    print(i,end=" ")
print()
# 第二种: 不写步长
for i in range(0,10): # 从0开始 到10结束 默认每一次走一个步
    print(i,end=" ")
print()
# 第三种: 全写
for i in range(0,10,2): # 表示 从0开始 到10结束 每一次走2步  包头不包尾
    print(i,end=" ")

#
print()
my_name = "我的姓名叫:龙仔"
for i in my_name:
    print(i)