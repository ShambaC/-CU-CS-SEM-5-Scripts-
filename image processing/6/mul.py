import cv2

img1 = cv2.imread('puppy.jpg')
img2 = cv2.imread('cat.jpg')

img2 = cv2.resize(img2, (512, 512))
img1 = cv2.resize(img1, (512, 512))

mul_res = cv2.multiply(img1, img2)
cv2.imwrite('Mul_ishani.jpg', mul_res)