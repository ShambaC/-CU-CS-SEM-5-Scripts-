import cv2

img1 = cv2.imread('puppy.jpg')
img2 = cv2.imread('cat.jpg')

img2 = cv2.resize(img2, (512, 512))
img1 = cv2.resize(img1, (512, 512))

sub = cv2.subtract(img1, img2)
cv2.imwrite('SUB_ishani.jpg', sub)