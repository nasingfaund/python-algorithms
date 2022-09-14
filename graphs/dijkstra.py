from queue import PriorityQueue

graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 3)],
    'C': [('B', 4), ('E', 2)],
    'E': [('D', 1), ('F', 4)],
    'D': [('F', 2)],
    'F': []

}


def dikstra(graph, start: str, end: str):
    queue = PriorityQueue()
    queue.put_nowait((start, 0))

    result_map = defaultdict(lambda: float('inf'))

    while not queue.empty():
        node, weight = queue.get_nowait()

        result_map[node] = min(result_map[node], weight)

        for label, w in graph[node]:
            queue.put_nowait([label, w + weight])

    return result_map[end]


print(dikstra(graph, 'A', 'F'))



graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('A', 2), ('C', 4), ('D', 3)],
    'C': [('A', 1), ('B', 4), ('E', 2)],
    'E': [('C', 2), ('D', 1), ('F', 4)],
    'D': [('B', 3), ('E', 1), ('F', 2)],
    'F': [('D', 2), ('E', 4)]

}


def dijkstra(graph, start: str):
    result_map = defaultdict(lambda: float('inf'))
    result_map[start] = 0

    visited = set()

    queue = [(0, start)]

    while queue:
        weight, v = heapq.heappop(queue)
        visited.add(v)

        for u, w in graph[v]:
            if u not in visited:
                result_map[u] = min(w + weight, result_map[u])
                heapq.heappush(queue, [w + weight, u])

    return result_map

