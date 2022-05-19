def dfs(graph, start, visited):
    if start not in visited:
        visited.append(start)
        for node in graph[start]:
            dfs(graph, node, visited)
    return visited


def _dfs(graph, source, visited):
    visited.append(source)
    for node in graph[source]:
        if node not in visited:
            _dfs(graph, node, visited)
    return visited


def dfs_iter(graph, start):
    visited = [start]
    stack = [start]
    while stack:
        for vertex in graph[start]:
            if vertex not in visited:
                stack.append(vertex)
        top = stack.pop()
        if top not in visited:
            visited.append(top)
        start = top
    return visited
