import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsv hue sat value
    lower_red = np.array([150, 150, 50])
    upper_red = np.array([180, 255, 150])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res  = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF == ord('q')
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()