#!/usr/bin/env python

import unittest
from kata import *

class TestKata(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty(self):
        self.assertEqual(self.calc.Add(""), 0)

    def test_one(self):
        self.assertEqual(self.calc.Add("1"), 1)

if __name__ == '__main__':
    unittest.main()
