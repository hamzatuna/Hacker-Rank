"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""


def insert(r, val):
    if not r:
        return Node(val)
    t = r
    while(t):
        if val > t.data and t.right is None:
            t.right = Node(val)
            return r
        elif val > t.data:
            t = t.right
        if val < t.data and t.left is None:
            t.left = Node(val)
            return r
        elif val < t.data:
            t = t.left
