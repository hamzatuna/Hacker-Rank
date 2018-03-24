'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))
