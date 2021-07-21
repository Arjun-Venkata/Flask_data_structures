class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    
    def peek(self):
        if self.head:
            return self.head.data
        return self.head

    def push(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        node = self.head
        self.head = node.next
        return node.data


