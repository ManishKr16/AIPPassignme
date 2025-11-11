class ShoppingCart:
    """
    A class to manage a shopping cart with items and their prices.
    """
    def __init__(self):
        """Initialize an empty shopping cart"""
        self.items = {}  # Dictionary to store items with their prices

    def add_item(self, name, price):
        """
        Add an item to the shopping cart
        
        Args:
            name (str): The name of the item
            price (float): The price of the item
            
        Raises:
            ValueError: If price is negative or name is empty
            TypeError: If name is not string or price is not a number
        """
        # Validate input types
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
            
        # Validate input values
        if not name.strip():
            raise ValueError("Item name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
            
        # Add or update item in cart
        self.items[name.lower()] = price

    def remove_item(self, name):
        """
        Remove an item from the shopping cart
        
        Args:
            name (str): The name of the item to remove
            
        Raises:
            ValueError: If item is not in cart
            TypeError: If name is not a string
        """
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
            
        name = name.lower()
        if name not in self.items:
            raise ValueError(f"Item '{name}' not found in cart")
            
        del self.items[name]

    def total_cost(self):
        """
        Calculate the total cost of all items in the cart
        
        Returns:
            float: The total cost of all items
        """
        return sum(self.items.values())

# Test cases
def test_add_item_basic():
    cart = ShoppingCart()
    # Test adding single item
    cart.add_item("Apple", 0.50)
    assert cart.items["apple"] == 0.50
    
    # Test adding multiple items
    cart.add_item("Banana", 0.75)
    cart.add_item("Orange", 0.60)
    assert len(cart.items) == 3
    assert cart.items["banana"] == 0.75

def test_add_item_case_insensitive():
    cart = ShoppingCart()
    # Test case insensitivity
    cart.add_item("Apple", 0.50)
    cart.add_item("aPPle", 0.60)  # Should update the price
    assert len(cart.items) == 1
    assert cart.items["apple"] == 0.60

def test_add_item_invalid_input():
    cart = ShoppingCart()
    
    # Test invalid price types
    try:
        cart.add_item("Apple", "0.50")
        assert False, "Should raise TypeError for string price"
    except TypeError as e:
        assert str(e) == "Price must be a number"
    
    # Test invalid name types
    try:
        cart.add_item(123, 0.50)
        assert False, "Should raise TypeError for numeric name"
    except TypeError as e:
        assert str(e) == "Item name must be a string"
    
    # Test empty name
    try:
        cart.add_item("", 0.50)
        assert False, "Should raise ValueError for empty name"
    except ValueError as e:
        assert str(e) == "Item name cannot be empty"
    
    # Test negative price
    try:
        cart.add_item("Apple", -0.50)
        assert False, "Should raise ValueError for negative price"
    except ValueError as e:
        assert str(e) == "Price cannot be negative"

def test_remove_item():
    cart = ShoppingCart()
    # Add and remove item
    cart.add_item("Apple", 0.50)
    cart.remove_item("Apple")
    assert len(cart.items) == 0
    
    # Test case insensitivity in removal
    cart.add_item("Banana", 0.75)
    cart.remove_item("BANANA")
    assert len(cart.items) == 0
    
    # Test removing non-existent item
    try:
        cart.remove_item("Orange")
        assert False, "Should raise ValueError for non-existent item"
    except ValueError as e:
        assert str(e) == "Item 'orange' not found in cart"

def test_total_cost():
    cart = ShoppingCart()
    # Test empty cart
    assert cart.total_cost() == 0
    
    # Test with one item
    cart.add_item("Apple", 0.50)
    assert cart.total_cost() == 0.50
    
    # Test with multiple items
    cart.add_item("Banana", 0.75)
    cart.add_item("Orange", 0.60)
    assert cart.total_cost() == 1.85
    
    # Test after removing item
    cart.remove_item("Apple")
    assert cart.total_cost() == 1.35

if __name__ == '__main__':
    print("Welcome to the Shopping Cart System!")
    print("-----------------------------------")
    print("Available commands:")
    print("1. add item_name price")
    print("2. remove item_name")
    print("3. total")
    print("4. quit")
    print("-----------------------------------")
    
    cart = ShoppingCart()
    
    while True:
        try:
            command = input("\nEnter command: ").strip().lower()
            
            if command == 'quit':
                print("\nThank you for using the Shopping Cart System!")
                break
                
            elif command == 'total':
                total = cart.total_cost()
                print(f"Total cost: ${total:.2f}")
                
            elif command.startswith('add '):
                # Parse add command: "add item_name price"
                parts = command.split()
                if len(parts) < 3:
                    print("Error: Please provide both item name and price")
                    continue
                    
                name = ' '.join(parts[1:-1])  # Join multi-word item names
                price = float(parts[-1])
                cart.add_item(name, price)
                print(f"Added '{name}' at ${price:.2f}")
                
            elif command.startswith('remove '):
                # Parse remove command: "remove item_name"
                name = command[7:].strip()
                cart.remove_item(name)
                print(f"Removed '{name}' from cart")
                
            else:
                print("Invalid command. Please try again.")
                
        except ValueError as e:
            print(f"Error: {str(e)}")
        except TypeError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
