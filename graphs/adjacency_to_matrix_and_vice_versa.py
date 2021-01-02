graph_list = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 5],
    4: [2],
    5: [3]
}


def from_list_to_matrix(graph):
    dist = [[0] * len(graph) for i in range(len(graph))]
    for v in graph:
        for u in graph[v]:
            dist[v - 1][u - 1] = 1
    return dist


##############################################
graph_matrix = [[0, 1, 1, 0, 0],
         [1, 0, 1, 1, 0],
         [1, 1, 0, 0, 1],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0]]


def to_list_adjacency(graph):
    dist = {}
    for i in range(len(graph)):
        dist.update({
            i + 1: []})
        for j in range(len(graph)):
            if graph[i][j] == 1:
                dist[i + 1].append(j + 1)
    return dist
