class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        if self.tail is None:
            self.tail = self.head = Node(data)
            return
        self.tail.next_node = Node(data)
        self.tail = self.tail.next_node
    
    def dequeue(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next_node
        if self.head is None:
            self.tail = self.head
        return node.data

    def print_q(self):
        node = self.head
        str = ""
        while node:
            str += f"{node.data} -> " 
            node = node.next_node
        print(str + "None")

q = Queue()
q.enqueue(3)
q.enqueue(25)
q.print_q()
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.print_q()