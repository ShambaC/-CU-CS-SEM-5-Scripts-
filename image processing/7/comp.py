import cv2

img1=cv2.imread('Lenna.png')
img2=cv2.imread('arceus.jpg')

img2=cv2.resize(img2,(512,512))

diff=cv2.subtract(img1,img2)
R,G,B=cv2.split(diff)

if cv2.countNonZero(R) == 0 and cv2.countNonZero(G) == 0 and cv2.countNonZero(B) == 0:
    print("the images are completely equal")
else:
    print("the images are not equal")  