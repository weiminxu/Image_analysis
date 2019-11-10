import numpy as np
import cv2

# img = cv2.imread('D:\git\Python\Machine_Leaning\cow1.jpg', cv2.IMREAD_COLOR)
# cv2.line(img, (0,0), (150,150), (255, 255, 255), 15)
# cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)
# cv2.circle(img, (100, 63), 55, (0,0,255), -1)
#
# pts = np.array([[10, 5],[20, 30],[70, 20],[50, 10]], np.int32)
# cv2.polylines(img, [pts], True, (0, 255, 255), 5)
#
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, 'OpenCV Tuts!', (0, 130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)
#
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#create a black image
img = np.zeros((512, 512, 3), np.uint8)

#draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

#draw a rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (255, 0, 0), 3)

#draw circle
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

#draw a polygon
pts = np.array([[10, 5],[20, 30],[70, 20],[50, 11]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 255, 255))

#add text to image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()