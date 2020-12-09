def in_order_iter(root):
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.val)
        in_order(root.right)

