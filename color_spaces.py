import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image = cv.imread("C:\\Users\HRITHIK REDDY\Opencv\Photos\park.jpg")
cv.imshow("image",image)
plt.imshow(image)
plt.show()

#BGR to gray
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#BGR to HSV(Hue, Saturation, Value)
hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

#BGR to LAB
lab=cv.cvtColor(image,cv.COLOR_BGR2LAB)
cv.imshow("LAb",lab)

cv.waitKey(0)