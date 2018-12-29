""""图像轮廓和直方图"""
from PIL import Image
from pylab import *

#读取一幅图像到数组中
image = array(Image.open('test.jpg').convert('L'))

#新建一个图像
figure()

#不使用颜色信息
gray()

#在原点的左上角显示轮廓图像
contour(image,origin='image')
axis('equal')
axis('off')
show()

#绘制图像直方图
figure()
hist(image.flatten(),128)
show()

