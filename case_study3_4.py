class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    stack = []
    current = root

    while current is not None or len(stack) > 0:

        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()

        print(current.data, end=" ")

        current = current.right


# Creating Binary Tree

root = Node("E201")

root.left = Node("E202")
root.right = Node("E203")

root.left.left = Node("E204")
root.left.right = Node("E205")

root.right.right = Node("E206")


# Inorder Traversal

print("Employee IDs:")
inorder(root)