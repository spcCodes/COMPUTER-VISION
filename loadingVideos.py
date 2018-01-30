#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 06:06:27 2018

@author: suman
"""
import cv2
import numpy as np


cap = cv2.VideoCapture(0) #0 refers to only web cam

#use a codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#create a output file for saving the video
out = cv2.VideoWriter('VideoOutput.avi', fourcc , 20.0 , (640,480))


while True:
    ret , frame =cap.read()
    
    #changing the video to gray
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
    #SAVING THE FRAME
    out.write(frame)
    
    #displaying the video frame
    cv2.imshow('Video Frame',frame )
    cv2.imshow('Gray video Frame' , gray)
    
    #break the video sequence using any key
    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

#Sometimes the windows doesnot get destroyed so use this
for i in range (1,5):
    cv2.waitKey(1)