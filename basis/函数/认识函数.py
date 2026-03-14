'''定义函数f1:

    1.函数功能: 接受3个字符串参数，打印出每个输入字符串的首字符
    2.参数: 3个字符串
    3.定义完成以后,需要调用执行

    要求至少使用2种方式来定义'''

# 使用 def 定义函数
def f1(str1, str2, str3):
    """函数功能：打印每个输入字符串的首字符"""
    print(str1[0] if str1 else "空字符串")
    print(str2[0] if str2 else "空字符串")
    print(str3[0] if str3 else "空字符串")

# 调用函数
f1("Hello", "World", "Python")























