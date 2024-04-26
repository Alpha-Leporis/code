'''
# check if it is a binary search tree or not.

This code defines a TreeNode class to represent nodes in the binary tree and a function is_bst 
to check if the given binary tree represented by its root node is a valid binary search tree. 
The is_bst function performs an in-order traversal of the tree and checks if the values encountered
are in sorted order. If they are, it returns True; otherwise, it returns False.

time complexity: O(n), where n is the number of nodes in the binary tree
space complexity: O(h), where h is the height of the binary tree
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(root):
    # Helper function for in-order traversal
    def inorder_traversal(node):
        nonlocal prev_value
        if node:
            if not inorder_traversal(node.left):
                return False
            if prev_value is not None and node.value <= prev_value:
                return False
            prev_value = node.value
            return inorder_traversal(node.right)
        return True

    # Initialize previous value to None
    prev_value = None
    return inorder_traversal(root)

# Example usage:
# Construct a binary tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

# Check if the tree is a BST
if is_bst(root):
    print("The tree is a binary search tree.")
else:
    print("The tree is not a binary search tree.")
