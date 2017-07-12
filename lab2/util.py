from gopigo import *
from control import *
import time

ZERO = 3    # tolerance of m line
LOWER = 30.0        # < LOWER too close to wall
UPPER = 40.0        # < UPPER too far away from wall
INF = 130.0        # Dist. > INF means no object
MID = 79            # Mid point of camera
RANGE = 70          # Scanning range centered at MID
TARGET_DIST = 20    # Desired distance from the object
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
    enc_tgt(1,1,pulse)
    if deg < 0:
        right_rot()
    else:
        left_rot()
