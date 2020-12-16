def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.val)
        in_order(root.right)
