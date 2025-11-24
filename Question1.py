def generate_fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def prompt_positive_integer(message: str) -> int:
    """Prompt until user supplies a positive integer."""
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive integer.")


def main() -> None:
    n = prompt_positive_integer("Enter how many Fibonacci numbers to print: ")

    sequence = generate_fibonacci(n)
    print("Fibonacci sequence:", sequence)


if __name__ == "__main__":
    main()

