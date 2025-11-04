"""Vowel counting utility.

Provides `count_vowels(s: str) -> int` which counts the letters a,e,i,o,u
(case-insensitive) in the input string. Non-letter characters are ignored.
"""

def count_vowels(s: str) -> int:
	"""Return the number of vowels (a,e,i,o,u) in `s` (case-insensitive).

	Parameters
	----------
	s : str
		Input string. If `s` is not a string, a TypeError is raised.

	Returns
	-------
	int
		Count of vowels in `s`.
	"""
	if not isinstance(s, str):
		raise TypeError("s must be a string")
	return sum(1 for ch in s.lower() if ch in "aeiou")


def _quick_tests():
	assert count_vowels("hello") == 2
	assert count_vowels("AEIoU") == 5
	assert count_vowels("123, hi!") == 1
	assert count_vowels("") == 0


if __name__ == "__main__":
	_quick_tests()
	print("All quick tests passed for count_vowels().")
	samples = ["hello", "AEIoU", "123, hi!", "", "rhythm"]
	for s in samples:
		print(f"{s!r} -> {count_vowels(s)}")

