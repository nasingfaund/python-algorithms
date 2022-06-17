graph = {
    0: [1, 2],
    1: [],
    2: [0, 3, 4],
    3: [2, 4],
    4: [2, 3]

}


def is_cycle(graph):
    visited = []

    def dfs(start, parent):
        visited.append(start)
        for node in graph[start]:
            if node == parent:
                continue
            if node in visited:
                return True
            if dfs(node, start):
                return True

        return False

    for n in graph:
        if n not in visited:
            if dfs(n, -1):
                return True
    return False


assert is_cycle(graph) == True
