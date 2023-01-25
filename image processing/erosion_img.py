import cv2
import numpy as np

img = cv2.imread('075.png')
img = cv2.resize(img, (512, 712))

cv2.imshow('ORIGINAL', img)

kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('eroded', erosion)
cv2.imshow('dilated', dilation)

while cv2.waitKey(0) == ord('q') :
    cv2.destroyAllWindows()
    break