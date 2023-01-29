import cv2
import matplotlib.pyplot as plt


img = cv2.imread("arceus.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img1 = cv2.GaussianBlur(img, (5, 5), 0)
img1 = cv2.Canny(img, 100, 200)

plt.figure(figsize=[18,12])


plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("O_image")

plt.subplot(1, 2, 2)
plt.imshow(img1, cmap="gray")
plt.title("canny_image")

plt.show()