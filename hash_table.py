import random
import string

class Node: 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value *= (hash_value * ord(i))
        return hash_value%self.table_size

    def double_tree_size(self):
        self.table_size *= 2
        old_table = self.hash_table
        self.hash_table = [None] * self.table_size

        for bucket in old_table:
            while bucket:
                self.add_key_value(bucket.data.key, bucket.data.value)
                bucket = bucket.next_node


    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            if node.data.key is key:
                node.data.value = value
                return                            
            count = 0
            while node.next_node:
                if node.data.key is key:
                    node.data.value = value
                    return
                node = node.next_node
                count += 1
            node.next_node = Node(Data(key, value), None)      
            if count > 3:
                self.double_tree_size()

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        node = self.hash_table[hashed_key]
        while node:
            if node.data.key is key:
                return node.data.value
            node = node.next_node
        return None


    def print_table(self):
        count = 0
        for bucket in self.hash_table:
            st = f"{str(count)} : "
            count += 1
            node = bucket
            while node:
                st += f"{str(node.data.value)} -> "
                node = node.next_node
            st += "None"
            print(st)

    
# letters = string.ascii_letters

# def create_random_string():
#     str = ""
#     str = str.join(random.choice(letters) for i in range(4))
#     return str

# h = HashTable(13)

# for i in range(42):
#     h.add_key_value(create_random_string(), create_random_string())

# h.print_table()        
