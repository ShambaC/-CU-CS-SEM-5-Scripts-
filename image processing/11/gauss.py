import cv2
import numpy as np

img = cv2.imread('arceus.jpg')
s = img.size

# Generate Gaussian noise
gauss = np.random.normal(0,1,s)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')

# Add the Gaussian noise to the image
img_gauss = cv2.add(img,gauss)

cv2.imshow('gauss_arceus.png',img_gauss)



# Removal with fiolter
gblur = cv2.GaussianBlur(img_gauss, (3, 3), 0)
cv2.imshow('gauss_arceus2.png',gblur)

M = np.float32([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
gblur2 = cv2.filter2D(img_gauss, None, M)
cv2.imshow('gauss_arceus3.png',gblur2)

cv2.waitKey(4000)
cv2.destroyAllWindows()