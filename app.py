"""A small calculator application for the CMSC 426 CI assignment."""


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract_numbers(a, b):
    """Return the difference between two numbers."""
    return a - b


if __name__ == "__main__":
    print("Application started")
    print("2 + 3 =", add_numbers(2, 3))
