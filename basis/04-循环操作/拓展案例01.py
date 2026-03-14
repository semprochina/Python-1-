import random
counts = random.randint(1,80)
times = 0
while times < 3:
    try:
        guess = int(input("猜猜心跳多少次了"))
    except ValueError:
        print('请正确输入')
    else:
        if guess == counts:
            print("Bingo!!!")
            break
        elif guess > counts:
            print("猜大咯")
        else:
            print("猜小咯")
        times +=  1
        if times == 3:
            print("没机会喽，下次再玩吧！")



