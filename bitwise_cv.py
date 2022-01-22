import cv2 as cv
import numpy as np
blank = np.zeros([500,500],dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(50,50),(450,450),255,-1)
circle = cv.circle(blank.copy(),(250,250),225,255,-1)

cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

#Bitwise AND
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("bitwise_and",bitwise_and)

#Bitwise OR
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("bitwise_or",bitwise_or)

#Bitwise Xor
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise_xor",bitwise_xor)

#Bitwise Not
rectangle_not=cv.bitwise_not(rectangle)
cv.imshow("Rectangle not",rectangle_not)
cv.waitKey(0)