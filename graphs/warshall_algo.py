"""
Floyd–Warshall algorithm:
Is an algorithm for finding shortest paths in a weighted graph
with positive or negative edge weights (but with no negative cycles).

"""

graph = {
    0: {
        2: -2},
    1: {
        0: 4,
        2: 3},
    2: {
        3: 2},
    3: {
        1: -1}
}


def floyd_warshall(graph):
    dist = [[float('inf')] * len(graph) for i in range(len(graph))]

    for v in range(len(graph)):
        dist[v][v] = 0

    for u in graph:
        for v in graph[u]:
            dist[u][v] = graph[u][v]

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


print(floyd_warshall(graph))
