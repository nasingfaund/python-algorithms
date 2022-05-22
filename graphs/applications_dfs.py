# 1) find the path from start to destination/not optimal 

def _find_path(graph, start, end, path):
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = _find_path(graph, node, end, path + [node])
            if newpath:
                return newpath


def find_path(graph, start, end):
    return _find_path(graph, start, end, [start])

# 2) find the shortest path from start to destination

# It can be shown that, for unweighted graphs
# the BFS is equivalent to Dijkstra's algorithm and thus finds the shortest path in this circumstance.

# It has the extremely useful property that if all of the edges in a graph are unweighted (or the same weight)
# then the first time a node is visited is the shortest path to that node from the source node
def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if n not in dist:
                dist[n] = [dist[node], n]
                if n == end:
                    return dist.get(end)  # [[['A'], 'B'], 'D']
                queue.append(n)
    return None


print(find_shortest_path(graph, 'A', 'D'))
