import hashlib
import secrets
import sqlite3
from getpass import getpass

class LoginSystem:
    def __init__(self):
        # Initialize database
        self.conn = sqlite3.connect('users.db')
        self.create_users_table()
    
    def create_users_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL
            )
        ''')
        self.conn.commit()
    
    def hash_password(self, password: str, salt: str = None) -> tuple:
        if salt is None:
            # Generate a random salt for new passwords
            salt = secrets.token_hex(16)
        # Combine password with salt and hash
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return password_hash, salt
    
    def register(self, username: str, password: str) -> bool:
        try:
            cursor = self.conn.cursor()
            # Check if username already exists
            cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
            if cursor.fetchone():
                print("Username already exists!")
                return False
            
            # Hash password with salt
            password_hash, salt = self.hash_password(password)
            
            # Store user credentials
            cursor.execute(
                'INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)',
                (username, password_hash, salt)
            )
            self.conn.commit()
            print("Registration successful!")
            return True
        except Exception as e:
            print(f"Registration failed: {e}")
            return False
    
    def login(self, username: str, password: str) -> bool:
        try:
            cursor = self.conn.cursor()
            # Get user's stored credentials
            cursor.execute(
                'SELECT password_hash, salt FROM users WHERE username = ?',
                (username,)
            )
            result = cursor.fetchone()
            
            if not result:
                print("Invalid username or password!")
                return False
            
            stored_hash, salt = result
            # Hash the provided password with stored salt
            password_hash, _ = self.hash_password(password, salt)
            
            if password_hash == stored_hash:
                print("Login successful!")
                return True
            else:
                print("Invalid username or password!")
                return False
        except Exception as e:
            print(f"Login failed: {e}")
            return False
    
    def __del__(self):
        self.conn.close()

def main():
    login_system = LoginSystem()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = getpass("Enter password: ")  # getpass hides the password input
            login_system.register(username, password)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            login_system.login(username, password)
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()