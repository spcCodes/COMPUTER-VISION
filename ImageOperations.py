#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:51:44 2018

@author: suman
"""

import numpy as np
import cv2

img = cv2.imread('./images/coffee.jpg' , cv2.IMREAD_COLOR)

#making a particular pixel white
img[55,55] =[255,255,255]
px = img[55,55]

#making a region in the image white
img[100:150 , 100:150] = [255,255,255]

#selecting a particular region and copying it somewhere else
coffee_part = img[37:114 , 103:182]
img[0:77 , 0:79] = coffee_part

cv2.imshow('Image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(1,6):
    cv2.waitKey(1)