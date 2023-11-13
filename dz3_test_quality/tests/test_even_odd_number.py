from dz3_test_quality.task_one.even_odd_number import even_odd_number

from unittest import TestCase


class EvenOddNumberTest(TestCase):
    """Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, является ли переданное число четным или нечетным."""

    def test_even_number(self):
        self.assertTrue(even_odd_number(6))

    def test_odd_number(self):
        self.assertFalse(even_odd_number(5))
