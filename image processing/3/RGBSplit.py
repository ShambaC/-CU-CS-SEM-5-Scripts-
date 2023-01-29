import cv2

img = cv2.imread('RED.jpg')
# B, G, R = cv2.split((img))
B, G, R = cv2.split(img)

cv2.imshow('Lenna_RED.jpg', R)
cv2.imshow('Lenna_GREEN.jpg', G)
cv2.imshow('Lenna_BLUE.jpg', B)

cv2.waitKey(3000)

# m_img = cv2.merge((B, G, R))
# cv2.imwrite('Lenna_M.jpg', m_img)