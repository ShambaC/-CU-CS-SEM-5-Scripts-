import cv2

x = [255, 180, 160]
img = cv2.imread('Lenna.png')

replicate = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT)

cv2.imshow('original', img)
cv2.imshow('replicate', replicate)
cv2.imshow('reflect', reflect)
cv2.imshow('reflect101', reflect101)
cv2.imshow('wrap', wrap)
cv2.imshow('constant', constant)

while cv2.waitKey(0) == ord('q') :
    cv2.destroyAllWindows()
    break
