#!/usr/bin/python


import unittest
import io

from exercises.aoj import q0001


class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0001.deffind.__doc__)

    def test_nodef(self):
        f = io.StringIO('foo\nbar\nika\ntako')
        xs = q0001.deffind(f)
        self.assertEqual([], xs)

    def test_somedef(self):
        f = io.StringIO('foo\nbar\ndefone\nika\ntako\ndeftwo')
        xs = q0001.deffind(f)
        self.assertEqual(['defone\n', 'deftwo'], xs)


if __name__ == '__main__':
    unittest.main()
