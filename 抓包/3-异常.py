try:  # 捕获异常(错误)
    print(1)
    print(a)
    print(1)
    print(1)
# except Exception as e:  # 能够将报错的描述拿到, 赋值给e
except:
    # 如果程序出错了, 程序就会直接过来
    print('程序出错了')  # 可以写出错后, 给出的提示
    # print(e)
    print('123')
