

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

    