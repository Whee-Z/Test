#插入排序算法,输入数字时以逗号隔开,输入exit退出循环
class Insertion_sort(object):
    def __init__(self):
        pass

    def insertion_sort(self,alist):
        n = len(alist)
        for i in range(1,n):
            for j in range(i,0,-1):
                if alist[j] < alist[j-1]:
                    alist[j],alist[j-1] = alist[j-1],alist[j]

def main():
    insertion = Insertion_sort()
    while True:
        alist_str = input("Please input a list:")
        alist = []
        if 'exit' == alist_str:
            break
        for i in eval(alist_str):
            alist.append(i)    

        insertion.insertion_sort(alist)
        print(alist)

if __name__ == '__main__':
    main()
