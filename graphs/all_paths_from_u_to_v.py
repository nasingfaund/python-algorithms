graph = {
    1: [3, 4],
    3: [4],
    4: [5],
    5: []
}


def dfs(graph, start, end, paths, visited):
    if start and end in visited:
        paths.append(list(visited))
        return paths
    if start not in visited:
        visited.append(start)
        for node in graph[start]:
            dfs(graph, node, end, paths, visited)

    visited.pop()
    return paths


assert dfs(graph, 1, 4, [], []) == [[1, 3, 4], [1, 4]]
