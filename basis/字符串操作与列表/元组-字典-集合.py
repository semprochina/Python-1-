'''元组-tuple'''
#元组的创建
#a=("sempro",1.65,19)#小括号可以省略
#print(a)
#b="sempro",1.65,19
#print(b)

#c='sempro',
#print(c)
#print(type(c))

#c=tuple('sempro')#创建一个空元组
#print(c)

#o = tuple([1,2,3,47,56])
#print(o)
#基本操作

'''字典'''
'''集合'''


# 有如下字典内容用程序解答下面的题目
dic_1 = { 'python': 95,'java': 99,'c': 100}
# 1. 字典的长度是多少
print(len(dic_1))
# 2. 请修改'java' 这个key对应的value值为98
'''字典是以键值对的形式来进⾏保存数据key:value   需要注意的是key是不可以改变的 value值是可以改变的 
语法格式: 
{key:value,key:value....}'''
dic_2 = { 'python': 95,'java': 98,'c': 100}
dic_1.update(dic_2)
print(dic_1)
# 3. 删除 c 这个key
del dic_1['c']
print(dic_1)
# 4. 增加一个key-value对，key值为 php, value是90
dic_1 = { 'python': 95,'java': 99,'c': 100,'php':90}
print(dic_1)
# 5. 获取所有的key值，存储在列表里
line=[dic_1.keys()]
print(line)
# 6. 获取所有的value值，存储在列表里
line2=[dic_1.values()]
print(line2)
# 7. 判断 'javascript'这个字符串 是否在字典的key中
a=dic_1.keys()
i='javascript'
if i in a:
    print('ture')
else:print('false')
# 8. 获得字典里所有value 的和
n=tuple(dic_1.values())
print(sum(n))