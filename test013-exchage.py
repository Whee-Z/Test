#三种交换变量的方式

a = 0
b = 1

#第一种
a,b = b,a

#第二种
a = b-a
b = b-a

#第三种
c = 0
c = a
a = b
b = c

print(a,b)