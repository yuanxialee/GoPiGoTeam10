import numpy as np
import matplotlib.pyplot as plt
from graph import edge, graph, vertex

if __name__ == '__main__':
    p1 = np.array([0,0])
    p2 = np.array([2,4])
    p3 = np.array([3,3])
    p4 = np.array([2,0])
    #p1 = np.array([0,0])
    #p2 = np.array([1,1])
    #p3 = np.array([2,3])
    #p4 = np.array([2,0])

    points = np.array([p1,p2,p3,p4])
    print points
    vec1 = p3 - p1
    vec2 = p4 - p2
    V = np.array([vec1, -vec2])
    print 'v1: ',vec1
    print 'v2: ',vec2
    print 'V: ',V
    P = p2 - p1
    alpha, beta = P.dot(np.linalg.inv(V))
    print alpha
    print beta
    #intersect = p1 + alpha * vec1
    intersect = p2 + beta * vec2
    plt.plot(intersect[0],intersect[1],'ro')
    plt.plot(points[:,0],points[:,1],'ko')
    plt.arrow(p1[0],p1[1],vec1[0],vec1[1],head_length=-0.1,head_width=0.05,ec='b')
    plt.arrow(p2[0],p2[1],vec2[0],vec2[1],head_length=-0.1,head_width=0.05,ec='b')
    plt.margins(0.15,0.15)
    plt.show()
    print (alpha > 0 and alpha < 1) and (beta > 0 and beta < 1)
