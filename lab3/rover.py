import sys
import numpy as np
import time
import matplotlib.pyplot as plt
from pylab import figure, axes, title, show
from util import *

class rover:
    route = []					  # record rover location					  
    data = []

    def __init__(self, s1, s2, x, y):
        ''' Constructor'''
            # 2D has 3 degree of freedom(DOF)
            # xpos, ypos, and theta are world configuration of robot
        self.state = 'gotogoal'        
        self.xpos = s1
        self.ypos = s2
        self.theta = 0      			  # radians

        self.xgoal = x				  # goal coordinates
        self.ygoal = y
        self.dgoal = 0                # target orientation


    def move(self, dist):
	'''Move the robot and update position'''
        set_left_speed(240)
        set_right_speed(250)
        time.sleep(0.4)
        fwd_cm(dist)
        time.sleep(4.5)
        self.xpos += dist * np.cos(self.theta)
        self.ypos += dist * np.sin(self.theta)
        time.sleep(1)


    def rotate(self, degree):
	'''Rotate the robot and update orientation'''
        set_left_speed(150)
        set_right_speed(160)
        time.sleep(1)
        rot_deg(degree)
        radian = degree / 180. * np.pi
        self.theta += radian
        time.sleep(1)
        set_left_speed(150)
        set_right_speed(160)


    def on_goal(self):
        return abs(self.xgoal - self.xpos)+abs(self.ygoal-self.ypos) <= 4.


    def turn_to_goal(self, x, y):
	'''
	Move toward the goal until encountering a hit point or making the goal
	'''
        print "Current goal = ({}, {})".format(x, y)
        self.dgoal = np.arctan(float(y)/float(x))
        diff_rad = self.dgoal - self.theta
        diff_deg = diff_rad/np.pi*180
        print 'diff_rad = ', diff_rad
    	print 'diff_deg = ', diff_deg
        print "Current position = ({},{})", self.xpos, self.ypos
    	self.rotate(diff_deg)
        time.sleep(WAIT)
        dist = np.sqrt((x-self.xpos)**2+(y-self.ypos)**2)
        print "Distance to go = ", dist
        self.move(dist)
        time.sleep(1)


    def report(self):
        print 'Rover state:'
        print '(x, y, theta, angle) = ({}, {}, {}, {})'.format(self.xpos,self.ypos,self.theta, self.angle)
        print 'On m line? ',self.on_m_line()
        print 'Reach goal? ', self.on_goal()
        print


    def record_route(self):
	   self.route.append((self.xpos,self.ypos))
