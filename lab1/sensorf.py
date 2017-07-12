from gopigo import *
import time

"""
#what we'd do if the sensor were accurate
set_speed(100)

while us_dist(15) < 25:
	bwd()
	print us_dist(15)

while us_dist(15) > 25:
	fwd() 
	print us_dist(15)
"""

dist = 25.0
enable_servo()
angle = 79
INF = 70
servo(angle)
time.sleep(1)


while us_dist(15) < INF:
	angle += 2
	servo(angle)
	time.sleep(0.2)

print angle
print us_dist(15)

angle = angle - 79
width = math.tan(math.radians(angle))*2.0*dist

print width






