import unittest
from number_in_interval import number_in_interval


class MyTestCase(unittest.TestCase):
    def test_less_left(self):
        for i in range(-1000, 25):
            with self.subTest(i=i):
                self.assertFalse(number_in_interval(i))

    def test_greater_right(self):
        for i in range(101, 1000):
            with self.subTest(i=i):
                self.assertFalse(number_in_interval(i))

    def test_in_interval(self):
        for i in range(25, 101):
            with self.subTest(i=i):
                self.assertTrue(number_in_interval(i))


if __name__ == '__main__':
    unittest.main()
