import cv2 as cv
import numpy as np
from frame_rescale import *


image=cv.imread("C://Users/HRITHIK REDDY/Opencv/Photos/cats.jpg")
img=frame_rescale(image,0.8)

#blank img for later use 
blank=np.zeros(img.shape,dtype=np.uint8)

#conversion to gray
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray_img)

#blurring the image 
blur=cv.GaussianBlur(gray_img,(5,5),cv.BORDER_DEFAULT)

#Finding the edges of the image 
canny=cv.Canny(blur,125,175)
cv.imshow("The gray canny",canny)

#Advanced concept Threshold->Converting the image to binary form i.e. black or white 
ret,threshold=cv.threshold(gray_img,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh",threshold)

#Storing all the edge points as a list 'contours'
contours,heirachies=cv.findContours(threshold,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours),"is the total number of countours")

#Drawing the image using the contours list on blank image 
cv.drawContours(blank,contours,-1,(0,0,255),thickness=1)
cv.imshow("Blank",blank)



cv.waitKey(0)