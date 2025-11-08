"""
fib_recursive.py
A simple, well-documented recursive Fibonacci implementation for demonstration and testing.

Usage:
    python fib_recursive.py
    # or import fib from this module and call fib(n)

Notes:
- This recursive implementation is intentionally simple to show recursion and base cases.
- It's not efficient for large n; see the explanation document for improvements.
"""
from typing import Union


def fib(n: int) -> int:
    """Return the n-th Fibonacci number using simple recursion.

    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n >= 2

    Args:
        n: Non-negative integer index into the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number as an integer.

    Raises:
        ValueError: If n is not an integer or is negative.

    Complexity:
        Time: O(2^n) (exponential) — many overlapping subproblems.
        Space: O(n) recursion depth (call stack).
    """
    # Input validation: ensure an integer non-negative n
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases
    if n == 0:
        # F(0) = 0
        return 0
    if n == 1:
        # F(1) = 1
        return 1

    # Recursive step: F(n) = F(n-1) + F(n-2)
    # Note: This will recompute the same values many times for larger n.
    return fib(n - 1) + fib(n - 2)


def _run_smoke_tests():
    """Run a few smoke tests to verify correctness for small n."""
    test_values = list(range(0, 11))  # 0..10
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    all_ok = True

    for tv, exp in zip(test_values, expected):
        got = fib(tv)
        print(f"fib({tv}) = {got} (expected {exp})")
        if got != exp:
            all_ok = False

    if all_ok:
        print("All smoke tests passed.")
    else:
        print("One or more smoke tests failed.")


if __name__ == "__main__":
    # When run as a script, execute smoke tests and show a short example
    print("Running smoke tests for recursive Fibonacci implementation...")
    _run_smoke_tests()
    print("\nExample: fib(20) (may be slow because recursion is exponential)...")
    try:
        print("fib(20) =", fib(20))
    except RecursionError:
        print("Recursion depth exceeded for fib(20).")
