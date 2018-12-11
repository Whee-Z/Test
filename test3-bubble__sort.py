#冒泡算法,输入数字时以逗号隔开,输入exit退出循环
class Bubble_sort(object):
    def __init__(self):
        pass

    def bubble_sort(self,alist):
        n = len(alist)
        for i in range(n-1,0,-1):
            for j in range(i):
                if alist[j] > alist[j+1]:
                    alist[j],alist[j+1] = alist[j+1],alist[j]
    
def main():
    b = Bubble_sort()
    while True:
        alist_str = input("please input a list:")
        alist = []
        if 'exit' == alist_str:
            break
        for i in eval(alist_str):
            alist.append(i)
        
        b.bubble_sort(alist)
        print(alist)

if __name__ == '__main__':
    main()