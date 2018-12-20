import random
import string

class Datatype(object):
    """"生成随机数的练习"""
    def __init__(self):
        pass

    def type_int(self,datatype):
        """"生成[0,10000]之间的随机整数"""
        if 'int' == datatype:
            print(random.randint(0,10000))

    def type_float(self,datatype):
        """"生成[0,10000]之间的随机浮点数"""
        if 'float' == datatype:
            print(random.uniform(0,10000))

    def type_str(self,datatype):
        """"生成随机的字符串"""
        if 'str' == datatype:
            state = 1
            while state:
                strlength = input("please int the length of the str:")
                if not strlength.isdigit():
                    print("请输入数字")
                else:
                    state = 0
            str_list = [random.choice(string.digits + string.ascii_letters) for i in range(int(strlength))]
            print(''.join(str_list))

    def type_phone(self,datatype):
        """"生成以1开头的随机号码"""
        if 'phone' == datatype:
            phone_list =[1] + [random.randint(0,9) for i in range(10)]
            print("".join([str(j) for j in phone_list]))


    def type_others(self,datatype):
        """"其他指令报错"""
        if datatype not in ['int','float','str','phone','exit']:
            print("error.Please input int,float,str or phone")

def main():
    dtype = Datatype()    
    state = 1
    while state:
        datatype = input("please input a data type:")
        dtype.type_int(datatype)
        dtype.type_float(datatype)
        dtype.type_str(datatype)
        dtype.type_phone(datatype)
        dtype.type_others(datatype)
        if 'exit' == datatype:
            state = 0
    print("谢谢使用")

if __name__ =='__main__':
    main()

    
    
    
    
    
   
        