import cv2
img = cv2.imread('arceus.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb_back = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
cv2.imwrite('arceus_rgb.jpg', rgb_back)