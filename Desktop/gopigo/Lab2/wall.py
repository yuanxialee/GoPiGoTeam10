from gopigo import *
import time
from control import *
import numpy as np

LOWER = 30.0        # < LOWER too close to wall
UPPER = 40.0        # < UPPER too far away from wall
INF = 130.0        # Dist. > INF means no object
MID = 79            # Mid point of camera
RANGE = 70          # Scanning range centered at MID
TARGET_DIST = 20    # Desired distance from the object
WAIT = 0.5	    # Waiting time to measure distance
RESOLUTION = 4	    # Default scanning resolution
def scan(rel=RESOLUTION):
    """
    Scan through range by given resolution
    """
    jump = []
    obj = []
    servo(MID-RANGE)		# move to first position
    time.sleep(WAIT)		# take time to measure distance
    prev_dist = avg_dist(5)
    time.sleep(WAIT)
    for angle in np.arange(MID-RANGE,MID+RANGE,rel):
        servo(angle)
	time.sleep(WAIT)
        curr_dist = avg_dist(5)
	print "Angle = ", angle
	print "Prev = ", prev_dist
	print "Curr = ", curr_dist
	print "Diff = ", curr_dist - prev_dist
	print 
	# if the difference to previous measurement is large
	# and an object is detected, consider it a jump
	if abs(curr_dist - prev_dist) > THRESH and \
		(min(curr_dist, prev_dist)<INF) and \
		angle > (MID-RANGE):
            jump.append(angle)

	# keep track of the distance to the object
	# after the first jump is detected
        if len(jump) == 1 and curr_dist < INF:
	    obj.append(curr_dist)
        prev_dist = curr_dist
        time.sleep(WAIT)
    stop()
    servo(MID)
    time.sleep(WAIT)
    print "Intensity jumps: ",jump
    return jump, obj;

def avg_dist(n=3):
    """
    Average n distance measurements to compensate for noise
    """
    measure = []
    for i in xrange(n):
        measure.append(us_dist(15))
    return sum(measure)/float(n)

# main
stop()
angle = 180
enable_servo()
servo(angle)
time.sleep(WAIT)
while(True):
	curr_dist = avg_dist(3)
	time.sleep(WAIT)
	set_speed(80)
	print "Current distance = ", curr_dist
	if curr_dist < LOWER:
		right_deg(4)
		angle = angle+4
		angle = np.clip(angle,0,180)
		time.sleep(WAIT)
		print "Current angle = ", angle
		enable_servo()
		servo(angle)
		time.sleep(WAIT)
		fwd_cm(1)
	elif curr_dist > UPPER and curr_dist < INF:
		left_deg(1)
		angle = angle - 30
		angle = np.clip(angle,0,180)
		time.sleep(WAIT)
		print "Current angle = ", angle	
		enable_servo()
		servo(angle)
		time.sleep(WAIT)
		fwd_cm(1)
	elif curr_dist >= INF:
		stop()
		break;
	else:
		fwd_cm(1)
		time.sleep(WAIT)
		print "Current distance moving forward = ", avg_dist()
