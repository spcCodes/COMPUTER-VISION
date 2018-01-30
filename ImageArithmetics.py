#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:21:07 2018

@author: suman
"""

import numpy as np 
import cv2

img1 = cv2.imread('./images/a.png')
img2 = cv2.imread('./images/b.png')
img3 = cv2.imread('./images/python.png')

#### ADDING UP TWO IMAGES BY OVERLAPPING TWO OF THEM 
#AddImage = img1 + img2
#AddImage = cv2.add(img1 , img2)
#AddImage = cv2.addWeighted(img1 , 0.6 , img2 , 0.4 , 0)

#GETTING THE ROWS , CHANNNELS OF IMAGE 2
rows , cols , channels = img3.shape
#setting up the region of interest
roi = img1[0:rows , 0:cols]

#making the second image gray
img2gray = cv2.cvtColor(img3 , cv2.COLOR_BGR2GRAY)
ret , mask = cv2.threshold(img2gray , 220 , 255 , cv2.THRESH_BINARY_INV)

#masked image
mask_inv = cv2.bitwise_not(mask)


img1_bg = cv2.bitwise_and(roi , roi , mask =mask_inv)
img3_fg = cv2.bitwise_and(img3 , img3 , mask = mask)


addImage = cv2.add(img1_bg , img3_fg)
img1[0:rows , 0:cols] = addImage


cv2.imshow('Added Image' , img1)
cv2.imshow('mask_image' , mask_inv)
cv2.imshow('img1_bg' , img1_bg)
cv2.imshow('img3_fg ' , img3_fg )
cv2.imshow('AddedSmall Image ' , addImage )

#cv2.imshow('Added Image' , AddImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
for i in range (1,10):
    cv2.waitKey(1)
    