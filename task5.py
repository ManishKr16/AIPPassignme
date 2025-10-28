
from typing import Iterable, Optional, Union

Number = Union[int, float]


# Function to find largest number in a list
def find_max_iterative(seq: Iterable[Number]) -> Optional[Number]:
	"""Return the largest number in seq using an explicit iterative scan.

	This implementation walks the sequence once, keeping the current maximum.
	It returns None for empty sequences. It will raise a TypeError if
	elements are not comparable with each other (e.g., mixing numbers with
	non-numeric data).

	Complexity: O(n) time, O(1) extra space.

	Args:
		seq: An iterable of numbers (ints or floats).

	Returns:
		The largest element, or None if the iterable is empty.
	"""
	it = iter(seq)
	try:
		current_max = next(it)
	except StopIteration:
		return None

	for x in it:
		# rely on Python's comparison semantics; will raise if incompatible
		if x > current_max:
			current_max = x
	return current_max


# Function that uses Python's built-in max (C-optimized)
def find_max_builtin(seq: Iterable[Number]) -> Optional[Number]:
	"""Return the largest element using Python's built-in max().

	This is concise and generally fastest for large lists because max() is
	implemented in C and avoids some Python-level overhead. Returns None for
	empty iterables.

	Complexity: O(n) time, O(1) extra space.
	"""
	try:
		return max(seq)
	except ValueError:
		# raised when seq is empty
		return None


if __name__ == "__main__":
	# Quick tests and demonstrations
	test_cases = [
		([], None),
		([1], 1),
		([1, 3, 2], 3),
		([-5, -1, -10], -1),
		([2.5, 3.1, 3.0], 3.1),
	]

	for seq, expected in test_cases:
		it = find_max_iterative(seq)
		bt = find_max_builtin(seq)
		print(f"seq={seq} -> iterative={it}, builtin={bt}, expected={expected}")
		assert it == expected, f"iterative failed for {seq}: got {it}, expected {expected}"
		assert bt == expected, f"builtin failed for {seq}: got {bt}, expected {expected}"

	# Example showing behavior with mixed types would raise on comparison
	# Uncommenting the following line would raise TypeError in the iterative version
	# print(find_max_iterative([1, "two", 3]))

	print("All find_max checks passed.")

