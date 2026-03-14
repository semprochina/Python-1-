#修改字符
#修改大小写
'''upper全部大写
   lower全部小写
   title每个单词首字母大写
   capitalize首字母大写转换
   swapcase大小写相互转换'''
#去除空白字符
'''strip()：去除首尾空格
   lstrip()：去除左边空格
   rstrip():去除右边空格
   '''
#替换操作
'''replace(要替换的字符,替换成什么字符,替换的次数) 重点'''
#字符串填充
'''center()居中
   ljust（）左对齐
   rjust（）右对齐'''
#删除指定字符
'''strip(要删除的字符串): 去除⾸尾空⽩'''
'''text = "--Python--"
print(text.strip("-"))
print(text.lstrip("-"))
print(text.rstrip("-"))'''

#查找字符串
'''ndex: 查找⼦字符串的起始索引  找不到就报错
   find: 查找⼦字符串的起始索引 找不到返回-1  推荐使⽤'''
#text='人生苦短，我用Python'
#print(text.index('生'))
#print(text.find('生'))

#try:
#    print(text.index('Sempro'))
#except ValueError:
#    print('无法找到')

#index = text.find('Sempro')
#if index == -1:
#    print('找不到')
#统计字符串的次数
'''count:⽤于统计⼦字符串的次数'''

'''a = input("请随便输⼊26个字⺟⻓度不限制").lower()
print(a)
b = input("请问呢你要统计哪⼀个字符出现的次数").lower()
print(a.count(b))'''
#检查字符串的开头和结尾 返回的是布尔类型 过滤 清洗  筛选
'''startswith():检查字符串的开头
   endswith(): 检查字符串的结尾'''
#判断字符串
'''1.判断字符串的内容
1. 是否是全数字: isdigit () 重点
2. 是否是全字⺟: isalpha() 
3. 是否是全字⺟+数字(数字,字⺟,数字+字⺟)都可以 : isalnum()
4. 是否是全空格: isspace()'''
#判断字符串格式 了解
'''1. 判断是否是全⼩写: islower() 了解即可
   2. 判断是否是全⼤写: isupper() 了解即可
   3. 是否为标题格式: istitle() 了解即可'''

'''分割与拼接'''
#分割
'''split(指定字符默认是空格,次数): 按照指定字符进⾏分割 得到⼀组数据
   rsplit(指定字符默认是空格,次数): 从右按照指定字符进⾏分割 得到⼀组数据
   splitlinens(): 按照换⾏符 \n  进⾏分割 得到⼀组数据'''
#拼接
'''join() : 将⼀组数据 通过指定的字符进⾏拼接 成为⼀个字符串'''
'''列表'''
#列表就是相当于存放多个数据的盒⼦以前我们创建变量的时候就是⼀个值对应⼀个变量名 有了列表的出现 就是多个值对应⼀个变量名
#基本方式 可迭代对象可使用索引和切片


#列表操作
'''添加：append:尾部追加元素
        insert: 插⼊元素'''