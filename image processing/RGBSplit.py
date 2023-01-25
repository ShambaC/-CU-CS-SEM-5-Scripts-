import cv2

r_img = cv2.imread('RGBsample.png')

#img = cv2.cvtColor(r_img, cv2.COLOR_BGR2RGB)

B, G, R = cv2.split((r_img))

while 1:
    cv2.imshow('ORIGINAL', r_img)
    cv2.imshow('RED', R)
    cv2.imshow('GREEN', G)
    cv2.imshow('BLUE', B)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()