import cv2
import numpy as np
import random


img = cv2.imread("arceus.jpg")
h, w, _ = img.shape
img1 = np.zeros(shape=(h, w, 3), dtype=np.uint8)
pepper = 0.05
salt = 1-0.05
for i in range(h):
    for j in range(w):
        y=random.random()
        if y < pepper:
            img1[i][j] = [0, 0, 0]
        elif y > salt:
            img1[i][j] = [255,255,255]
        else:
            img1[i][j] = img[i][j]

cv2.imwrite('salted_arceus.png', img1)