"""
Basic Python Calculator

Features:
- Object-oriented design
- Input validation
- Loop-based menu system
- Safe division handling
"""

from typing import Union


Number = Union[int, float]


class Calculator:
    """
    A basic calculator that performs arithmetic operations
    on two numbers provided at initialization.
    """

    def __init__(self, a: Number, b: Number) -> None:
        self.a = a
        self.b = b

    def add(self) -> Number:
        return self.a + self.b

    def subtract(self) -> Number:
        return self.a - self.b

    def multiply(self) -> Number:
        return self.a * self.b

    def divide(self) -> Union[Number, str]:
        if self.b == 0:
            return "Error: Division by zero is not allowed"
        return self.a / self.b


def _read_number(prompt: str) -> Number:
    """
    Reads a number from user input with validation.
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
    Runs the calculator program in a loop until the user exits.
    """
    while True:
        a = _read_number("Enter a: ")
        b = _read_number("Enter b: ")

        calculator = Calculator(a, b)

        _print_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            print(f"Result: {calculator.add()}")
        elif choice == "2":
            print(f"Result: {calculator.subtract()}")
        elif choice == "3":
            print(f"Result: {calculator.multiply()}")
        elif choice == "4":
            print(f"Result: {calculator.divide()}")
        elif choice == "0":
            continue
        else:
            print("Exiting calculator.")
            break


if __name__ == "__main__":
    run_calculator()
