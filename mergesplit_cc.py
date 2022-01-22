import cv2 as cv
import numpy as np
image = cv.imread("C:\\Users\HRITHIK REDDY\Opencv\Photos\park.jpg")
blank = np.zeros(image.shape[:2],dtype='uint8')

blue,green,red=cv.split(image)
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)

print(image.shape)
print(red.shape)
print(blue.shape)
print(green.shape)

merged = cv.merge([blue,green,blank])
cv.imshow("Merged Image",merged)



cv.waitKey(0)