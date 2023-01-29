import cv2
import numpy as np

#read image
image = cv2.imread('arceus.jpg')

#define gamma
gamma = 2.2

#create lookup table
values = np.arange(0, 256)
lt = np.uint8(255 * np.power((values/255.0), gamma))

#gamma adjustment.
result = cv2.LUT(image, lt)

cv2.imwrite('Power_arceus.png', result)