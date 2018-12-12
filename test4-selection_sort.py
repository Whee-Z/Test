#选择排序算法,输入数字时以逗号隔开,输入exit退出循环
class Selection_sort(object):
    def __init__(self):
        pass

    def selection_sort(self,alist):
        n = len(alist)
        for i in range(n-1):
            min_index = i
            for j in range(i+1,n):
                if alist[j] < alist[min_index]:
                    min_index = j
            if min_index != i:
                alist[i],alist[min_index] = alist[min_index],alist[i]
    
def main():
    s = Selection_sort()
    while True:
        alist_str = input("please input a list:")
        alist = []
        if 'exit' == alist_str:
            break
        for i in eval(alist_str):
            alist.append(i)
        
        s.selection_sort(alist)
        print(alist)

if __name__ == '__main__':
    main()