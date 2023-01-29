import cv2
import numpy as np


img = cv2.imread("arceus.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)

sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

# cv2.imwrite('sobelx.jpg',sobelX)
# cv2.imwrite('sobely.jpg',sobelY)
cv2.imwrite('arceus_sobel.jpg',sobelX+sobelY)