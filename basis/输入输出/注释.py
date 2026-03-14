#单行注释
'''
多行注释
'''
infort='Name Age Hobby'
e=infort.split(' ')
print(e)
print('Sempro','19','Photography',sep=' ',end='thanks')

''''Guess which number form 1 to 9 I am thinking now'''
import random
counts = 3
A = random.randint(1,9)
while counts > 0:
    u=input('不妨猜猜Sempro心里想的数字')
    guess = int(u)

    if guess == A:
        print('你是Sempro肚子里的蛔虫吗？！')
        print('hhhh猜对了也没奖励')
        break
    else:
         if guess < A :
           print('小了哟')
         else:
           print('大咯')
         counts = counts - 1
print('游戏结束不玩啦')