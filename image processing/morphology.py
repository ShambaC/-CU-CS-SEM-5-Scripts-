import cv2
import numpy as np

img = cv2.imread('075.png')
img = cv2.resize(img, (512, 712))

cv2.imshow('ORIGINAL', img)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)             #erosion + dilation
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)            #dilation + erosion
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)        #dilation - erosion
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)         #i/p - opening
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)       #closing - o/p

cv2.imshow('OPENING', opening)
cv2.imshow('CLOSING', closing)
cv2.imshow('GRADIENT', gradient)
cv2.imshow('TOP HAT', top_hat)
cv2.imshow('BLACK HAT', black_hat)

while cv2.waitKey(0) == ord('q') :
    cv2.destroyAllWindows()
    break