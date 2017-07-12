import sys
import numpy as np
import time
from util import *
WAIT = 0.5
ZERO = 3
class rover:
    obstacles = []
    ql = [] # BUG memory
    qh = []

    def __init__(self, x, y):
        ''' Constructor'''
            # 2D has 3 degree of freedom(DOF)
            # xpos, ypos and theta are world configuration of robot
        self.xpos = 0
        self.ypos = 0
        self.theta = 0      # radian

        self.angle = 79 #MID
        #servo(self.angle)
        #set_speed(80)
            # set goal
        self.xgoal = x
        self.ygoal = y
        set_left_speed(160)
        set_right_speed(120)

    def move(self, dist):
        time.sleep(WAIT)
        fwd_cm(dist)
        self.xpos += dist * np.cos(self.theta)
        self.ypos += dist * np.sin(self.theta)
        time.sleep(WAIT)

    def rotate(self, degree):
        time.sleep(WAIT)
        rot_deg(degree)
        radian = degree / 180. * np.pi
        self.theta += radian
        time.sleep(WAIT)

    def adj_angle(self, degree):
        self.angle = np.clip(self.angle + degree,0,180)
        servo(self.angle)

    def on_m_line(self):
        return self.xpos*self.ygoal - self.ypos*self.xgoal <= ZERO

    def on_goal(self):
        return abs(self.xgoal - self.xpos)+abs(self.ygoal-self.ypos) <= ZERO

    def report(self):
        print 'Rover state:'
        print '(x, y, theta, angle) = ({}, {}, {}, {})'.format(self.xpos,self.ypos,self.theta, self.angle)
        print 'On m line? ',self.on_m_line()
        print 'Reach goal? ', self.on_goal()
        print
    
    def record_obstacle(self, dist):
        '''
        Record and obsticle on either front side or left-hand side.
        Because BUG2 turns left by default, servo angle should only
        ranges betweeen [0. MID]. Otherwise report an error.
        '''
        if self.angle == MID:
            xobs = self.xpos + dist * np.cos(self.theta)
            yobs = self.ypos + dist * np.sin(self.theta)
            self.obstacles.append((xobs,yobs))
        elif self.angle < MID and self.angle >= 0:
            xobs = self.xpos + dist * np.sin(self.theta)
            yobs = self.ypos - dist * np.cos(self.theta)
            self.obstacles.append((xobs,yobs))
        else:
            print 'Unexpected Servo Angle!'

    def follow_wall(self, initial_angle):
        '''
        Follow the wall and record obtacles
        '''
        stop()
        self.angle = initial_angle
        servo(self.angle)
        time.sleep(WAIT)
        while(True):
            curr_dist = avg_dist(3)
            self.record_obstacle(curr_dist)
            time.sleep(WAIT)
            if curr_dist < LOWER:
                rot_deg(-4)
                self.angle = np.clip(self.angle+4,0,180)
                servo(self.angle)
                time.sleep(WAIT)
                self.move(1)
            elif curr_dist > UPPER and curr_dist < INF:
                rot_deg(1)
                self.angle = np.clip(self.angle - 30,0,180)
                servo(self.angle)
                time.sleep(WAIT)
                self.move(1)
            elif curr_dist >= INF:
                stop()
                break
            else:
                self.move(3)
                time.sleep(WAIT)

if __name__ == '__main__':
    gopigo = rover(20, 30)  # set goal (20,30)
    
    if sys.argv[1] == '1':
        # coordinate transform
        gopigo.move(10)
        gopigo.report()
        gopigo.rotate(90)
        gopigo.report()
        gopigo.move(15)
        gopigo.report()
        gopigo.rotate(-33.7)
        gopigo.move(18)
        gopigo.report()
        '''
    elif sys.argv[1] == '2':
        # follow the wall
        gopigo.follow_wall(0)
        print gopigo.obstacles
        '''
