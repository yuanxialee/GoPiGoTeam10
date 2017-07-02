from gopigo import *
from control import *
import numpy as np
import time

ZERO = 3            # tolerance of m line
LOWER = 30.0        # < LOWER too close to wall
UPPER = 40.0        # < UPPER too far away from wall
INF = 40.0         # Dist. > INF means no object
MID = 90            # Mid point of camera
RANGE = 80          # Scanning range centered at MID
WAIT = 0.8	    # Waiting time to measure distance
RESOLUTION = 4	    # Default scanning resolution

def avg_dist(n=3):
    """
    Average n distance measurements to compensate for noise
    """
    measure = []
    for i in xrange(n):
        measure.append(us_dist(15))
    return sum(measure)/float(n)

def rot_deg(deg):
    pulse = int(abs(deg)/DPR/2)
    if pulse < 1:
	   pulse = 1
       
    if deg < 0:
        enc_tgt(1,0,1)
        right_rot()
    else:
	enc_tgt(0,1,1)
        left_rot()
        


