##In this we will see gradients and edge detection

import cv2 as cv
import numpy as np 

image = cv.imread("C://Users/HRITHIK REDDY/Opencv/Photos/park.jpg")
# cv.imshow("Cat",image)
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

##Laplacian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)


##Sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow("SX",sobelx)
cv.imshow("SY",sobely)
cv.imshow("Sobel",combined_sobel)




cv.waitKey(0)