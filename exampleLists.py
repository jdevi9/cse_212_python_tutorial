"""Example code for creating and traversing a Linked List"""

from unittest.mock import NonCallableMagicMock


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
    


class Node:
    def __init__(self, data):
        self.data = data # starts the data 
        self.next = None # starts the next

    def __repr__(self):
        return self.data

    
    
linked_list = LinkedList() # declaring the list to get it started
print(linked_list)

first_node = Node("hello")
linked_list.head = first_node # adds hello as the head node
print(linked_list)

second_node = Node("world") #assigning the second node to a data of world
third_node = Node("cats")
first_node.next = second_node #applying that the second node world is attached to the first node hello
second_node.next = third_node # same as above comment but with 2 and three node
print(linked_list)
print() # blank line


print("Iteration example below:\n")
for node in linked_list: # iterates through the list and prints each one to the console
    print(node)

print() #blank space

print("Adding a new first node to the linked list:\n")
print("Original List:")
print(linked_list)
print() # blank space
linked_list.add_first(Node("Chicken")) # calls the add first function to put chicken at front
print(linked_list)


