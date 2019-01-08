#利用ellipse 和 rectangle 画图
from tkinter import *

#创建窗口
window = Tk()
#给窗口命名
window.title("test1")
#画布大小及背景色
canvas = Canvas(window,width = 500,height = 600,bg = 'blue')

left = 20
right = 50
top = 50
num = 15
for i in range(num):
    canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
    canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
    canvas.create_rectangle(20 - 2 * i,20 - 2 * i,10 * (i + 2),10 * ( i + 2))
    right += 5
    left += 5
    top += 10

canvas.pack()
mainloop()