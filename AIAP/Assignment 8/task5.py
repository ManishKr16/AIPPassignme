def convert_date_format(date_str):
    """
    Converts a date string from 'YYYY-MM-DD' to 'DD-MM-YYYY' format.
    
    Args:
        date_str (str): Date string in 'YYYY-MM-DD' format
    Returns:
        str: Date string in 'DD-MM-YYYY' format
    Raises:
        ValueError: If input is not a valid date string
    """
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Date must be in 'YYYY-MM-DD' format")
    year, month, day = parts
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Date must contain only digits and dashes")
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        raise ValueError("Date parts must be in 'YYYY-MM-DD' format")
    return f"{day}-{month}-{year}"

# Test cases
def test_convert_date_format_valid():
    assert convert_date_format("2023-10-15") == "15-10-2023"
    assert convert_date_format("2000-01-01") == "01-01-2000"
    assert convert_date_format("1999-12-31") == "31-12-1999"
    assert convert_date_format("2025-11-11") == "11-11-2025"

def test_convert_date_format_invalid():
    # Invalid format
    try:
        convert_date_format("2023/10/15")
        assert False, "Should raise ValueError for wrong separator"
    except ValueError as e:
        assert str(e) == "Date must be in 'YYYY-MM-DD' format"
    # Not enough parts
    try:
        convert_date_format("2023-10")
        assert False, "Should raise ValueError for missing parts"
    except ValueError as e:
        assert str(e) == "Date must be in 'YYYY-MM-DD' format"
    # Non-digit parts
    try:
        convert_date_format("2023-10-xx")
        assert False, "Should raise ValueError for non-digit day"
    except ValueError as e:
        assert str(e) == "Date must contain only digits and dashes"
    # Wrong length
    try:
        convert_date_format("23-10-15")
        assert False, "Should raise ValueError for year length"
    except ValueError as e:
        assert str(e) == "Date parts must be in 'YYYY-MM-DD' format"
    # Not a string
    try:
        convert_date_format(20231015)
        assert False, "Should raise ValueError for non-string input"
    except ValueError as e:
        assert str(e) == "Input must be a string"

def test_convert_date_format_edge_cases():
    # Empty string
    try:
        convert_date_format("")
        assert False, "Should raise ValueError for empty string"
    except ValueError as e:
        assert str(e) == "Date must be in 'YYYY-MM-DD' format"
    # Extra dashes
    try:
        convert_date_format("2023-10-15-01")
        assert False, "Should raise ValueError for too many parts"
    except ValueError as e:
        assert str(e) == "Date must be in 'YYYY-MM-DD' format"

if __name__ == '__main__':
    print("Welcome to the Date Format Converter!")
    print("-------------------------------------")
    print("Enter a date in 'YYYY-MM-DD' format to convert to 'DD-MM-YYYY'.")
    print("Type 'q' to quit.")
    while True:
        user_input = input("\nEnter date: ").strip()
        if user_input.lower() == 'q':
            print("Thank you for using the converter!")
            break
        try:
            result = convert_date_format(user_input)
            print(f"Converted date: {result}")
        except Exception as e:
            print(f"Error: {str(e)}")
