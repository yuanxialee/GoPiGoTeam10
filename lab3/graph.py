import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

INF = 99999.
class vertex:

    def __init__(self, id, x, y, b):
        # basic info.
        self.id = id
        self.x = float(x)
        self.y = float(y)
        self.block = b
        self.neighbors = []
        # for Dijkstra
        self.known = False
        self.dist = INF
        self.prev = None

    def __str__(self):
        return "{} ({}, {})".format(self.id, self.x, self.y)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

class edge:

    def __init__(self, s, t):
        self.source = s #vertex
        self.target = t #vertex
        self.weight = round(np.sqrt((t.x-s.x)**2 + (t.y-s.y)**2),4)

    def __str__(self):
        return "{} -- {} -> {}".format(self.source,self.weight,self.target)

    #TODO: add comparator??
    def __cmp__(self, other):
        return self.source == self.source and self.target == self.target
class graph:

    def __init__(self):
        self.vertices = {}
        self.start = None

    def add_vertex(self, id, x, y, b):
        self.vertices[id] = vertex(id, x, y, b)

    def add_edge(self, id1, id2, directed = False):
        v1 = self.get_vertex(id1)
        v2 = self.get_vertex(id2)
        v1.neighbors.append(edge(v1, v2))
        if not directed:
            v2.neighbors.append(edge(v2, v1))

    def distance(self, id1, id2):
        edge = self.get_edge(id1, id2)
        if edge is None:
            return None
        return edge.weight

    def get_edge(self, id1, id2):
        v1 = self.get_vertex(id1)
        v2 = self.get_vertex(id2)

        for neighbor in v1.neighbors:
            if neighbor.target == v2:
                return neighbor
        return None

    def get_vertex(self, id):
        if id not in self.vertices:
            raise ValueError('Key does not exist.')
        return self.vertices[id]

    def intersect(self, edge1, edge2):
        p1 = np.array([edge1.source.x, edge1.source.y])
        p2 = np.array([edge2.source.x, edge2.source.y])
        p3 = np.array([edge1.target.x, edge1.target.y])
        p4 = np.array([edge2.target.x, edge2.target.y])
    
        vec1 = p3 - p1
        vec2 = p4 - p2
        V = np.array([vec1, -vec2])
        P = p2 - p1
        if np.linalg.det(V) == 0:
            # check if on the same line
            M = np.array([vec1, P])
            if np.linalg.det(M) == 0:
                d1 = p2 - p1
                ratio1 = vec1.dot(d1)/np.linalg.norm(vec1,2)**2

                d2 = p4 - p1
                ratio2 = vec1.dot(d2)/np.linalg.norm(vec1,2)**2

                d3 = p1 - p4
                ratio3 = vec2.dot(d2)/np.linalg.norm(vec2,2)**2

                d4 = p3 - p4
                ratio4 = vec2.dot(d2)/np.linalg.norm(vec2,2)**2
                if (ratio1 > 0 and ratio1 < 1) or \
                        (ratio2 > 0 and ratio2 < 1) or \
                        (ratio3 > 0 and ratio3 < 1) or \
                        (ratio4 > 0 and ratio4 < 1):
                    return True
            return False

        alpha, beta = P.dot(np.linalg.inv(V))
        return (alpha > 0 and alpha < 1) \
                and (beta > 0 and beta < 1)
        

    def min_dist(self, visit = []):
        i = 0
        mini = self.get_vertex(visit[i].id).dist
        node = self.get_vertex(visit[i].id)
        n_nodes = len(visit)
        i += 1
        n_nodes -= 1
        while n_nodes > 0:
            if self.get_vertex(visit[i].id).dist < mini:
                mini = self.get_vertex(visit[i].id).dist
                node = self.get_vertex(visit[i].id)
            i += 1
            n_nodes -= 1
        return node
    
    def visualize(self, patches = None, lines = None):
        fig, ax = plt.subplots()
        if patches is not None:
            for patch in patches:
                ax.add_patch(Polygon(patch, fill=True))
        for v in self.vertices.values():
            ax.plot(v.x, v.y, 'ko')
            ax.text(v.x-0.5, v.y+0.5, str(v.id))
            for neighbor in v.neighbors:
                ax.plot([v.x, neighbor.target.x], [v.y, neighbor.target.y], linewidth = 0.3, color='#808080')
        if lines is not None:
            arr = np.array(lines)
            print arr
            ax.plot(arr[:,0], arr[:,1], 'r', linewidth=3.0)
        ax.margins(0.15, 0.15)
        plt.show()

    def path(self, to):
        if to not in self.vertices:
            raise ValueError('{} does not exist.'.format(to))
        path = []
        curr = self.get_vertex(to)
        while (curr is not None):
            path.insert(0, [curr.x, curr.y])
            curr = curr.prev
        return path

    def dijkstra(self, id):
        self.start = id
        complete = []
        visit = []
        for vertex in self.vertices:
            visit.append(self.get_vertex(vertex))


        n_nodes = len(self.vertices)
        self.get_vertex(id).dist = 0
        while n_nodes > 0:
            minv = self.min_dist(visit)            

            for neighbor in minv.neighbors:
                w = neighbor.weight
                t = self.get_vertex(neighbor.target.id)
                if minv.dist + w < t.dist:
                    t.dist = minv.dist + w
                    t.prev = minv

            minv.known = True
            complete.append(minv.id)
            

            j = len(visit)
            i = 0
            while j > 0:
                if minv.id == self.get_vertex(visit[i].id).id:
                    visit.remove(self.get_vertex(visit[i].id))
                    j -= 1
                i += 1
                j -= 1
            if len(visit) > 0:
                id = self.get_vertex(visit[0].id).id
            n_nodes -= 1



if __name__ == '__main__':
    g = graph()
    g.add_vertex('New York',50,30)
    g.add_vertex('Boston',55, 45)
    g.add_edge('New York', 'Boston')
    g.dijkstra('New York')
    print g.distance('New York', 'Boston')
    print g.get_vertex('Boston')
    g.visualize()
    '''
    g = graph()
    v1 = vertex(1,2,2)
    v2 = vertex(2,2,2)
    v3 = vertex(3,0,0)
    v4 = vertex(4,4,3)
    e1 = edge(v1, v3)
    e2 = edge(v2, v4)
    print g.intersect(e1, e2)
    '''
