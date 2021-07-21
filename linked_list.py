class Node: 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;
    
    def print_list(self):
        ll_string = ""
        node = self.head
        if node is None:
            print("None")
        else:
            while node:
                ll_string += f" {str(node.data)} ->"
                node = node.next_node
            ll_string += " None"
        print(ll_string)


    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    def insert_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
        else:
            self.tail.next_node = Node(data)
            self.tail = self.tail.next_node

    def to_list(self):
        arr = []
        if self.head is None:
            return arr
        node = self.head
        while node:
            arr.append(node.data)
            node = node.next_node
        return arr

    def get_user_by_id(self, id):
        node = self.head
        while node:
            if node.data["id"] is int(id):
                return node.data
            node = node.next_node
        return None


