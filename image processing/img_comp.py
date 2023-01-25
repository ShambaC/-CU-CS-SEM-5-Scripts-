import cv2

img1 = cv2.imread('Lenna.png')
img3 = img1
#img3 = cv2.imread('hotarou.png')

img3 = cv2.resize(img3, (512,512))

diff = cv2.subtract(img1, img3)

R, G, B = cv2.split(diff)

print(cv2.countNonZero(B))
print(cv2.countNonZero(G))
print(cv2.countNonZero(R))

if(cv2.countNonZero(R) == 0 and cv2.countNonZero(G) == 0 and cv2.countNonZero(B) == 0):
    print('equal')
else:
    print('not equal')