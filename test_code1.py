import cv2
import numpy as np
import random

import pandas as pd  
from PIL import Image

img = cv2.imread(r'C:\Users\liguangzhi-001\Desktop\yc6_point.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
# 找到图像中的黑色像素
indices = np.where((img[:,:,0] == 0) & (img[:,:,1] == 0) & (img[:,:,2] == 0))

# 将黑色像素的alpha通道设为0
img[indices[0], indices[1], 3] = 0

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 读取图像
#img = cv2.imread('your_image.png', cv2.IMREAD_GRAYSCALE)

# 对图像进行二值化处理
_, binary_img = cv2.threshold(img_gray, 1, 255, cv2.THRESH_BINARY)

# 找到二值化图像中的前景像素
foreground = cv2.bitwise_and(img, img, mask=binary_img)

# 显示前景图像

# 保存结果图像为png格式
cv2.imwrite('foreground.png', foreground)
cv2.imshow('img', foreground)

cv2.waitKey(1000)



print("changed")

# img = Image.open(r'C:\Users\liguangzhi-001\Desktop\yc6_point.png')
# img.show()
