"""复制一个文件"""
#输入用户想要复制的文件
file_name = input("请输入想要复制的文件名：")

#打开用户想要复制的文件
old_file = open(file_name,"r")
position = file_name.rfind(".")
new_filename = file_name[0:position] + "[复件]" + file_name[position:]
#创建一个新文件来保存复制的文件
new_file = open(new_filename,"w")
while True:
    content = old_file.read(1024)
    if len(content) == 0:
        break
    new_file.write(content)
#关闭文件
old_file.close()
new_file.close()