import cv2, numpy as np
import sys
img2=cv2.imread('homo.jpg',1)
row=img2.shape[0]
col=img2.shape[1]
# row/=2
# col/=2

img = np.zeros((row,col, 3), np.uint8)
# cv2.rectangle(img,(2,2),(200,128),(255,0,0),2)
# newimg=cv2.add(img2,cv2.circle(img,(92,88),3,(0,0,255)))
# img = np.zeros((row,col, 3), np.uint8)
# newimg=cv2.add(newimg,cv2.circle(img,(308,105),3,(0,0,255)))
# img = np.zeros((row,col, 3), np.uint8)
# newimg=cv2.add(newimg,cv2.circle(img,(317,403),3,(0,0,255)))
# img = np.zeros((row,col, 3), np.uint8)
# newimg=cv2.add(newimg,cv2.circle(img,(38,385),3,(0,0,255)))
# cv2.imshow('hii',newimg)
# img = np.zeros((row,col, 3), np.uint8)
contours=np.ndarray([[92,88],[308,105],[317,403],[38,385]])
cv2.drawContours(img,contours, -1, (0, 255, 0), 10)
newimg=cv2.add(newimg,img)
cv2.imshow('hii',newimg)

# cv2.waitKey(0)
cv2.destroyAllWindows()