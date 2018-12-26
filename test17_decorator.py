#实现一个通用装饰器
def w1(func):
    def w2(*args,**kwargs):
        print("-------记录日志--------")
        ret = func(*args,**kwargs)
        return ret
    return w2

@w1
def test1():
    print("test1")
    return "haha"

@w1
def test2():
    print("test2")

@w1
def test3(a):
    print("test3---a=%d"%a)

ret = test1()
print(ret)
test2()
test3(5)
