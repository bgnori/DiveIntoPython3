#!/usr/bin/python


import unittest

from exercises.chap3 import q0004


class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0004.foo.__doc__)

    def test_result(self):
        d = q0004.foo()
        self.assertEqual(100, len(d))
        for i in range(100):
            self.assertIn(i, d)
            self.assertEqual(i*i, d[i])


if __name__ == '__main__':
    unittest.main()
