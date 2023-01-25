import cv2
import matplotlib.pyplot as plt
import numpy as np

# Grayscale histogram
G_img = cv2.imread("Lenna.png", 0)

hist = cv2.calcHist([G_img], [0], None, [256], [0, 256])

plt.plot(np.arange(0, 256), hist.reshape(256))
plt.fill_between(np.arange(0, 256), hist.reshape(256,))
plt.title("GRAY IMAGE")
plt.show()

# RGB
R_img = cv2.imread("Lenna.png")

for i, col in enumerate(['b', 'g', 'r']) :
    hist2 = cv2.calcHist([R_img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 255])

plt.title("RGB IMAGE")
plt.show()