#!/usr/bin/env python

import unittest
from kata import *

class TestKata(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_no_operands(self):
        self.assertEqual(self.calc.Add(""), 0)

    def test_one_operand(self):
        self.assertEqual(self.calc.Add("1"), 1)
        self.assertEqual(self.calc.Add("2"), 2)

if __name__ == '__main__':
    unittest.main()
