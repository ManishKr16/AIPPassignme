class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return "Queue: " + str(self.items)


# Interactive part
if __name__ == "__main__":
    q = Queue()
    while True:
        print("\nChoose an operation:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Check if empty")
        print("4. Show queue")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            item = input("Enter item to enqueue: ")
            q.enqueue(item)
            print(f"Enqueued: {item}")

        elif choice == "2":
            item = q.dequeue()
            if item is not None:
                print(f"Dequeued: {item}")

        elif choice == "3":
            print("Queue is empty!" if q.is_empty() else "Queue is not empty.")

        elif choice == "4":
            print(q)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again.")
