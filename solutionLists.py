"""Solution for practice probelm"""

class LinkedList:
    def __init__(self):
        self.head = None # creates the root of the list

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")

        return " -> ".join(nodes) # adds an arrow for readability

    # The below makes it possible to traverse the linked list
    def __iter__(self): 
        node = self.head
        while node is not None: #
            yield node
            node = node.next    

    # adds a new node to the front
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # adds a new node to the end of the linked list
    def add_last(self, node):
        if self.head is None: #checks if there is a head first
            self.head = node 
            return
        for current_node in self:
            pass 
        current_node.next = node

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is Empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return 

            prev_node = node
        
        raise Exception ("Node with Data '%s' not found" % target_node_data)

    


class Node:
    def __init__(self, data):
        self.data = data # starts the data 
        self.next = None # starts the next

    def __repr__(self):
        return self.data

    
    
linked_list = LinkedList() 
# step 1
first_node = Node("chocolate bar")
linked_list.head = first_node 
second_node = Node("Flour") 
third_node = Node("eggs")
first_node.next = second_node 
second_node.next = third_node

# step 2
linked_list.add_first(Node("vegetable shortnening"))

# step 3
linked_list.add_last(Node("sugar"))

# step 4  
linked_list.add_before("eggs", Node("butter"))

# step 5 
print(linked_list)
