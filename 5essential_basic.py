###5 Essential basic function that will be useful doing any opencv projects ####

import cv2 as cv
image=cv.imread("C:\\Users\HRITHIK REDDY\Opencv\Photos\park.jpg")
#cv.imshow("Orginal",image)

#1.Coverting an image to gray scale
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)


#2.Blur an image 
blur=cv.GaussianBlur(image,(7,7),cv.BORDER_DEFAULT)


#3.How to find the edge cascade which is basically finding the edges of the images 
canny=cv.Canny(image,125,175)
canny_blur=cv.Canny(blur,125,175)
cv.imshow("The blur canny",canny_blur)
cv.imshow("The canny",canny)



#4.dilating the images(Dilation adds pixels to the boundaries of objects in an image, while erosion removes pixels on object boundaries)


dialated=cv.dilate(canny_blur,(7,7),iterations=3)
#cv.imshow("The dilated image",dialated)


#5.Errode function
erroded=cv.erode(dialated,(7,7),iterations=3)
#cv.imshow("The errode",erroded)


### Resize and crop an image 
##
#
resized=cv.resize(image,(500,500),interpolation=cv.INTER_LINEAR)
#mentioning interpolation=cv.INTER_AREA is helpful if u are shrinking the image smaller than the orginal dimensions 
#However if u are increasing the size of the image then use interpolation=cv.INTER_LINEAR or INTER_CUBIC
#INTER_CUBIC is slower than the other two as it prioratizes qaulity

#cv.imshow("resized",resized)

###Cropping 

cropped=image[50:200,200:400]
#cv.imshow("Cropped",cropped)

cv.waitKey(0)

