import pytest
from basic_calculator import Calculator


class TestCalculator:
    @pytest.fixture
    def calc(self) -> Calculator:
        """
        Provides a fresh Calculator instance for each test.
        """
        return Calculator()

    @pytest.mark.parametrize("a, b, expected", [
        (10, 5, 15),
        (-1, 1, 0),
        (-5, -5, -10),
        (2.5, 2.5, 5.0)
    ])
    def test_addition(self, calc, a, b, expected):
        assert calc.add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 5, 5),
        (5, 2, 3),
        (-2, -3, 1)
    ])
    def test_subtraction(self, calc, a, b, expected):
        assert calc.subtract(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 5, 50),
        (0, 100, 0),
        (-2, 3, -6)
    ])
    def test_multiplication(self, calc, a, b, expected):
        assert calc.multiply(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 5, 2.0),
        (5, 2, 2.5),
        (0, 5, 0.0)
    ])
    def test_division(self, calc, a, b, expectepytest -vd):
        assert calc.divide(a, b) == expected

    def test_division_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.divide(10, 0)
