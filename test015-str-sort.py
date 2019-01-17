#字符串排序
str1 = input('请输入排序的第一个字符串:')
str2 = input('请输入排序的第二个字符串:')
str3 = input('请输入排序的第三个字符串:')
print("排序前：",str1, str2, str3)

if str1 > str2: str1, str2 = str2, str1
if str1 > str3: str1, str3 = str3, str1
if str2 > str3: str2, str3 = str3, str2

print("排序后：",str1, str2, str3)