from gopigo import *
import time
from control import *


"""
while us_dist(15) >= INF 
	angle += 2
	servo(angle)
"""
THRESH = 100.0
INF = 175
bool found = False

def find():
	angle = 0
	enable_servo()
	servo(angle)
	jump=[]
	prev_dist = us_dist(15)

	while len(jump) < 2:
		angle += 2.
		if (angle > 180):
			break;
		servo(angle)
		curr_dist = us_dist(15)
		if (abs(curr_dist - prev_dist) > THRESH):
			jump.append(angle)
		prev_dist = curr_dist
	return jump


# main
while not found: 
	location = find()
	if len(location) == 2:
		found = True;
	else:
		left_rot()
		time.sleep(0.7)
		stop()

avg = (location[0] + location[1])/2.0

