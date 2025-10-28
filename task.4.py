
from typing import Optional


# Recursive factorial
def factorial_recursive(n: int) -> int:
	"""Compute n! using recursion.

	Raises ValueError for negative inputs.

	Args:
		n: Non-negative integer whose factorial is required.

	Returns:
		The factorial of n as an int.
	"""
	if n < 0:
		raise ValueError("factorial is not defined for negative integers")
	if n == 0 or n == 1:
		return 1
	return n * factorial_recursive(n - 1)


# Iterative factorial
def factorial_iterative(n: int) -> int:
	"""Compute n! using an iterative loop.

	Raises ValueError for negative inputs.

	Args:
		n: Non-negative integer whose factorial is required.

	Returns:
		The factorial of n as an int.
	"""
	if n < 0:
		raise ValueError("factorial is not defined for negative integers")
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


if __name__ == "__main__":
	# Quick checks for factorial implementations
	cases = {
		0: 1,
		1: 1,
		2: 2,
		3: 6,
		5: 120,
		10: 3628800,
	}

	for n, expected in cases.items():
		r = factorial_recursive(n)
		it = factorial_iterative(n)
		print(f"n={n}: recursive={r}, iterative={it}, expected={expected}")
		assert r == expected, f"recursive failed for {n}: got {r}, expected {expected}"
		assert it == expected, f"iterative failed for {n}: got {it}, expected {expected}"

	# Check negative input raises
	for func in (factorial_recursive, factorial_iterative):
		try:
			func(-1)
		except ValueError:
			print(f"{func.__name__} correctly raised ValueError for -1")
		else:
			raise AssertionError(f"{func.__name__} did not raise for negative input")

	print("All factorial checks passed.")

