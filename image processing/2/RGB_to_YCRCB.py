import cv2

img  = cv2.imread('arceus.jpg')

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
cv2.imwrite('arceus_ycrcb.jpg', img2)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


th1, res1 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('arceus_THRESH_BINARY.jpg', res1)

th2, res2 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite('arceus_THRESH_BINARY_INV.jpg', res2)

th3, res3 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TRUNC)
cv2.imwrite('arceus_THRESH_TRUNC.jpg', res3)

th4, res4 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TOZERO)
cv2.imwrite('arceus_THRESH_TOZERO.jpg', res4)

th5, res5 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imwrite('arceus_THRESH_TOZERO_INV.jpg', res5)