# Homework for Topic 8:

class Node:
    """Represents a node in a binary search tree."""
    def __init__(self, key):
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
        self.val = key    # Value stored in the node

def insert(root, key):
    """Inserts a new node with the given key into the binary search tree."""
    if root is None:
        return Node(key)  # Create a new node if the tree is empty
    else:
        if key < root.val:
            root.left = insert(root.left, key)  # Recursively insert into the left subtree
        else:
            root.right = insert(root.right, key)  # Recursively insert into the right subtree
    return root

# Create a sample binary search tree
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

def find_max(root):
    """Finds the maximum value in the binary search tree."""
    if root is None:
        raise ValueError("The tree is empty.")

    current = root
    # Traverse right until the rightmost node is reached (the maximum value)
    while current.right is not None:
        current = current.right
    return current.val

def find_min(root):
    """Finds the minimum value in the binary search tree."""
    if root is None:
        raise ValueError("The tree is empty.")

    current = root
    # Traverse left until the leftmost node is reached (the minimum value)
    while current.left is not None:
        current = current.left
    return current.val

def sum_of_bst(root):
    """Calculates the sum of all values in the binary search tree."""
    if root is None:
        return 0  # Base case: empty tree has a sum of 0
    else:
        # Recursively calculate the sum for left subtree, right subtree, and current node value
        return root.val + sum_of_bst(root.left) + sum_of_bst(root.right)

# Example usage
print("Maximum value:", find_max(root))
print("Minimum value:", find_min(root))
print("Sum of values:", sum_of_bst(root))
