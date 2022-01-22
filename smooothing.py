'''Smoothing is nothing but blurring of images 
    In this  python file 
    you will see various blurring methods in opencv '''


import cv2 as cv
import numpy as np
img = cv.imread("C://Users/HRITHIK REDDY/Opencv/Photos/cats.jpg")
cv.imshow("Cats",img)

#Averaging 
average = cv.blur(img,(3,3))
##(3,3) is the kernel size ,the higher the kernel size, the image is more blurred
cv.imshow("Average",average)

#Gausssian Blur 
##Gaussianblur does something similar to average but gives a specific weight to all the surrounding pixels
##and the absolute centre is the specific avg
###It is more natural
###Its blurring effect is less and more even than blur for the same kernel size
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gaussian_blur",gauss)

#Median 
##Median blurring is same as average but takes the median istead of average
##It is very effective in reducing noise in the image 
##People tend to use this this function advanced computer vision projects in which there is a need to 
##reduce substantial amount of noise

median=cv.medianBlur(img,3)     #kernel size is not a tuple but an integer for this function 
                                #the cv2 lib understands the int as a 1*2 tuple of same int 
                                #median blur is not ideal for higher kernel size as 7 or even 5
cv.imshow("Median",median)

#Bilatteral
#Bilateral blurrinmg is the most effective and used in a lot of cv projects 
#Traditional blurring doesn't retain the edges whereas
#bilateral blurring does

bilateral = cv.bilateralFilter(img,5,15,15)
'''5 here is the diameter and not the kernel size,15 is the sigma color (the higher the value more 
    colors will be taken into consideration when computing the blur
    the seconf 15 is sigma space which influences distance between centre and pixels'''
cv.imshow("Bilatteral blur",bilateral)
cv.waitKey(0)