'''
给图片产生划痕
数量 起点 方向 走向 长度
随机的
'''

import cv2
import numpy as np
import random

def cv_show(name, img):
    img = cv2.resize(img, (3 * img.shape[1], 3 * img.shape[0]))
    cv2.imshow(name, img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# 读取原始图像
pic = './01A03035=2.jpg'
img = cv2.imread(pic)

# 获取图片形状
h, w, c = img.shape
meanHW = (h + w) // 2

tmp = img.copy()
for _ in range(10):

    # 划痕数量
    num = random.sample([1, 2, 3], 1)[0]

    # 画出划痕
    for _ in range(num):

        # 设置起点
        # pt1 = (w//2, h//2) #x and y
        pt1 = (int(random.uniform(0.4, 0.6) * w), int(random.uniform(0.4, 0.6) * h))
        # 设置方向
        xDirection, yDirection = random.sample([-1, 1], 1)[0], random.sample([-1, 1], 1)[0] #大致方向，每条划痕只有一个大致方向
        for _ in range(num):
            for _ in range( int(random.uniform(3, 10)) ):
                xUnitLength, yUnitLength = random.uniform(0, random.uniform(0, 0.07 * meanHW)), random.uniform(0, random.uniform(0, 0.07 * meanHW)) #每一步的方向，随机的，但是不会跳出大致方向
                pt2 = (pt1[0] + int(xDirection * xUnitLength), pt1[1] + int(yDirection * yUnitLength))
                cv2.line(img, pt1, pt2, (255, 255, 255), 1)
                pt1 = pt2

    # 展示图片
    cv_show('name', img)

    # 保存
    cv2.imwrite(pic[:-4]+'-scratch.jpg', img)

    img = tmp.copy()




