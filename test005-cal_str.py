#统计出其中英文字母、空格、数字和其它字符的个数
import string

sen = input('请输入一个字符串:')
letters = 0
spaces = 0
digits = 0
others = 0
i=0
while i < len(sen):
    c = sen[i]
    i += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        spaces += 1
    elif c.isdigit():
        digits += 1
    else:
        others += 1
print ("letters = %d,spaces = %d,digits = %d,others = %d" % (letters,spaces,digits,others))