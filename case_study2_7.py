class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class BrowserHistory:
    def __init__(self):
        self.head = None

    # Insert website
    def insert(self, data):
        n = Node(data)

        if self.head is None:
            self.head = n
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = n

    # Display history
    def display(self):
        if self.head is None:
            print("History is Empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Delete specific website
    def delete(self, key):

        if self.head is None:
            print("History is Empty")
            return

        # If first node is to be deleted
        if self.head.data == key:
            self.head = self.head.next
            return

        prev = None
        temp = self.head

        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Website Not Found")
            return

        prev.next = temp.next

        print("Deleted Website:", key)


# Main Program

b = BrowserHistory()

b.insert("Google")
b.insert("YouTube")
b.insert("Gmail")
b.insert("ChatGPT")

print("Original Browser History:")
b.display()

print("\nDeleting YouTube:")
b.delete("YouTube")

print("\nUpdated Browser History:")
b.display()