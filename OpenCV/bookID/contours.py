
import cv2, numpy as np
import sys
img2=cv2.imread('check.jpg',1)
row=img2.shape[0]
col=img2.shape[1]
# row/=2
# col/=2

img = np.zeros((row,col, 3), np.uint8)
# cv2.rectangle(img,(2,2),(200,128),(255,0,0),2)
# img=cv2.add(img,cv2.circle(img,(202,164),3,(0,0,255),5))
# img = np.zeros((row,col, 3), np.uint8)
# img=cv2.add(img,cv2.circle(img,(341,239),3,(0,0,255),5))
# img = np.zeros((row,col, 3), np.uint8)
# img=cv2.add(img,cv2.circle(img,(203,428),3,(0,0,255),5))
# img = np.zeros((row,col, 3), np.uint8)
# img=cv2.add(img,cv2.circle(img,(45,303),3,(0,0,255),5))
# img=cv2.add(newimg,img2)
# cv2.imshow('hii',newimg)
# img = np.zeros((row,col, 3), np.uint8)
contours=[]
contours.append([202,164])
contours.append([45,303])
contours.append([203,428])
contours.append([341,239])
# print type(np.array(contours))
newimg=cv2.add(img2,cv2.drawContours(img,[np.array(contours)],0, (0, 255, 0), -1))
# newimg=cv2.add(newimg,img)
cv2.imshow('hii',newimg)

cv2.waitKey(0)
cv2.destroyAllWindows()