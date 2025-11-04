"""Name formatter: format full names as "Last, First".

This module implements `format_name(full_name: str) -> str` using the
simple rule: the last whitespace-separated token is the last name; all
preceding tokens are treated as the first name (preserving their order).

Behavior:
- Strip leading/trailing whitespace.
- If input is not a string, raise TypeError.
- If the name contains only one token, return it unchanged.
"""

def format_name(full_name: str) -> str:
    """Format `full_name` as "Last, First".

    Examples
    --------
    >>> format_name('John Doe')
    'Doe, John'

    >>> format_name('Mary Ann Smith')
    'Smith, Mary Ann'
    """
    if not isinstance(full_name, str):
        raise TypeError("full_name must be a string")
    name = full_name.strip()
    if not name:
        return name  # empty string stays empty
    parts = name.split()
    if len(parts) == 1:
        return parts[0]
    last = parts[-1]
    first = " ".join(parts[:-1])
    return f"{last}, {first}"


def _quick_tests():
    # Basic checks
    assert format_name("John Doe") == "Doe, John"
    assert format_name("Mary Ann Smith") == "Smith, Mary Ann"
    assert format_name("  SingleName  ") == "SingleName"
    # trimming and multi-part first names
    assert format_name("  Juan Martín del Potro  ") == "Potro, Juan Martín del"


if __name__ == "__main__":
    _quick_tests()
    print("All quick tests passed for format_name().")
    samples = [
        "John Doe",
        "Mary Ann Smith",
        "  SingleName  ",
        "  Juan Martín del Potro  ",
    ]
    for s in samples:
        print(f"{s!r} -> {format_name(s)!r}")
