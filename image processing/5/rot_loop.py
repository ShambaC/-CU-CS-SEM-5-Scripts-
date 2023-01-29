import cv2

img = cv2.imread('arceus.jpg')

h, w, c = (img.shape)

cx = h/2 - 1
cy = w/2 - 1

for i in range(30, 180, 30) : 
    M_90 = cv2.getRotationMatrix2D((cx, cy), -i, 1)
    img1 = cv2.warpAffine(img, M_90, (w, h))
    cv2.imshow(f"Arceus_AC{i}.jpg", img1)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()