import numpy as np
import cv2 as cv

capture = cv.VideoCapture(0)
if not capture.isOpened():
    print("Cannot open camera")
    exit()
while True:
    #frame by frame capture
    ret, frame = capture.read()

    if not ret:
        print("cannot capture")
        break

    #Converting to HSV
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #Range for ball
    ball_lower_bound = np.array([0, 220, 0])
    ball_upper_bound = np.array([47, 255, 255])

    #Range for spoon
    spoon_lower_bound = np.array([100, 150, 0])
    spoon_upper_bound = np.array([140, 172, 255])

    #Get mask
    mask_y = cv.inRange(hsv_frame, ball_lower_bound, ball_upper_bound)
    mask_b = cv.inRange(hsv_frame, spoon_lower_bound, spoon_upper_bound)

    #AND to get masks
    result_y = cv.bitwise_and(frame, frame, mask= mask_y)
    result_b = cv.bitwise_and(frame, frame, mask= mask_b)

    #OR to get combined result
    res = cv.bitwise_or(result_y, result_b)

    cv.imshow('MASKED RESULT', res)
    cv.imshow('INPUT', frame)
    cv.imshow('MASK_Y', mask_y)
    cv.imshow('MASK_B', mask_b)
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()