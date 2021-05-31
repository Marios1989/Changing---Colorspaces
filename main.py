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

    lower_green = np.array([50, 50, 120])
    upper_green = np.array([70, 255, 255])

    lower_red = np.array([136, 87, 111])
    upper_red = np.array([180, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv.inRange(hsv, lower_green, upper_green)
    mask_red = cv.inRange(hsv, lower_red, upper_red)

    mask = mask + mask_green + mask_red

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)
    res2 = cv.bitwise_and(frame, frame, mask=mask_green)
    res3 = cv.bitwise_and(frame, frame, mask=mask_red)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    cv.imshow('frame_green', frame)
    cv.imshow('mask_green', mask_green)
    cv.imshow('res_green', res2)

    cv.imshow('frame_red', frame)
    cv.imshow('mask_red', mask_red)
    cv.imshow('res_red', res3)

    out0.write(frame)
    out1.write(mask)
    out2.write(res)

    out0.write(frame)
    out1.write(mask_green)
    out2.write(res2)

    out0.write(frame)
    out1.write(mask_red)
    out2.write(res3)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out0.release()
out1.release()
out2.release()
cv.destroyAllWindows()
