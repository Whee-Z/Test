#两种去重方式

#第一种方式
alist = [2,2,6,3,2,5,2]
alist1 = list(set(alist))
print(alist1)

#第二种方式
alist2=[4,4,6,4,4,5,3]
def duplicate_removal(alist):
    l=[]
    for i in alist2:
        if i not in l:
            l.append(i)
    return l
print(duplicate_removal(alist))



