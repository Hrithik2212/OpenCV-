from frame_rescale import *
import cv2 as cv

####Reading Videos

#VideoCapture() function
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    #cv.imshow('Video',frame)
    cv.imshow('Video',frame)
    if cv.waitKey(1) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows
