#斐波拉契数列
def fibonacci(times):
    n=0
    a = 0
    b = 1
    while n<times:
        print(b)
        a,b = b,a+b
        n+=1
    return 'ok'
         

b = fibonacci(6)
print(b)