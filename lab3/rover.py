import sys
import numpy as np
import time
import matplotlib.pyplot as plt
from pylab import figure, axes, title, show
from util import *

class rover:
    path = []					  # record rover location					  
    data = []

    def __init__(self, x, y):
        ''' Constructor'''
            # 2D has 3 degree of freedom(DOF)
            # xpos, ypos, and theta are world configuration of robot
        self.state = 'gotogoal'        
        self.xpos = 0
        self.ypos = 0
        self.theta = 0      			  # radians
        self.xgoal = x				  # goal coordinates
        self.ygoal = y
        #self.dgoal = np.arctan(float(y)/float(x)) # target orientation


    def move(self, dist):
	'''Move the robot and update position'''
        set_left_speed(180)
        set_right_speed(180)
        time.sleep(0.4)
        fwd_cm(dist)
        self.xpos += dist * np.cos(self.theta)
        self.ypos += dist * np.sin(self.theta)
        time.sleep(0.4)


    def rotate(self, degree):
	'''Rotate the robot and update orientation'''
        set_left_speed(120)
        set_right_speed(120)
        time.sleep(WAIT)
        rot_deg(degree)
        radian = degree / 180. * np.pi
        self.theta += radian
        time.sleep(WAIT)
        set_left_speed(120)
        set_right_speed(120)


    def on_goal(self):
        return abs(self.xgoal - self.xpos)+abs(self.ygoal-self.ypos) <= 5.


    def turn_to_goal(self):
	'''
	Move toward the goal until encountering a hit point or making the goal
	'''
        servo(MID)
        diff_rad = self.dgoal - self.theta
        diff_deg = diff_rad/np.pi*180
        print 'diff_rad = ', diff_rad
    	print 'diff_deg = ', diff_deg
    	self.rotate(diff_deg)

    	while avg_dist(4) > 30:
    	    gopigo.record_path()
    	    print self.report()
    	    gopigo.move(3)
    	    time.sleep(0.2)
    	    if self.on_goal():
    		break


    def dist_to_goal(self, xpos, ypos):
        return np.sqrt((self.xgoal-xpos)**2+(self.ygoal-ypos)**2)



    def report(self):
        print 'Rover state:'
        print '(x, y, theta, angle) = ({}, {}, {}, {})'.format(self.xpos,self.ypos,self.theta, self.angle)
        print 'On m line? ',self.on_m_line()
        print 'Reach goal? ', self.on_goal()
        print


    def record_path(self):
	   self.path.append((self.xpos,self.ypos))
