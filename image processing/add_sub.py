import cv2

img1 = cv2.imread('Lenna.png')
img2 = cv2.imread('hotarou.png')

img2 = cv2.resize(img2, (512,512))

img3 = img1 + img2

img4 = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)

img5 = img1 - img2
img6 = cv2.subtract(img1, img2)

while True:
    cv2.imshow('IMG3', img3)
    cv2.imshow('IMG4', img4)

    cv2.imshow('IMG5', img5)
    cv2.imshow('IMG6', img6)

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break