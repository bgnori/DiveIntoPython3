#!/usr/bin/python


import io
import unittest

from exercises.aoj import q0002


class TestCase(unittest.TestCase):
    def test_docstring(self):
        self.assertIsNotNone(q0002.foo.__doc__)

    def test_nodef(self):
        f = io.StringIO('foo\nbar\nika\ntako')
        xs = q0002.deffind()
        self.assertEqual([], xs)

    def test_somedef(self):
        f = io.StringIO('foo\nbar):\defone\nika\ntako):\ndeftwo')
        xs = q0002.deffind()
        self.assertEqual(['bar):', 'tako):'], xs)

if __name__ == '__main__':
    unittest.main()
