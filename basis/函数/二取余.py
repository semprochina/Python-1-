''' def DecToBin_int(d):
        if d == 0:
            return '0'

        sign = ''
        if d < 0:
            d = -d
            sign = '-'

        b = ''
        while d != 0:
            b = str(d % 2) + b
            d = d // 2
        return sign + b


    d = int(input('d='))
    print(DecToBin_int(d))'''

#递归
def f(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return f(n-2)+f(n-1)
#print(f(20))

#算法复杂度
'''8进制和16进制'''
#便于记录分析

