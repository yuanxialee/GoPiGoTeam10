import sys
import numpy as np 
import matplotlib.pyplot as plt

class obstacles:

	def __init__(self):
		self.blocks = [] #the original blocks
		self.shapes = [] #append the first coordinate points to the end so that plotting looks nice
		self.gblocks = [] #grown obstacles

	def add_block(self, b, x): 
		self.blocks.append(b.get_block()) #add block points to obstacles list
		self.shapes.append(b.connect()) #connect block points for plotting shape
		self.gblocks.append(b.grow_blocks(x)) #grow block b by x square

	def get_obstacle(self, x):
		return self.blocks[x]

	def get_obstacles(self):
		return self.blocks

	def get_shape(self, x):
		return self.shapes[x]

	def get_shapes(self):
		return self.shapes

	def get_gobstacle(self, x):
		return self.gblocks[x]

	def get_gobstacles(self):
		return self.gblocks

	def get_points(self, x, y, z):
		return self.blocks[x][y][z]



class block: 

	def __init__(self):
		self.points = [] #used for singular obstacle or "block"
		self.vertices = [] #used for plotting shape
		self.gpoints = [] #used for grown block


	def add_points(self, x, y):
		self.points.append([x,y])

	def get_block(self):
		return self.points

	def connect(self):
		self.vertices.extend(self.points)
		self.vertices.append(self.points[0])

		return self.vertices

	def grow_blocks(self, x):
		i = 0
		sides = len(self.points)

		#use square growth
		while sides > 0:
			self.gpoints.append(self.points[i])
			self.gpoints.append([self.points[i][0], self.points[i][1]+x])
			self.gpoints.append([self.points[i][0]+x, self.points[i][1]])
			self.gpoints.append([self.points[i][0]+x, self.points[i][1]+x])
			i += 1
			sides -= 1

		return self.gpoints




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


	print len(obs.get_gobstacles())
	print obs.get_gobstacle(3)

'''
	print start, goal, dim, numobs
	print obs.get_obstacle(0)
	print obs.get_obstacle(1)
	print obs.get_obstacle(2)
	print obs.get_obstacle(3)
	print len(obs.get_obstacles())
	print obs.get_shape(1)
	'''
	
