import numpy as np
from collections import deque

def angle(pt1, pt2):
    return (np.arctan2(pt2[1]-pt1[1], pt2[0]-pt1[0]) / np.pi * 180) % 360

def left_turn(pt1, pt2, pt3):
    vec1 = np.array(pt2) - np.array(pt1)
    vec2 = np.array(pt3) - np.array(pt2)
    return vec1[0] * vec2[1] - vec1[1] * vec2[0] > 0

def convex_hull(points):
    # find out the the point with least y-value
    lowest = None
    for point in points:
        if lowest is None or point[1] < lowest[1]:
            lowest = point

    # sort point by the angles relative to lowest
    data = []
    for point in points:
        data.append((point, angle(lowest, point)))

    # sort by angle
    data.sort( key = lambda tup : tup[1])

    # place sorted list
    sorted_pts = []

    while len(data) > 0:
        sorted_pts.append(data.pop()[0])
    del data

    # jettison right turning points
    convex = [sorted_pts[0], sorted_pts.pop()]
    while len(sorted_pts) > 0:
        top1 = convex.pop()
        top2 = convex.pop()
        new = sorted_pts.pop()
        if left_turn(top2, top1, new):
            convex.append(top2)
            convex.append(top1)
            convex.append(new)

        else:
            convex.append(top2)
            # jettison top1
            convex.append(new)
    return convex

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    # Test Case 1: sorted point list
    points = [[0., 1.], [4., 2.], [10., 10.], \
              [7., 9.], [-3., 12.], [-3., 3.]]
    polygon = np.array(points)
    plt.plot(polygon[:,0], polygon[:,1],'ko', label = 'polygon points')

    ch = np.array(convex_hull(points))
    plt.plot(ch[:,0], ch[:,1],'r--',label = 'convex hull')
    plt.legend()
    plt.margins(0.05,0.1)
    plt.show()

    # Test Case 2: sorted point list
    points = [[3., 12.], [-3., 6.], [4., 6.], [8., 8.], \
              [0., 5.], [6., 3.], [0., 0.]]
    #shasha = [[200., 220.], [221.213203436, 241.213203436], [210.606601718, 251.819805153], [189.393398282, 230.606601718], [200., 220.]]
    shasha = [[230., 170.], [251.501987353, 190.920433549], [230.503960307, 191.208287996], [230., 170.]]
    test = np.array(shasha)
    polygon = np.array(points)
    plt.plot(polygon[:,0], polygon[:,1],'ko', label = 'polygon points')
    plt.plot(test[:,0], test[:,1], 'b', label = 'test') 
    ch = np.array(convex_hull(points))
    plt.plot(ch[:,0], ch[:,1],'r--',label = 'convex hull')
    plt.legend()
    plt.margins(0.05,0.1)
    plt.show()
