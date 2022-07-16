

class BST:
    """
    Binary Search Tree data (BST) structure
    The node class below is an inner class.
    To create a Node object we need to specifiy BST.Node
    """

    class Node: 
        """
        Each node of the tree will have data and links to the left
        and right sub tree.
        """

        def __init__(self, data): 
            """
            Initialize the node to the data provided. Initially set to None. 
            """

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        starts an empty BST.
        """

        self.root = None

    def insert(self, data):
        """ 
        Insert a new node into the BST. If the BST is empty then the new node becomes the root. 
        Otherwise we call the function recursively to find the location to put the new node. 
        """
        if self.root is None: 
            self.root = BST.Node(data)
        else: 
            self._insert(data, self.root) 

    def _insert(self, data, node):
        """
        This looks for the right place to put the new node. 
        The current sub-tree is the "node".
        """
        if data == node.data: 
            return 0

        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.

                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)

    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root
 
    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        
        if data == node.data:# base case
            return True

        else: 
            if data < node.data:
                if node.left is None:
                    return False
                else: 
                    return self._contains(data, node.left)
 
            elif data >= node.data:
                if node.right is None:
                    return False
                else:
                    return self._contains(data, node.right)
                    
    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)