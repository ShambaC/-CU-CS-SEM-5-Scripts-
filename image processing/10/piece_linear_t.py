import cv2


img = cv2.imread('arceus.jpg', 0)
h, w = img.shape

r1 = 1
s1 = 1
r2 = 255
s2 = 255

for i in range(0,h):
    for j in range(0,w):
        if 0 <= img[i, j] and img[i, j] <= r1:
            img[i, j] = (s1 / r1) * img[i, j]
        elif img[i, j] > r1 and img[i,j] <= r2:
            img[i, j] = ((s2 - s1) / (r2 - r1)) * (img[i, j] -r1) + s1
        else:
            img[i, j] = ((255 - s2) / (255 - r2)) * (img[i, j] - r2) + s2
            
cv2.imwrite('Pice_arceus.png',img)