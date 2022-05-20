from collections import deque

# bfs differs from dfs in two ways:
# 1) it uses a queue (First In First Out) instead of a stack and
# 2) it checks whether a vertex has been explored before enqueueing the vertex 
# rather than delaying this check until the vertex is dequeued from the queue.

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
