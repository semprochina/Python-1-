'''1. 构建一个列表,.通过随机数插入5个整数,
将这个列表末尾添加"张翠山"
在第4个位置添加'高圆圆'
循环打印这个列表
   2. 构建一个空列表用来作为账号保存的容器, 控制台输入账号数据添加到这个列表中,要求如下:
注册的数据不大于5个
如果输入已经存在的用户,提示"用户名太受欢迎'''
import random
a= random.randint(0,100)
b= random.randint(0,100)
c= random.randint(1,100)
d= random.randint(1,100)
e= random.randint(1,100)
f=[a,b,c,d,e]
f.append("张翠山")
f.insert(4,"高圆圆")
print(f)

list =[]
print("最多可以注册5个账号")

while len(list) < 5:
    user = input(f"\n请输入第 {len(list) + 1} 个账号（输入'quit'退出）: ").strip()

    if user in list:
        print(f"错误：用户名 '{user}' 太受欢迎，已存在！")
