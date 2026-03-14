#+加法 -减法 **幂次方 /浮点除法 //整数除法
#%取余 （）优先级 *乘法
#字符串内只支持加减
'''+= a+=2 a=a+2
-= a-=2 a=a-2
*= a*=2 a=a*2
/= a/=2 a=a/2
//= a//=2 a=a//2
**= a**=2 a=a**2
%= a%=2 a=a%2'''
#复合运算符就是 把算术运算符和赋值运算符结合起来了 只能对⾃身进⾏使⽤  ⽆法赋值给第三⽅变量
'''⽐较运算符 (重点中的重点) 
运算符
==  等于 ⽐较左边的值是否等于右边的值  
!=  不等于 ⽐较左边的值是否不等于右边的值 
>   ⼤于  ⽐较左边的值是否⼤于右边的值 
<   ⼩于  ⽐较左边的值是否⼩于右边的值 
>=  ⼤于或者等于  ⽐较左边的值是否⼤于或者等于右边的值 
<=  ⼩于或者等于  ⽐较左边的值是否⼩于或者等于右边的值 

'''

def login():
    """登录验证，最多尝试3次"""
    valid_username = "Sempro"
    valid_password = "061124"

    attempts = 3  # 最大尝试次数

    for i in range(attempts):
        print(f"\n登录尝试 ({i + 1}/{attempts})")
        user = input("请输入用户名: ")
        password = input("请输入密码: ")

        if user == valid_username and password == valid_password:
            print("登录成功！")
            return True
        else:
            print("用户名或密码错误！")

    print("尝试次数过多，程序结束。")
    return False


def get_grade():
    """成绩等级判断系统"""
    while True:
        try:
            print("\n" + "=" * 30)
            score = float(input("请输入成绩（0-100），输入-1退出: "))

            if score == -1:
                print("退出评分系统。")
                break
            elif score < 0 or score > 100:
                print("错误：成绩必须在 0-100 之间")
            elif score == 100:
                print(f"成绩{score}分，满分")
            elif score >= 90:
                print(f"成绩 {score} 分，优秀")
            elif score >= 80:
                print(f"成绩 {score} 分，良好")
            elif score >= 70:
                print(f"成绩 {score} 分，中）")
            elif score >= 60:
                print(f"成绩 {score} 分，及格")
            else:
                print(f"成绩 {score} 分，不及格")

        except ValueError:
            print("错误：请输入有效的数字！")


def main():
    """主程序"""
    print("=== 用户登录系统 ===")

    # 登录验证
    if login():
        # 登录成功后进入评分系统
        print("\n欢迎使用成绩等级判断系统！")
        get_grade()
        print("程序运行完毕。")


# 运行程序
if __name__ == "__main__":
    main()


