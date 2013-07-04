#!/usr/bin/python


import unittest
import string

from exercises.chap3 import q0008


class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0008.foo.__doc__)

    def test_one(self):
        self.assertEqual({'a': 'a'}, q0008.circular(1))

    def test_two(self):
        self.assertEqual({'a': 'b', 'b': 'a'}, q0008.circular(2))

    def test_az(self):
        alph = string.ascii_lowercase
        d = q0008.circular(len(alph))

        self.assertEqual(len(alph), len(d))
        self.assertEqual('a', d['z'])

        for i, c in enumerate(alph[:-1]):
            self.assertEqual(alph[i+1], d[c])


if __name__ == '__main__':
    unittest.main()
