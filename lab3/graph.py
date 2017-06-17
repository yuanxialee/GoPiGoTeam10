import numpy as np
import matplotlib.pyplot as plt

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

    def add_vertex(self, id, x, y, b):
        self.vertices[id] = vertex(id, x, y, b)

    def add_edge(self, id1, id2):
        v1 = self.get_vertex(id1)
        v2 = self.get_vertex(id2)
        v1.neighbors.append(edge(v1, v2))
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
        if edge1 == edge2:
            return True
        p1 = np.array([edge1.source.x, edge1.source.y])
        p2 = np.array([edge2.source.x, edge2.source.y])
        p3 = np.array([edge1.target.x, edge1.target.y])
        p4 = np.array([edge2.target.x, edge2.target.y])
    
        vec1 = p3 - p1
        vec2 = p4 - p2
        V = np.array([vec1, -vec2])
        P = p2 - p1
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
    
    def visualize(self):
        for v in self.vertices.values():
            plt.plot(v.x, v.y, 'ko')
            plt.text(v.x-0.5, v.y+0.5, str(v.id))
            for neighbor in v.neighbors:
                plt.plot([v.x, neighbor.target.x], [v.y, neighbor.target.y], 'k-')
        plt.margins(0.15, 0.15)
        plt.show()

    def dijkstra(self, id):
        complete = []
        visit = []
        for vertex in self.vertices:
            visit.append(self.get_vertex(vertex))

        print self.get_vertex(visit[0].id).known

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
            print "Minv id = ", self.get_vertex(minv.id).id
            complete.append(minv.id)
            print "First indice of visit = ", self.get_vertex(visit[0].id).id
            print self.get_vertex(visit[0].id).known

            j = len(visit)
            i = 0
            while j > 0:
                if minv.id == self.get_vertex(visit[i].id).id:
                    visit.remove(self.get_vertex(visit[i].id))
                i += 1
                j -= 1
            if len(visit) > 0:
                id = self.get_vertex(visit[0].id).id
            n_nodes -= 1

        print "Complete ", complete
        print "Visit ", visit

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
