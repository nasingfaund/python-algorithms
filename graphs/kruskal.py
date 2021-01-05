"""
Kruskal's algorithm is a minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which
    form a tree that includes every vertex
    has the minimum sum of weights among all the trees that can be formed from the graph
"""


from disjoint_set import DisjointSet


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])


def kruskal(graph):
    ds = DisjointSet()
    A = set()
    for v in graph.V:
        ds.find(v)

    for u, v, w in sorted(graph.edges, key=lambda x: x[2]):
        if ds.find(u) != ds.find(v):
            A = A | {(u, v)}
            ds.union(u, v)
    return A


g = Graph(range(6))

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)

print(kruskal(g))
