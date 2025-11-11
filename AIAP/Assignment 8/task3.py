def is_sentence_palindrome(sentence):
    """
    Check if a sentence is a palindrome, ignoring case, spaces, and punctuation.
    
    Args:
        sentence (str): The input sentence to check
        
    Returns:
        bool: True if the sentence is a palindrome, False otherwise
        
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove spaces, punctuation and convert to lowercase
    clean_text = ''.join(char.lower() for char in sentence if char.isalnum())
    
    # Compare the string with its reverse
    return clean_text == clean_text[::-1]

# Test cases
def test_palindrome_classic_examples():
    # Test well-known palindrome sentences
    assert is_sentence_palindrome("A man a plan a canal Panama") == True
    assert is_sentence_palindrome("Race a car") == False
    assert is_sentence_palindrome("Was it a car or a cat I saw?") == True
    assert is_sentence_palindrome("hello world") == False

def test_palindrome_with_punctuation():
    # Test sentences with various punctuation marks
    assert is_sentence_palindrome("Eva, can I see bees in a cave?") == True
    assert is_sentence_palindrome("Mr. Owl ate my metal worm!") == True
    assert is_sentence_palindrome("A Santa lived as a devil at NASA!!!") == True
    assert is_sentence_palindrome("This is, not a palindrome...") == False

def test_palindrome_with_numbers():
    # Test sentences with numbers and mixed characters
    assert is_sentence_palindrome("A1b2c3c2b1a") == True
    assert is_sentence_palindrome("12321") == True
    assert is_sentence_palindrome("A12 321a") == True
    assert is_sentence_palindrome("123 abc") == False

def test_palindrome_special_cases():
    # Test edge cases and special inputs
    assert is_sentence_palindrome("") == True  # Empty string is considered palindrome
    assert is_sentence_palindrome(" ") == True  # Space only
    assert is_sentence_palindrome("a") == True  # Single character
    assert is_sentence_palindrome("aA") == True  # Case insensitive

def test_palindrome_invalid_input():
    # Test invalid input types
    try:
        is_sentence_palindrome(None)
        assert False, "Should raise TypeError for None input"
    except TypeError as e:
        assert str(e) == "Input must be a string"
    
    try:
        is_sentence_palindrome(123)
        assert False, "Should raise TypeError for numeric input"
    except TypeError as e:
        assert str(e) == "Input must be a string"

if __name__ == '__main__':
    print("Welcome to the Palindrome Sentence Checker!")
    print("----------------------------------------")
    print("This program checks if a sentence is a palindrome.")
    print("Rules:")
    print("- Ignores spaces")
    print("- Ignores punctuation")
    print("- Ignores letter case")
    print("Enter 'q' to quit")
    print("----------------------------------------")
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter a sentence to check (or 'q' to quit): ").strip()
            
            # Check if user wants to quit
            if user_input.lower() == 'q':
                print("\nThank you for using the Palindrome Checker!")
                break
            
            # Check if input is empty
            if not user_input:
                print("Error: Input cannot be empty. Please enter a sentence.")
                continue
            
            # Check if the sentence is a palindrome
            result = is_sentence_palindrome(user_input)
            
            # Display result with explanation
            print(f"\nOriginal text: {user_input}")
            clean_text = ''.join(char.lower() for char in user_input if char.isalnum())
            print(f"Processed text: {clean_text}")
            print(f"Reversed text: {clean_text[::-1]}")
            
            if result:
                print("Result: This IS a palindrome! ✓")
            else:
                print("Result: This is NOT a palindrome! ✗")
                
        except TypeError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
