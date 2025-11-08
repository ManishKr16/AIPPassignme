# Define a class to manage bank account operations
class BankAccount:
    """
    A class representing a bank account with basic banking operations.
    This class provides fundamental banking features like deposit, withdraw,
    and balance checking while maintaining data security through encapsulation.
    """
    
    def __init__(self, account_holder, initial_balance=0.0):
        """
        Initialize a new bank account.
        
        Args:
            account_holder (str): Name of the account holder
            initial_balance (float): Initial amount in the account (default: 0.0)
            
        Note:
            The balance is stored as a private variable (__balance) to prevent
            direct access from outside the class, ensuring data integrity.
        """
        # Store the account holder's name
        self.account_holder = account_holder
        
        # Initialize the private balance variable
        # Double underscore (__) makes it a private variable in Python
        # This prevents direct access to balance from outside the class
        self.__balance = initial_balance
        
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
        Returns:
            str: Success or error message
        """
        if amount > 0:
            self.__balance += amount
            return f"Successfully deposited ${amount:.2f}"
        return "Invalid deposit amount. Amount must be positive."
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
        Returns:
            str: Success or error message
        """
        if amount <= 0:
            return "Invalid withdrawal amount. Amount must be positive."
        if amount > self.__balance:
            return "Insufficient funds."
        
        self.__balance -= amount
        return f"Successfully withdrew ${amount:.2f}"
    
    def get_balance(self):
        """
        Get the current balance of the account.
        
        Returns:
            float: Current balance
        """
        return self.__balance
    
    def __str__(self):
        """
        String representation of the bank account.
        
        Returns:
            str: Account information
        """
        return f"Account Holder: {self.account_holder}\nCurrent Balance: ${self.__balance:.2f}"


# Test the BankAccount class
def test_bank_account():
    print("Testing BankAccount class:")
    # Create a new account
    account = BankAccount("John Doe", 1000.0)
    print("\nInitial account status:")
    print(account)
    
    # Test deposit
    print("\nTesting deposits:")
    print(account.deposit(500.0))
    print(account.deposit(-50.0))  # Should show error
    
    # Test withdraw
    print("\nTesting withdrawals:")
    print(account.withdraw(200.0))
    print(account.withdraw(2000.0))  # Should show insufficient funds
    print(account.withdraw(-50.0))   # Should show error
    
    # Check final balance
    print("\nFinal account status:")
    print(account)

if __name__ == "__main__":
    test_bank_account()
