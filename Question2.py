class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty. Cannot dequeue."
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty. Nothing to peek."
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# -----------------------
# USER INPUT MENU SYSTEM
# -----------------------

q = Queue()

while True:
    print("\n---- Queue Operations ----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Size")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        value = input("Enter value to enqueue: ")
        q.enqueue(value)
        print("Enqueued:", value)

    elif choice == "2":
        print("Dequeue result:", q.dequeue())

    elif choice == "3":
        print("Peek:", q.peek())

    elif choice == "4":
        print("Queue size:", q.size())

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select between 1-5.")
