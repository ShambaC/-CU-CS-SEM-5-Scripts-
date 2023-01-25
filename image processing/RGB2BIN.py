import cv2

img  = cv2.imread('Lenna.png')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while 1:
    th1, res1 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('THRESH_BINARY', res1)

    th2, res2 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('THRESH_BINARY_INV', res2)

    th3, res3 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TRUNC)
    cv2.imshow('THRESH_TRUNC', res3)

    th4, res4 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TOZERO)
    cv2.imshow('THRESH_TOZERO', res4)

    th5, res5 = cv2.threshold(gray_img, 127, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('THRESH_TOZERO_INV', res5)

    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()