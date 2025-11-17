class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        """Delete the first occurrence of a node with given data."""
        temp = self.head

        # If head node itself holds the key
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key
        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        # If key not found
        if temp is None:
            print(f"Value {key} not found in list.")
            return

        # Unlink the node
        prev.next = temp.next
        temp = None

    def display(self):
        """Display the linked list."""
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Interactive menu
if __name__ == "__main__":
    sll = SinglyLinkedList()

    while True:
        print("\nChoose an operation:")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Delete a node")
        print("4. Display list")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            val = input("Enter value to insert at beginning: ")
            sll.insert_at_beginning(val)
            print(f"Inserted {val} at beginning.")

        elif choice == "2":
            val = input("Enter value to insert at end: ")
            sll.insert_at_end(val)
            print(f"Inserted {val} at end.")

        elif choice == "3":
            val = input("Enter value to delete: ")
            sll.delete_node(val)

        elif choice == "4":
            print("Linked List contents:")
            sll.display()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again.")
