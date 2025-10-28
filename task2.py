from typing import Any


def is_prime(n: int) -> bool:
	"""Return True if n is a prime number, otherwise False.

	Implementation details:
	- Handles negative numbers, 0 and 1 (these are not prime).
	- Checks small primes directly (2 and 3).
	- Eliminates multiples of 2 and 3 early.
	- Uses 6k +/- 1 optimization for trial division up to sqrt(n).

	Args:
		n: Integer to test for primality.

	Returns:
		True if `n` is prime, False otherwise.
	"""
	if n <= 1:
		return False
	if n <= 3:
		return True
	# Eliminate even numbers and multiples of 3
	if n % 2 == 0:
		return False
	if n % 3 == 0:
		return False

	i = 5
	# Test divisors of form 6k-1 and 6k+1
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True


if __name__ == "__main__":
	# Quick self-checks (happy path + edge cases)
	_tests = {
		-1: False,
		0: False,
		1: False,
		2: True,
		3: True,
		4: False,
		17: True,
		18: False,
		19: True,
		7919: True,  # known prime
	}

	for k, expected in _tests.items():
		result = is_prime(k)
		print(f"is_prime({k}) => {result} (expected {expected})")
		assert result == expected, f"Failed for {k}: got {result}, expected {expected}"

	print("All checks passed for is_prime().")
