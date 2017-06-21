# standart packages
import sys
import numpy as np 
import itertools
from collections import deque
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
# include files
from map import *
from convex_hull import *
from graph import *
from rover import *

if __name__ == '__main__':

	obs = obstacles()
	b = block()

	info = []
	start = []
	goal = []
	dim = []
	numobs = 0

	#open file and put info into list as floats
	with open(sys.argv[1]) as f:
	    for line in f:
	        data = line.split()
	        for i in range(len(data)):
	            info.append(float(data[i].strip('\n')))

	
	gopigo = rover(info[0], info[1], info[2], info[3]) #initiate rover with info
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

	i = 0
	j = len(obs.get_gobstacles())
	k = 0
	gobs = obstacles() #set of grown obstacles

	#iterate, send to plot, and add grown obstacles to 'gobs'
	while j > 0:
		l = 0
		b = block()
		points = obs.get_gobstacle(i)
		corners = obs.get_shape(i)
		polygon = np.array(points)
		plt.plot(polygon[:,0], polygon[:,1],'ko', label = 'grown obstacle')
		original = np.array(corners)
		plt.plot(original[:,0], original[:,1], 'b', label = 'original obstacle')
		ch = np.array(convex_hull(points))
		k = len(ch)
		while k > 0:
			b.add_points(ch[l][0],ch[l][1])
			k -= 1
			l += 1
		gobs.add_block(b, 0)
		b = block()
		plt.plot(ch[:,0], ch[:,1],'r--',label = 'convex hull')
		i+=1
		j-=1
	plt.xlim([0,dim[0]])
	plt.ylim([0,dim[1]])
	plt.legend()
	plt.margins(0.05,0.1)
	plt.show()


	# Visibility graph 
	block_edges = []
	i = 0           # id counter
	g = graph()
        g.add_vertex(i, start[0], start[1], -1)
        i += 1
        g.add_vertex(i, goal[0], goal[1], -1)
        i += 1

        # construct obstacles in graph
	for blockid, block in enumerate(gobs.get_obstacles()):

                # create vertex and edges in graph
		start = i
		end = start + len(block) - 1

	        for x, y in block:
		        if i == end:
                                break
			g.add_vertex(i, x, y, blockid)

		        if i != start:
			        g.add_edge(i-1, i)
                                block_edges.append(g.get_edge(i-1,i))
                                block_edges.append(g.get_edge(i,i-1))
                        i += 1
	        g.add_edge(start, end-1)
                block_edges.append(g.get_edge(start, end-1))
                block_edges.append(g.get_edge(end-1, start))
        
        g.visualize(gobs.get_obstacles()) #constructed grown obstacles with vertices and edges (filled in in plot)
        
        # create eligible path edgs
        for v1 in g.vertices.values():
                for v2 in g.vertices.values():
                        if v1 == v2 or v1.block == v2.block:
                                continue
                        potential_edge = edge(v1, v2)
                        crossed = False
                        for block_edge in block_edges:
                                if g.intersect(potential_edge, block_edge):
                                        crossed = True
                                        break
                        if not crossed:
                                g.add_edge(v1.id, v2.id, directed = True)

        g.visualize(gobs.get_obstacles()) #visibility graph
        
        g.dijkstra(0)
        g.visualize(gobs.get_obstacles(), g.path(1)) #dijkstra's path
        
	
	#for the gopigo to run
	path = g.path(1)
	l = len(path)
	i = 1
	gopigo.record_route()
	
	#iterate through vertex points in path
	while l > 1:
		gopigo.turn_to_goal(path[i][0], path[i][1])
		i+=1
		l-=1
		gopigo.record_route()
		if gopigo.on_goal():
			stop()
			gopigo.record_route()
			gopigo.state = 'success'
	
	print "Current position = ({},{})".format(gopigo.xpos, gopigo.ypos)
	