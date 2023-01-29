import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("arceus.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
 
lap=cv2.Laplacian(img,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))

plt.figure(figsize=[18,12])

plt.subplot(1,2,1)
plt.imshow(img,cmap="gray")
plt.title("Original_image")

plt.subplot(1,2,2)
plt.imshow(lap,cmap="gray")
plt.title("laplacian_image")

plt.show()