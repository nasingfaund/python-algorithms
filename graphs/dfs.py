def dfs(graph, start, visited):
    if start not in visited:
        visited.append(start)
        for node in graph[start]:
            dfs(graph, node, visited)
    return visited
