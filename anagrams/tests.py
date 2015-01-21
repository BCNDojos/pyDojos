#!/usr/bin/env python

import unittest
from kata import *

class TestAnagrams(unittest.TestCase):
     def test_basic_anagrams(self):
         '''tests basic anagrams'''
         self.assertEqual([''], anagramize(''))
         self.assertEqual(['a'], anagramize('a'))
         self.assertEqual(['ab', 'ba'], anagramize('ab'))

     def test_3_length_anagram(self):
         anagrams = anagramize('abc')
         self.assertEqual(6,len(set(anagrams)))
         for word in anagrams:
             self.assertEqual(3, len(word))
             for char in set('abc'):
                 self.assertTrue(char in word)

if __name__ == '__main__':
    unittest.main()
