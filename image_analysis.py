import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

#img = cv2.imread('D:\git\Python\Machine_Leaning\cow1.jpg', -1)
#IMREAD_GRAYSCALE(=0), IMREAD_COLOR(=1), IMREAD_UNCHANGED(=-1)

#read image form local folder, and show it on the screen

# plt.imshow(img, cmap='gray', interpolation = 'bicubic')
# #plt.plot([50,100],[80,100], 'c', linewith = 5)
# plt.show()

# cv2.imshow("image", img)
# cv2.imwrite("cow2.jpg", img)

# cv2.imshow('cow', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# px = img[100, 100]
# blue = img[100, 100, 0]
# print(blue)

#accessing red value
# print(img.item(10, 10, 2))
# img.itemset((10, 10, 2),100)
# print(img.item(10, 10, 2))

# print(img.shape)
# print(img.size)
# print(img.dtype)

#splitting and merging image channels
#b, g, r = cv2.split(img)
#img = cv2.merge((b, g, r))

#cv2.imshow('image', img)
# b = img[:, :, 1]
# cv2.imshow('b', b)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#making borders for images(padding)
# BLUE = [255, 0, 0]
#
# replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
# constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
# plt.subplot(231),plt.imshow(img, 'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate, 'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect, 'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
#
# plt.show()

#add, addweighted
# dst = cv2.addWeighted(img, 0.7, img, 0.3, 0)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#bitwise operations
#load two images
img = cv2.imread('D:\git\Python\Machine_Leaning\cow1.jpg', -1)

#i want to put logo on top-left corner, so i create a ROI
rows, cols, channels = img.shape
roi = img[0:rows, 0:cols]

#now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask =cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

#now black-out the area of logo in ROI
img_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

#take only region of logo from logo image
img_fg = cv2.bitwise_and(img, img, mask = mask)

#put logo in roi and modify the main image
dst = cv2.add(img_bg, img_fg)
img[0:rows, 0:cols] = dst

cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
