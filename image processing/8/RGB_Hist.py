import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("arceus.jpg")

for i, col in enumerate(['b', 'g', 'r']) :
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.subplot(1, 2, 2)
    plt.title("Histogram")
    plt.plot(hist, color=col)
    plt.xlim([0,255])

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Image")
plt.show()