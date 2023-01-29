import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('arceus.jpg', 0)
plt.figure(figsize=[17, 13])

img = cv2.resize(img,(500,500))

img1 = cv2.equalizeHist(img)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
img2 = clahe.apply(img)

hist = cv2.calcHist([img], [0], None, [256], [0,256])
hist1 = cv2.calcHist([img1], [0], None, [256], [0,256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0,256])


plt.subplot(3, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("O_image")

plt.subplot(3, 2, 2)
plt.plot(hist)
plt.plot(np.arange(0, 256),hist.reshape(256))
plt.fill_between(np.arange(0, 256),hist.reshape(256, ))
plt.xlim([0, 256])
plt.title("O_hist")

plt.subplot(3, 2, 3)
plt.imshow(img1, cmap="gray")
plt.title("img1_image")

plt.subplot(3, 2, 4)
plt.plot(hist1)
plt.plot(np.arange(0, 256),hist.reshape(256))
plt.fill_between(np.arange(0, 256),hist.reshape(256, ))
plt.xlim([0, 256])
plt.title("img1_hist")

plt.subplot(3, 2, 5)
plt.imshow(img2,cmap="gray")
plt.title("img2_image")

plt.subplot(3, 2, 6)
plt.plot(hist2)
plt.plot(np.arange(0, 256),hist.reshape(256))
plt.fill_between(np.arange(0, 256),hist.reshape(256, ))
plt.xlim([0, 256])
plt.title("img2_hist")

plt.show()