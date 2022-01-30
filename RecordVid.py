import cv2 as cv
import numpy as np
import os

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

# Standard Video Dimensions Sizes
STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

filename="video.avi"
fps=24.0
res='480p'

def get_dims(cap,res='480p'):  
    width,height=STD_DIMENSIONS[res]
    change_res(cap,width,height)
    return width,height

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']




capture=cv.VideoCapture(0)
dims=get_dims(capture)
video_type=get_video_type(filename)
out=cv.VideoWriter(filename,video_type,fps,dims)

while True:
     isTrue,frame=capture.read()
     out.write(frame)
     cv.imshow("Video",frame)
     if cv.waitKey(1) & 0xff==ord('d'):
         break
capture.release()
out.release()
cv.destroyAllWindows()

