# -*- coding: utf-8 -*-
"""这是一个来访信息管理系统"""
person = []
flag = 1
"""功能：打印操作指南"""
print("操作指南如下：")
print("输入数字1添加来访人员信息")
print("输入数字2修改来访人员信息")
print("输入数字3删除来访人员信息")
print("输入数字4查找来访人员信息")
print("输入数字5显示来访人员信息")
print("输入数字6保存来访人员信息")
print("输入数字0退出该系统")




class Sysm(object):
        def __init__(self):
               pass

        def tianjia(self,person):
                """功能：添加来访人员信息"""
                if self == 1:
                        name = input("请输入你的名字：")
                        age = input("请输入你的年龄：")
                
                        QQ = input("请输入你的QQ号：")
                        wechat = input("请输入你的微信号：")
                        new_person = {}
                        new_person["name"] = name
                        new_person["age"] = age
                        new_person["QQ"] = QQ
                        new_person["wechat"] = wechat
                        person.append(new_person)
                

        def xiugai(self,person):
                """功能：修改来访人员信息"""
                if self == 2:
                        change_infor = input("请输入你想更改的对象name:")
                
                        for temp in person:
                                if change_infor == temp["name"]:
                                        change1_infor = input("请输入你想更改的信息类型name/age/QQ/wechat:")
                                        new_infor = input("请输入你想更改的信息内容:")
                                        temp[change1_infor] = new_infor
                                        break
                        else:
                                print("查无此人")

        def shanchu(self,person):
                """功能：删除来访人员信息"""
                if self == 3:
                        del_person = input("请输入你要删除的名字：")
                        for temp in person:
                                if del_person == temp["name"]:
                                        person.remove(temp) 
                                        #print(person)
                                        break
                        else:
                                print("查无此人请再操作一遍")

        def chaxun(self,person):
                """功能：查询来访人员信息"""
                if self == 4:
                        find_name = input("请输入你想查找的名字：")
                        for temp in person:
                                if find_name == temp["name"]:
                                        print("%s\t%s\t%s\t%s"%(temp["name"],temp["age"],temp["QQ"],temp["wechat"]))
                                        break
                        else: 
                                print("查无此人")

        def xianshi(self,person):
                """功能：显示来访人员信息"""
                if self == 5:
                        print("姓名\t年龄\tQQ\t微信")
                        for temp in person:
                                print("%s\t%s\t%s\t%s"%(temp["name"],temp["age"],temp["QQ"],temp["wechat"]))

        def save_data(self,person):
                if self == 6:
                        f = open("backup.data","w")
                        f.write(str(person))
                        f.close()
                        print("保存成功！")

        def load_data(self):
                try:
                        f = open("backup.data")
                        person = eval(f.read())
                        f.close()
                except Exception:
                        pass

        def tuichu(self,person):
                """功能：退出此系统"""
                if self == 0:
                        print("欢迎下次再来")
                        global flag
                        flag = 0

        def berror(self,person):
                """功能：操作有误提醒重新输入"""
                if self not in range(0,7):
                        print("输入错误，请重新输入相应数字进行系统操作")



def main():
        Sysm.load_data(1)
        num = int(input("请输入相应数字进行系统操作："))
        Sysm.tianjia(num,person)
        Sysm.xiugai(num,person)
        Sysm.shanchu(num,person)
        Sysm.chaxun(num,person)
        Sysm.xianshi(num,person)
        Sysm.save_data(num,person)
        Sysm.tuichu(num,person)
        Sysm.berror(num,person)
        

while flag:
        if __name__ == "__main__":
                main()
                