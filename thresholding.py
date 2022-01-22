import cv2 as cv
image = cv.imread("C://Users/HRITHIK REDDY/Opencv/Photos/cats.jpg")
# cv.imshow("Cats",image)

#Simple Thresholding 
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

threshold,thresh=cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("simple Threshold",thresh)

threshold,thresh_inv=cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("simple Threshold Inverse",thresh_inv)

##Adaptive Threshold

adaptive_Threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Adaptive Threshold",adaptive_Threshold)

cv.waitKey(0)