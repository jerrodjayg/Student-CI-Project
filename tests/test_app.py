import unittest

from app import add_numbers, subtract_numbers


class CalculatorTests(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_zero(self):
        self.assertEqual(add_numbers(5, 0), 5)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(8, 3), 5)


if __name__ == "__main__":
    unittest.main()
