#!/usr/bin/python


import unittest

from exercises.chap3 import q0005


class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0005.foo.__doc__)

    def test_zero(self):
        self.assertEqual(['Fizz Buzz'], q0005.foo(0))

    def test_one(self):
        self.assertEqual(['Fizz Buzz', 1], q0005.foo(1))

    def test_two(self):
        self.assertEqual(['Fizz Buzz', 1, 2], q0005.foo(2))

    def test_three(self):
        self.assertEqual(['Fizz Buzz', 1, 2, 'Fizz'], q0005.foo(3))

    def test_15(self):
        xs = q0005.foo(15)
        self.assertEqual(16, len(xs))
        self.assertEqual('Fizz Buzz', xs[15])


if __name__ == '__main__':
    unittest.main()
