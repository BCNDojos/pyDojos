#!/usr/bin/env python

import unittest
from kata import *

class TestAnagrams(unittest.TestCase):
     def test_basic_anagrams(self):
         '''tests basic anagrams'''
         self.assertEqual([''], anagramize(''))
         self.assertEqual(['a'], anagramize('a'))

if __name__ == '__main__':
    unittest.main()
