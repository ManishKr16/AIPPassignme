class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty! Nothing to peek.")
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


# Interactive menu
if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Size of stack")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            value = input("Enter value to push: ")
            stack.push(value)
            print(f"Pushed {value} onto stack.")

        elif choice == "2":
            popped = stack.pop()
            if popped is not None:
                print(f"Popped: {popped}")

        elif choice == "3":
            top = stack.peek()
            if top is not None:
                print(f"Top element: {top}")

        elif choice == "4":
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")

        elif choice == "5":
            print(f"Stack size: {len(stack)}")

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")
