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
        self.assertIsNotNone(q0002.fizzbuff.__doc__)

    def test_by_data(self):
        for i, expected in enumerate(data):
            self.assertEqual(expected, q0002.fizzbuff(i))

    def test_1000(self):
        self.assertEqual('Buzz', q0002.fizzbuff(1000))

    def test_1000000(self):
        self.assertEqual('Buzz', q0002.fizzbuff(1000000))

    def test_3000003(self):
        self.assertEqual('Fizz', q0002.fizzbuff(3000003))

    def test_3000000(self):
        self.assertEqual('Fizz Buzz', q0002.fizzbuff(3000000))

    def test_K(self):
        self.assertEqual('Fizz Buzz', q0002.fizzbuff(K))

    def test_M(self):
        self.assertEqual('Fizz Buzz', q0002.fizzbuff(M))

    def test_G(self):
        self.assertEqual('Fizz Buzz', q0002.fizzbuff(G))

    def test_T(self):
        self.assertEqual('Fizz Buzz', q0002.fizzbuff(T))

if __name__ == '__main__':
    unittest.main()
