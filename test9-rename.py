import os

#输入你想重命名的文件夹名
folder_name = input("请输入你想修改的文件夹名字：")

#os.chdir(folder_name)

#获取文件夹中的所有文件的文件名
all_file = os.listdir(folder_name)

#对文件名进行修改
for file in all_file:
    print(file)
    old_name = folder_name + "/" + file
    new_name = folder_name + "/" + "[Whee出品]" + file
    os.rename(file,new_name)
