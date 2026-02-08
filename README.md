# Basic Python Calculator (OOP)

## Overview

This repository contains a command-line calculator implemented in Python using object-oriented design principles.  
While the arithmetic itself is simple, the project emphasizes **software craftsmanship**, clean architecture, and professional testing practices.

---

## Technical Highlights

- Stateless `Calculator` class for testability
- Complete separation of core logic and CLI interface
- Automated unit testing with pytest
- Defensive programming with explicit exception handling
- No external runtime dependencies

---

## Project Structure

```
basic-python-calculator/
├── basic_calculator.py   # Core logic + CLI entry point
├── test_calculator.py    # Automated unit tests
├── README.md
├── LICENSE
└── .gitignore
```

---

## Running the Calculator

```
python basic_calculator.py
```

---

## Running Tests

Install pytest if needed:

```
pip install pytest
```

Run the test suite:

```
pytest -v
```

---

## Why This Project Matters

• Demonstrates understanding of the Software Development Life Cycle
• Shows the difference between manual testing and automated verification
• Uses industry-standard error handling patterns
• Mirrors structure used in real-world Python projects

---

## Disclaimer

This project is created strictly for educational purposes and portfolio demonstration only.
It is not intended for production use or critical financial calculations.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/cherryaugusta/basic-python-calculator/blob/main/LICENSE) file for details.
