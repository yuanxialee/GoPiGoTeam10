import picamera
import cv2
import numpy as np
import time
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from gopigo import *
from util import *
from dip import *
from rover import *
sv_color = [29, 217, 151] 
camera = picamera.PiCamera()

k = 0 
camera.capture('img'+str(k)+'.jpg')
img = cv2.imread('img'+str(k)+'.jpg')
#center, area = color_filter('img'+str(k)+'.jpg')
#print "First Center = ", center
#print "First Area = ", area
k+=1
time.sleep(2)

A = []
for i in xrange(3):
    camera.capture('img'+str(k)+'.jpg')
    img = cv2.imread('img'+str(k)+'.jpg')
    center, area = color_filter('img'+str(k)+'.jpg')
    A.append(area)
    time.sleep(0.2)
    k+=1
gopigo = rover(240, 360, np.mean(area))
print "Rover Center = ".format({},{}), gopigo.cx, gopigo.cy
print "Rover Area = ", np.mean(area)
raw_input('Press enter to start tracking')
while(True):
	camera.capture('img'+str(k)+'.jpg')
	img = cv2.imread('img'+str(k)+'.jpg')
	center, area = color_filter('img'+str(k)+'.jpg')
	print "This is image", str(k)
	print "Center = ", center
	print "Area = ", area
	print "Y diff = ", center[1]-gopigo.cy
	print "Area diff = ", area-gopigo.carea
	print "Tolerance is ", gopigo.tolerance(area)
	print 
	if abs(center[1]-gopigo.cy) < ZERO and gopigo.tolerance(area):
		print "You've tracked the object!"
		break
	if center[0] <= 20:
		print "This is untrackable"
		break
	gopigo.move(center[0],center[1],area)
	time.sleep(0.3)
	k+=1
	
