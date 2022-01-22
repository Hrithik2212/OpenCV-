import cv2 as cv
import numpy as np

img = cv.imread("C:\\Users\HRITHIK REDDY\Opencv\Photos\park.jpg")

#Translation i.e. changing the axes of the image (Shortening the total image from frame size)
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#-x implies to shift left 
#-y implies to shift up
#x implies shift right 
#y implies shift left 
translated=translate(img , -100, -100)
#cv.imshow('Translated',translated)

#Rotation
def rotate(image,angle,rotPoint=None):
    width=image.shape[1]
    height=image.shape[0]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
#cv.imshow("Rotated",rotate(img,45))

#resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
#cv.imshow("Resized",rotate(resized,45))

#flipping
cv.imshow("Flip",cv.flip(img,-1))
cv.imshow("Flip2",cv.flip(img,1))
cv.imshow("Flip3",cv.flip(img,0))

#cropping
cropped_img=img[0:500,100:400]
cv.imshow("Cropped",cropped_img)


cv.waitKey(0)