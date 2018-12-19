from PIL import Image
import os
#import imtools

#读取一幅图像
pil_im = Image.open('test.jpg')
pil_im.show()

#转换为灰度图像
pil_im = Image.open('test.jpg').convert('L')
pil_im.show()

#复制和粘贴图像区域
box = (100,100,200,200)
region = pil_im.crop(box)
region.show()
region = region.transpose(Image.ROTATE_180)
region.show()
pil_im.paste(region,box)
pil_im.show()

#调整尺寸和旋转图像
out = pil_im.resize((1024,1024))
out.show()
out = pil_im.rotate(45)
out.show()

#创建缩略图
pil_im.thumbnail((128, 128))
pil_im.show()
