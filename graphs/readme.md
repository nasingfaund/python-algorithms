# Graphs algorithms, that you should know

Algorithms for finding shortest path:
1. Depth-First Search (DFS)
2. Breadth-First Search (BFS)
3. Bidirectional Search
4. Dijkstra’s Algorithm
5. Bellman-Ford Algorithm 

How to find connected components of a graph?

### Terminology:

* [**Spanning Tree**](https://www.programiz.com/dsa/spanning-tree-and-minimum-spanning-tree#minimum-spanning) is a sub-graph of an undirected connected graph, 
which includes all the vertices of the graph with a minimum possible number of edges. If a vertex is missed, then it is not a spanning tree.
* **Minimum Spanning Tree** - A minimum spanning tree is a spanning tree in which the sum of the weight of the edges is as minimum as possible.

The minimum spanning tree from a graph is found using the following algorithms:
- **Prim's Algorithm**
- **Kruskal's Algorithm**


#### [Kruskal's Algorithm](https://www.programiz.com/dsa/kruskal-algorithm) (greedy algorithm)
Kruskal's algorithm is a minimum spanning tree algorithm that takes a graph as input and finds the subset of the edges of that graph which

- form a tree that includes every vertex
- has the minimum sum of weights among all the trees that can be formed from the graph

The **time complexity** of Kruskal's Algorithm is: **O(E log E)**.
