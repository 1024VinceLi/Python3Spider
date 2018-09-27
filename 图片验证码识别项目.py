import tesserocr
from PIL import Image

image = Image.open('code.jpg')

image = image.convert('L') # 将图片转化为灰度图片
threshold = 126 # 指定阈值
table = []
for i in range(256):
    if i < threshold:
        table.append(0) # 灰度小于阈值的删除
    else:
        table.append(1) # 灰度大于阈值的保留

image = image.point(table, '1') # point函数：返回给定查找表对应的图像像素值的拷贝。
result = tesserocr.image_to_text(image)
print(result)