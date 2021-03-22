# # node 
# class Node():
#     def __init__(self, data):
#         # data, next -> pointer
#         self.data = data
#         self.next = None

#     def __str__(self):
#         return f"Node: {self.data}\n Pointer -> {self.next}"

# # test
# node_one = Node(7)
# print(node_one)
# node_two = Node("hello")
# print(node_two)
# # linked list


# class linkedList():
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def __str__(self):
#         return f"Linked List\n Head -> {self.head}, Tail -> {self.tail}, length -> {self.length}"
    
#     def add_to_tail(self, data):
#         new_node = Node(data)

#         if not self.head:
#             self.head = new_node
#         else:
#             self.tail.next = new_node

#         self.tail = new_node
#         self.length += 1
#         return self 
        



#     def add_to_head(self, data):
#         new_node = Node(data)

#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.node.next = self.head
#             self.head = new_node

        
#         self.length += 1   
#         return self


#     def remove_head(self):
#         if not self.head: 
#             return None
#         current_head = self.head
#         self.head = current_head.next
#         self.length -= 1
#         if self.length == 0:
#             self.tail = None
#         return current_head



# list_one =  linkedList()    
# # list_one.add_to_tail(node_one)
# list_one.add_to_tail('yomi')
# list_one.add_to_head(8)
# list_one.add_to_head(77)
# list_one.remove_head()
# print(list_one)   


# List contains the nodes and the nodes contain the data and the pointer

# All of the different data structures are some form of an OBJECT

# data base
# table (collection) -> Node
# table (collection) -> Linked List

# association 
# Node belong to a Linked List
# {
#     id: ObjectId,
#     data: node.data
# }
# # Linked List will have many nodes
# {
#     id: ObjectId,
#     list: list_one,
#     nodes: [NodeId, NodeId]
# }

# We want to build an app
# Make an API
# How am I going to handle the data efficiently
    # - What data is coming in...
    # - How much data is coming in...
    # - How you want to handle the data
        # - access data
        # - add data
        # - update data
        # - remove data
        # - search for data



class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
            return f"Node: {self.data}\n Pointer -> {self.next}"

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return f"Linked List\n Head -> {self.head}, Tail -> {self.tail}, Length -> {self.length}"

    def add_to_tail(self, data):
        new_node = Node(data)

        if (not self.head):
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1
        return self

    def remove_tail(self):
        if not self.head: 
            return None

        current = self.head
        new_tail = current

        while current.next:
            new_tail = current
            current = current.next
    
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1

        if self.length == 0: # also can say if self:
            self.head = None
            self.tail = None

        return current
    
    def add_to_head(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return self

    def remove_head(self):
        '''Remove the head node from the list'''
        # hint: think about what if there is no head
        # hint: what if the length is 0
        # return current_head
        if not self.head: 
            return None
        current_head = self.head
        self.head = current_head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current_head

    def contains(self, target):
        node = self.head
        while node:
            if node.data == target: 
                return True
            node = node.next

        return False

    def get(self, index):
        if index < 0 or index >= self.length:
             return None
        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1

        return current

    def set(self, index, data):
        found_node = self.get(index)
        if found_node:
            found_node.data = data
            return True

        return False

    def insert(self, index, data):
        if index < 0 or index >= self.length: 
            return False
        if index == self.length:
            return not not self.add_to_tail(data)
        if index == 0:
            return not not self.add_to_head(data)

        new_node = Node(data)
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = new_node
        new_node.next = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.remove_head()
        if index == self.length - 1: 
            return self.remove_tail()
        previous_node = self.get(index - 1)
        removed = previous_node.next
        previous_node.next = removed.next
        self.length -= 1
        return removed

    def size(self):
        return self.length

list_one = LinkedList() # makes a new LinkedList and is set to variable list_one
list_one.add_to_tail('Rome')
list_one.add_to_head(8)
list_one.add_to_head(77)
print(list_one)
print(f"removed head {list_one.remove_head()}")