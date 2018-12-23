#实现一个单例
class Recycle(object):
    __instance = 0

    def __new__(cls):
        if cls.__instance == 0:
            cls.__instance=object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

a = Recycle()
print(id(a))
b = Recycle()
print(id(b))