""""绘制图像、点和线"""
from PIL import Image
from pylab import *

#读取一幅图像到数组中
image = array(Image.open('test.jpg'))

#绘制图像
imshow(image)

#给出一些点
x = [100,100,200,200]
y = [150,220,120,220]

#用红色星状标记这些点
plot(x,y,'r*')

#连接前两个点的线
plot(x[:2],y[:2])

#添加标题，显示图像
title('ploting:test.jpg')
show()

