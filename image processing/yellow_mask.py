import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    ret, frame = cap.read()

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #Range
    lower_bound = np.array([10,160,30])
    upper_bound = np.array([50,255,255])

    mask = cv.inRange(hsv_frame, lower_bound, upper_bound)

    result = cv.bitwise_and(frame, frame, mask= mask)

    cv.imshow('ORIGINAL', frame)
    cv.imshow('MASK', mask)
    cv.imshow('RESULT', result)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()