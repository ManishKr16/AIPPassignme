class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        elif key > root.key:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)
        # Ignore duplicates

    def search(self, key):
        """Search for a key in the BST."""
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def delete(self, key):
        """Delete a key from the BST."""
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # Node with one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: find inorder successor
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.key, end=" ")
            self._inorder(root.right)

    def preorder_traversal(self):
        self._preorder(self.root)
        print()

    def _preorder(self, root):
        if root:
            print(root.key, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    def postorder_traversal(self):
        self._postorder(self.root)
        print()

    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print(root.key, end=" ")

if __name__ == "__main__":
    bst = BST()

    while True:
        print("\nChoose an operation:")
        print("1. Insert a value")
        print("2. Search a value")
        print("3. Delete a value")
        print("4. Inorder Traversal")
        print("5. Preorder Traversal")
        print("6. Postorder Traversal")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == "1":
            val = int(input("Enter value to insert: "))
            bst.insert(val)
            print(f"Inserted {val} into BST.")

        elif choice == "2":
            val = int(input("Enter value to search: "))
            node = bst.search(val)
            if node:
                print(f"Value {val} found in BST.")
            else:
                print(f"Value {val} not found.")

        elif choice == "3":
            val = int(input("Enter value to delete: "))
            bst.delete(val)
            print(f"Deleted {val} from BST (if it existed).")

        elif choice == "4":
            print("Inorder Traversal:")
            bst.inorder_traversal()

        elif choice == "5":
            print("Preorder Traversal:")
            bst.preorder_traversal()

        elif choice == "6":
            print("Postorder Traversal:")
            bst.postorder_traversal()

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again.")
