'''
给图片产生畸变
模拟撞击形变
'''

import cv2
import numpy as np
import random
import Augmentor
import Augmentor

def cv_show(name, img):
    img = cv2.resize(img, (3 * img.shape[1], 3 * img.shape[0]))
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 读取原始图像
pic = './01A03035=2.jpg'
img = cv2.imread(pic)

# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = [img]
p = Augmentor.DataPipeline(img)

# p.rotate(1, max_left_rotation=5, max_right_rotation=5)
# p.flip_top_bottom(0.5)
# p.zoom_random(1, percentage_area=0.5)
# p.random_distortion(probability=1, grid_width=3, grid_height=3, magnitude=5)
p.gaussian_distortion(probability=1, grid_width=2, grid_height=2, magnitude=1, corner='ul', method='in', mex=0.5, mey=0.5, sdx=0.05, sdy=0.05)


img = p.sample(1)
img = np.array(img)
img = img[0, :, :, :]

cv_show('name', img)

pass
