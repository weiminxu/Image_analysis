import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\git\Python\Machine_Leaning\cow1.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_GRAYSCALE(=0), IMREAD_COLOR(=1), IMREAD_UNCHANGED(=-1)

#read image form local folder, and show it on the screen
'''
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

# plt.imshow(img, cmap='gray', interpolation = 'bicubic')
# #plt.plot([50,100],[80,100], 'c', linewith = 5)
# plt.show()

cv2.imshow("image", img)
cv2.imwrite("cow2.jpg", img)

