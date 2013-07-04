#!/usr/bin/python


import io
import unittest

from exercises.aoj import q0004

data = """1 2
3 4 5
0"""

class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0004.reader.__doc__)

    def test_0(self):
        f = io.StringIO('0')
        xs = q0004.reader(f)
        self.assertEqual([], xs)

    def test_some(self):
        f = io.StringIO(data)
        xs = q0004.reader(f)
        self.assertEqual([[1, 2], [3, 4, 5]], xs)


if __name__ == '__main__':
    unittest.main()
