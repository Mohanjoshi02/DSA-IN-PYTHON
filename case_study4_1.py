class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert node into BST
def insert(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Recursive Inorder Traversal
def inorder(root):

    if root is not None:
        inorder(root.left)

        print(root.data, end=" ")

        inorder(root.right)


# Main Program

root = None

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter student roll number: "))
    root = insert(root, roll)


print("\nStudent Roll Numbers in Sorted Order:")
inorder(root)