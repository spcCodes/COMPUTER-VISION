#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:41:03 2018

@author: suman
"""

import numpy as np
import cv2

img = cv2.imread('./images/bookpage.jpg')

#most ideal thresholding technique
retval , threshold = cv2.threshold(img, 12 , 255 , cv2.THRESH_BINARY)

#converting it into gray and then do thresholding
grayScaled = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

#simple threshold technique  
retval2 , threshold2 = cv2.threshold(grayScaled, 12 , 255 , cv2.THRESH_BINARY)

#gaussian adaptive threshold technique
gausImage = cv2.adaptiveThreshold(grayScaled , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 115 , 1)

#otsu thresholding technique (genrally may work well sometimes)
retval3 , otsu = cv2.threshold(grayScaled , 12 , 255 , cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('Original Image' , img)
cv2.imshow('Thresholded Image' , threshold)
cv2.imshow('GrayScaled Thresholded Image', threshold2)
cv2.imshow('GrayScaled Adaptive Thresholded Image', gausImage)
cv2.imshow('GrayScaled OTSU Threshold Image', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(1,20):
    cv2.waitKey(1)