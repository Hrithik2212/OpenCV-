import cv2 as cv
from frame_rescale import *
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')


#1.Paint the image a certain color 

blank[200:300,300:400]=0,0,255
    #By mentioning the pixels i can get the specified colour in a certain area of the image 
    #using 0,0,255 i get red
    #using 0,255,0 i get green 
cv.imshow("Green Blank",blank)

#2.Draw a Rectangle 

cv.rectangle(blank,(0,0),(250,500),(0,255,0),-1)
### (0,0)is the starting coordinate ,(250,250) is endining coordinate ,(0,255,0) is colour green 
cv.imshow("Rectangle",blank)


#3.Draw a circle 

cv.circle(blank,(250,250),50,(0,0,255),thickness=-1)
cv.imshow("Circle blank",blank)

#4.Draw a line 

cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
cv.imshow("Line",blank)

#5.How to write text on a image 

cv.putText(blank,"Helllo Suckers",(0,100),cv.FONT_HERSHEY_TRIPLEX,1,(255,255,255),thickness=5)
cv.imshow("Letters",blank)

cv.waitKey(0)


