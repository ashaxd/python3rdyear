class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data, end=" ")
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
print("PostOrder Traversel:", end=" ")
PostOrder(root)
