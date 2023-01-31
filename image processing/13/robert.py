import cv2
import numpy as np


img = cv2.imread("arceus.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


 
kX=np.array([[1, 0], [0, -1]])
kY=np.array([[0, 1], [-1, 0]])

RobertX=cv2.filter2D(img, -1, kX)
RobertY=cv2.filter2D(img, -1, kY)
#pxy=cv2.addWeighted(prewittX,0.5,prewittY,0.5,0)

res = cv2.add(RobertX, RobertY)


# cv2.imwrite('Px.jpg',prewittX)
# cv2.imwrite('Py.jpg',prewittY)
cv2.imshow('arceus_Gxy.jpg',res)
cv2.waitKey(0)