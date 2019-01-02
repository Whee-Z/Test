#打印一个棱形

def prismatic(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print(" ", end="")
        print('* ' * i)
    for i in range(0, n):
        for k in range(0, i):
            print(" ", end="")
        print('* ' * (n-i))

prismatic(10)
