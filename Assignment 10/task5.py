def divide_numbers(a, b):
    """
    Safely divides two numbers and handles division errors.

    Args:
        a (float or int): Numerator.
        b (float or int): Denominator.

    Returns:
        float: Result of the division if valid.
        str: Error message when division by zero occurs.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


print(divide_numbers(10, 0))
