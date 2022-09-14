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
