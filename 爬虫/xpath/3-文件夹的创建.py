import os  # 系统模块

# make: 创建 dir:directer
# os.mkdir('致美化')

# 如果没有这个文件夹, 才创建
if not os.path.exists('12'):
    os.mkdir('12')
