from collections import deque

def bfs(graph, source):
    queue = deque([source])
    visited = {source}

    while queue:
        node = queue.popleft()

        for n in graph[node]:
            if n not in visited:
                queue.append(n)
                visited.add(n)
    return visited
