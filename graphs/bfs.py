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
