'''1.什么是Pyautogui⾃动化操作 '''
import random

#Pyautogui: 是⼀个Python的模块 可以模拟⽤户在屏幕上的操作如 : ⿏标或者键盘 ,它可以⾃动化操作 执⾏各种任务
'''2.Pyautogui⾃动化操作具体能够做什么'''
#移动⿏标  控制键盘 查看⻋票轰炸 QQ轰炸
'''3.Pyautogui⾃动化操作如果操作'''
#3.1 模块的安装
'''1.打开终端'''
'''2.输⼊命令 '''
'''1.更新PIP 
python -m pip install --upgrade pip -i https://repo.huaweicloud.com/repository/pypi/simple/ 
2. 下载⾃动化模块 
pip install  pyautogui==0.9.54 -i https://repo.huaweicloud.com/repository/pypi/simple/'''
#3.2 Pyautogui⾃动化操作基本操作
'''鼠标操作'''
import  pyautogui as pg
import time
#pg.moveTo(0,2,9)
time.sleep(3)
for i in range(10):
    pg.moveTo(random.randint(0,1920),random.randint(0,1080),0.5)
    print('程序结束')
pg.click(1000,10,button='left')
pg.doubleClick(1000,10,button='right')
'''钢琴案例'''
'''键盘操作'''
'''案例优化'''
'''获取鼠标位置'''
'''屏幕截图'''
'''图片位置识别'''
