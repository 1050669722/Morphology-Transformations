'''
对图片实现对焦模糊
'''

import cv2
import numpy as np
import random

def cv_show(name, img):
    img = cv2.resize(img, (3 * img.shape[1], 3 * img.shape[0]))
    cv2.imshow(name, img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# img = cv2.imread(' ')
#
# filter = 1 / 16 * np.ones((4, 4))
# img_filter = cv2.filter2D(img, -1, filter)
# # img_filter = cv2.GaussianBlur(img, (5, 5), 1)
#
# cv_show('img', img_filter)

pic = ' '
img = cv2.imread(pic)

tmp = img.copy()
k_sizes = [2, 3]#[2, 3, 4]#
for _ in range(10):
    k_size = random.sample(k_sizes, 1)[0]
    filter = 1 / (k_size * k_size) * np.ones((k_size, k_size))
    img_filter = cv2.filter2D(img[119:119+17, 56:56+51], -1, filter) #56 119 51 17
    img[119:119+17, 56:56+51] = img_filter

    cv_show('img', img)
    cv2.imwrite(pic[:-4]+'-focus-blurred.jpg', img)

    img = tmp.copy()

