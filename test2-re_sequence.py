#输入n个字符，打印出相反顺序，即逆序
class Sequence(object):
    def __init__(self,sequence):
        pass

    def input_str(self,sequence):
        print("这是你原来输入的序列：%s"%sequence)
        reversed_sequence = []
        for i in sequence:
            reversed_sequence.insert(0,i)
        reversed_sequence = "".join([str(j) for j in reversed_sequence])
        print("这是反转后的序列：%s"%reversed_sequence)

def main():
    state = 1
    while state:
        sequence = input("请输入那你想转换的序列：")
        if 'exit' == sequence:
            break
        S = Sequence(sequence)
        S.input_str(sequence)
    
if __name__ == '__main__':
    main()