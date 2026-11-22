class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Recursive Postorder Traversal
def postorder(root):

    if root is not None:

        postorder(root.left)

        postorder(root.right)

        print(root.data, end=" ")


# Creating Binary Tree

root = Node(101)

root.left = Node(102)
root.right = Node(103)

root.left.left = Node(104)
root.left.right = Node(105)

root.right.left = Node(106)
root.right.right = Node(107)


# Display Postorder Traversal

print("Patient Registration Numbers:")
postorder(root)