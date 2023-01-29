import cv2

img1 = cv2.imread('puppy.jpg')
img2 = cv2.imread('cat.jpg')

img2 = cv2.resize(img2, (512, 512))
img1 = cv2.resize(img1, (512, 512))

div_res = cv2.divide(img1, img2)
cv2.imwrite('div_ishani.jpg', div_res)