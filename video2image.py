import os
import sys
import numpy as np
import cv2
import time
import logging


# video_path = "/Users/shallwego2/Desktop/inspire2.mp4"
video_path = "/Users/shallwego2/Pictures/droneandplane.mp4"
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(video_path)

for j in range(0,4650):
    ret,frame = cap.read()

i = 0

while(True):
    ret, frame = cap.read()
    ret, frame = cap.read()
    frame = cv2.flip(frame, 0)
    frame = cv2.flip(frame, 1)
    cv2.imshow('frame', frame)


    save_image_name = '/Users/shallwego2/Pictures/seq10/frame'+"{0:04d}".format(i)+'.jpg'
    cv2.imwrite(save_image_name, frame)
    i = i+2
    if i>500:
        break
    cv2.waitKey(10)

cv2.destroyAllWindows()