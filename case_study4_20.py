class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# User-defined Stack
class Stack:
    def __init__(self):
        self.st = []

    def push(self, data):
        self.st.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.st.pop()

    def is_empty(self):
        return len(self.st) == 0


# Insert into BST
def insert(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Recursive Inorder (Left, Root, Right)
def inorder(root, result):

    if root is not None:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)


# Recursive Preorder (Root, Left, Right)
def preorder(root, result):

    if root is not None:
        result.append(root.data)
        preorder(root.left, result)
        preorder(root.right, result)


# Recursive Postorder (Left, Right, Root)
def postorder(root, result):

    if root is not None:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.data)


# Non-Recursive Inorder
def inorder_nonrecursive(root):

    s = Stack()
    result = []
    current = root

    while current is not None or not s.is_empty():

        while current is not None:
            s.push(current)
            current = current.left

        current = s.pop()
        result.append(current.data)

        current = current.right

    return result


# Non-Recursive Preorder
def preorder_nonrecursive(root):

    s = Stack()
    result = []

    if root is None:
        return result

    s.push(root)

    while not s.is_empty():

        current = s.pop()
        result.append(current.data)

        if current.right is not None:
            s.push(current.right)

        if current.left is not None:
            s.push(current.left)

    return result


# Non-Recursive Postorder
def postorder_nonrecursive(root):

    s1 = Stack()
    s2 = Stack()
    result = []

    if root is None:
        return result

    s1.push(root)

    while not s1.is_empty():

        current = s1.pop()
        s2.push(current)

        if current.left is not None:
            s1.push(current.left)

        if current.right is not None:
            s1.push(current.right)

    while not s2.is_empty():
        current = s2.pop()
        result.append(current.data)

    return result


# Main Program
root = None

print("Enter Student Roll Numbers (0 to stop):")

while True:

    num = int(input("Enter Roll Number: "))

    if num == 0:
        break

    root = insert(root, num)


# Recursive Traversals
in_result = []
pre_result = []
post_result = []

inorder(root, in_result)
preorder(root, pre_result)
postorder(root, post_result)


# Non-Recursive Traversals
in_nr = inorder_nonrecursive(root)
pre_nr = preorder_nonrecursive(root)
post_nr = postorder_nonrecursive(root)


# Display Results
print("\n----- RECURSIVE TRAVERSALS -----")

print("Inorder:", in_result)
print("Preorder:", pre_result)
print("Postorder:", post_result)


print("\n----- NON-RECURSIVE TRAVERSALS -----")

print("Inorder:", in_nr)
print("Preorder:", pre_nr)
print("Postorder:", post_nr)


# Verify Results
print("\n----- VERIFICATION -----")

print("Inorder Match:", in_result == in_nr)
print("Preorder Match:", pre_result == pre_nr)
print("Postorder Match:", post_result == post_nr)