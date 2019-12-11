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
contours=[]
contours.append([92,88])
contours.append([308,105])
contours.append([317,403])
contours.append([38,385])
print type(np.array(contours))
newimg=cv2.drawContours(img,[np.array(contours)],0, (0, 255, 0), -1)
newimg=cv2.add(newimg,img2)
cv2.imshow('hii',newimg)
# Read source image.
im_src = cv2.imread('homo.jpg')
# Four corners of the book in source image
pts_src = np.array([[92, 88], [308, 105], [317, 403],[38, 385]])
# Read destination image.
im_dst = np.zeros((501,501, 3), np.uint8)
    # Four corners of the book in destination image.
pts_dst = np.array([[0, 0],[500, 0],[500, 500],[0, 500]])
 
    # Calculate Homography
h, status = cv2.findHomography(pts_src, pts_dst)
     
    # Warp source image to destination based on homography
im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
     
    # Display images
cv2.imshow("Source Image", im_src)
cv2.waitKey(0)
# cv2.imshow("Destination Image", im_dst)
cv2.imshow("Warped Source Image", im_out)

cv2.imwrite('ideal.jpg',im_out)


#  im_out is the final processed image that ought to be same when compared to the existing image of 1:1 ratio
cv2.waitKey(0)
cv2.destroyAllWindows()
