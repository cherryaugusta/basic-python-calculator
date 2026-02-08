"""
Basic Python Calculator

Features:
- Object-oriented design
- Clear separation of logic and UI
- Safe exception-based error handling
- Designed for automated unit testing
"""

from typing import Union

Number = Union[int, float]


class Calculator:
    """
    Stateless calculator providing basic arithmetic operations.
    """

    def add(self, a: Number, b: Number) -> Number:
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        return a * b

    def divide(self, a: Number, b: Number) -> Number:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b


def _read_number(prompt: str) -> Number:
    """
    Reads a numeric value from user input with validation.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def _print_menu() -> None:
    """
    Displays the calculator menu.
    """
    print("\nChoose an operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("0 - Restart")
    print("Any other key - Exit")


def run_calculator() -> None:
    """
    Runs the interactive calculator loop.
    """
    calculator = Calculator()

    while True:
        a = _read_number("Enter a: ")
        b = _read_number("Enter b: ")

        _print_menu()
        choice = input("Your choice: ").strip()

        try:
            if choice == "1":
                print(f"Result: {calculator.add(a, b)}")
            elif choice == "2":
                print(f"Result: {calculator.subtract(a, b)}")
            elif choice == "3":
                print(f"Result: {calculator.multiply(a, b)}")
            elif choice == "4":
                print(f"Result: {calculator.divide(a, b)}")
            elif choice == "0":
                continue
            else:
                print("Exiting calculator.")
                break
        except ZeroDivisionError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    run_calculator()
