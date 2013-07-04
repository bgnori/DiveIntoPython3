#!/usr/bin/python


import unittest

from exercises.chap3 import q0009


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        primes = []
        with open("a000040.txt") as f:
            for line in f:
                idx, prime = line.split()
                primes.append(prime)
        cls.primes = primes

    def test_docstring(self):
        self.assertIsNotNone(q0009.is_prime.__doc__)
        self.assertIsNotNone(q0009.prime.__doc__)

    def test_is_prime_1(self):
        self.assertFalse(q0009.is_prime(1))

    def test_is_prime_2(self):
        self.assertTrue(q0009.is_prime(2))

    def test_is_prime_4(self):
        self.assertFalse(q0009.is_prime(4))

    def test_1(self):
        self.assertEqual([2], q0009.prime(1))

    def test_2(self):
        self.assertEqual([2, 3], q0009.prime(2))

    def test_3(self):
        self.assertEqual([2, 3, 5], q0009.prime(3))

    def test_5(self):
        self.assertEqual([2, 3, 5, 7, 11], q0009.prime(5))

    def test_58(self):
        xs = q0009.prime(58)
        ys = zip(self.primes, xs)
        for p, q in ys:
            self.assertEqual(p, q)

    def test_1000(self):
        xs = q0009.prime(1000)
        ys = zip(self.primes, xs)
        for p, q in ys:
            self.assertEqual(p, q)

            self.assertEqual(p, q)


if __name__ == '__main__':
    unittest.main()
