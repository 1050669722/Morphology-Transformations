'''
给图片添加弱光效果
'''

import cv2
import numpy as np
import random
import time
import math

def cv_show(name, img):
    img = cv2.resize(img, (3 * img.shape[1], 3 * img.shape[0]))
    cv2.imshow(name, img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

def lowLight(img, strength=200):
    # 获取图像行和列
    rows, cols = img.shape[:2]
    # 设置中心点
    centerX = rows // 2
    centerY = cols // 2
    centerX += random.uniform(-1, 1) * 0.5 * centerX
    centerY += random.uniform(-1, 1) * 0.5 * centerY
    # print(centerX, centerY)
    # radius = min(centerX, centerY)
    radius = max(centerX, centerY)
    # print(radius)
    # 新建目标图像
    dst = np.zeros((rows, cols, 3), dtype="uint8")
    # 图像光照特效
    # t0 = time.perf_counter()
    # for _ in range(1000):
    for i in range(rows):  #可以一次性完成，不用循环
        for j in range(cols):
            # 计算当前点到光照中心距离(平面坐标系中两点之间的距离)
            distance = math.pow((centerY - j), 2) + math.pow((centerX - i), 2)
            # 获取原始图像
            B = img[i, j][0]
            G = img[i, j][1]
            R = img[i, j][2]
            if (distance < radius * radius):
                # 按照距离大小计算增强的光照值
                result = (int)(strength * (1.0 - math.sqrt(distance) / radius))
                B = img[i, j][0] + result
                G = img[i, j][1] + result
                R = img[i, j][2] + result
                # 判断边界 防止越界
                B = min(255, max(0, B))
                G = min(255, max(0, G))
                R = min(255, max(0, R))
                dst[i, j] = np.uint8((B, G, R))
            else:
                dst[i, j] = np.uint8((B, G, R))
    # print(time.perf_counter()-t0)
    return dst


# 读取原始图像
pic = ' '
img = cv2.imread(pic)

tmp = img.copy()
for _ in range(10):
    # 处理图像
    s = random.uniform(-150, -50)
    img_filter = lowLight(img[119:119+17, 56:56+51], strength=s)

    # 显示图像
    img[119:119+17, 56:56+51] = img_filter
    cv_show('img', img)

    # 保存
    cv2.imwrite(pic[:-4]+'-low-light.jpg', img)

    img = tmp.copy()

