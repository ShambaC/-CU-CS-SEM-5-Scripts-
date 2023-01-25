import cv2

img = cv2.imread('Lenna.png')

h, w, c = (img.shape)

cx = h/2
cy = w/2

for i in range(0, 180, 20):
    M = cv2.getRotationMatrix2D((cx, cy), -i, 1)
    img1 = cv2.warpAffine(img, M, (w, h))
    cv2.imshow('WINDOW', img1)
    cv2.waitKey(1000)
cv2.destroyAllWindows()