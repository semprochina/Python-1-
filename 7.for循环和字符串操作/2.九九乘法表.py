for i in range(1,10):
    # print(f"i当前的值{i}")
    for j in range(1,i+1):
        # range(1,2) 打印一次
        # range(1,3) 打印二次
        # range(1,4) 打印4次
        # range(1,5) 打印5次
        print(f"{j}*{i} = {j*i}",end=" ")
    print()
    # if i == 5:
    #     break
else:
    print("九九乘法表正常打印完成")