#阶乘
def jiecheng(num):
    #res=1
    if num<=1:
        return 1
    else:
        res=num*jiecheng(num-1)
        return res

print(jiecheng(3))
print(jiecheng(0))
print(jiecheng(5))