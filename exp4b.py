class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Inorder: Left, Root, Right
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder: Root, Left, Right
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder: Left, Right, Root
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Creating Binary Tree

root = Node("Python")

root.left = Node("C Programming")
root.right = Node("Java")

root.left.left = Node("Data Structures")
root.left.right = Node("DBMS")

root.right.left = Node("Operating System")
root.right.right = Node("Computer Networks")


# Display Book Records

print("Library Book Catalog")

print("\nInorder Traversal:")
inorder(root)

print("\n\nPreorder Traversal:")
preorder(root)

print("\n\nPostorder Traversal:")
postorder(root)

print()