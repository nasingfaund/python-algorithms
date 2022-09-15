from collections import defaultdict

graph = {
    'A': {('B', 2), ('C', 1)},
    'B': {('A', 2), ('C', 4), ('D', 3)},
    'C': {('A', 1), ('B', 4), ('E', 2)},
    'E': {('C', 2), ('D', 1), ('F', 4)},
    'D': {('B', 3), ('E', 1), ('F', 2)},
    'F': {('D', 2), ('E', 4)}

}

graph_edges = []

for key, edges in graph.items():
    for edge in edges:
        graph_edges.append((key,) + edge)


def bellman_ford(edges, start: str):
    result = defaultdict(lambda: float('inf'))
    result[start] = 0

    for _ in graph:
        for edge in edges:
            src, dst, weight = edge
            result[dst] = min(result[dst], result[src] + weight)
    return result


print(bellman_ford(graph_edges, 'A'))


# https://www.youtube.com/watch?v=-mOEd_3gTK0
vertices = {'A', 'B', 'C', 'D', 'E'}
edges = [('A', 'D', 8), ('A', 'C', 5), ('A', 'B', 4), ('B', 'C', -3), ('C', 'E', 4), ('D', 'E', 2), ('E', 'D', 1)]


def bellman_ford2(edges, start: str):
    distance = {v: float('inf') for v in vertices}
    parent = {v: None for v in vertices}
    distance[start] = 0

    for _ in range(len(vertices) - 1):
        for src, dst, w in edges:
            if distance[src] + w < distance[dst]:
                distance[dst] = distance[src] + w
                parent[dst] = src
    path = []
    key = 'C'
    while True:
        if not key:
            break
        path.insert(0, key)
        key = parent[key]

    return path


print(bellman_ford2(edges, 'A'))
