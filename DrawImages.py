#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:11:53 2018

@author: suman
"""

###draw images on images
import cv2
import numpy as np

#getting the image
img = cv2.imread('./images/coffee.jpg', cv2.IMREAD_COLOR)

#drawing on the images
cv2.line(img , (0,0) , (150,150) , (255,255,255),5)
cv2.rectangle(img , (15,25),(100,80),(0,0,255) , 3)
cv2.circle(img , (25,25) , 25 , (0,255,0) , 4)

pts=np.array([[10,5] , [23,6] , [50,78] , [80,95]] , np.int32)
cv2.polylines(img , [pts] , True , (0,255,255) , 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img , 'Hello there!' , (10,23) , font , 1 , (145,247,213) , 1 , cv2.LINE_AA)



#dispalying the image
cv2.imshow('Image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
for i in range (1,7):
    cv2.waitKey(1)
