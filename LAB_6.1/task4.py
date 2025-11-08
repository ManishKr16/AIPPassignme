def sum_to_n(n):
    """
    Calculate the sum of first n natural numbers.
    
    Args:
        n (int): A positive integer
    Returns:
        int: Sum of first n natural numbers
    """
    if n < 0:
        return "Please enter a positive number"
    
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Test the function
def test_sum_to_n():
    print("Testing sum_to_n function:")
    print(f"Sum of first 5 numbers: {sum_to_n(5)}")  # Should be 15
    print(f"Sum of first 10 numbers: {sum_to_n(10)}")  # Should be 55
    print(f"Testing negative input: {sum_to_n(-1)}")  # Should handle negative input

if __name__ == "__main__":
    test_sum_to_n()
