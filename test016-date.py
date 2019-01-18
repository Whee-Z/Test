#输出指定格式的日期
import datetime

#输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print(datetime.date.today().strftime('%d/%m/%Y'))

#创建日期对象
BirthDate = datetime.date(1949,10,1)
print(BirthDate.strftime('%m/%d/%Y'))

#日期算术运算
miyazakiBirthNextDay = BirthDate + datetime.timedelta(days=1)
print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

#日期替换
FirstBirthday = BirthDate.replace(year=BirthDate.year + 1)
print(FirstBirthday.strftime('%Y/%m/%d'))