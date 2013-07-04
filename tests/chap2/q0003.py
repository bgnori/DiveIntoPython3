#!/usr/bin/python


import unittest

from exercises.chap2 import q0003

data = ['Fizz Buzz', 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz',
        11, 'Fizz', 13, 14, 'Fizz Buzz', 16, 17, 'Fizz', 19, 'Buzz',
        'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'Fizz Buzz',
        31, 32, 'Fizz', 34]

class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0003.fizzbuzz_t.__doc__)

    def test_0(self):
        self.assertEqual(tuple(data[0]), q0003.fizzbuzz_t(0))

    def test_15(self):
        self.assertEqual(tuple(data[:15]), q0003.fizzbuzz_t(15))

    def test_30(self):
        self.assertEqual(tuple(data[:30]), q0003.fizzbuzz_t(30))

    def test_100(self):
        xt = q0003.fizzbuzz_t(100)
        for i, x in enumerate(xt):
            if i % 3 == 0 or i % 5 == 0:
                self.assertIsInstance(x, str)
            else:
                self.assertEqual(i, x)


if __name__ == '__main__':
    unittest.main()
