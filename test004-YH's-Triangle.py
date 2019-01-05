#打印杨辉三角
from sys import stdout

def yanghui(n):
    a = []
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(0)

    for i in range(n):
        a[i][0] = 1
        a[i][i] = 1

    for i in range(2,n):
        for j in range(1,i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]

    for i in range(n):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write('\t')
        print("")

n = int(input("请输入你想生成的杨辉三角行数："))
yanghui(n)