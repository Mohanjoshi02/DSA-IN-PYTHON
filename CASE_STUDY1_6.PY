class SupermarketQueue:

    def __init__(self):
        self.queue = [None] * 40
        self.front = -1
        self.rear = -1
        self.customer_ids = set()

    # Add Customer (Enqueue)
    def enqueue(self, cid, has_cart):

        # Check shopping cart
        if has_cart.lower() != "yes":
            print("Customer must have a shopping cart!")
            return

        # Check duplicate Customer ID
        if cid in self.customer_ids:
            print("Duplicate Customer ID Not Allowed!")
            return

        # Check Queue Overflow
        if (self.rear + 1) % 40 == self.front:
            print("Queue Overflow! No New Customer Allowed.")
            return

        # Insert Customer
        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % 40
        self.queue[self.rear] = cid

        self.customer_ids.add(cid)

        print("Customer Added Successfully!")


    # Bill Customer (Dequeue)
    def dequeue(self):

        if self.front == -1:
            print("Queue is Empty!")
            return

        cid = self.queue[self.front]

        print("Bill Completed for Customer:", cid)

        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % 40


    # View Next Customer (Peek)
    def peek(self):

        if self.front == -1:
            print("Queue is Empty!")
        else:
            print("Next Customer:", self.queue[self.front])


    # Display Queue
    def display(self):

        if self.front == -1:
            print("Queue is Empty!")
            return

        print("Supermarket Billing Queue:")

        i = self.front

        while True:

            print(self.queue[i])

            if i == self.rear:
                break

            i = (i + 1) % 40


# Main Program

s = SupermarketQueue()

while True:

    print("\n--- SUPERMARKET BILLING QUEUE ---")
    print("1. Add Customer")
    print("2. Bill Customer")
    print("3. View Next Customer")
    print("4. Display Billing Queue")
    print("5. Exit")

    ch = int(input("Enter Your Choice: "))

    if ch == 1:

        cid = int(input("Enter Customer ID: "))
        cart = input("Do you have a shopping cart? (yes/no): ")

        s.enqueue(cid, cart)

    elif ch == 2:
        s.dequeue()

    elif ch == 3:
        s.peek()

    elif ch == 4:
        s.display()

    elif ch == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")