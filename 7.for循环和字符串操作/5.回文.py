text = input("请输入一段回文")

# print(text[::-1]) # 反转字符串操作
# if text ==  text[::-1]:
#     print("是回文")
# else:
#     print("不是回文")


text = input("请输入一段回文")
#不使用切片的方式
text2 =""
for i in range(len(text)-1,-1,-1):
    print(text[i])
    text2 = text2+text[i]
print(text2)
if text == text2:
    print("是回文")
else:
    print("不是回文")