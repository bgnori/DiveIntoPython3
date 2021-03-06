#!/usr/bin/python


import unittest

from exercises.chap2 import q0002

data = ['Fizz Buzz', 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz',
        11, 'Fizz', 13, 14, 'Fizz Buzz', 16, 17, 'Fizz', 19, 'Buzz',
        'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'Fizz Buzz',
        31, 32, 'Fizz', 34]


K = 1000
M = K*K
G = M*K
T = G*K



class FizzBuzzTestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0002.fizzbuzz.__doc__)

    def test_by_data(self):
        for i, expected in enumerate(data):
            self.assertEqual(expected, q0002.fizzbuzz(i))

    def test_1000(self):
        self.assertEqual('Buzz', q0002.fizzbuzz(1000))

    def test_1000000(self):
        self.assertEqual('Buzz', q0002.fizzbuzz(1000000))

    def test_3000003(self):
        self.assertEqual('Fizz', q0002.fizzbuzz(3000003))

    def test_3000000(self):
        self.assertEqual('Fizz Buzz', q0002.fizzbuzz(3000000))

    def test_3K(self):
        self.assertEqual('Fizz Buzz', q0002.fizzbuzz(3*K))

    def test_3M(self):
        self.assertEqual('Fizz Buzz', q0002.fizzbuzz(3*M))

    def test_3G(self):
        self.assertEqual('Fizz Buzz', q0002.fizzbuzz(3*G))

    def test_3T(self):
        self.assertEqual('Fizz Buzz', q0002.fizzbuzz(3*T))

if __name__ == '__main__':
    unittest.main()
