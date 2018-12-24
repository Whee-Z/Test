#有消息来了头像显示数字
from PIL import Image,ImageDraw,ImageFont

def addNum(num,image):
    img = Image.open(image)
    width,height = img.size
    fontSize = height//10
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default().font
    #确定显示的 位置，数字，颜色，字体
    draw.text((width-fontSize,10),num,(256,0,0))
    del draw
    img.save('test_addNum.jpg')
    img.show()
if __name__ == '__main__':
    addNum('666','test.jpg')

