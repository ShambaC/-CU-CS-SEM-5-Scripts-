import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Lenna.png")

plt.figure(figsize=[16, 12])

red = cv2.calcHist([img], [0], None, [256], [0, 255])
green = cv2.calcHist([img], [1], None, [256], [0, 255])
blue = cv2.calcHist([img], [2], None, [256], [0, 255])

plt.subplot(4, 2, 1)
plt.imshow(img)

plt.subplot(4, 2, 2)
plt.xlim([0, 256])
plt.plot(red, color='r')
plt.title("red-scale")

plt.subplot(4, 2, 4)
plt.xlim([0, 256])
plt.plot(green, color='g')
plt.title("green-scale")

plt.subplot(4, 2, 6)
plt.xlim([0, 256])
plt.plot(blue, color='b')
plt.title("blue-scale")

plt.show()