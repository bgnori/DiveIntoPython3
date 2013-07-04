#!/usr/bin/python


import io
import unittest

from exercises.aoj import q0002


class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0002.colonfind.__doc__)

    def test_nodef(self):
        f = io.StringIO('foo\nbar\nika\ntako')
        xs = q0002.colonfind(f)
        self.assertEqual([], xs)

    def test_somedef(self):
        f = io.StringIO('foo\nbar):\ndefone\nika\ntako):\ndeftwo')
        xs = q0002.colonfind(f)
        self.assertEqual(['bar):\n', 'tako):\n'], xs)

if __name__ == '__main__':
    unittest.main()
