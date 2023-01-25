import numpy as np
import cv2 as cv

pencil_color = np.uint8([[[35, 66, 100]]])
hsv_pencil = cv.cvtColor(pencil_color, cv.COLOR_BGR2HSV)
print(hsv_pencil)