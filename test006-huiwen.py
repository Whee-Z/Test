#判断是否回文
astr = input("请输入一个数字:")
flag = True

for i in range(len(astr) // 2):
    if astr[i] != astr[-i - 1]:
        flag = False
        break
if flag:
    print("%s 是一个回文数!" %astr)
else:
    print("%s 不是一个回文数!" %astr)
