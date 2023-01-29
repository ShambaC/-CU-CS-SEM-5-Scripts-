import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('arceus.jpg')
img = cv2.resize(img, (500, 500))

plt.figure(figsize=[24, 18])

R, G, B = cv2.split(img)

R_O = cv2.equalizeHist(R)
G_O = cv2.equalizeHist(G)
B_O = cv2.equalizeHist(B)

img1 = cv2.merge((R_O, G_O, B_O))

#ADAPTIVE HISTOGRAM METHOD
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

R1_O = clahe.apply(R)
G1_O = clahe.apply(G)
B1_O = clahe.apply(B)

img2 = cv2.merge((R1_O, G1_O, B1_O))

#histogram calculation of all image
hist = cv2.calcHist([img], [0], None, [256], [0,256])
hist1 = cv2.calcHist([img1], [0], None, [256], [0,256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0,256])

#plotting with image

plt.subplot(3, 2, 1)
plt.imshow(img)
plt.title("O_image")

plt.subplot(3, 2, 2)
plt.plot(hist)
plt.plot(np.arange(0, 256), hist.reshape(256))
plt.fill_between(np.arange(0, 256), hist.reshape(256, ))
plt.xlim([0, 256])
plt.title("O_hist")

plt.subplot(3, 2, 3)
plt.imshow(img1)
plt.title("img1_image")

plt.subplot(3, 2, 4)
plt.plot(hist1)
plt.plot(np.arange(0, 256), hist.reshape(256))
plt.fill_between(np.arange(0, 256), hist.reshape(256, ))
plt.xlim([0, 256])
plt.title("img1_hist")

plt.subplot(3, 2, 5)
plt.imshow(img2)
plt.title("img2_image")

plt.subplot(3, 2, 6)
plt.plot(hist2)
plt.plot(np.arange(0, 256), hist.reshape(256))
plt.fill_between(np.arange(0, 256), hist.reshape(256, ))
plt.xlim([0, 256])
plt.title("img2_hist")

plt.show()