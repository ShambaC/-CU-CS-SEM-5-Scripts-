import cv2

img = cv2.imread('Lenna.png')

img2 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('90 CLOCK', img2)
cv2.waitKey(2000)
cv2.destroyAllWindows()

img2 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('90 ANTICLOCK', img2)
cv2.waitKey(2000)
cv2.destroyAllWindows()

img2 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('180', img2)
cv2.waitKey(2000)
cv2.destroyAllWindows()