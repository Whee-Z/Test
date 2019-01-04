#对Excel进行读操作
import xlrd

#打开指定路径中的.xls文件
xlsfile = r"E:\test1.xls"
#创建一个对象
book = xlrd.open_workbook(xlsfile)
#通过sheet索引获得sheet对象
sheet0 = book.sheet_by_index(0)
#获得指定索引sheet表的名字
sheet_name = book.sheet_names()[0]
print("表格的名字%s"%sheet_name)
#通过sheet名字获取sheet对象
sheet1 = book.sheet_by_name(sheet_name)
#获取总行数
sum_rows = sheet0.nrows
print("表格的总行数%s"%sum_rows)
#循环打印每一行的内容
for i in range(sum_rows):
    print("第%d行的数据为%s"%(i+1,sheet1.row_values(i)))
#获取总列数
sum_cols = sheet0.ncols
print("表格的总列数%s"%sum_cols)
#获取第一行数据
row_data = sheet0.row_values(0)
print("表格的第一行数据%s"%row_data)
#获取第一列数据
col_data = sheet0.col_values(0)
print("表格的第一列数据%s"%col_data)
#通过坐标获取表格数据
cell_value1 = sheet0.cell_value(0,0)
cell_value2 = sheet0.cell_value(0,1)
print("（0,0）坐标的值是%s，（0,1）坐标的值是%s"%(cell_value1,cell_value2))
