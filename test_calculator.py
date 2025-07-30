# test_calculator.py
import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 6) # Changed 5 to 6 to force a failure
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
