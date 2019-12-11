import cv2
import time
import os
cwd = os.getcwd()
# print cwd
img=cv2.imread("test.jpg",1)
img2=cv2.imread('test.jpg',0)
for i in range(101):
	cv2.imshow('testing',cv2.addWeighted(img2,float(i)/100,img,1-(float(i)/100),0))
	cv2.waitKey(40)
cv2.imshow('testing',img)
cv2.waitKey(0)
cv2.destroyAllWindows()