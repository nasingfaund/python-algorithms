graph = {
    1: [3, 2],
    2: [4],
    3: [4],
    4: []
}


def topological_sort(graph, start, visited, result):
    if start not in visited:
        visited.append(start)
        for node in graph[start]:
            topological_sort(graph, node, visited, result)
        result.insert(0, start)
    return result


print(topological_sort(graph, 1, [], []))
