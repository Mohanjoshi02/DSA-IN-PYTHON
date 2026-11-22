class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class EmployeeList:
    def __init__(self):
        self.head = None

    # Insert employee at end
    def insert(self, data):
        n = Node(data)

        if self.head is None:
            self.head = n
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = n

    # Display employee list
    def display(self):
        if self.head is None:
            print("Employee List is Empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Delete employee from beginning
    def delete_first(self):
        if self.head is None:
            print("List is Empty")
            return

        print("Deleted Employee:", self.head.data)

        self.head = self.head.next


# Main Program

e = EmployeeList()

e.insert("E201")
e.insert("E202")
e.insert("E203")
e.insert("E204")
e.insert("E205")

print("Original Employee List:")
e.display()

print("\nDeleting Head Node:")
e.delete_first()

print("\nUpdated Employee List:")
e.display()