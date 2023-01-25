import cv2
import numpy as np

img1 = cv2.imread('Lenna.png')
img2 = cv2.imread('hotarou.png')

img2 = cv2.resize(img2, (512,512))

h, w, _ = img1.shape

img0 = np.zeros(shape=(h, w, 3), dtype=np.uint8)

for i in range(0, h) :
    for j in range(0, w) :
        img0[i][j] = 2

img3 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
img3 = cv2.divide(img3, img0)

cv2.imshow('AVG', img3)
cv2.waitKey(3000)
cv2.destroyAllWindows()