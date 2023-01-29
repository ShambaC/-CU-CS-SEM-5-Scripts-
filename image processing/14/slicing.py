import cv2
import numpy as np

img1=cv2.imread('Lenna.png')
img2=cv2.imread('arceus.jpg')

img1=cv2.resize(img1,(256,256))
img2=cv2.resize(img2,(256,256))

img3=np.hstack((img2[:,0:127],img1[:,128:256]))


# cv2.imshow('Lenna_trimmed.jpg',img1[:,0:128])
# cv2.imshow('Arceus_trimmed.jpg',img2[:,128:256])
cv2.imwrite('Combined2.jpg',img3)