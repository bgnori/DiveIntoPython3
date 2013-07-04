#!/usr/bin/python


import io
import unittest

from exercises.aoj import q0003

data = """4
1 2
3 4 5 6
0 
2 7 8"""

class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0003.reader.__doc__)

    def test_0(self):
        f = io.StringIO('0')
        xs = q0003.reader(f)
        self.assertEqual([], xs)

    def test_some(self):
        f = io.StringIO(data)
        xs = q0003.reader(f)
        self.assertEqual([[2], [4, 5, 6], [], [7, 8]], xs)


if __name__ == '__main__':
    unittest.main()
