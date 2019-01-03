#对Excel进行写操作
import xlwt

#创建一个Workbook对象，相当于创建一个Excel文件
# 默认编码是ascii,style_compression表示是否压缩，不常用
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
#创建一个sheet对象，相当于一个表格
# 第一个参数代表表格的名字，第二个参数表是否覆盖单元格
sheet = book.add_sheet('info',cell_overwrite_ok=True)
#添加数据,前两个参数代表坐标
sheet.write(0,0,'name')
sheet.write(0,1,'age')

sheet.write(1,0,u'小明')
sheet.write(1,1,19)
#保存数据
book.save(r'e:\test1.xls')

