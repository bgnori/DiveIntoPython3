#!/usr/bin/python


import unittest

from exercises.chap3 import q0007


class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0007.foo.__doc__)

    def test_zero(self):
        self.assertEqual({}, q0007.circular(0))

    def test_one(self):
        self.assertEqual({0: 0}, q0007.circular(1))

    def test_two(self):
        self.assertEqual({0: 1, 1: 0}, q0007.circular(2))

    def test_three(self):
        self.assertEqual({0: 1, 1: 2, 2: 0}, q0007.circular(3))

    def test_four(self):
        self.assertEqual({0: 1, 1: 2, 2: 3, 3: 0}, q0007.circular(4))

    def test_1000(self):
        d = q0007.circular(1000)
        self.assertEqual(1000, len(d))
        self.assertEqual(0, d[999])

        for i in range(999):
            self.assertEqual(i+1, d[i])


if __name__ == '__main__':
    unittest.main()
