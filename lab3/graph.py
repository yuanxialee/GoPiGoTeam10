import numpy as np
INF = 99999.
class vertex:
    def __init__(self, id, x, y):
        # basic info.
        self.id = id
        self.x = float(x)
        self.y = float(y)
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
        self.source = s
        self.target = t
        self.weight = round(np.sqrt((t.x-s.x)**2 + (t.y-s.y)**2),4)

    def __str__(self):
        return "{} -- {} -> {}".format(self.source,self.weight,self.target)

class graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, id, x, y):
        self.vertices[id] = vertex(id, x, y)

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

if __name__ == '__main__':
    g = graph()
    g.add_vertex('New York',50,30)
    g.add_vertex('Boston',55, 45)
    g.add_edge('New York', 'Boston')
    print g.distance('New York', 'Boston')
