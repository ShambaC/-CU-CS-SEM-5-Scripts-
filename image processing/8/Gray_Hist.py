import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("arceus.jpg", 0)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Image")

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.subplot(1, 2, 2)
plt.plot(hist, color='black')
plt.title("Histogram")
plt.show()