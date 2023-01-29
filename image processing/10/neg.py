import cv2

img = cv2.imread('arceus.jpg')
row, col, _ = img.shape

neg = img.copy()


for i in range(0, row):
    for j in range(0, col):
        neg[i, j] = 255-img[i, j]
        
cv2.imwrite('Negetive_arceus.png',neg)