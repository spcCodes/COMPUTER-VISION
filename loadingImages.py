import cv2
import numpy as np
import matplotlib.pyplot as plt

#reading an image Aand converting to  gray scale
img = cv2.imread('./images/watch.jpeg' , cv2.IMREAD_GRAYSCALE)

'''
IMAGE_GRAYSCALE=0
IMAGE_COLOR=1
IMAGE_UNCHANGED=-1
JUST PUT 0,1,-1 AFTER THE IMAGE FILE
'''

#display the image using imshow
cv2.imshow('Image of an watch' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Sometimes the windows doesnot get destroyed so use this
for i in range (1,5):
    cv2.waitKey(1)

#plot using matplotlib
#plt.imshow(img , cmap='gray' , interpolation='bicubic')
#plt.show()

#saving an image
cv2.imwrite('GrayWatch.png',img)