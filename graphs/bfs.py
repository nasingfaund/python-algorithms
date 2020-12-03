def bfs(graph, start):
    queue = [start]
    visited = [start]
    while queue:
        curr = queue.pop(0)
        for v in graph[curr]:
            if v not in visited:
                queue.append(v)
                visited.append(v)

    return visited
