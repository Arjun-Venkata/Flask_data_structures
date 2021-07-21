class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, data, node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            return

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _print_rec(self, node):
        if node is None:
            return 
        print(node.data)
        self._print_rec(node.left)
        self._print_rec(node.right)
        return

    def print_table(self):
        node = self.root
        self._print_rec(node)

    def _search(self, value, node):
        
        if node is None:
            return None
        if node.data["id"] is value:
            return node.data
        if node.data["id"] < value:
            return self._search(value, node.right)
        else:
            return self._search(value, node.left)


    def search(self, value):
        node = self.root
        return self._search(int(value), node)

# p = BinarySearchTree()
# p.insert(4)
# p.insert(6)
# p.insert(5)
# p.insert(2)
# p.print_table()