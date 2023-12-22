class Node:
    def __init__(self, data):
         self.data = data
         self.left = None
         self.right = None
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
         root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root
#Helper function to print the inorder traversal of the 
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)
#Example usage
#Constructing the initial BST
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
print("Original BST: ", end="")
inorder_traversal(root)
print()
#Inserting a value into the BST
value_to_insert = 6
root = insert(root, value_to_insert)
print(f"updated BST after inserting {value_to_insert}:")
inorder_traversal(root)
print()                                  
