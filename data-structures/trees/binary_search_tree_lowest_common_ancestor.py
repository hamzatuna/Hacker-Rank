"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def lca(root, v1, v2):
    n = root
    while(n):
        if n.data > v1 and n.data > v2:
            n = n.left
        elif n.data < v1 and n.data < 2:
            n = n.right
        else:
            return n
    return root
