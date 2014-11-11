#!/usr/bin/env python

import unittest
from kata import *

class TestKata(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty(self):
        self.assertEqual(self.calc.Add(""), 0)

if __name__ == '__main__':
    unittest.main()
