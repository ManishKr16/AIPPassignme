"""Count lines in a text file and self-test with sample files.

This script implements `count_lines_in_file(path)` and, when run as
__main__, creates three sample files (`example.txt`, `empty.txt`,
`trailing.txt`), runs asserts, and prints results.
"""

from pathlib import Path


def count_lines_in_file(path: str) -> int:
    """Return the number of lines in the text file at `path`.

    Parameters
    ----------
    path : str
        Path to the text file. If `path` is not a str, raise TypeError.

    Returns
    -------
    int
        Number of lines in the file.
    """
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    p = Path(path)
    # Open in text mode and count lines efficiently without loading entire file
    with p.open("r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def _write_sample_files(base_dir: Path):
    example = base_dir / "example.txt"
    empty = base_dir / "empty.txt"
    trailing = base_dir / "trailing.txt"

    example.write_text("line1\nline2\nline3\n", encoding="utf-8")
    empty.write_text("", encoding="utf-8")
    # trailing.txt: two lines, ends with a newline after second line
    trailing.write_text("a\nb\n", encoding="utf-8")


def _quick_tests(base_dir: Path):
    # Use filenames relative to base_dir
    assert count_lines_in_file(str(base_dir / "example.txt")) == 3
    assert count_lines_in_file(str(base_dir / "empty.txt")) == 0
    assert count_lines_in_file(str(base_dir / "trailing.txt")) == 2


if __name__ == "__main__":
    base = Path(__file__).resolve().parent
    _write_sample_files(base)
    _quick_tests(base)
    print("All quick tests passed for count_lines_in_file().")
    for name in ("example.txt", "empty.txt", "trailing.txt"):
        path = base / name
        print(f"{name}: {count_lines_in_file(str(path))} lines")
