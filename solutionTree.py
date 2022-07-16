"""These are to be added to your already exisitng BST Class"""

#################
# Requirement 1 #
#################

def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

def _traverse_backward(self, node):
    """
    Does a backwards traversal (reverse in-order traversal) through the 
    BST.  If the node that we are given (which is the current
    sub-tree) exists, then we will keep traversing on the right
    side (thus getting the larger numbers first), then we will 
    provide the data in the current node, and finally we will 
    traverse on the left side (thus getting the smaller numbers last).

     This function is intended to be called the first time by 
    the __reversed__ function.        
    """
    # Replace this when you implement your solution
    if node is not None:
        yield from self._traverse_backward(node.right)
        yield node.data
        yield from self._traverse_backward(node.left)


#################
# Requirement 2 #
#################

 
def minValueNode(node):
    """This function will look for the next minimum node in the current branch"""
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current
 
 
def deleteNode(root, key):
    """This function deletes the desired node. We have to add
    extra logic to handle when a node has children underneath. 
    That way those items are moved over.
    """
 
    # Base Case
    if root is None:
        return root
 
    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    # If the key to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
 
    return root

