import cv2

image = cv2.imread('Lenna.png', 0)

#cv2.imwrite('Lenna_Gray.png', image)

cv2.imshow('lennagray.jpg', image)
cv2.waitKey(3000)
cv2.destroyAllWindows()