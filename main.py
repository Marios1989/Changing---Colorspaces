import cv2 as cv
import numpy as np


cap = cv.VideoCapture('/home/user/Downloads/The Last of Us Part II .avi')

fourcc = cv.VideoWriter_fourcc(*'M', 'J', 'P', 'G')

out0 = cv.VideoWriter('original-frame-output.avi', fourcc, 20.0, (1280, 720))
out1 = cv.VideoWriter('mask-frame-output.avi', fourcc, 20.0, (1280, 720))
out2 = cv.VideoWriter('res-frame-output.avi', fourcc, 20.0, (1280, 720))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame(stream end).Exiting...")
        break

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    out0.write(res)
    out1.write(res)
    out2.write(res)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out0.release()
out1.release()
out2.release()
cv.destroyAllWindows()
