import cv2
import numpy as np

img = cv2.imread("Lenna.png")

kernel = np.ones((5, 5), np.float32) / 25

#box filter
hblur = cv2.filter2D(img, -1, kernel)
cv2.imshow('arceus_mean.jpg', hblur)

# Gauss filter
gblur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('arceus_gaussian.jpg', gblur)

#median filter
mblur = cv2.medianBlur(img, 5)
cv2.imshow('arceus_median.jpg', mblur)

#average filter
ablur = cv2.blur(img, (5, 5))
cv2.imshow('arceus_avg.jpg', ablur)

#bilateral filter
b_blur = cv2.bilateralFilter(img, 9, 70, 80)
cv2.imshow('arceus_bilat.jpg', b_blur)

cv2.waitKey(4000)
cv2.destroyAllWindows()