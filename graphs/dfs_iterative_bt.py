class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.left.right = Node(7)

root.left.right = Node(5)
root.left.right.right = Node(6)


def dfs(root):
    stack = [root]
    visited = []
    while stack:
        curr = stack.pop()
        if curr.val not in visited:
            while curr.left:
                if curr.left.val in visited:
                    break
                stack.append(curr)
                curr = curr.left
            while curr.right:
                if curr.right.val in visited:
                    break
                stack.append(curr)
                curr = curr.right

            visited.insert(0, int(curr.val))
    return visited
