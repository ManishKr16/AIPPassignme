"""
Manual module docstring (NumPy style)
-----------------------------------

A small calculator module that provides four basic arithmetic functions:
`add`, `subtract`, `multiply`, and `divide`.

This module demonstrates structured documentation using the NumPy docstring
style and includes a set of AI-generated docstrings for comparison.

Notes
-----
The AI-generated docstrings are included as separate *_ai functions and
as the variable `ai_module_docstring` so students can compare style,
clarity, and content.
"""

# AI-generated module docstring (simulated)
ai_module_docstring = """
AI-generated module docstring (simulated)
---------------------------------------

Provides basic calculator functions (add, subtract, multiply, divide).
Each function accepts two numeric inputs and returns the arithmetic result.

The AI docstrings focus on succinct explanation and example usage. They are
more narrative and less strictly formatted compared to the manual NumPy
style docstring at the top of this file.
"""

# Manual NumPy-style function docstrings and implementations

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        First addend.
    b : float
        Second addend.

    Returns
    -------
    float
        The sum of ``a`` and ``b``.

    Examples
    --------
    >>> add(1, 2)
    3
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : float
        Minuend (value to subtract from).
    b : float
        Subtrahend (value to subtract).

    Returns
    -------
    float
        The difference ``a - b``.

    Examples
    --------
    >>> subtract(5, 3)
    2
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        First factor.
    b : float
        Second factor.

    Returns
    -------
    float
        The product ``a * b``.

    Examples
    --------
    >>> multiply(2, 3)
    6
    """
    return a * b


def divide(a, b):
    """
    Divide one number by another.

    Parameters
    ----------
    a : float
        Numerator.
    b : float
        Denominator.

    Returns
    -------
    float
        The quotient ``a / b``.

    Raises
    ------
    ValueError
        If ``b`` is zero.

    Examples
    --------
    >>> divide(6, 2)
    3.0
    """
    if b == 0:
        raise ValueError("Denominator 'b' cannot be zero.")
    return a / b


# AI-generated versions (simulated) with AI-style docstrings

def add_ai(a, b):
    """
    Adds two numeric values and returns the result.

    This function takes two inputs, adds them, and returns the sum. Works
    with ints and floats.

    Parameters
    ----------
    a, b : numbers
        Operands to add.

    Returns
    -------
    number
        Sum of the inputs.

    Example
    -------
    >>> add_ai(1, 2)
    3
    """
    return a + b


def subtract_ai(a, b):
    """
    Subtracts the second value from the first and returns the difference.

    The function performs a straightforward subtraction and returns the
    numeric result.
    """
    return a - b


def multiply_ai(a, b):
    """
    Multiplies two numbers and returns the product.
    """
    return a * b


def divide_ai(a, b):
    """
    Divides a by b and returns the quotient. Raises an error on division
    by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Comparison helper

def compare_docstrings(func_manual, func_ai):
    """
    Compare two functions' docstrings and print a short summary.

    Parameters
    ----------
    func_manual : callable
        Function object with manual (NumPy-style) docstring.
    func_ai : callable
        Function object with AI-generated docstring.
    """
    dm = func_manual.__doc__ or "(no docstring)"
    da = func_ai.__doc__ or "(no docstring)"
    print("\n" + "-"*60)
    print(f"Comparing docstrings for: {func_manual.__name__} vs {func_ai.__name__}")
    print("-"*60)
    print("MANUAL (NumPy-style):")
    print(dm.strip())
    print("\nAI-GENERATED (simulated):")
    print(da.strip())
    # Very small automated comment-level comparison
    print("\nQuick differences:")
    len_dm = len(dm)
    len_da = len(da)
    print(f"  - Manual docstring length: {len_dm} characters")
    print(f"  - AI docstring length:     {len_da} characters")
    print("  - Manual tends to be more structured (sections).\n  - AI tends to be more narrative/concise.")


# Basic tests and demonstration
if __name__ == "__main__":
    # Interactive CLI: get two numbers and an operation from the user
    def get_number(prompt):
        """Prompt repeatedly until the user enters a valid number or quits.

        Parameters
        ----------
        prompt : str
            Text shown to the user when asking for input.

        Returns
        -------
        float
            The user-provided numeric value.

        Raises
        ------
        SystemExit
            If the user types 'q' or 'quit' to exit the program.
        """
        while True:
            s = input(prompt).strip()
            if s.lower() in ("q", "quit", "exit"):
                print("Exiting interactive calculator.")
                raise SystemExit
            try:
                return float(s)
            except ValueError:
                print("Invalid number. Please enter a valid numeric value or 'q' to quit.")

    ops = {
        '+': (add, add_ai),
        '-': (subtract, subtract_ai),
        '*': (multiply, multiply_ai),
        '/': (divide, divide_ai),
    }

    print("Interactive calculator (type 'q' at any prompt to quit).")
    try:
        while True:
            a = get_number("Enter first number: ")
            b = get_number("Enter second number: ")

            op = input("Choose operation (+, -, *, /) or type 'doc' to compare docstrings: ").strip()
            if op.lower() in ("doc", "compare"):
                # Show module-level comparison and function docstring comparisons
                print("\nModule-level docstring comparison:")
                print("Manual module docstring (first 200 chars):")
                print((__doc__ or "").strip()[:200])
                print("\nAI-generated module docstring (simulated, first 200 chars):")
                print(ai_module_docstring.strip()[:200])
                compare_docstrings(add, add_ai)
                compare_docstrings(subtract, subtract_ai)
                compare_docstrings(multiply, multiply_ai)
                compare_docstrings(divide, divide_ai)
                continue

            if op not in ops:
                print("Invalid operation. Choose one of +, -, *, / or 'doc'.")
                continue

            func_manual, func_ai = ops[op]
            try:
                result_manual = func_manual(a, b)
            except Exception as e:
                result_manual = f"Error: {e}"
            try:
                result_ai = func_ai(a, b)
            except Exception as e:
                result_ai = f"Error: {e}"

            print("\nResults:")
            print(f"  Manual implementation ({func_manual.__name__}): {result_manual}")
            print(f"  AI implementation     ({func_ai.__name__}): {result_ai}\n")

            # Ask whether to continue
            cont = input("Perform another operation? (y/n): ").strip().lower()
            if cont not in ('y', 'yes'):
                print("Goodbye.")
                break
    except SystemExit:
        pass
