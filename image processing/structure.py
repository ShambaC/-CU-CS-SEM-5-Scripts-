from email.mime import image
import cv2
import numpy as np

img = cv2.imread('075.png')
img = cv2.resize(img, (512, 712))

cv2.imshow('ORIGINAL', img)

element = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
eroded_img = cv2.erode(img, element)

cv2.imshow('erode', eroded_img)

while cv2.waitKey(0) == ord('q') :
    cv2.destroyAllWindows()
    break