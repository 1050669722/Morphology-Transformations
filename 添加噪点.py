'''
给图片添加噪点
'''

import cv2
import numpy as np
import random
from skimage.util import random_noise

def cv_show(name, img):
    img = cv2.resize(img, (3 * img.shape[1], 3 * img.shape[0]))
    cv2.imshow(name, img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# 读取原始图像
pic = ' '
img = cv2.imread(pic)

# 处理图像
img_filter = random_noise(img[119:119+17, 56:56+51], mode='gaussian', clip=True)
# img = random_noise(img, mode='gaussian', clip=True)
# img = random_noise(img, mode='salt', clip=True)
# img = random_noise(img, mode='pepper', clip=True)
# img = random_noise(img, mode='speckle', clip=True)
# img = random_noise(img, mode='s&p', clip=True)

# 显示图像
img[119:119+17, 56:56+51] = img_filter * 255 #img_filter.min = 0.0, img_filter.max() = 1.0
cv_show('img', img)

# # 保存
cv2.imwrite(pic[:-4] + '-RandomNoise.jpg', img)




