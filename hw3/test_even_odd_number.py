import unittest
from even_odd_number import is_even


class MyTestCase(unittest.TestCase):
    def test_even_2(self):
        self.assertTrue(is_even(2))

    def test_even_0(self):
        self.assertTrue(is_even(0))

    def test_even_1(self):
        self.assertFalse(is_even(1))


if __name__ == '__main__':
    unittest.main()
