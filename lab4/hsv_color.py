import cv2
import numpy as np
import sys

# This is a simple program to pick hsv color 
# in openCV format.

hsv = np.zeros((250,250,3), np.uint8)
hsv[:,:,0] = int(sys.argv[1])
hsv[:,:,1] = int(sys.argv[2])
hsv[:,:,2] = int(sys.argv[3])

bgr = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
cv2.imshow('Color picker', bgr)
cv2.waitKey(0)
