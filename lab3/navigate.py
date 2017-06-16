import sys
import numpy as np 
import matplotlib.pyplot as plt
from collections import deque
from map import *
from convex_hull import *
from graph import *


if __name__ == '__main__':

	obs = obstacles()
	b = block()

	info = []
	start = []
	goal = []
	dim = []
	numobs = 0

	#open file and put into list as floats
	with open(sys.argv[1]) as f:
	    for line in f:
	        data = line.split()
	        for i in range(len(data)):
	            info.append(float(data[i].strip('\n')))

	start.extend((info[0],info[1]))
	goal.extend((info[2],info[3]))
	dim.extend((info[4],info[5]))
	numobs = int(info[6])

	sides = int(info[7])
	count = 7

	#iterate, create blocks, add blocks to obstacles list
	while sides > 0:
		b.add_points(info[count+1], info[count+2])
		count += 2
		sides -= 1
		if sides == 0 and count+1 is not len(info):
			count += 1
			sides = int(info[count])
			obs.add_block(b, int(sys.argv[2]))
			b = block()
		elif sides == 0 and count+1 is len(info):
			obs.add_block(b, int(sys.argv[2]))


	#print len(obs.get_gobstacles())
	#print obs.get_gobstacle(3)

	i = 0
	j = len(obs.get_gobstacles())
	gobs = obstacles()
	while j > 0:
		points = obs.get_gobstacle(i)
		corners = obs.get_shape(i)
		i+=1
		j-=1
		polygon = np.array(points)
		plt.plot(polygon[:,0], polygon[:,1],'ko', label = 'grown obstacle')
		original = np.array(corners)
		plt.plot(original[:,0], original[:,1], 'b', label = 'original obstacle')
		ch = np.array(convex_hull(points))
		ch.tolist()
		print ch
		plt.plot(ch[:,0], ch[:,1],'r--',label = 'convex hull')
	plt.xlim([0,dim[0]])
	plt.ylim([0,dim[1]])
	plt.legend()
	plt.margins(0.05,0.1)
	plt.show()