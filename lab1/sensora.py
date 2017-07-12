from gopigo import *
import time

set_speed(100)

while us_dist(15) < 5:
	bwd()
	print us_dist(15)

while us_dist(15) > 5 and us_dist(15) < 18:
	fwd() 
	print us_dist(15)

while us_dist(15) > 17 and us_dist(15) < 30:
	bwd() 
	print us_dist(15)

while us_dist(15) > 30 and us_dist(15) < 46:
	fwd() 
	print us_dist(15)

while us_dist(15) > 45 and us_dist(15) < 60:
	bwd() 
	print us_dist(15)

while us_dist(15) > 60:
	fwd() 
	print us_dist(15)

stop()




