
# Function to reverse a string
def reverse_string(s: str) -> str:
	"""Return the reverse of the input string.

	This function accepts a string and returns a new string which is the
	character-wise reversal of the input. It treats the input as a sequence
	of characters and preserves any Unicode characters.

	Args:
		s: The string to reverse.

	Returns:
		A new string which is the reverse of `s`.
	"""
	# Fast, idiomatic Python using slicing
	return s[::-1]


if __name__ == "__main__":
	# Quick checks
	cases = {
		"": "",
		"a": "a",
		"ab": "ba",
		"hello": "olleh",
		"A😊B": "B😊A",
	}

	for inp, expected in cases.items():
		out = reverse_string(inp)
		print(f"reverse_string({inp!r}) -> {out!r} (expected {expected!r})")
		assert out == expected, f"Failed: {inp!r} -> {out!r}, expected {expected!r}"

	print("All reverse_string checks passed.")

