#!/usr/bin/env python

import unittest
from StringCalculator import *

class TestKata(unittest.TestCase):
  def setUp(self):
    self.calc = StringCalculator()

  def test_no_operands(self):
    self.assertEqual(self.calc.Add(""), 0)

  def test_n_operands(self):
    self.assertEqual(self.calc.Add("1"), 1)
    self.assertEqual(self.calc.Add("2"), 2)
    self.assertEqual(self.calc.Add("1,2"), 3)
    self.assertEqual(self.calc.Add("1,2,3"), 6)

  def test_n_digit_operands(self):
    self.assertEqual(self.calc.Add("12,3"), 15)
    self.assertEqual(self.calc.Add("21,42"), 63)
    self.assertEqual(self.calc.Add("123,12345"), 12468)

  def test_delimiter_newline(self):
    self.assertEqual(self.calc.Add("1\n2"), 3)
    self.assertEqual(self.calc.Add("1\n2,3"), 6)

  def test_delimiter_choice(self):
    self.assertEqual(self.calc.Add("//;\n1;2,3\n4"), 10)

if __name__ == '__main__':
  unittest.main()
