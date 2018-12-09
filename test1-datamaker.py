#用于数据获取的简易练习
import random
import string

class Datatype(object):
    def __init__(self):
        pass

    def type_int(self,datatype):
        if 'int' == datatype:
            print(random.randint(0,10000))

    def type_float(self,datatype):
        if 'float' == datatype:
            print(random.uniform(0,10000))

    def type_str(self,datatype):
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
        if 'phone' == datatype:
            phone_list =[1] + [random.randint(0,9) for i in range(10)]
            print("".join([str(j) for j in phone_list]))


    def type_others(self,datatype):
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

    
    
    
    
    
   
        