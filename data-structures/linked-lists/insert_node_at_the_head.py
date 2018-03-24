def insert(head, data):
    new_node = Node(data)
    new_node.next, head = head, new_node
    return head
