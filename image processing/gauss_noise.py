import cv2
import numpy as np

img = cv2.imread('lenna.png')
s = img.size

# Generate Gaussian noise
gauss = np.random.normal(0, 1, s)
gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')

# Add the Gaussian noise to the image
img_gauss = cv2.add(img,gauss)

# Display the image
cv2.imshow('a', img_gauss)
#cv2.imwrite('gauss_image.jpg', img_gauss)
cv2.waitKey(5000)
cv2.destroyAllWindows()