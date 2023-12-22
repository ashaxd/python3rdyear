class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def PreOrder(root):
    if root:
        #print thr current node's data
        print(root.data, end=" ")
        #recursively traverse the left subtree
        PreOrder(root.left)
        #recursively traverse the right subtree
        PreOrder(root.right)
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
#Calling pPreOrder function to print the Preorder traversel
print("PreOrder Traversel:", end=" ")
PreOrder(root)
