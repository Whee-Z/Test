#快速排序算法,输入数字时以逗号隔开,输入exit退出循环
class Quick_sort(object):
    def __init__(self):
        pass

    def quick_sort(self,alist,start,end):
        #递归退出条件
        if start >= end:
            return

        #设定基准元素
        mid = alist[start]

        #设定序列左右的游标
        low = start
        high = end

        #开始排序咯
        while low < high:
            while low < high and alist[high] >= mid:
                high -= 1
            alist[low] = alist[high]

            while low < high and alist[low] < mid:
                low += 1
            alist[high] = alist[low]

        #将基准元素赋给这个位置
        alist[low] = mid

        #对基准元素左右边的子序列进行递归快排
        self.quick_sort(alist,start,low-1)
        self.quick_sort(alist,low+1,end)

def main():
    quick = Quick_sort()
    while True:
        alist_str = input("Please input a list:")
        alist = []
        if 'exit' == alist_str:
            break
        for i in eval(alist_str):
            alist.append(i)    

        quick.quick_sort(alist,0,len(alist)-1)
        print(alist)

if __name__ == '__main__':
    main()




