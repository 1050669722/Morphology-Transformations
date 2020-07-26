'''
对图像实现运动模糊
'''

import cv2
import numpy as np
import random

def cv_show(name, img):
    img = cv2.resize(img, (3 * img.shape[1], 3 * img.shape[0]))
    cv2.imshow(name, img)
    # cv2.resizeWindow(name, 600, 600)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# motion filter
def motion_filter(img, K_size=3):
    H, W, C = img.shape

    # Kernel
    K = np.diag([1] * K_size).astype(np.float)
    K /= K_size

    # zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
    out[pad: pad + H, pad: pad + W] = img.copy().astype(np.float)
    tmp = out.copy()

    # filtering #应该可以一次性完成，不用循环
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out

# Read image
pic = ' '
img = cv2.imread(pic)

tmp = img.copy()
k_sizes = [2, 3]#[2, 3, 4]#
for _ in range(10):
    # motion filtering
    k_size = random.sample(k_sizes, 1)[0]
    img_filter = motion_filter(img[119:119+17, 56:56+51], K_size=k_size)
    img[119:119+17, 56:56+51] = img_filter

    # Save result
    # img = cv2.resize(img, (600, 600))
    cv_show("result", img)
    cv2.imwrite(pic[:-4]+'-motion-blurred.jpg', img)

    img = tmp.copy()
