#字符串常用操作

STR = "  a    ssfsfasg  234231,dfsdg   "

#首字母变大写
str1 = STR.capitalize()
print(str1)
#统计字符出现的次数
str2 = STR.count('s')
print(str2)
#字符串放在中间
str3 = STR.center(50,'#')
print(str3)
#是否以某一字符串结尾
str4 = STR.endswith('haha')
print(str4)
#查找字符串第一次出现的位置，返回索引值
str5 = STR.find('a')
print(str5)
#判断是否全为数字
str6 = STR.isalnum()
print(str6)
#判断是否全为字母
str7 = STR.isalpha()
print(str7)
#判断是否全为整数
str8 = STR.isdigit()
print(str8)
#判断是否是一个合法的标识符
str9 = STR.isidentifier()
print(str9)
#判断是否全为大写
str10 = STR.isupper()
print(str10)
#判断是否全为小写
str11 = STR.islower()
print(str11)
#小写变大写
str12 = STR.lower()
print(str12)
#大写变小写
str13 = STR.upper()
print(str13)
#去空格
str14 = STR.strip()
print(str14)
#替换
str15 = STR.replace('s','zgh',3)
print(str15)
#切割,返回一个列表
str16 = STR.split(',')
print(str16)

