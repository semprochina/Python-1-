#for循环与while循环的比较
#while从无到有
#for循环从有到无的迭代数据‘for遍历数据’
#range生产数字序列
'''range(开始位置,结束位置,步⻓)
开始位置 : 从那个数字开始 默认是0  可以写也可以不写
结束位置: 到那个数字结束   必须写
步⻓ : 设置步数  可以设置也可以不设置   默认是1步 '''
#a=range(10)
#print(a)
""" 
for 的语法格式
for 变量名 in 可迭代数据:
    代码块
"""
#for i in a:
#    print(i)#包头不包尾
'''写法一：不写开始与步长'''
#for i in range(10) :
#   print(i,end=" ")
#print()
#写法二：不写步长
#for i in range(0,10):
#    print(i,end=" ")
#print()
#写法三：全写
#for i in range(0,10,2):
#    print(i,end=' ')

'''my_name = "我的名字是Sempro"
for i in my_name:
    print(i,end=' ')'''


'''range(1,10)'''
#for i in range(1,10):
#    for j in range(1,i+1):
#        print(f"{j}*{i}={j*i}",end=' ')
#    print()

'''for...else'''
#for i in range(1,10):
#    for j in range(1,i+1):
#        print(f"{j}*{i}={j*i}",end=' ')
#    print()

   # if i==5:
   #    break
#else:
#    print('successed')

#序列
#索引
'''什么是索引? 索引就是每个字符的房间号(位置编号)
正索引 :从左往右数  索引从0开始
负索引 : 从右往左数 索引从-1开始'''
#切片
'''什么是切⽚:  切⽚就是索引的plus版本
切⽚的核⼼就是索引 但是索引是获取单个字符串 ⽽切⽚是获取
⼀段⽂本信息的'''
#字符串
#[开始索引:结束索引:步⻓]
#开始索引:  开始哪⾥开始   默认是0
#结束索引: 到哪⾥结束 默认len(字符串)
#步⻓: 每⼀次⾛⼏步 默认是1

'''text = "不管⼼情多糟糕都要和爱的⼈好好说话"# 第⼀种:省略开始索引和步⻓
print(text[:7])
# 第⼆种:省略结束索引和步⻓
print(text[7:])
# 第三种:省略步⻓
# len是通⽤操作可以对列表字符串字典集合元组使⽤
# 专⻔是获取⻓度的
print(len(text))  # len获取⻓度是从1开始数的
# 如果我想获取这个字符串的最⼤索引怎么办？
print(len(text) - 1)  # 获取最⼤索引值
print(text[7:len(text)])
# 加上步⻓
print(text[7:17:2])
text = "不管⼼情多糟糕都要和爱的⼈好好说话"
# 负索引
print(text[-1:-7:-1])  # 从 - 1⾛到 - 7每⼀次⾛⼀步有数据吗？
# 步⻓:1print(text[-7:-1]'''


#字符串操作

'''name = " a重生之a我是张无忌a无敌a叼霸天a无忌A "

# 请输出 name 变量对应的值的第 2 个字符

# 统计a一共出现了多少次

# 循环打印name的每一个字符,至少使用2种方式[选做]'''

name = "a重生之a我是张无忌a无敌a叼霸天a无忌A "
print(name[1])

number = name.count('a')
print(number)

'''for...range'''
print("\n")
for i in range(len(name)):
    print(name[i], end=' ')
print()  # 换行

'''for'''
for i in name:
    print(i,end=' ')
