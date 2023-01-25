import cv2

img = cv2.imread('Lenna.png', 0)
img_bright = img.copy()
img_dark = img.copy()
img_contrast = img.copy()
img_no_back = img.copy()

h, w = img.shape

for i in range(h) :
    for j in range(w) :
        img_bright[i, j] += 50  # Brightness enchancement
        img_dark[i, j] -= 50    # Brightness supression

# Contrast manipulation
for i in range(h) :
    for j in range(w) :
        if img_contrast[i, j] > 127 :
            img_contrast[i, j] += 30
        else :
            img_contrast[i, j] -= 30

# Gray w/o BG
for i in range(h) :
    for j in range(w) :
        if img_no_back[i, j] > 50 and img_no_back[i, j] < 150 :
            img_no_back[i, j] = 255

while True :
    cv2.imshow('BRIGHT', img_bright)
    cv2.imshow('DARK', img_dark)
    cv2.imshow('CONTRAST', img_contrast)
    cv2.imshow('NO BG', img_no_back)
    cv2.imshow('ORIGINAL', img)

    if cv2.waitKey(1) == ord('q') :
        cv2.destroyAllWindows()
        break