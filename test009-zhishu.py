#求出质数
l = []
n = int(input("请输入一个数："))
for i in range (2,n+1):
    flag = 0
    for j in range (2,i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        l.append(i)

print(l)