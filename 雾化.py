'''
雾化
模拟撞击形变
'''

import cv2
import numpy as np
import random

def cv_show(name, img):
    img = cv2.resize(img, (3 * img.shape[1], 3 * img.shape[0]))
    cv2.imshow(name, img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


def addFog(img):
    tmp = img.copy()
    h, w, c = img.shape
    for i in range(h): #可以一次性实现
        for j in range(w): #同一个通道得绑定在一起
            # k = random.uniform(0, max(h, w))
            # k = random.uniform(0, 3)
            k = random.uniform(0, random.sample([5, 10], 1)[0]) #此处k需要每轮不一样
            # k = random.sample([1, 2], 1)[0]
            k %= 20#3# #对于k的限制 #不会大于等于4
            k = int(k)
            # k = 1
            dy = min(i + k, h - 1)
            dx = min(j + k, w - 1)
            img[i, j, :] = tmp[dy, dx, :]

    return img


# 读取原始图像
pic = ' '
img = cv2.imread(pic)

# 获取图片形状
h, w, c = img.shape
meanHW = (h + w) // 2

tmp = img.copy()
for _ in range(10):
    # 选择区域
    top = int(random.uniform(0.3, 0.5) * h)
    height = int(random.uniform(0.3 * meanHW, 0.5 * meanHW))
    left = int(random.uniform(0.1, 0.4) * w)
    width = int(random.uniform(0.3 * meanHW, 0.5 * meanHW))

    # 处理图像
    img_filter = addFog(img[top : top + height, left : left + width])
    # img_filter = addFog(img)

    # 显示图像
    img[top : top + height, left : left + width] = img_filter
    # img = img_filter
    cv_show('img', img)

    # 保存
    cv2.imwrite(pic[:-4] + '-strike.jpg', img)

    img = tmp.copy()
