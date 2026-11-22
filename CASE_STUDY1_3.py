class BankQueue:
    def __init__(self):
        self.queue = [None] * 60
        self.front = -1
        self.rear = -1
        self.used_tokens = set()

        # Sample valid tokens issued by the bank
        self.valid_tokens = set(range(1, 101))

    def enqueue(self, token):

        # Check whether token is valid
        if token not in self.valid_tokens:
            print("Invalid Token Number")
            return

        # Check duplicate token
        if token in self.used_tokens:
            print("Duplicate Token Number Not Allowed")
            return

        # Check queue overflow
        if (self.rear + 1) % 60 == self.front:
            print("Queue Overflow! Bank Queue is Full")
            return

        # Insert customer
        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % 60
        self.queue[self.rear] = token

        self.used_tokens.add(token)

        print("Customer Added Successfully")

    def dequeue(self):

        if self.front == -1:
            print("Queue is Empty")
            return

        customer = self.queue[self.front]
        print("Customer Served:", customer)

        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % 60

    def peek(self):

        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Next Customer:", self.queue[self.front])

    def display(self):

        if self.front == -1:
            print("Queue is Empty")
            return

        print("Customer Queue:")

        i = self.front

        while True:
            print(self.queue[i])

            if i == self.rear:
                break

            i = (i + 1) % 60


# Main Program

b = BankQueue()

while True:

    print("\n--- BANK CUSTOMER QUEUE ---")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. View Next Customer")
    print("4. Display Customer Queue")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        token = int(input("Enter Token Number: "))
        b.enqueue(token)

    elif choice == 2:
        b.dequeue()

    elif choice == 3:
        b.peek()

    elif choice == 4:
        b.display()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")