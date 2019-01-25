#简单for循环
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'等于','*',n//x)
            break
    else:
        print(n,'是质数')