#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 06:06:27 2018

@author: suman
"""
import cv2
import numpy as np


cap = cv2.VideoCapture(0) #0 refers to only web cam

while True:
    ret , frame =cap.read()
    cv2.imshow('Video Frame',frame )
    
    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#Sometimes the windows doesnot get destroyed so use this
for i in range (1,5):
    cv2.waitKey(1)