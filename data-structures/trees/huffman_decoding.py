"""
class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT


def decodeHuff(root, s):
    result = ''
    l = list(s)
    n = root
    key = ''
    while l:
        if n.data != '\0':
            result += n.data
            n = root
        elif l.pop(0) == '1':
            n = n.right
        else:
            n = n.left
    if n.data != '\0':
        result += n.data
    print result
