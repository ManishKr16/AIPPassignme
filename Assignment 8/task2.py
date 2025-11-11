def assign_grade(score):
    """
    Assigns a letter grade based on the numerical score.
    
    Args:
        score: A numerical value representing the student's score
        
    Returns:
        str: Letter grade ('A', 'B', 'C', 'D', or 'F')
        
    Raises:
        ValueError: If score is not a valid number between 0 and 100
    """
    if not isinstance(score, (int, float)):
        raise ValueError("Score must be a number")
    
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Test cases
def test_assign_grade_boundaries():
    # Test upper boundaries
    assert assign_grade(100) == 'A'  # Maximum score
    assert assign_grade(90) == 'A'   # Minimum A
    assert assign_grade(89.9) == 'B' # Just below A
    assert assign_grade(80) == 'B'   # Minimum B
    assert assign_grade(79.9) == 'C' # Just below B
    assert assign_grade(70) == 'C'   # Minimum C
    assert assign_grade(69.9) == 'D' # Just below C
    assert assign_grade(60) == 'D'   # Minimum D
    assert assign_grade(59.9) == 'F' # Just below D

def test_assign_grade_mid_range():
    # Test middle of each grade range
    assert assign_grade(95) == 'A'
    assert assign_grade(85) == 'B'
    assert assign_grade(75) == 'C'
    assert assign_grade(65) == 'D'
    assert assign_grade(30) == 'F'

def test_assign_grade_invalid_numeric():
    # Test out of range values
    try:
        assign_grade(-5)
        assert False, "Should raise ValueError for negative numbers"
    except ValueError as e:
        assert str(e) == "Score must be between 0 and 100"
    
    try:
        assign_grade(105)
        assert False, "Should raise ValueError for numbers over 100"
    except ValueError as e:
        assert str(e) == "Score must be between 0 and 100"

def test_assign_grade_invalid_types():
    # Test invalid input types
    invalid_inputs = ["eighty", None, [], {}]
    for invalid_input in invalid_inputs:
        try:
            assign_grade(invalid_input)
            assert False, f"Should raise ValueError for input: {invalid_input}"
        except ValueError as e:
            assert str(e) == "Score must be a number"

if __name__ == '__main__':
    print("Welcome to the Grade Calculator!")
    print("--------------------------------")
    print("Valid inputs: Numbers between 0 and 100")
    print("Examples of invalid inputs that will be caught:")
    print("- Negative numbers (e.g., -5)")
    print("- Numbers above 100 (e.g., 105)")
    print("- Text inputs (e.g., 'eighty')")
    print("- Special characters")
    print("Enter 'q' to quit the program")
    print("--------------------------------")

    while True:
        try:
            # Get user input
            user_input = input("\nEnter a score (0-100) or 'q' to quit: ").strip()
            
            # Check if user wants to quit
            if user_input.lower() == 'q':
                print("\nThank you for using the grade calculator!")
                break
            
            # Check if input is empty
            if not user_input:
                print("Error: Input cannot be empty. Please enter a number between 0 and 100.")
                continue
                
            # Check if input contains alphabets (except 'q')
            if any(c.isalpha() for c in user_input):
                print("Error: Text input is not allowed. Please enter a number between 0 and 100.")
                print("Example: Enter '80' instead of 'eighty'")
                continue
            
            # Convert input to float and get grade
            score = float(user_input)
            grade = assign_grade(score)
            print(f"\nScore: {score}")
            print(f"Grade: {grade}")
            
            # Provide additional feedback for boundary cases
            if score == 100:
                print("Perfect score!")
            elif score == 0:
                print("Minimum possible score.")
            elif score in [90, 80, 70, 60]:
                print("This is a grade boundary score!")
            
        except ValueError as e:
            if "must be between 0 and 100" in str(e):
                print(f"Error: {str(e)}")
                print("Please enter a number within the valid range (0-100)")
            else:
                print("Error: Invalid input. Please enter a valid number.")
                print("Examples of valid inputs: 75, 82.5, 90")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
