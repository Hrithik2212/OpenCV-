import cv2 as cv
from frame_rescale import *
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("C:\\Users\HRITHIK REDDY\Opencv\Photos\cats.jpg")
img = frame_rescale(image,0.8)
gray = cv.cvtColor(frame_rescale(image,0.8) ,cv.COLOR_BGR2GRAY)
blank=np.zeros(gray.shape[:2],dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(70,70),(gray.shape[1]-110,gray.shape[0]-130),255,-1,)
mask=cv.circle(blank.copy(),(gray.shape[1]//2+25,gray.shape[0]//2-30),70,255,-1)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("Rectangle",masked)

#Calculating a Histogram 
histogram = cv.calcHist([masked],[0],None,[256],[0,256])
#plt.figure()
# plt.title("Gray Histogram")
# plt.xlabel("bins")
# plt.ylabel("No of pixels")
# plt.xlim([0,256])
# plt.plot(histogram)
#plt.show()
plt.figure()
plt.title("Color Histogram")
plt.xlabel("bins")
plt.ylabel("No of pixels")
plt.xlim([0,256])
# plt.plot(histogram)

color = ('b','g','r')
for i,col in enumerate(color):
    hist = cv.calcHist((img),[i],None,[256],[0,256])
    plt.plot(hist,color=col)
plt.show()
    


cv.waitKey(0)