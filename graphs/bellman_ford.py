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
