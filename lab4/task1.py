"""Leap year checker.

This module provides a single function `is_leap_year(year)` which returns
True when `year` is a leap year in the Gregorian calendar.
"""

def is_leap_year(year):
	"""Return True if `year` is a leap year (Gregorian rules).

	Rules:
	- divisible by 4 -> leap year
	- divisible by 100 -> not a leap year, unless also divisible by 400

	Parameters
	----------
	year : int
		Year number (must be integer >= 1)

	Returns
	-------
	bool
		True if `year` is a leap year, False otherwise.

	Raises
	------
	TypeError
		If `year` is not an int.
	ValueError
		If `year` is less than 1.

	One-line explanation: divisible by 4 but years divisible by 100 are
	excluded unless divisible by 400.
	"""
	if not isinstance(year, int):
		raise TypeError("year must be an integer")
	if year < 1:
		raise ValueError("year must be >= 1")
	return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


def _quick_self_test():
	# Minimal unit-like checks (happy path + edge cases)
	assert is_leap_year(2000) is True   # divisible by 400
	assert is_leap_year(1900) is False  # divisible by 100 but not 400
	assert is_leap_year(2024) is True   # divisible by 4
	assert is_leap_year(2023) is False  # not divisible by 4


if __name__ == "__main__":
	# Run quick tests and show a small interactive demo
	_quick_self_test()
	print("All quick tests passed.")
	# simple demo
	for y in (1999, 2000, 2004, 1900, 2100, 2400):
		print(f"{y}: {is_leap_year(y)}")

