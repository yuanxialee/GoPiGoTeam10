from gopigo import *
import time
import random
import numpy as np

count = 0.0
while count < 20:
	x = np.random.choice(4,1)[0]
	if x == 0:
		fwd()
	elif x == 1:
		bwd()
	elif x == 2:
		left()
	else: 
		right()

	n = random.uniform(0,2)
	
	if count + n > 20:
		n = 20 - count

	time.sleep(n)
	count = count + n
	stop()

