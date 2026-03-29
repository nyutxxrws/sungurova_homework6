import unittest
import sys
def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result
class TestFactorial(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(factorial(0), 1)
    def test_one(self):
        self.assertEqual(factorial(1), 1)
    def test_two(self):
        self.assertEqual(factorial(2), 2)
    def test_three(self):
        self.assertEqual(factorial(3), 6)
    def test_four(self):
        self.assertEqual(factorial(4), 24)
    def test_five(self):
        self.assertEqual(factorial(5), 120)
    def test_minus(self):
        with self.assertRaises(ValueError):
            factorial(-5)
if __name__ == "__main__":
    unittest.main()