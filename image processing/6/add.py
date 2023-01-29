import cv2

img1 = cv2.imread('puppy.jpg')
img2 = cv2.imread('cat.jpg')

img2 = cv2.resize(img2, (512, 512))
img1 = cv2.resize(img1, (512, 512))

w_sum = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)
cv2.imwrite('W_SUM_ishani.jpg', w_sum)