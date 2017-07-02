from gopigo import *
from util import *
from control import *

ZERO = 15

class rover:

	global ZERO	

	def __init__(self, x, y, area):
		self.cx = x
		self.cy = y
		self.carea = area

	def move(self, x, y, area):
		if abs(y-self.cy) > 15:
			if y < self.cy:
				rot_deg(10)
				time.sleep(0.3)
			elif y > self.cy:
				rot_deg(-10)
				time.sleep(0.3)
		if abs(area-self.carea) > ZERO:
			if area < self.carea:
				fwd_cm(2)
				time.sleep(0.2)
			if area > self.carea:
				bwd_cm(2)
				time.sleep(0.2)

	def tolerance(self, area):
		global ZERO 
		ZERO = float(area)*(4./43.)+162.
		print "Area is ", area
		print "ZERO is ", ZERO
		if abs(area-self.carea) < ZERO:
			return True
		else: 
			return False 
