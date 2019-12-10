from skimage.measure import compare_ssim as ssim
import numpy as np
import cv2
import sys
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	return err
 
def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	# print 'basic : %f' % (m)
	return (s)

contours=[]
contours.append([202,164])
contours.append([341,239])
contours.append([203,428])
contours.append([45,303])

src_im = cv2.imread('check.jpg')
pts_src = np.array(contours)
dst_im = np.zeros((501,501, 3), np.uint8)
pts_dst = np.array([[0, 0],[500, 0],[500, 500],[0, 500]])
h, status = cv2.findHomography(pts_src, pts_dst)
check = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
cv2.imshow('Warped pic - User',check)
cv2.waitKey(0)
check = cv2.cvtColor(check, cv2.COLOR_BGR2GRAY)
ideal=cv2.imread('ideal.jpg',0)

# compare the images
factor = compare_images(ideal, check, "Original vs. Check")
if factor > 0.7:
	print 'SAME BOOK'
else:
	print 'DIFFERENT BOOK' 