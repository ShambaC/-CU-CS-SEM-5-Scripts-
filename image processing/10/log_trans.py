import cv2
import numpy as np

G_img = cv2.imread('arceus.jpg',0)
row, col = G_img.shape
log_img = np.copy(G_img)

c = 255 / np.log(1 + np.amax(G_img))

for i in range(0, row):
    for j in range(0, col):
        log_img[i, j] = c * np.log(1 + G_img[i, j])
   
# Specify the data type so that 
# float value will be converted to int 
log_img = np.array(log_img, dtype = np.uint8)


cv2.imwrite('Log_T_arceus.png',log_img)