﻿#计算前n个数的和
n = int(input("请输入一个数："))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)