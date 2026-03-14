'''条件语句'''
#三元运算符结构
#多分支选择结构
#优化版本
#选择结构的嵌套
'''循环语句 While for'''

# 初始化变量
num = 1
total = 0

print("1-100以内的所有奇数：")

# 使用while循环
'''while num <= 100:
    # 判断是否为奇数
    if num % 2 != 0:
        print(num, end=" ")
        total += num
    num += 1

print(f"\n1-100以内所有奇数的和为：{total}")
'''

# 初始化变量
#num = 1
#total = 0

#print("1-100以内的所有奇数：")

# 直接从1开始，每次加2，这样都是奇数
#while num <= 100:
 #   print(num, end=" ")
 #   total += num
 #   num += 2  # 直接跳到下一个奇数

#print(f"\n1-100以内所有奇数的和为：{total}")

# 初始化变量
'''num = 1
total = 0
count = 0  # 用于计数

print("1-100以内的所有奇数：")

while num <= 100:
    if num % 2 == 1:  # 判断奇数的另一种方法
        count += 1
        print(f"{num:3d}", end=" ")  # 格式化输出，每个数字占3位

        # 每10个数字换一行
        if count % 10 == 0:
            print()

        total += num
    num += 1

print(f"\n\n统计结果：")
print(f"奇数个数：{count}")
print(f"奇数和：{total}")
'''
num = 1
total = 0
odd_numbers = []  # 用于存储所有奇数

while True:
    if num > 100:
        break  # 当数字大于100时退出循环

    if num % 2 == 1:
        odd_numbers.append(num)
        total += num

    num += 1

print("1-100以内的所有奇数：")
print(odd_numbers)
print(f"1-100以内所有奇数的和为：{total}")



a=1
while a <= 100:
   a+=2




