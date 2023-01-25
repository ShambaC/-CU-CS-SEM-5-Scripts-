import cv2
import numpy as np

img1 = np.zeros((500, 500), dtype="uint8")
cv2.rectangle(img1, (100, 100), (400, 400), 255, -1)

img2 = np.zeros((500, 500), dtype="uint8")
cv2.circle(img2, (400, 400), 90, 255, -1)

b_AND = cv2.bitwise_and(img1, img2)
b_OR = cv2.bitwise_or(img1, img2)
b_NOT1 = cv2.bitwise_not(img1)
b_NOT2 = cv2.bitwise_not(img2)

cv2.imshow('WINDOW', img1)
cv2.waitKey(1500)
cv2.imshow('WINDOW', img2)
cv2.waitKey(1500)
cv2.imshow('WINDOW', b_AND)
cv2.waitKey(1500)
cv2.imshow('WINDOW', b_OR)
cv2.waitKey(1500)
cv2.imshow('WINDOW', b_NOT1)
cv2.waitKey(1500)
cv2.imshow('WINDOW', b_NOT2)
cv2.waitKey(1500)