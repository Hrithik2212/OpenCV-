import cv2 as cv  #importing the computer vision library

####Reading Images
#The imread function and imshow fuction 
cat = cv.imread("C:\\Users\HRITHIK REDDY\Opencv\Photos\cat.jpg")
cv.imshow("cat",cat)
cv.waitKey(0)