import cv2 as cv
import numpy as np

image =cv.imread("C://Users/HRITHIK REDDY/Opencv/Photos/cats.jpg")
blank = np.zeros(image.shape[:2],dtype='uint8')

mask =cv.circle(blank,(image.shape[1]//2,image.shape[0]//2),100,255,-1)
cv.imshow("Mask",mask)
masked=cv.bitwise_and(image,image,mask=mask)
cv.imshow("Masked",masked)

cv.waitKey(0)