import unittest2 as unittest
from .discount_calculator import Calculator, ArithmeticException


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_calculateDiscount_validInput(self):
        self.assertEqual(self.calculator.calculateDiscount(100, 10), 90)
        self.assertEqual(self.calculator.calculateDiscount(200, 20), 160)
        self.assertEqual(self.calculator.calculateDiscount(500, 25), 375)

    def test_calculateDiscount_invalidInput(self):
        self.assertRaises(ArithmeticException, self.calculator.calculateDiscount, -100, 10)
        self.assertRaises(ArithmeticException, self.calculator.calculateDiscount, 100, -10)
        self.assertRaises(ArithmeticException, self.calculator.calculateDiscount, 100, 110)


if __name__ == '__main__':
    unittest.main()
